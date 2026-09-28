import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='root').exists():
    User.objects.create_superuser('root', 'root@example.com', 'Root@1234')
    print("Superuser 'root' created successfully!")
else:
    u = User.objects.get(username='root')
    u.set_password('Root@1234')
    u.save()
    print("Superuser 'root' password updated to Root@1234 successfully!")
