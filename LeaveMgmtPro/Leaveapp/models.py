from django.db import models


# Create your models here.
class Leavemgmnt(models.Model):
    Name=models.CharField(max_length=120)
    desgination=models.CharField(max_length=120)
    AplyDate = models.DateField()
    toDate=models.DateField()
    Reason = models.CharField(max_length=120)
    days = models.CharField(max_length=120)
    choice = (
        ('pending', 'pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('None', 'None')
    )
    leave_status = models.CharField(max_length=120, choices=choice, default='None')
    Total_leave = models.IntegerField(default=5)

    def __str__(self):
        return self.AplyDate
