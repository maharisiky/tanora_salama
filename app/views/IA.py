from app.models import *
from dotenv import load_dotenv
import os
import google.generativeai as genai

class IA :
    def __init__(self):
        load_dotenv()
        self.gemini_api_key = os.environ.get("GEMINI_API_KEY")
        self.gemini_ai = genai.configure(api_key=self.gemini_api_key) 
        self.gemini_model = genai.GenerativeModel('gemini-flash-latest')

    def get_prompt(self):
        prompt = ""
        with open('static/prompt.txt', 'r') as file:
            prompt = file.read()
        return prompt

    def ask_gemini(self, sender, message, save=True):
            try:
                # get or create user
                user, _ = User.objects.get_or_create(fb_id=sender)

                # extract text from message object
                message_text = message.get('text', '') if isinstance(message, dict) else str(message)

                # save new message
                if save:
                    Messages.objects.create(sender=user, role='USER', content=message_text)

                # history messages
                history = Messages.objects.filter(sender=user).order_by('-created_at')[:20]
                role_map = {'user': 'user', 'chatbot': 'model'}
                messages = [
                    {"role": role_map.get(msg.role.lower(), "user"), "parts": [msg.content]}
                    for msg in reversed(history)
                ]

                messages.append({
                    "role": "user",
                    "parts": [self.get_prompt()]
                })
                
                chat = self.gemini_model.start_chat(
                    history=messages
                )

                # Safety settings to prevent blocking
                safety_settings = {
                    genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
                    genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.BLOCK_NONE,
                    # genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: genai.types.HarmBlockThreshold.BLOCK_NONE,
                    genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
                }

                response = chat.send_message(
                    message_text,
                    safety_settings=safety_settings
                )
                
                try:
                    reply_text = response.text.strip()
                except ValueError:
                    print(f"Gemini response has no text. Finish reason: {response.candidates[0].finish_reason}")
                    reply_text = "..."

                if save:
                    Messages.objects.create(sender=user, role='CHATBOT', content=reply_text).save()

                return self.clean_text(reply_text)
            except Exception as e:
                print(f"Error in ask_gemini: {type(e).__name__}: {str(e)}")
                import traceback
                traceback.print_exc()
                return "Désolé, une erreur s'est produite lors du traitement de votre message. Veuillez réessayer."

    def clean_text(self, text):
        text = text.replace('**', '')
        # text = re.sub(r'(?<=\n)(\d+\.)', r'\n\1', text)
        return text
