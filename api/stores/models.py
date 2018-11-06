from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# isoweekday
WEEKDAYS = [
    (1, _("Monday")),
    (2, _("Tuesday")),
    (3, _("Wednesday")),
    (4, _("Thursday")),
    (5, _("Friday")),
    (6, _("Saturday")),
    (0, _("Sunday")),
]

class StoreType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.name)

class Store(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=200)
    type = models.ForeignKey(StoreType , on_delete=models.CASCADE);


    def __str__(self):
        return '%s' % (self.name)

class OpeningHours(models.Model):
    store = models.ForeignKey(Store, related_name="OpeningHours", on_delete=models.CASCADE)
    weekday = models.IntegerField(choices=WEEKDAYS)
    opening = models.TimeField()
    closeing = models.TimeField()

    def __str__(self):
        return '%s %s' % (self.weekday, self.store)