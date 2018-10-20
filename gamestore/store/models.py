from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'


class Web(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name="Nombre")
    access_key = models.CharField(max_length=255,
                                  verbose_name="Clave de acceso")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'


class Game(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name="Nombre")
    company = models.CharField(max_length=255,
                               null=True,
                               blank=True,
                               verbose_name="Compañía")

    def __str__(self):
        return "%s (%s)" % (self.name, self.company)

    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'


class Bundle(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bundle'
        verbose_name_plural = 'Bundles'


class GameKey(models.Model):
    game = models.ForeignKey(Game,
                             on_delete=models.CASCADE,
                             verbose_name="Juego")
    key = models.CharField(max_length=255,
                           unique=True,
                           verbose_name="Key")
    buyer = models.ForeignKey(Member,
                              on_delete=models.CASCADE,
                              verbose_name="Comprador")
    buy_date = models.DateField(
        verbose_name="Fecha de compra")
    buy_price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Precio de compra")
    minimum_sell_price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Precio mínimo de venta",
        null=True,
        blank=True
    )
    sell_date = models.DateField(
        verbose_name="Fecha de venta",
        null=True,
        blank=True
    )
    sell_price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Precio de venta",
        null=True,
        blank=True
    )
    sell_web = models.ForeignKey(Web,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name="Web de venta")
    bundle = models.ForeignKey(Bundle,
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL,
                               verbose_name="Bundle")

    def __str__(self):
        return "%s - %s" % (self.game.name, self.key)

    @property
    def profit(self):
        return (self.sell_price or 0) - (self.buy_price or 0)

    @property
    def profit_pct(self):
        return self.profit / self.buy_price * 100

    class Meta:
        verbose_name = 'Key'
        verbose_name_plural = 'Keys'
