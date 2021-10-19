# Generated by Django 3.2.5 on 2021-08-18 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0011_auto_20210817_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspecao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inspecao', models.DateField()),
                ('horario_inspecao', models.TimeField()),
                ('fiscal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terrenos.fiscal')),
                ('protocolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terrenos.protocolo')),
                ('terreno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terrenos.terreno')),
            ],
        ),
        migrations.DeleteModel(
            name='Imagens',
        ),
    ]