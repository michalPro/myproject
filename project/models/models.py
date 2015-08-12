from django.db import models

BIKETYPE = \
    (0, 'Sport'),\
    (1, 'No sport'),\
    (2, 'Normal'),


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    text = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title


class Type(models.Model):
    type = models.IntegerField(choices=BIKETYPE, default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __unicode__(self):
        return self.type


class Bike(models.Model):
    name = models.CharField(max_length=20)
    type = models.ForeignKey(Type)

    def __unicode__(self):
        return self.name

