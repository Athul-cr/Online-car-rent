from django.db import models


class HrUserMod(models.Model):
    Name = models.CharField(max_length=120)
    Position = models.CharField(max_length=120)
    Worklocation = models.CharField(max_length=120)
    Age = models.IntegerField()
    Startdate = models.DateField()
    salary = models.IntegerField()
    image = models.ImageField(upload_to="images")
    Edu_qual = models.CharField(max_length=120)
    Experience = models.IntegerField()
    address = models.CharField(max_length=120)
    wrkmail = models.EmailField(max_length=220, unique=True)
    phone = models.IntegerField()

    def __str__(self):
        return self.Name




