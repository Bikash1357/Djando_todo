import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')
django.setup()

if __name__ == "__main__":
    call_command('runserver', '0.0.0.0:5000')
