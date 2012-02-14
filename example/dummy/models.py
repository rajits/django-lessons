from django.db import models

class Photo(models.Model):
    name = models.CharField(max_length=128)

class ResourceCarousel(models.Model):
    name = models.CharField(max_length=128)

class Promo(models.Model):
	name = models.CharField(max_length=128)
