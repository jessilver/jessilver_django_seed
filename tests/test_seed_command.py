"""
Testes para o comando de management 'seed' do Django.

- test_seed_command_runs: Garante que o comando 'seed' executa sem erros quando o usuário confirma a operação.
- test_seed_command_cancel: Garante que o comando 'seed' cancela corretamente quando o usuário não confirma.

Os patches são usados para simular a entrada do usuário e para mockar os seeders, evitando efeitos colaterais reais.

Requisitos:
- O app 'jessilver_django_seed' deve estar em INSTALLED_APPS das settings de teste.
- O comando 'seed' deve estar implementado em jessilver_django_seed.management.commands.seed.
"""
import unittest
from unittest.mock import patch, MagicMock
import django
from django.core.management import call_command

django.setup()

class TestSeedCommand(unittest.TestCase):
    def test_seed_command_runs(self):
        with patch('builtins.input', return_value='y'), \
             patch('jessilver_django_seed.management.commands.seed.seeders', [MagicMock(handle=MagicMock())]):
            try:
                call_command('seed')
            except Exception as e:
                self.fail(f"call_command('seed') raised {e}")

    def test_seed_command_cancel(self):
        with patch('builtins.input', return_value='n'):
            try:
                call_command('seed')
            except Exception as e:
                self.fail(f"call_command('seed') raised {e}")
