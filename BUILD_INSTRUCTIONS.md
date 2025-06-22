# Build Instructions

Este arquivo contém instruções para build e instalação do pacote `jessilver_django_seed` em ambientes de desenvolvimento.

## Pré-requisitos
- Python 3.7+
- pip
- (Opcional) Ambiente virtual Python

## Passos para build local

1. Clone o repositório:
   ```bash
   git clone https://github.com/jessilver/django_seed.git
   cd django_seed
   ```
2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Instale o pacote localmente (modo editável):
   ```bash
   pip install -e .
   ```

## Testes

Para rodar todos os testes, execute:
```bash
export DJANGO_SETTINGS_MODULE=tests.django_test_settings
python -m unittest discover tests
```

Ou para rodar um teste específico:
```bash
python -m unittest tests/test_base_seeder.py
python -m unittest tests/test_seed_command.py
python -m unittest tests/test_seed_command_only.py
```

## Execução seletiva de seeders

Você pode rodar apenas seeders específicos usando o argumento `--only`:
```bash
python manage.py seed --only UserSeeder,ProductSeeder
```

## Observações
- Este arquivo **não** será incluído no build/distribuição do pacote, pois não está listado no `MANIFEST.in`.
- Mantenha este arquivo atualizado para facilitar a colaboração.
