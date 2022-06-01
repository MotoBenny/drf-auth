from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.


class Moto(models.Model):
    moto_brands = [('KTM', 'KTM'), ('YAMAHA', 'YAMAHA'),
                   ('Ducati', 'Ducati'), ('Husqvarna', 'Husqvarna'),
                   ('Aprilia', 'Aprilia'), ('MV Agusta', 'MV Agusta')]
    years = [('2022', '2022'), ('2021', '2021'), ('2020', '2020'),
             ('2019', '2019'), ('2018', '2018'), ('2017', '2017'),
             ('2016', '2016'), ('2015', '2015'), ('2014', '2014'),
             ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010')]
    # choices=moto_brands,

    model = models.CharField(max_length=64)
    brand = models.CharField(max_length=64, choices=moto_brands)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    engine_size = models.CharField(max_length=4)
    year = models.CharField(max_length=4, choices=years)

    def __str__(self):
        return self.model
