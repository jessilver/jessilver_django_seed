from django.core.management.base import BaseCommand
from django.conf import settings
import importlib.util
import inspect
import os

seeders = []

for app in settings.SEEDER_APPS:
    app_seeders_dir = os.path.join(settings.BASE_DIR, app, 'seeders')
    if os.path.isdir(app_seeders_dir):
        # Ordena os arquivos pelo nome
        for filename in sorted(os.listdir(app_seeders_dir)):
            if filename.endswith('.py') and filename != '__init__.py' and filename != 'BaseSeeder.py':
                module_name = filename[:-3]
                module_path = os.path.join(app_seeders_dir, filename)

                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if name.endswith('Seeder') and name != 'BaseSeeder':
                        seeders.append(obj)

class Command(BaseCommand):
    help = 'Populate the database with all or selected seeders'

    def add_arguments(self, parser):
        parser.add_argument(
            '--only',
            type=str,
            help='Comma-separated list of seeder class names to run (ex: UserSeeder,ProductSeeder)'
        )

    def handle(self, *args, **options):
        only = options.get('only')
        selected_seeders = seeders
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