import os
import ast
import astor

def create_seeder(app, create, settings, style, stdout):
    """
    Creates a new seeder file in the specified app, adds the app to SEEDER_APPS in settings.py if needed
    using AST parsing for robustness, and creates the seeders directory if it does not exist.
    Returns True if created, False otherwise.
    """
    app_path = os.path.join(settings.BASE_DIR, app)
    if not os.path.isdir(app_path):
        stdout.write(style.ERROR(f"App '{app}' does not exist."))
        return False
    settings_path = os.path.join(settings.BASE_DIR, 'settings.py')
    with open(settings_path, 'r') as f:
        settings_content = f.read()
    # Parse settings.py using AST
    tree = ast.parse(settings_content)
    seeder_apps_found = False
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == 'SEEDER_APPS':
                    seeder_apps_found = True
                    if isinstance(node.value, ast.List):
                        # Use ast.Constant for Python 3.8+ compatibility
                        existing_apps = [elt.value for elt in node.value.elts if isinstance(elt, ast.Constant) and isinstance(elt.value, str)]
                        if app not in existing_apps:
                            node.value.elts.append(ast.Constant(value=app))
                            with open(settings_path, 'w') as f:
                                f.write(astor.to_source(tree))
                            stdout.write(style.SUCCESS(f"App '{app}' added to SEEDER_APPS in settings.py."))
                    break
    if not seeder_apps_found:
        stdout.write(style.ERROR("SEEDER_APPS not found in settings.py."))
        return False
    seeders_dir = os.path.join(app_path, 'seeders')
    if not os.path.isdir(seeders_dir):
        os.makedirs(seeders_dir)
        stdout.write(style.SUCCESS(f"Created directory: {seeders_dir}"))
    seeder_file = os.path.join(seeders_dir, f"{create}.py")
    if os.path.exists(seeder_file):
        stdout.write(style.ERROR(f"Seeder '{create}' already exists in app '{app}'."))
        return False
    # Validate seeder class name
    if not create.isidentifier() or not create[0].isupper():
        stdout.write(style.ERROR(f"'{create}' is not a valid Python class name (should be CamelCase and a valid identifier)."))
        return False
    example = f"""from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder\n\nclass {create}(BaseSeeder):\n    @property\n    def seeder_name(self):\n        return \"{create}\"\n    def seed(self):\n        # Add your seeding logic here\n        self.succes(\"{create} executed!\")\n"""
    with open(seeder_file, 'w') as f:
        f.write(example)
    stdout.write(style.SUCCESS(f"Seeder '{create}' created in app '{app}'."))
    return True
