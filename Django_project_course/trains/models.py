from django.db import models
from cities.models import City
from django.core.exceptions import ValidationError

# Create your models here.
class Train(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Номер Поезда')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Откуда', related_name='from_city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Куда', related_name='to_city')
    travel_time = models.IntegerField(verbose_name='Время в пути')

    def clean(self, *args, **kwargs):
        qs = Train.objects.filter(to_city=self.to_city, from_city=self.from_city, travel_time=self.travel_time).exclude(pk=self.pk)
        if len(qs) != 0:
            raise ValidationError("There is a train with this parametrs")
        if self.from_city == self.to_city:
            raise ValidationError("Terminal city can be equal Arrival city")
        return super().clean(*args,**kwargs)

    def __str__(self):
        return f'Train №{self.name} from {self.from_city} to {self.to_city}'
    
    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['name']
