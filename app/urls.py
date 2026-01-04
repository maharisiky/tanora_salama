from django.urls import path

from rest_framework.routers import DefaultRouter

from app.views.Webhook import *
from app.views.Extra import *

router = DefaultRouter()

router.register('user', UserViewSet, 'user')

urlpatterns = [
    path('webhook/', WebhookView.as_view(), name='webhook'),
    path('health_check/', healthView, name='health_check'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('terms-of-service/', TermsOfServiceView.as_view(), name='terms_of_service'),
]

urlpatterns += router.urls