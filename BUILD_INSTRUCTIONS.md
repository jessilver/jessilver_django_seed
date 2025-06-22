# Build Instructions

Este arquivo contém instruções **apenas para build e publicação** do pacote `jessilver_django_seed`.

## Pré-requisitos
- Python 3.7+
- pip
- (Opcional) Ambiente virtual Python
- Conta no PyPI (https://pypi.org/)
- Token de API do PyPI (veja instruções abaixo)

## Passos para build e publicação

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
3. Instale as dependências de build:
   ```bash
   pip install -r requirements.txt
   pip install build twine
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
6. (Opcional) Teste o pacote localmente:
   ```bash
   pip install dist/jessilver_django_seed-<versao>.whl
   # ou
   pip install dist/jessilver_django_seed-<versao>.tar.gz
   ```
7. Configure seu token do PyPI:
   - Gere um token em https://pypi.org/manage/account/#api-tokens
   - Crie/edite o arquivo `~/.pypirc` com:
     ```ini
     [distutils]
     index-servers =
         pypi

     [pypi]
     username = __token__
     password = pypi-SEU_TOKEN_AQUI
     ```
8. Publique no PyPI:
   ```bash
   twine upload dist/*
   ```

Pronto! Seu pacote estará disponível no PyPI.
