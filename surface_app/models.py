from django.db import models



class SurfaceLocation(models.Model):
    name: models.CharField = models.CharField(max_length=255, verbose_name='Местоположение')
    # is_active: models.BooleanField = models.BooleanField(verbose_name='Активно', default=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'
    def __str__(self):
        return self.name
    

# Create Surface model
class Surface(models.Model):
    # This is the surface model that will be used in the app
    name: models.CharField = models.CharField(max_length=255, verbose_name='Рекламная поверхность')
    description: models.TextField = models.TextField(verbose_name='Описание')
    width: models.IntegerField = models.IntegerField(verbose_name='Ширина')
    height: models.IntegerField = models.IntegerField(verbose_name='Высота')
    base_production_price: models.PositiveIntegerField = models.PositiveIntegerField(verbose_name='Базовая цена',)
    base_installation_price: models.PositiveIntegerField = models.PositiveIntegerField(verbose_name='Базовая цена монтажа',)
    base_dismantling_price: models.PositiveIntegerField = models.PositiveIntegerField(verbose_name='Базовая цена демонтажа',)
    overhead_costs: models.PositiveIntegerField = models.PositiveIntegerField(verbose_name='Накладные расходы', default=0)
    location: models.ForeignKey = models.ForeignKey(
        SurfaceLocation, on_delete=models.PROTECT, verbose_name='Местоположение'
    )
    is_active: models.BooleanField = models.BooleanField(verbose_name='Активно', default=True)


    class Meta:
        verbose_name = 'Рекламная поверхность'
        verbose_name_plural = 'Рекламные поверхности'
    
    def __str__(self):
        return self.name
    
    def get_area(self):
        # '''
        # This function returns surface area in square meters.
        # '''
        return round(self.width * self.height / 1_000_000, 2)
    

class SurfaceImage(models.Model):
    surface: models.ForeignKey = models.ForeignKey(
        Surface, on_delete=models.CASCADE
    )
    image: models.ImageField = models.ImageField(upload_to='surface_images/', verbose_name='Изображение')
