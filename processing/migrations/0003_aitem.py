# Generated by Django 4.2.7 on 2023-12-09 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0002_alter_url_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='AItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element', models.TextField()),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processing.url')),
            ],
        ),
    ]
