from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)
    def __str__(self):
        return self.name

#to add : anthony.languages.add(python) where anthony and python are objects made before
#to query : anthony.languages.all()      python.programmer_set.all() (because Language doesn't have programmer)


