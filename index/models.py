from django.urls import reverse
from django.db import models
from .utils import code_gen, photo_path
from django.db.models.signals import post_delete, post_save


class District(models.Model):
    folder = 'district'
    name = models.CharField(max_length=255)
    population = models.PositiveIntegerField(
        blank=True, null=True, default=1000)
    map_image = models.ImageField(blank=True, null=True, upload_to=photo_path)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('district-view', kwargs={'pk': self.pk, 'name': self.name})


class Species(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='species/')
    districts = models.ManyToManyField(
        District, blank=True, related_name='species')


class ShapeImage(models.Model):
    folder = "district-maps"
    title = models.CharField(blank=True, null=True, max_length=255)
    name = models.CharField(blank=False, null=False, max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    districts = models.ManyToManyField(
        District, blank=True, related_name='shape_image')
    summary = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, primary_key=False)
    image = models.ImageField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('shape-image', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = code_gen()
        if not self.slug:
            self.slug = "%s-%s" % (self.name.replace(" ", ''), self.code)

        super().save(*args, **kwargs)

    def __str__(self):
        return "%s - %s" % (self.code, self.name)


class Testimony(models.Model):
    author = models.CharField(max_length=200, blank=False, null=False)
    avatar = models.ImageField(
        upload_to='testimony/', blank=True, null=True, default='testimony/avatar.jpg')
    message = models.TextField(blank=False, null=False)
    approved = models.BooleanField(default=True)
    role = models.CharField(max_length=50, blank=True,
                            null=True, default='Developer')

    def __str__(self):
        return self.author


class Member(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    avatar = models.ImageField(
        upload_to='team/', blank=True, null=True, default='avatar.jpg')

    def __str__(self):
        return self.name


class Example(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    summary = models.TextField()
