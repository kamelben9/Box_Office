# Generated by Django 4.2.11 on 2024-05-22 15:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActeursFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acteur', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'acteurs_films',
            },
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='film',
        ),
        migrations.RenameField(
            model_name='boxoffice',
            old_name='boxoffice',
            new_name='box_office_first_week',
        ),
        migrations.AddField(
            model_name='boxoffice',
            name='box_office_title',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='box_office_first_week',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='budget',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='film',
            name='press_eval',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='viewers_eval',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='film',
            name='views',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boxoffice',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boxoffice', to='monapp.film'),
        ),
        migrations.AlterModelTable(
            name='film',
            table='films',
        ),
        migrations.DeleteModel(
            name='Acteurs_films',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.DeleteModel(
            name='Prediction',
        ),
        migrations.AddField(
            model_name='acteursfilm',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acteurs', to='monapp.film'),
        ),
    ]
