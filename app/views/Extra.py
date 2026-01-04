import os
from dotenv import load_dotenv
from django.http import response, HttpResponse, JsonResponse
from rest_framework.views import APIView
import requests
from rest_framework.response import Response

class PrivacyPolicyView(APIView):
    def get(self, request):
        privacy_policy = """
        ### Politique de confidentialité

        **Dernière mise à jour : 8 avril 2025**

        Bienvenue sur Hosodoko-bot, un bot Messenger développé par Monja. Nous nous engageons à protéger votre vie privée. Cette Politique de confidentialité explique comment nous collectons, utilisons, partageons et protégeons vos données personnelles lorsque vous interagissez avec notre bot via Facebook Messenger (ci-après « le Bot »). En utilisant le Bot, vous acceptez les pratiques décrites ici.

        #### 1. Informations que nous collectons
        - **Données personnelles identifiables** : Votre identifiant Facebook unique (Page-Scoped ID, ou PSID), fourni par Facebook Messenger lorsque vous nous envoyez un message. Les messages que vous envoyez au Bot, y compris leur contenu textuel.
        - **Données d’utilisation** : Informations sur vos interactions avec le Bot, comme les horodatages des messages et les réponses générées. Données techniques, telles que l’agent utilisateur de votre appareil (collecté via les requêtes HTTP).
        - **Données via Facebook** : Toute information supplémentaire fournie par l’API Messenger (ex. : votre nom public, si disponible), selon les permissions accordées.

        #### 2. Comment nous utilisons vos informations
        Nous utilisons vos données pour :  
        - Faire fonctionner le Bot et répondre à vos messages via Facebook Messenger.  
        - Améliorer les fonctionnalités du Bot et personnaliser vos interactions.  
        - Analyser les performances et résoudre les problèmes techniques.  
        - Respecter nos obligations légales.

        #### 3. Partage de vos informations
        Nous ne vendons ni ne louons vos données personnelles. Elles peuvent être partagées dans ces cas :  
        - **Avec Facebook** : Le Bot fonctionne via l’API Messenger de Facebook, qui traite vos messages et identifiants selon sa propre politique de confidentialité.  
        - **Avec des prestataires techniques** : Nous utilisons des services d’hébergement (ex. : serveurs Django) qui peuvent accéder à vos données pour assurer le fonctionnement du Bot. Ces prestataires sont tenus à la confidentialité.  
        - **Pour des raisons légales** : Nous pouvons divulguer vos données si la loi l’exige ou pour protéger nos droits.

        #### 4. Bases légales du traitement
        Nous traitons vos données sur ces bases :  
        - **Consentement** : En envoyant un message au Bot, vous consentez à ce que nous traitions vos données pour répondre.  
        - **Intérêt légitime** : Améliorer le Bot et assurer son bon fonctionnement.  
        - **Obligations légales** : Respecter les lois applicables.

        #### 5. Conservation des données
        - Les messages et identifiants (PSID) sont conservés pendant 12 mois, sauf si vous demandez leur suppression avant.  
        - Les logs techniques (ex. : erreurs serveur) sont conservés pendant 30 jours.  
        - Après ces périodes, les données sont anonymisées ou supprimées, sauf exigence légale contraire.

        #### 6. Sécurité des données
        Nous utilisons des mesures comme le chiffrement HTTPS et des pratiques sécurisées dans Django pour protéger vos données. Cependant, la transmission via Messenger dépend aussi des mesures de sécurité de Facebook, sur lesquelles nous n’avons pas de contrôle total.

        #### 7. Vos droits
        Vous avez les droits suivants :  
        - **Accès** : Demander les données que nous avons sur vous (ex. : vos messages).  
        - **Rectification** : Corriger des informations inexactes.  
        - **Suppression** : Demander la suppression de vos données.  
        - **Opposition** : Refuser certains traitements (bien que cela puisse limiter l’usage du Bot).  
        Pour exercer ces droits, envoyez un message au Bot avec votre demande ou contactez-nous à monja22.aps2a@gmail.com  . Nous répondrons sous 30 jours.

        #### 8. Services tiers
        Le Bot repose sur Facebook Messenger. Vos interactions sont également soumises à la [Politique de confidentialité de Facebook](https://www.facebook.com/privacy/policy/). Nous vous encourageons à la lire.

        #### 9. Modifications de cette politique
        Nous pouvons mettre à jour cette politique. Les changements seront publiés ici, avec une nouvelle date. Consultez-la régulièrement.

        #### 10. Nous contacter
        Pour toute question, contactez-nous :  
        - **Via le Bot** : Envoyez un message avec « Confidentialité ».  
        - **E-mail** : monja22.aps2a@gmail.com  
        Si vous avez une réclamation, vous pouvez contacter une autorité de protection des données (ex. : CNIL en France).
        """
        return HttpResponse(privacy_policy, content_type="text/plain; charset=utf-8")


