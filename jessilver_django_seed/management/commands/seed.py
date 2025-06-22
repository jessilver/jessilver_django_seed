from django.core.management.base import BaseCommand
from django.conf import settings
import importlib.util
import inspect
import os

def get_seeder_classes_from_module(module):
    """
    Retorna todas as classes Seeder (exceto BaseSeeder) de um módulo.
    """
    return [
        obj for name, obj in inspect.getmembers(module, inspect.isclass)
        if name.endswith('Seeder') and name != 'BaseSeeder'
    ]

def load_seeders_from_dir(seed_dir):
    """
    Carrega dinamicamente todos os módulos Python do diretório de seeders,
    retornando uma lista de classes Seeder encontradas.
    """
    seeder_classes = []
    for filename in sorted(os.listdir(seed_dir)):
        if filename.endswith('.py') and filename not in ('__init__.py', 'BaseSeeder.py'):
            module_name = filename[:-3]
            module_path = os.path.join(seed_dir, filename)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            seeder_classes.extend(get_seeder_classes_from_module(module))
    return seeder_classes

# Lista global para armazenar as classes de seeders encontradas
seeders = []

# Para cada app listado em SEEDER_APPS nas configurações do projeto
for app in settings.SEEDER_APPS:
    # Monta o caminho absoluto para a pasta 'seeders' do app
    app_seeders_dir = os.path.join(settings.BASE_DIR, app, 'seeders')
    if os.path.isdir(app_seeders_dir):
        # Lista e ordena alfabeticamente todos os arquivos Python na pasta de seeders
        seeders.extend(load_seeders_from_dir(app_seeders_dir))

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