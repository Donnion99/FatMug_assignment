# Generated by Django 5.0.4 on 2024-05-07 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_track', '0009_rename_acknowledgment_date_po_model_acknowledgment_dates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='po_model',
            old_name='acknowledgment_dates',
            new_name='acknowledgment_date',
        ),
    ]
