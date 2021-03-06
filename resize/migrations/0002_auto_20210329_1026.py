# Generated by Django 3.1.7 on 2021-03-29 04:56

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('resize', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='img',
            field=models.ImageField(upload_to='media/resize/'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='post_image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=0, size=[200, 200], upload_to='media/resize/'),
        ),
    ]
