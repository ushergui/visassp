# Generated by Django 3.2.5 on 2021-08-19 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0012_auto_20210818_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspecao',
            name='foto_inspecao_1',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]