class TermsOfServiceView(APIView):
    def get(self, request):
        terms_of_service = """
        ### Conditions de service

        **Dernière mise à jour : 09 avril 2025**

        Bienvenue sur [Nom de ton bot/application] (ci-après « le Bot »), un service de messagerie automatisé fonctionnant via Facebook Messenger et développé avec Django par [Nom de ton entreprise/ton nom]. Ces Conditions de service régissent votre utilisation du Bot. En interagissant avec le Bot, vous acceptez de respecter ces conditions. Si vous n’êtes pas d’accord, veuillez cesser d’utiliser le Bot.

        #### 1. Description du service
        Le Bot est une application automatisée conçue pour répondre à vos messages via Facebook Messenger. Il peut fournir des informations, répondre à des questions ou exécuter des tâches simples selon sa programmation. Le Bot est hébergé sur nos serveurs et utilise l’API Messenger de Facebook pour fonctionner.

        #### 2. Éligibilité
        Pour utiliser le Bot, vous devez :  
        - Avoir un compte Facebook actif et accès à Messenger.  
        - Être âgé d’au moins 13 ans (ou l’âge minimum requis par la loi dans votre juridiction).  
        - Respecter les politiques de Facebook, disponibles sur [facebook.com/policies](https://www.facebook.com/policies).

        #### 3. Utilisation autorisée
        Vous acceptez d’utiliser le Bot uniquement à des fins légales et conformément à ces conditions. Vous ne devez pas :  
        - Envoyer des messages contenant du contenu illégal, offensant, diffamatoire, ou nuisible.  
        - Tenter d’exploiter, pirater ou contourner les fonctionnalités du Bot.  
        - Utiliser le Bot pour spammer ou harceler d’autres utilisateurs ou entités.  
        Nous nous réservons le droit de suspendre ou de bloquer votre accès au Bot en cas de violation de ces règles.

        #### 4. Propriété intellectuelle
        - Le Bot, son code, son design et son contenu (sauf les messages des utilisateurs) sont la propriété de [Nom de ton entreprise/ton nom] et protégés par les lois sur la propriété intellectuelle.  
        - Vous conservez la propriété des messages que vous envoyez, mais vous nous accordez une licence non exclusive pour les traiter afin de fournir le service.

        #### 5. Limitation de responsabilité
        - Le Bot est fourni « tel quel » sans garantie explicite ou implicite. Nous ne garantissons pas qu’il sera toujours disponible, sans erreur ou adapté à tous vos besoins.  
        - Nous ne sommes pas responsables des dommages indirects, accidentels ou consécutifs découlant de votre utilisation du Bot, sauf si la loi l’exige.  
        - Le Bot dépend de Facebook Messenger. Toute interruption ou problème lié à la plateforme de Facebook est hors de notre contrôle.

        #### 6. Données personnelles
        Votre utilisation du Bot implique la collecte et le traitement de données personnelles, comme décrit dans notre [Politique de confidentialité](#) (lien à remplacer par l’URL réelle une fois configurée). Veuillez la consulter pour plus de détails.

        #### 7. Modifications du service ou des conditions
        Nous pouvons modifier, suspendre ou interrompre le Bot à tout moment sans préavis. Ces Conditions de service peuvent également être mises à jour. Les modifications seront publiées ici avec une nouvelle date. Votre utilisation continue du Bot après ces changements vaut acceptation.

        #### 8. Résiliation
        - Vous pouvez cesser d’utiliser le Bot à tout moment en arrêtant de lui envoyer des messages.  
        - Nous pouvons résilier votre accès au Bot si vous violez ces conditions ou pour toute autre raison à notre discrétion.

        #### 9. Droit applicable
        Ces conditions sont régies par les lois de [indique ta juridiction, ex. : France]. Tout litige sera soumis aux tribunaux compétents de [ville/pays].

        #### 10. Nous contacter
        Pour toute question sur ces Conditions de service :  
        - **Via le Bot** : Envoyez « Conditions » dans Messenger.  
        - **E-mail** : monja22.aps2a@gmail.com
        """
        return HttpResponse(terms_of_service, content_type="text/plain; charset=utf-8")
