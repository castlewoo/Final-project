from django.db import models

# Create your models here.
class FoodInfoWithTaboo(models.Model):
    food = models.TextField(primary_key = True)
    info = models.TextField(blank=True, null=True)
    ingredient = models.TextField(blank=True, null=True)
    taboo_ingredient = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_info_with_taboo'


class RestaurantInfo(models.Model):
    food = models.TextField(blank=True, null=True)
    store_name = models.TextField(blank=True, null=True)
    addr = models.TextField(blank=True, null=True)
    tel = models.TextField(blank=True, null=True)
    x좌표 = models.FloatField(blank=True, null=True)
    y좌표 = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(primary_key = True)

    class Meta:
        managed = False
        db_table = 'restaurant_info'
    
    
