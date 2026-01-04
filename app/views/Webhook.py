import os
from dotenv import load_dotenv
from django.http import response, HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from app.serializers import *
from app.models import *
import requests
from rest_framework.response import Response
from bs4 import BeautifulSoup
import time
from app.views.IA import IA


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WebhookView(APIView):
    def __init__(self):
        load_dotenv()
        # getting verify token from .env
        self.verify_token = os.getenv("VERIFY_TOKEN")
        self.page_access_token = os.getenv("PAGE_ACCESS_TOKEN")
        self.messaging_endpoint = os.getenv('MESSAGING_ENDPOINT')
        self.page_url = f"{self.messaging_endpoint}?access_token={self.page_access_token}"

        self.ia = IA()

    def get(self, request):
        if request.query_params.get('hub.verify_token') == self.verify_token:
            return Response(int(request.query_params.get('hub.challenge')), status=status.HTTP_200_OK)
        else:
            return Response("Erreur de vérification", status=status.HTTP_403_FORBIDDEN)

    def post(self, request):
        try:
            data = request.data
            messaging = data['entry'][0]['messaging'][0]
            sender_id = messaging['sender']['id']

            message = messaging['message']
            self.actions(sender_id, 'mark_seen')
            self.actions(sender_id, 'typing_on')

            # if the message is not a text message
            if 'text' not in message:
                message = """
                    Je suis désolé, je ne peux pas traiter ce type de message pour le moment. \nMerci d'envoyer un message texte.
                """
                self.actions(sender_id, 'typing_off')
                self.send_message(sender_id, message)
                return Response("ok", status=status.HTTP_200_OK)

            response_message = self.ia.ask_gemini(sender_id, message)
            
            self.send_message(sender_id, response_message)
            self.actions(sender_id, 'typing_off')
            return Response("ok", status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error in webhook post: {type(e).__name__}: {str(e)}")
            import traceback
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def send_message(self, recipient_id, message_text):
        params = {
            "access_token": self.page_access_token
        }
        headers = {
            "Content-Type": "application/json"
        }

        
        data = {
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": message_text, 
            }
        }

        try:
            response = requests.post(
                self.messaging_endpoint,
                params=params,
                headers=headers,
                json=data
            )
            
            response.raise_for_status()
        except Exception as e:
            print(f"Error sending message: {type(e).__name__}: {str(e)}")
            import traceback
            traceback.print_exc()


    def actions(self,recipient_id, action):
        payload = {
            'recipient': {'id': recipient_id},
            'sender_action': action,
        }
        headers = {'Content-Type': 'application/json'}
        requests.post(self.page_url, headers=headers, json=payload)


def healthView(request):
    return JsonResponse({"status": "ok"})