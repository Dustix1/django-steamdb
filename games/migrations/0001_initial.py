# Generated by Django 3.2.19 on 2023-05-09 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte název hry', max_length=50, unique=True, verbose_name='Název hry')),
                ('cena', models.IntegerField(help_text='Zadejte cenu hry', verbose_name='Cena hry')),
                ('datumVydani', models.DateTimeField(help_text='Zadejte datum vydání hry', verbose_name='Datum vydání hry')),
            ],
            options={
                'verbose_name': 'Hra',
                'verbose_name_plural': 'Hry',
                'ordering': ['nazev'],
            },
        ),
        migrations.CreateModel(
            name='Kategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazevKategorie', models.CharField(help_text='Zadejte název kategorie', max_length=45, unique=True, verbose_name='Kategorie')),
            ],
            options={
                'verbose_name': 'Kategorie',
                'verbose_name_plural': 'Kategorie',
                'ordering': ['nazevKategorie'],
            },
        ),
        migrations.CreateModel(
            name='Vyvojar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmenoVyvojare', models.CharField(help_text='Zadejte jméno vývojáře', max_length=45, unique=True, verbose_name='Jméno vývojáře')),
            ],
            options={
                'verbose_name': 'Jméno vývojáře',
                'verbose_name_plural': 'Jména vývojářů',
                'ordering': ['jmenoVyvojare'],
            },
        ),
        migrations.CreateModel(
            name='HraHasKategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.hra', verbose_name='Hra')),
                ('kategorie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.kategorie', verbose_name='Kategorie')),
            ],
            options={
                'verbose_name': 'Hra má kategorie',
                'verbose_name_plural': 'Hra má kategorie',
                'ordering': ['hra'],
            },
        ),
        migrations.AddField(
            model_name='hra',
            name='vyvojar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.vyvojar', verbose_name='Vývojář'),
        ),
    ]
