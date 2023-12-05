from djongo import models
from djongo.models.fields import ObjectIdField

class Processed(models.Model):
    _id = ObjectIdField()
    time = models.CharField(max_length=128)
    temperature = models.FloatField()

    class Meta:
        db_table = "processed"
        verbose_name = "Tabo Historical Data"
        verbose_name_plural = "Tabo Historical Data"

    def __str__(self):
        return str(self.time)