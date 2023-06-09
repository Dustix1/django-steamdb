# Generated by Django 3.2.19 on 2023-05-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_alter_hra_cena'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hrahaskategorie',
            options={'verbose_name': 'Hra má kategorie', 'verbose_name_plural': 'Hra má kategorie'},
        ),
        migrations.RemoveField(
            model_name='hrahaskategorie',
            name='hra',
        ),
        migrations.AddField(
            model_name='hrahaskategorie',
            name='hra',
            field=models.ManyToManyField(blank=True, null=True, to='games.Hra', verbose_name='Hra'),
        ),
        migrations.RemoveField(
            model_name='hrahaskategorie',
            name='kategorie',
        ),
        migrations.AddField(
            model_name='hrahaskategorie',
            name='kategorie',
            field=models.ManyToManyField(blank=True, null=True, to='games.Kategorie', verbose_name='Kategorie'),
        ),
    ]
