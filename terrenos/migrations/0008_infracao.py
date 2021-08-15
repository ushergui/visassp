# Generated by Django 3.2.5 on 2021-08-13 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0007_alter_notificacao_cumpriu_notificacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_auto', models.DateField()),
                ('data_inspecao_2', models.DateField()),
                ('horario_inspecao_2', models.TimeField()),
                ('rastreio_infracao', models.CharField(blank=True, max_length=13, null=True)),
                ('data_entrega_autuacao', models.DateField(blank=True, null=True)),
                ('defendeu', models.CharField(choices=[('PENDENTE', 'PENDENTE'), ('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=15)),
                ('notificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terrenos.notificacao')),
            ],
        ),
    ]
