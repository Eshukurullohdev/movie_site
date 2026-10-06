from django.db import models

class Main_banner(models.Model):
    img = models.ImageField(upload_to='main_banners/', blank=True, null=True)
    description = models.TextField()


    def __str__(self):
        return self.description

class Yili(models.Model):
    yil = models.IntegerField()

    def __str__(self):
        return str(self.yil)
class Davlati(models.Model):
    davlati = models.TextField()

    def __str__(self):
        return self.davlati
    
class Janri(models.Model):
    janri = models.TextField()

    def __str__(self):
        return self.janri
    
class Catalog(models.Model):
    catalog = models.TextField()

    def __str__(self):
        return self.catalog

class Movie(models.Model):
    img = models.ImageField(upload_to='top_banners/', blank=True, null=True)
    davlati = models.ForeignKey(Davlati, on_delete=models.CASCADE, blank=True, null=True)
    janri = models.ForeignKey(Janri, on_delete=models.CASCADE, blank=True, null=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, blank=True, null=True)
    nomi = models.TextField()
    davomiyligi = models.TextField()
    yosh = models.IntegerField()
    qisqa = models.TextField()
    tavsifi = models.TextField()
    is_serial = models.BooleanField(default=False)
    is_film = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.nomi
