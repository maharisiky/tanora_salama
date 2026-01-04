import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Créer un superuser admin avec un mot de passe depuis les variables d\'environnement'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='admin',
            help='Nom d\'utilisateur pour l\'admin (défaut: admin)'
        )
        parser.add_argument(
            '--email',
            type=str,
            default='admin@hosodoko-ko.com',
            help='Email pour l\'admin (défaut: admin@hosodoko-ko.com)'
        )

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        
        # Récupérer le mot de passe depuis les variables d'environnement
        password = os.getenv('ADMIN_PASSWORD')
        
        if not password:
            self.stdout.write(
                self.style.ERROR(
                    'ERREUR: La variable d\'environnement ADMIN_PASSWORD n\'est pas définie. '
                    'Veuillez définir ADMIN_PASSWORD dans votre fichier .env ou vos variables d\'environnement.'
                )
            )
            return

        # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            
            # Mettre à jour le mot de passe et s'assurer que c'est un superuser
            user.set_password(password)
            user.email = email
            user.is_staff = True
            user.is_superuser = True
            user.save()
            
            self.stdout.write(
                self.style.WARNING(f'Utilisateur admin "{username}" existe déjà. Mot de passe et permissions mis à jour.')
            )
        else:
            # Créer un nouveau superuser
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'Superuser admin "{username}" créé avec succès!')
            )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Admin configuré:\n'
                f'  - Nom d\'utilisateur: {username}\n'
                f'  - Email: {email}\n'
                f'  - Mot de passe: [depuis ADMIN_PASSWORD]\n'
                f'  - Accès admin: ✓\n'
                f'  - Superuser: ✓'
            )
        )
