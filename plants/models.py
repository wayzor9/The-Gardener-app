from django.db import models
from django.conf import settings

from dynamic_filenames import FilePattern
from model_utils import Choices
from model_utils.models import TimeStampedModel
from stdimage import StdImageField


class Plant(TimeStampedModel):
    name = models.CharField(max_length=200)
    plant = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class CommonName(TimeStampedModel):
    name = models.CharField(max_length=200)
    plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, related_name="common_names"
    )

    def __str__(self):
        return self.name


upload_to_pattern = FilePattern(
    filename_pattern="plant_{uuid:base64}{ext}"
)


class Picture(TimeStampedModel):
    image = StdImageField(
        upload_to=upload_to_pattern,
    )
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True, blank=True ,related_name="pictures")


class Description(models.Model):
    # choices
    DURATION = Choices("annual", "biennial", "perennial")
    TOXICITY = Choices(('none', "none"), ('low',"low"), ('medium', "medium"), ('high', "high"))

    plant = models.OneToOneField(Plant, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    # specifications
    duration = models.CharField(max_length=10, choices=DURATION, blank=True)
    growth_habit = models.CharField(max_length=250, blank=True)
    growth_rate = models.CharField(max_length=250, blank=True)
    average_height = models.CharField(max_length=250, blank=True)
    maximum_height = models.CharField(max_length=250, blank=True)
    toxicity = models.CharField(
        max_length=6, choices=TOXICITY, blank=True, default=TOXICITY.none
    )
    # growth
    sowing = models.CharField(max_length=250, blank=True)
    ph_maximum = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True
    )
    ph_minimum = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True
    )
    light = models.IntegerField(blank=True, null=True)  # 0 > 10
    atmospheric_humidity = models.IntegerField(blank=True, null=True)
    growth_months = models.CharField(max_length=200, blank=True)
    bloom_months = models.CharField(max_length=200, blank=True)
    fruit_months = models.CharField(max_length=200, blank=True)
    minimum_precipitation = models.CharField(max_length=250, blank=True)
    maximum_precipitation = models.CharField(max_length=250, blank=True)
    minimum_temperature = models.CharField(max_length=250, blank=True)
    soil_nutriments = models.IntegerField(blank=True, null=True)  # 0 > 10
    soil_salinity = models.IntegerField(blank=True, null=True)  # 0 > 10
    soil_texture = models.IntegerField(blank=True, null=True)  # 0 > 10
    soil_humidity = models.IntegerField(blank=True, null=True)  # 0 > 10

    def __str__(self):
        return f"{self.plant.name}"


class Service(TimeStampedModel):
    name = models.CharField(max_length=200)
    internal_id = models.IntegerField()
    external_id = models.IntegerField()
