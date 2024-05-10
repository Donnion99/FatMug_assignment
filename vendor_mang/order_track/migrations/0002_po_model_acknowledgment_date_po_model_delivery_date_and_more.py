# Generated by Django 5.0.4 on 2024-05-07 11:41

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_track', '0001_initial'),
        ('vendor_pfp', '0003_alter_vendor_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='po_model',
            name='acknowledgment_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='po_model',
            name='delivery_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='po_model',
            name='issue_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='po_model',
            name='items',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='po_model',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='po_model',
            name='po_number',
            field=models.CharField(default=uuid.uuid4, max_length=72, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='po_model',
            name='quality_rating',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='po_model',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='po_model',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
        migrations.AddField(
            model_name='po_model',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor_pfp.vendor_profile'),
        ),
    ]
