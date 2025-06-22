import unittest
import os
import shutil
from types import SimpleNamespace
from jessilver_django_seed.management.commands.seeder_creation import create_seeder

class DummyStyle:
    def SUCCESS(self, msg):
        return msg
    def ERROR(self, msg):
        return msg

class DummyStdout:
    def __init__(self):
        self.messages = []
    def write(self, msg):
        self.messages.append(msg)

class TestSeederCreation(unittest.TestCase):
    def setUp(self):
        self.base_dir = 'tests/tmp_app'
        self.app_name = 'myapp'
        self.settings_path = os.path.join(self.base_dir, 'settings.py')
        os.makedirs(os.path.join(self.base_dir, self.app_name), exist_ok=True)
        with open(self.settings_path, 'w') as f:
            f.write("SEEDER_APPS = []\n")
        self.settings = SimpleNamespace(BASE_DIR=self.base_dir)
        self.style = DummyStyle()
        self.stdout = DummyStdout()

    def tearDown(self):
        shutil.rmtree(self.base_dir)

    def test_create_seeder_success(self):
        result = create_seeder(self.app_name, 'UserSeeder', self.settings, self.style, self.stdout)
        self.assertTrue(result)
        seeder_file = os.path.join(self.base_dir, self.app_name, 'seeders', 'UserSeeder.py')
        self.assertTrue(os.path.exists(seeder_file))
        with open(self.settings_path) as f:
            self.assertIn(self.app_name, f.read())

    def test_create_seeder_already_exists(self):
        create_seeder(self.app_name, 'UserSeeder', self.settings, self.style, self.stdout)
        result = create_seeder(self.app_name, 'UserSeeder', self.settings, self.style, self.stdout)
        self.assertFalse(result)
        self.assertIn("already exists", ''.join(self.stdout.messages))

    def test_create_seeder_invalid_class_name(self):
        result = create_seeder(self.app_name, 'userSeeder', self.settings, self.style, self.stdout)
        self.assertFalse(result)
        self.assertIn("not a valid Python class name", ''.join(self.stdout.messages))

    def test_create_seeder_app_not_found(self):
        result = create_seeder('noapp', 'UserSeeder', self.settings, self.style, self.stdout)
        self.assertFalse(result)
        self.assertIn("does not exist", ''.join(self.stdout.messages))

    def test_create_seeder_no_seeder_apps(self):
        # Remove SEEDER_APPS from settings.py
        with open(self.settings_path, 'w') as f:
            f.write("# no SEEDER_APPS here\n")
        result = create_seeder(self.app_name, 'UserSeeder', self.settings, self.style, self.stdout)
        self.assertFalse(result)
        self.assertIn("SEEDER_APPS not found", ''.join(self.stdout.messages))
