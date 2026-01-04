from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Exécuter tous les seeders de l\'application'

    def add_arguments(self, parser):
        parser.add_argument(
            '--quick-replies-only',
            action='store_true',
            help='Exécuter seulement le seeder des quick replies',
        )
        parser.add_argument(
            '--admin-only',
            action='store_true',
            help='Créer seulement le superuser admin',
        )

    def handle(self, *args, **options):
        if options['quick_replies_only']:
            self.stdout.write('Exécution du seeder des quick replies...')
            call_command('seed_quickreplies')
        elif options['admin_only']:
            self.stdout.write('Création du superuser admin...')
            call_command('seed_admin')
        else:
            self.stdout.write('Exécution de tous les seeders...')
            
            # Appeler tous les seeders ici
            self.stdout.write('1. Création du superuser admin...')
            call_command('seed_admin')
            
            self.stdout.write('2. Seeding quick replies...')
            call_command('seed_quickreplies')
            
            
        self.stdout.write(
            self.style.SUCCESS('Tous les seeders ont été exécutés avec succès!')
        )
