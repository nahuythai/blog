# Generated by Django 3.1 on 2020-08-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='a', upload_to=''),
            preserve_default=False,
        ),
    ]
