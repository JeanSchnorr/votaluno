# Generated by Django 2.2.6 on 2019-11-01 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacoes', '0005_auto_20191031_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voto',
            name='situacao',
            field=models.CharField(choices=[('Reprovar', 'Reprovar'), ('Abster', 'Abster'), ('Aprovar', 'Aprovar')], default='Abster', max_length=8),
        ),
    ]
