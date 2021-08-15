# Generated by Django 3.2.5 on 2021-08-14 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terrenos', '0008_infracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infracao',
            name='data_auto',
            field=models.DateField(verbose_name='Data da autuação'),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='data_entrega_autuacao',
            field=models.DateField(blank=True, null=True, verbose_name='Data da entrega do Auto de infração'),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='data_inspecao_2',
            field=models.DateField(verbose_name='Data da nova infração'),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='defendeu',
            field=models.CharField(choices=[('PENDENTE', 'PENDENTE'), ('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=15, verbose_name='Apresentou defesa?'),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='horario_inspecao_2',
            field=models.TimeField(verbose_name='Horário da infração'),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='notificacao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='terrenos.notificacao'),
        ),
        migrations.AlterField(
            model_name='infracao',
            name='rastreio_infracao',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Código de rastreio'),
        ),
    ]
