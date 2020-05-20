# Generated by Django 2.1.15 on 2020-05-19 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_create_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=255, unique=True)),
                ('account', models.CharField(max_length=255)),
                ('date', models.DateField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('type', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
