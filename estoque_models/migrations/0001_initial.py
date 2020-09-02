# Generated by Django 3.0.8 on 2020-07-30 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=255)),
                ('complemento', models.TextField(null=True)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('endereco_entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venda', to='estoque_models.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=0)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendas', to='estoque_models.Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='estoque_models.Venda')),
            ],
        ),
    ]