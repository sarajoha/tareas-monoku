from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Reservation(models.Model):
    MOTIVE_CHOICES = ((STANDUP, 'Stand Up'), (CLASS, 'Clase'), )

    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    end_time = models.TimeField() #time start + duration
    motive = models.CharField(choices=MOTIVE_CHOICES) #which choices?
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def calculate_time_end(self): #not sure if this works
        self.time_end = self.time_start + self.duration

    def __str__(self):
        return f'{self.motive} {self.date_time}'


#user makes a reservation through a form
