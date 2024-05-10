# Generated by Django 5.0.4 on 2024-05-07 12:14

import uuid
from django.db import migrations


def gen_uuid(apps, schema_editor):
    PO_MODEL = apps.get_model("order_track", "PO_MODEL")
    for row in PO_MODEL.objects.all():
        row.uuid = uuid.uuid4()
        print(f'Seetting{row.uuid} on {row.pk}')
        row.save(update_fields=["uuid"])

class Migration(migrations.Migration):

    dependencies = [
        ('order_track', '0006_alter_po_model_po_number'),
    ]

    operations = [
          # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
