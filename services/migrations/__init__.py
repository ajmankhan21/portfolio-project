from django.db import migrations
from django.utils import timezone

def set_created_at(apps, schema_editor):
    Service = apps.get_model('services', 'Service')
    Service.objects.filter(created_at__isnull=True).update(created_at=timezone.now())

class Migration(migrations.Migration):
    dependencies = [
        ('services', '0001_initial'),  # Replace with your last migration
    ]

    operations = [
        migrations.RunPython(set_created_at),
    ]