# Generated by Django 5.0.4 on 2024-05-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiodata',
            name='prompt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='audiodata',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
