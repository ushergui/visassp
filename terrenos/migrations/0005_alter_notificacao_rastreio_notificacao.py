# Generated by Django 3.2.5 on 2021-08-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0004_auto_20210805_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificacao',
            name='rastreio_notificacao',
            field=models.CharField(max_length=13, null=True),
        ),
    ]