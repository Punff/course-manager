# Generated by Django 4.2.11 on 2024-06-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upis', '0002_alter_korisnik_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='predmet',
            name='ects',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predmet',
            name='izborni',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predmet',
            name='kod',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predmet',
            name='program',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predmet',
            name='sem_izv',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predmet',
            name='sem_red',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]