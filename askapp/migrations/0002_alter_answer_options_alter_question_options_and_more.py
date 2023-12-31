# Generated by Django 4.2.6 on 2023-10-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Resposta', 'verbose_name_plural': 'Respostas'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Pergunta', 'verbose_name_plural': 'Perguntas'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=255, verbose_name='Resposta'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=255, verbose_name='Resposta'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=255, verbose_name='Pergunta'),
        ),
    ]
