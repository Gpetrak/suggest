from django.db import models

class Suggestion(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    organization = models.CharField(max_length=100)
    area = models.CharField(max_length=50)
    email = models.EmailField()
    datetime = models.DateTimeField()
    suggestion = models.TextField()
    

    def __str__(self):
        return "%s - %s" % (self.first_name, self.last_name)
