from django.db import models
from core import models as core_models

class Review(core_models.TimeStampedModel):

    """ Review model Definition """

    review = models.TextField()
    accuracy = model.IntegerField()
    communication = model.IntegerField()
    clealiness = model.IntegerField()
    location = model.IntegerField()
    check_in = model.IntegerField()
    value = model.IntegerField()
