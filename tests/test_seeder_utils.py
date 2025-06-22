import unittest
import types
import os
import shutil
from jessilver_django_seed.management.commands import seeder_utils

class DummySeeder:
    pass
class BaseSeeder:
    pass

class TestSeederUtils(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'tests/tmp_seeders'
        os.makedirs(self.test_dir, exist_ok=True)
        # Cria um seeder válido
        with open(os.path.join(self.test_dir, 'MySeeder.py'), 'w') as f:
            f.write('class MySeeder: pass')
        # Cria um BaseSeeder
        with open(os.path.join(self.test_dir, 'BaseSeeder.py'), 'w') as f:
            f.write('class BaseSeeder: pass')
        # Cria um __init__.py
        with open(os.path.join(self.test_dir, '__init__.py'), 'w') as f:
            f.write('')

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_get_seeder_classes_from_module(self):
        module = types.ModuleType('dummy')
        setattr(module, 'MySeeder', DummySeeder)
        setattr(module, 'BaseSeeder', BaseSeeder)
        result = seeder_utils.get_seeder_classes_from_module(module)
        self.assertIn(DummySeeder, result)
        self.assertNotIn(BaseSeeder, result)

    def test_load_seeders_from_dir(self):
        classes = seeder_utils.load_seeders_from_dir(self.test_dir)
        self.assertTrue(any(cls.__name__ == 'MySeeder' for cls in classes))
        self.assertFalse(any(cls.__name__ == 'BaseSeeder' for cls in classes))
