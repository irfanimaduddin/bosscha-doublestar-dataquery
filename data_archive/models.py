from django.db import models
from django.urls import reverse
from dbview.models import DbView


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    category_sign = models.CharField(max_length=5)
    cat = models.CharField(verbose_name="Category", max_length=12)

    class Meta:
        managed = False
        db_table = 'category'


class Crosscat(models.Model):
    id = models.IntegerField(primary_key=True)
    discoverer = models.CharField(max_length=50)
    jasname = models.CharField(max_length=10)
    ads = models.IntegerField(blank=True, null=True)
    bds = models.IntegerField(blank=True, null=True)
    ids = models.CharField(max_length=10, blank=True, null=True)
    wds = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crosscat'


class Method(models.Model):
    id = models.IntegerField(primary_key=True)
    method_sign = models.CharField(max_length=1)
    method = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'method'


class Objectcat(models.Model):
    crosscat = models.ForeignKey(Crosscat, on_delete=models.DO_NOTHING)
    ra = models.CharField(max_length=5)
    decl = models.CharField(max_length=5)
    gmaga = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    gmagb = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    gaia_sep = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    gaia_pa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    probability = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'objectcat'


class Observeddata(models.Model):
    crosscat = models.ForeignKey(Crosscat, on_delete=models.DO_NOTHING)
    epoch = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    data_pa = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    data_sep = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    count = models.IntegerField()
    observer = models.ForeignKey('Observer', on_delete=models.DO_NOTHING)
    publication = models.ForeignKey('Publication', on_delete=models.DO_NOTHING)
    method = models.ForeignKey(Method, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'observeddata'


class Observer(models.Model):
    id = models.IntegerField(primary_key=True)
    observer_sign = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'observer'


class Publication(models.Model):
    id = models.IntegerField(primary_key=True)
    pub_sign = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'publication'


class MainView(DbView):
    id = models.IntegerField(primary_key=True)
    jasname = models.CharField(verbose_name="JAS97 name", max_length=10)
    discoverer = models.CharField(verbose_name="Discoverer", max_length=50)
    ra = models.CharField(verbose_name="RA (hhmm.m)", max_length=5)
    decl = models.CharField(verbose_name="DEC (ddmm)", max_length=5)
    gmaga = models.DecimalField(verbose_name="Gmag_A", max_digits=4, decimal_places=2, blank=True, null=True)
    gmagb = models.DecimalField(verbose_name="Gmag_B", max_digits=4, decimal_places=2, blank=True, null=True)
    gaia_sep = models.DecimalField(verbose_name="Gaia Sep", max_digits=4, decimal_places=2, blank=True, null=True)
    gaia_pa = models.DecimalField(verbose_name="Gaia PA", max_digits=5, decimal_places=2, blank=True, null=True)
    probability = models.DecimalField(verbose_name="Binary Probability", max_digits=7, decimal_places=4, blank=True, null=True)
    cat = models.CharField(verbose_name="Category", max_length=12)

    class Meta:
        managed = False
        db_table = 'mainview'

    def get_absolute_url(self):
        return reverse("objectpage", kwargs={"discoverer": self.discoverer})


class PageView(DbView):
    id = models.IntegerField(primary_key=True)
    jasname = models.CharField(verbose_name="JAS97 name", max_length=10)
    discoverer = models.CharField(verbose_name="Discoverer", max_length=50)
    ads = models.IntegerField(verbose_name="ADS", blank=True, null=True)
    bds = models.IntegerField(verbose_name="BDS", blank=True, null=True)
    ids = models.CharField(verbose_name="IDS", max_length=10, blank=True, null=True)
    wds = models.CharField(verbose_name="WDS", max_length=10, blank=True, null=True)
    ra = models.CharField(verbose_name="RA (hhmm.m)", max_length=5)
    decl = models.CharField(verbose_name="DEC (ddmm)", max_length=5)
    gmaga = models.DecimalField(verbose_name="Gmag_A", max_digits=4, decimal_places=2, blank=True, null=True)
    gmagb = models.DecimalField(verbose_name="Gmag_B", max_digits=4, decimal_places=2, blank=True, null=True)
    gaia_sep = models.DecimalField(verbose_name="Gaia Sep", max_digits=4, decimal_places=2, blank=True, null=True)
    gaia_pa = models.DecimalField(verbose_name="Gaia PA", max_digits=5, decimal_places=2, blank=True, null=True)
    probability = models.DecimalField(verbose_name="Binary Probability", max_digits=7, decimal_places=4, blank=True, null=True)
    cat = models.CharField(verbose_name="Category", max_length=12)
    epoch = models.DecimalField(verbose_name="Epoch", max_digits=7, decimal_places=3, blank=True, null=True)
    data_pa = models.DecimalField(verbose_name="PA", max_digits=7, decimal_places=4, blank=True, null=True)
    data_sep = models.DecimalField(verbose_name="Sep", max_digits=7, decimal_places=4, blank=True, null=True)
    count = models.IntegerField(verbose_name="Count")
    observer_sign = models.CharField(verbose_name="Observer", max_length=6)
    pub_sign = models.CharField(verbose_name="Publication", max_length=6)
    method_sign = models.CharField(verbose_name="Method", max_length=1)

    class Meta:
        managed = False
        db_table = 'pageview'