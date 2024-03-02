from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)


    def  __str__(self):
        return self.name
    
    @classmethod
    def AllCategory(cls):
        return cls.objects.all()
    
    @classmethod
    def  get_category(cls,id):
        return Category.objects.get(id=id)
    
    @classmethod
    def  delete_category(cls,id):
        return Category.objects.filter(id=id).delete()

    @classmethod
    def showCategory(cls):
        return [(i.id, i.name) for i in cls.objects.all()]

