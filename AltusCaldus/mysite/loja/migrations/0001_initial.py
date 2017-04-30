# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
                ('desconto', models.IntegerField()),
                ('lucro', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('data', models.DateField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Historico_Entrada',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('valor', models.FloatField()),
                ('quantidade', models.FloatField()),
                ('id_total', models.ForeignKey(to='loja.Entrada')),
            ],
        ),
        migrations.CreateModel(
            name='Historico_Venda',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('valor', models.FloatField()),
                ('desconto', models.FloatField()),
                ('quantidade', models.FloatField()),
                ('cancelado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('valor_venda', models.FloatField()),
                ('valor_custo', models.FloatField()),
                ('valor_desc', models.FloatField()),
                ('percent_desc', models.IntegerField()),
                ('promocao', models.FloatField()),
                ('qtd_estoque', models.IntegerField()),
                ('grupo', models.ForeignKey(to='loja.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('data', models.DateField()),
                ('total', models.FloatField()),
                ('desconto', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='historico_venda',
            name='id_total',
            field=models.ForeignKey(to='loja.Venda'),
        ),
        migrations.AddField(
            model_name='historico_venda',
            name='produto',
            field=models.ManyToManyField(to='loja.Produto'),
        ),
        migrations.AddField(
            model_name='historico_entrada',
            name='produto',
            field=models.ManyToManyField(to='loja.Produto'),
        ),
    ]
