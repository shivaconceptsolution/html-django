from django.db import models
class Registration(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    def __str__(self):
        return "username is "+str(self.username) + " password is "+str(self.password)

class Student(models.Model):
    rno=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    def __str__(self):
        return "rno is "+ self.rno + " sname is "+self.sname
