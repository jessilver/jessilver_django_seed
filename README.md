# jessilver_django_seed

A library to facilitate the creation of fake data (seeds) in Django projects, with custom management commands, modularization, selective seeder execution, and easy integration.

## Installation

Install from PyPI:
```bash
pip install jessilver_django_seed
```

## Requirements
- Python 3.7+
- Django >= 3.2

## Configuration

1. Add `'jessilver_django_seed'` to your `INSTALLED_APPS`.
2. In your `settings.py`, define:
   ```python
   SEEDER_APPS = [
       'your_app_name',
       # ...other apps
   ]
   ```
   Each app directory should contain a `seeders/` folder with your seeder files.

## Seeder Structure

Create Python files in the `seeders/` folder of your app. Example:

```python
# myapp/seeders/UserSeeder.py
from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from myapp.models import User

class UserSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return "UserSeeder"
    def seed(self):
        for i in range(10):
            User.objects.create(username=f'user{i}')
        self.succes("10 users created!")
```

## Seed Command

Run all seeders:
```bash
python manage.py seed
```

### Selective Execution
Run only specific seeders:
```bash
python manage.py seed --only UserSeeder,ProductSeeder
```

## How it works
- The library looks for all apps listed in `SEEDER_APPS`.
- For each app, it dynamically loads all Python files in the `seeders/` folder.
- It searches for classes ending with `Seeder` (exemple `UserSeeder`).


### BaseSeeder
- `seeder_name`: Seeder name (required property).
- `seed()`: Required method where the data creation logic should be implemented.
- `success(message)`: Prints a success message.
- `info(message)`: Prints an info message.
- `warning(message)`: Prints an warning message.
- `debug(message)`: Prints an debug message.

### Seed Command
- Argument `--only`: Runs only the seeders whose class names are provided.
- Interactive confirmation before execution.
- Status messages and summary at the end.

## Examples

### Product Seeder
```python
# myapp/seeders/ProductSeeder.py
from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from myapp.models import Product

class ProductSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return "ProductSeeder"
    def seed(self):
        for i in range(5):
            Product.objects.create(name=f'Product {i}')
        self.succes("5 products created!")
```

### Running only the UserSeeder
```bash
python manage.py seed --only UserSeeder
```

## Contributing

Pull requests are welcome! Open issues for suggestions or problems.

## License
MIT
