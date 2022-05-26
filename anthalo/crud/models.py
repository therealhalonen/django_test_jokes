from django.db import models

class Crud(models.Model):
    name = models.CharField(max_length=300) # name
    def __str__(self):

        return self.name	

    name = models.CharField(max_length=300) # writer
    joke = models.TextField(max_length=300, default="") # joke
    origin = models.IntegerField(default=1900) #origin year
                
    def get_absolute_url(self):
	    return f"/{self.pk}"
