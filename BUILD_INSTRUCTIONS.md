# Build Instructions

Este arquivo contém instruções para build e instalação do pacote `jessilver_django_seed` em ambientes de desenvolvimento e produção.

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
4. (Recomendado) Limpe a pasta dist antes de gerar um novo build:
   ```bash
   rm -rf dist/*
   ```
5. Gere o build do pacote (sdist e wheel):
   ```bash
   python -m build
   ```
   Os arquivos gerados estarão na pasta `dist/`.
6. (Opcional) Instale o pacote localmente para testes:
   ```bash
   pip install dist/jessilver_django_seed-<versao>.whl
   # ou
   pip install dist/jessilver_django_seed-<versao>.tar.gz
   ```
7. (Opcional) Publique no PyPI:
   ```bash
   twine upload dist/*
   ```

## Testes

Para rodar todos os testes, execute:
```bash
export DJANGO_SETTINGS_MODULE=tests.django_test_settings
export PYTHONPATH=.
pytest --maxfail=1 --disable-warnings -q
```

Ou para rodar um teste específico:
```bash
pytest tests/test_base_seeder.py
pytest tests/test_seed_command.py
pytest tests/test_seed_command_only.py
```

## Execução seletiva de seeders

Você pode rodar apenas seeders específicos usando o argumento `--only`:
```bash
python manage.py seed --only UserSeeder,ProductSeeder
```

## Observações
- Este arquivo **não** será incluído no build/distribuição do pacote, pois não está listado no `MANIFEST.in`.
- Mantenha este arquivo atualizado para facilitar a colaboração.
