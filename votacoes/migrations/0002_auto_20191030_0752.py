# Generated by Django 2.2.6 on 2019-10-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voto',
            name='situacao',
            field=models.CharField(choices=[('Abster', 'Abster'), ('Aprovar', 'Aprovar'), ('Reprovar', 'Reprovar')], default='Abster', max_length=8),
        ),
    ]
