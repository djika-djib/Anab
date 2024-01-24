# Generated by Django 4.1.3 on 2023-01-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anab_app', '0003_service_partenaire_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateField()),
            ],
        ),
    ]