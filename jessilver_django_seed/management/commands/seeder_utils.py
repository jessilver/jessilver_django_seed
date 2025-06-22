import importlib.util
import inspect
import os


def get_seeder_classes_from_module(module):
    """
    Returns all Seeder classes (except BaseSeeder) from a module.
    """
    return [
        obj for name, obj in inspect.getmembers(module, inspect.isclass)
        if name.endswith('Seeder') and name != 'BaseSeeder'
    ]


def load_seeders_from_dir(seed_dir):
    """
    Dynamically loads all Python modules from the seeders directory,
    returning a list of found Seeder classes.
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
