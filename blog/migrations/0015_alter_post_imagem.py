# Generated by Django 4.2.11 on 2024-04-12 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagem/'),
        ),
    ]
