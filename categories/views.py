from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from.models import *

# Create your views here.

def show_categories(request):
    
    return render(request, 'categories/categories.html',{"categories" : Category.AllCategory()})


def add_category(request):
    if request.method == "POST":
        name = request.POST['category']
        category = Category(name=name)
        category.save()
        return HttpResponseRedirect(reverse('categories'))
    
    return render(request, 'categories/addcategory.html')


def show_category(request, id):
    category = Category.get_category(id)
    if category:
        return render(request,'categories/showcategory.html',{'category':category})
    else:
        return render(request, "notfound.html")

def delete_category(request, id):
    Category.delete_category(id)
    return HttpResponseRedirect(reverse("categories"))

def update_category(request, id):
    if request.method == "POST":
        new_name = request.POST["new_name"]
        Category.objects.filter(id=id).update(name=new_name)
        return HttpResponseRedirect(reverse('categories'))
    
    return render(request,'categories/updatecategory.html',{'category':Category.get_category(id)})


