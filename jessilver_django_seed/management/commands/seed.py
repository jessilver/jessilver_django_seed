from django.core.management.base import BaseCommand
from django.conf import settings
import os
import sys
from .seeder_utils import get_seeder_classes_from_module, load_seeders_from_dir
from .seeder_creation import create_seeder

# Global list to store found seeder classes
seeders = []

# For each app listed in SEEDER_APPS in project settings
for app in settings.SEEDER_APPS:
    app_seeders_dir = os.path.join(settings.BASE_DIR, app, 'seeders')
    if os.path.isdir(app_seeders_dir):
        seeders.extend(load_seeders_from_dir(app_seeders_dir))

class Command(BaseCommand):
    help = 'Populate the database with all or selected seeders, or create a new seeder file.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--only',
            type=str,
            help='Comma-separated list of seeder class names to run (ex: UserSeeder,ProductSeeder)'
        )
        parser.add_argument(
            '--create',
            type=str,
            help='Seeder class name to create (ex: UserSeeder)'
        )
        parser.add_argument(
            '--app',
            type=str,
            help='App name where the seeder is or will be located (ex: myapp)'
        )

    def handle(self, *args, **options):
        only = options.get('only')
        create = options.get('create')
        app = options.get('app')
        selected_seeders = seeders

        # Seeder creation mode
        if create and app:
            created = create_seeder(app, create, settings, self.style, self.stdout)
            return

        # Selective execution by --only
        if only:
            only_list = [name.strip() for name in only.split(',') if name.strip()]
            selected_seeders = [s for s in seeders if s.__name__ in only_list]
            if not selected_seeders:
                self.stdout.write(self.style.ERROR(f'No matching seeders found for: {only}'))
                return

        confirm = input("Are you sure you want to proceed with seeding? [y/N]: ")
        if confirm.lower() != 'y':
            self.stdout.write(self.style.ERROR('Seeding canceled.'))
            return
        self.stdout.write('')
        self.stdout.write(self.style.HTTP_SERVER_ERROR('Starting seeding... '))
        self.stdout.write('')

        for seeder_class in selected_seeders:
            seeder_class().handle()
            self.stdout.write('')
        self.stdout.write(self.style.HTTP_SERVER_ERROR('All seeders have been executed!'))