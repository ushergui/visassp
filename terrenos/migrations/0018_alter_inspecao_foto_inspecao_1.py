# Generated by Django 3.2.5 on 2021-08-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0017_alter_inspecao_foto_inspecao_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspecao',
            name='foto_inspecao_1',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
