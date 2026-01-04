from django.core.management.base import BaseCommand
from app.models import QuickReply


class Command(BaseCommand):
    help = 'Créer les quick replies pour le bot messenger'

    def handle(self, *args, **options):
        # Données des quick replies
        quick_replies_data = [
            {
                'title': 'À propos',
                'payload': 'ABOUT',
                'response_text': 'Hosodoko-ko est une association à but non lucratif qui vise à promouvoir la culture japonaise et à créer des liens entre les passionnés de cette culture. Nous organisons divers événements, ateliers et activités pour partager notre amour du Japon avec la communauté.'
            },
            {
                'title': 'Savoir-faire',
                'payload': 'SKILLS',
                'response_text': 'Nos savoir-faire incluent l\'organisation d\'événements culturels, la gestion de projets associatifs, la communication et le marketing, ainsi que la création de contenus'
            },
            {
                'title': 'Événements',
                'payload': 'EVENTS',
                'response_text': 'Nous organisons régulièrement des événements tels que des ateliers de cuisine japonaise, des projections de films, des cours de langue japonaise, et des festivals culturels. Consultez notre site web ou nos réseaux sociaux pour les prochaines dates !'
            },
            {
                'title': 'Challenges',
                'payload': 'CHALLENGES',
                'response_text': 'Nous relevons des défis tels que la sensibilisation à la culture japonaise dans notre communauté, l\'organisation d\'événements en ligne et en personne, et la création de partenariats avec d\'autres associations et institutions culturelles.'
            },
            # {
            #     'title': 'Quizz',
            #     'payload': 'QUIZ',
            #     'response_text': 'Quel est le plat japonais traditionnel souvent servi lors des célébrations ?\n1. Sushi\n2. Ramen\n3. Mochi\n4. Tempura\nRépondez avec le numéro de votre choix !'
            # }
        ]

        # Créer ou mettre à jour les quick replies
        for qr_data in quick_replies_data:
            quick_reply, created = QuickReply.objects.get_or_create(
                payload=qr_data['payload'],
                defaults={
                    'title': qr_data['title'],
                    'response_text': qr_data['response_text']
                }
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Quick reply "{quick_reply.title}" créé avec succès')
                )
            else:
                # Mettre à jour les champs si nécessaire
                updated = False
                if quick_reply.title != qr_data['title']:
                    quick_reply.title = qr_data['title']
                    updated = True
                if quick_reply.response_text != qr_data['response_text']:
                    quick_reply.response_text = qr_data['response_text']
                    updated = True
                
                if updated:
                    quick_reply.save()
                    self.stdout.write(
                        self.style.WARNING(f'Quick reply "{quick_reply.title}" mis à jour')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Quick reply "{quick_reply.title}" existe déjà')
                    )

        self.stdout.write(
            self.style.SUCCESS('Toutes les quick replies ont été traitées avec succès!')
        )
