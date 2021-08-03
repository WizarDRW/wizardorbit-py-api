from django.db import models

class GlobalWarning(models.Model):
    co2 = models.Field()
    nitrous = models.Field()
    methane = models.Field()
    arctic = models.Field()