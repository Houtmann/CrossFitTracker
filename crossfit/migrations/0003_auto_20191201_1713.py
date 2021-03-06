# Generated by Django 2.2.7 on 2019-12-01 17:13

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crossfit', '0002_auto_20191130_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.TextField()),
                ('score_json', django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='ScoreType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='wod',
            old_name='comment',
            new_name='description',
        ),
        migrations.AddField(
            model_name='typeof',
            name='descrition',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wod',
            name='description_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='wod',
            name='mouvements',
            field=models.ManyToManyField(to='crossfit.Mouvement'),
        ),
        migrations.AlterField(
            model_name='wod',
            name='score',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crossfit.Score'),
        ),
        migrations.AddField(
            model_name='score',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crossfit.ScoreType'),
        ),
    ]
