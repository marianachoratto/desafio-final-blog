# Generated by Django 4.2.11 on 2024-04-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]