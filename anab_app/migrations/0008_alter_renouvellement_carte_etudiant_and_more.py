# Generated by Django 4.1.3 on 2023-01-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anab_app', '0007_renouvellement_carte_etudiant_renouvellement_recu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renouvellement',
            name='Carte_etudiant',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='renouvellement',
            name='Recu',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='renouvellement',
            name='Releve_Notes',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
