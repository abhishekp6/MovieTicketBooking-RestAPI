from django.db import models

# Create your models here.
class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact_number = models.IntegerField()
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False) # Time when movie show will start
    current_time = models.DateTimeField(auto_now=True, auto_now_add=False) # Time When ticket is booked
    status = models.CharField(max_length=10, default='Active')

    def __str__(self):
        return self.name
