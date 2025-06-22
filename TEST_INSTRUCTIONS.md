# Test Instructions

This file contains instructions for running automated tests for the `jessilver_django_seed` package.

## Prerequisites
- Python environment set up (see BUILD_INSTRUCTIONS.md)
- Dependencies installed (`pip install -r requirements.txt`)

## Django Test Configuration
Some tests require Django and minimal settings. A test settings file is provided at `tests/django_test_settings.py`.

Before running tests, set the environment variable:
```bash
export DJANGO_SETTINGS_MODULE=tests.django_test_settings
```

## Recommended: Running All Tests with pytest
`pytest` is the recommended test runner for this project. It provides better output and test discovery.

To avoid import errors, set the `PYTHONPATH` to the project root:
```bash
export PYTHONPATH=.
pytest --maxfail=1 --disable-warnings -q
```

## Running Individual Tests with pytest
```bash
pytest tests/test_base_seeder.py
pytest tests/test_seed_command.py
pytest tests/test_seed_command_only.py
```

## Alternative: Running with unittest
You can also use Python's built-in unittest:
```bash
python -m unittest discover tests
```
Or run individual tests:
```bash
python -m unittest tests/test_base_seeder.py
python -m unittest tests/test_seed_command.py
python -m unittest tests/test_seed_command_only.py
```

## Selective Seeder Execution
The test `test_seed_command_only.py` covers the use of the `--only` argument to run specific seeders.

## Notes
- This file is **not** included in the build/distribution of the package, as it is not listed in `MANIFEST.in`.
- Keep this file updated to facilitate collaboration.
