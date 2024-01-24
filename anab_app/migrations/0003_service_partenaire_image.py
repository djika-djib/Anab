# Generated by Django 4.1.3 on 2023-01-24 13:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anab_app', '0002_partenaire_remove_userprofileinfo_portfolio_site_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='partenaire',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]