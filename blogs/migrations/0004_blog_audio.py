# Generated by Django 5.0.4 on 2024-04-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_remove_blog_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='audio',
            field=models.FileField(default='null', upload_to=''),
            preserve_default=False,
        ),
    ]
