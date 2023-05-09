from django.db import models

# Create your models here.

class Hra(models.Model):
    nazev = models.CharField(max_length=50, verbose_name='Název hry', help_text='Zadejte název hry', unique=True, blank=False, null=False)
    cena = models.PositiveIntegerField(verbose_name='Cena hry', help_text='Zadejte cenu hry', blank=False, null=False)
    datumVydani = models.DateField(verbose_name='Datum vydání hry', help_text='Zadejte datum vydání hry', null=False, blank=False)
    popisek = models.TextField(verbose_name='Popisek hry', help_text='Zadejte popisek hry', blank=True, null=True)
    vyvojar = models.ForeignKey('Vyvojar', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Vývojář')
    kategorie = models.ManyToManyField('Kategorie', blank=True, verbose_name='Kategorie')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Hra'
        verbose_name_plural = 'Hry'

    def __str__(self):
        return f'{self.nazev}'


class Vyvojar(models.Model):
    jmenoVyvojare = models.CharField(max_length=45, verbose_name='Jméno vývojáře', help_text='Zadejte jméno vývojáře', unique=True, blank=False, null=False)
    web = models.CharField(max_length=250, verbose_name='Webová stránka vývojáře', help_text='Zadejte odkaz na webovou stránku vývojáře', null=True, blank=True, unique=True)
    pocetVydanychHer = models.PositiveBigIntegerField(verbose_name='Počet vydaných her', help_text='Zadejte počet vydaných her', null=False, blank=False, default=0)

    class Meta:
        ordering = ['jmenoVyvojare']
        verbose_name = 'Vývojář'
        verbose_name_plural = 'Vývojáři'

    def __str__(self):
        return f'{self.jmenoVyvojare}'


class Kategorie(models.Model):
    nazevKategorie = models.CharField(max_length=45, verbose_name='Kategorie', help_text='Zadejte název kategorie', blank=False, null=False, unique=True)

    class Meta:
        ordering = ['nazevKategorie']
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return f'{self.nazevKategorie}'