# django_seed

`django_seed` é uma biblioteca para o framework Django que facilita a criação de dados (seeds) para popular o banco de dados durante o desenvolvimento e testes. Com `django_seed`, você pode rapidamente gerar dados realistas para suas aplicações Django, o que é útil para testar funcionalidades e visualizar como a aplicação se comporta com diferentes tipos de dados.

## Funcionalidades

- **Geração de dados fictícios**: Crie dados de teste para seus modelos Django com facilidade.
- **Configuração simples**: Integração fácil com projetos Django existentes.

## Configuração

### Instalação

Instale a biblioteca:

```bash
pip install django_seed
```

### Adição ao Projeto

Adicione `django_seed` em `INSTALLED_APPS` no seu arquivo `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_seed',
]
```

Crie uma constante chamada `SEEDER_APPS` para definir os aplicativos que você deseja popular com dados fictícios:

```python
SEEDER_APPS = [
    'app1',
    'app2',
    ...
]
```

## Uso

### Estrutura de Diretórios

Dentro da pasta dos apps adicionados em `SEEDER_APPS`, crie um diretório chamado `seeders`:

```plaintext
app1/
├── ...
├── seeders/
└── ...
```

### Criação de Seeders

Dentro do diretório `seeders`, você pode criar arquivos para definir os dados que deseja gerar. Por exemplo, um arquivo chamado `user_seeder.py`:

Para criar um seeder, você precisa implementar duas funções principais: `seeder_name` e `seed`. Vou explicar cada uma delas:

1. `seeder_name`

    Esta função é responsável por retornar o nome do seeder. Este nome é geralmente utilizado para identificar o seeder de forma única dentro do sistema. Pode ser útil para fins de organização e para garantir que o seeder correto está sendo executado.

    Exemplo:

    ```python
    def seeder_name():
        return "UserSeeder"
    ```

2. `seed`

    Esta função é onde a lógica de inserção de dados é implementada. Ela é responsável por popular o banco de dados com os dados desejados. A função `seed` geralmente contém comandos para criar registros no banco de dados, utilizando modelos ou queries diretas.

    Exemplo:

    ```python
    def seed():
        users = [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"},
        ]
        for user in users:
            # Supondo que você tenha um modelo User
            User.create(**user)
    ```

Exemplo de um seeder completo:

```python
from django_seed.seeders.BaseSeeder import BaseSeeder
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

Você pode criar vários arquivos ou apenas um contendo várias classes. A única obrigação é que o nome das classes termine com `Seeder`, caso contrário, não funcionará.

Por exemplo, você pode criar um arquivo `seeders.py` com várias classes:

```python
from django_seed.seeders.BaseSeeder import BaseSeeder
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

### Executando os Seeders

Agora, você pode rodar o comando para popular o banco de dados com os dados fictícios:

```bash
python manage.py seed
```
