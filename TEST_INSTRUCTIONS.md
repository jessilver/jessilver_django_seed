# Test Instructions

Este arquivo contém instruções para rodar os testes automatizados do pacote `jessilver_django_seed`.

## Pré-requisitos
- Ambiente Python configurado (veja BUILD_INSTRUCTIONS.md)
- Dependências instaladas (`pip install -r requirements.txt`)

## Configuração do Django para Testes
Alguns testes dependem do Django e de configurações mínimas. Já existe um arquivo de settings de teste em `tests/django_test_settings.py`.

Antes de rodar os testes, exporte a variável de ambiente:
```bash
export DJANGO_SETTINGS_MODULE=tests.django_test_settings
```

## Rodando todos os testes
```bash
python -m unittest discover tests
```

## Rodando testes individuais
```bash
python -m unittest tests/test_base_seeder.py
python -m unittest tests/test_seed_command.py
```

## Observações
- Este arquivo **não** será incluído no build/distribuição do pacote, pois não está listado no `MANIFEST.in`.
- Mantenha este arquivo atualizado para facilitar a colaboração.
