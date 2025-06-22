"""
Testes para execução seletiva do comando seed usando o argumento --only.
"""
import unittest
from unittest.mock import patch, MagicMock
import django
from django.core.management import call_command
from io import StringIO

django.setup()

class TestSeedCommandOnly(unittest.TestCase):
    def test_seed_command_only_executes_selected(self):
        dummy_seeder = MagicMock()
        dummy_seeder.__name__ = 'DummySeeder'
        with patch('builtins.input', return_value='y'), \
             patch('jessilver_django_seed.management.commands.seed.seeders', [dummy_seeder]):
            call_command('seed', only='DummySeeder')
            dummy_seeder().handle.assert_called_once()

    def test_seed_command_only_no_match(self):
        with patch('builtins.input', return_value='y'), \
             patch('jessilver_django_seed.management.commands.seed.seeders', []):
            out = StringIO()
            call_command('seed', only='NonExistentSeeder', stdout=out)
            self.assertIn('No matching seeders found for: NonExistentSeeder', out.getvalue())
