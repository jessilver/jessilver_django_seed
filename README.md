# jessilver_django_seed

`jessilver_django_seed` is a library for the Django framework that facilitates the creation of data (seeds) to populate the database during development and testing. With `jessilver_django_seed`, you can quickly generate realistic data for your Django applications, which is useful for testing functionalities and visualizing how the application behaves with different types of data.

## Features

- **Fake data generation**: Easily create test data for your Django models.
- **Simple configuration**: Easy integration with existing Django projects.

## Configuration

### Installation

Install the library:

```bash
pip install jessilver_django_seed
```

### Adding to the Project

Add `jessilver_django_seed` to `INSTALLED_APPS` in your `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'jessilver_django_seed',
]
```

Create a constant called `SEEDER_APPS` to define the apps you want to populate with fake data:

```python
SEEDER_APPS = [
    'app1',
    'app2',
    ...
]
```

## Usage

### Directory Structure

Inside the folder of the apps added in `SEEDER_APPS`, create a directory called `seeders`:

```plaintext
app1/
├── ...
├── seeders/
└── ...
```

### Creating Seeders

Inside the `seeders` directory, you can create files to define the data you want to generate. For example, a file called `user_seeder.py`:

To create a seeder, you need to implement two main functions: `seeder_name` and `seed`. I will explain each of them:

1. `seeder_name`

    This function is responsible for returning the name of the seeder. This name is generally used to uniquely identify the seeder within the system. It can be useful for organizational purposes and to ensure that the correct seeder is being executed.

    Example:

    ```python
    def seeder_name():
        return "UserSeeder"
    ```

2. `seed`

    This function is where the data insertion logic is implemented. It is responsible for populating the database with the desired data. The `seed` function usually contains commands to create records in the database, using models or direct queries.

    Example:

    ```python
    def seed():
        users = [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"},
        ]
        for user in users:
            # Assuming you have a User model
            User.create(**user)
    ```

Example of a complete seeder:

```python
from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from django.contrib.auth.models import User

class SuperUserSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'SuperUserSeeder'

    def seed(self):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='123456789',
                first_name='Admin',
                last_name='User'
            )
            self.success(f'Super User created')
        else:
            self.error(f'Super User already exists')
```

You can create multiple files or just one containing multiple classes. The only requirement is that the class names end with `Seeder`, otherwise, it will not work.

For example, you can create a file `seeders.py` with multiple classes:

```python
from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from django.contrib.auth.models import User
from myapp.models import Profile

class SuperUserSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'SuperUserSeeder'

    def seed(self):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='123456789',
                first_name='Admin',
                last_name='User'
            )
            self.success(f'Super User created')
        else:
            self.error(f'Super User already exists')

class ProfileSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'ProfileSeeder'

    def seed(self):
        for user in User.objects.all():
            Profile.objects.get_or_create(user=user, defaults={
                'bio': 'This is a bio',
                'location': 'Unknown'
            })
            self.success(f'Profile created for user {user.username}')
```

### Running the Seeders

Now, you can run the command to populate the database with fake data:

```bash
python manage.py seed
```
