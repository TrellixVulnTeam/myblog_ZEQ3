# Generated by Django 4.0.5 on 2022-06-08 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_mypost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='image',
            field=models.ImageField(default='defult.jpg', upload_to=''),
        ),
    ]
