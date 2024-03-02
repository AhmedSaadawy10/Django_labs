from django.shortcuts import render,get_object_or_404, redirect,reverse
from django.urls import reverse_lazy
from .models import  *
from django.http import HttpResponseRedirect
from .forms import ProductForm
from django.views.generic import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class Productlist(ListView):
    model = product
    template_name = 'product.html'
    context_object_name = 'data'

class Productdetail(DetailView):
    model = product
    template_name = 'details.html'
    context_object_name = 'product'

class Productupdate(UpdateView):
    model = product
    template_name = 'updateform.html'
    fields = '__all__'
    context_object_name = 'product'
    success_url = reverse_lazy('list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context




class Productadd(CreateView):
    model = product
    template_name = 'addforms.html'
    Form_class = 'form'
    fields = '__all__'
    # context_object_name = 'form'
    success_url = reverse_lazy('list')

class Deleteproduct(DeleteView):
    model = product
    template_name = 'delete.html'
    success_url = reverse_lazy('list')




def listproduct(request) :
    context = {'data': product.objects.all()}
    return render(request,'product.html',context)

def category(request) :
    context = {'data': product.objects.all()}
    return render(request,'category.html',context)

def home(request):
    return render(request,'home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required()
def productdetails(request,id):
    products_id = product.objects.get(id=id)
    context = {'product' : products_id }

    return render(request, 'details.html',context)
def productadd(request) :
    if (request.method == 'POST'):
        pname = request.POST['name']
        pmodel = request.POST['model']
        pprice = request.POST['price']
        ptype = request.POST['type']
        pimage = request.FILES['imge']
        product.objects.create(name=pname,price=pprice,model=pmodel,type=ptype,image=pimage)
        return HttpResponseRedirect(reverse('list'))

    return render(request,'insert.html')




def productaddforms(request):
    form = ProductForm()
    context = {'form': form}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            model = form.cleaned_data['model']
            price = form.cleaned_data['price']
            product_type = form.cleaned_data['type']
            category = Category.objects.get(id=form.cleaned_data['category'])

        try:
            ali = product(name=name, image=image, type=product_type, price=price, model=model, category=category)
            ali.save()
            return HttpResponseRedirect(reverse('list'))
        except :
            context['msg'] = "Name already exists"
            return render(request, 'addforms.html', context)


    return render(request, 'addforms.html', context)

def deleteproduct(request,id):
    product.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('list'))


def updateproduct(request, id):
    if request.method == 'POST':
        pname = request.POST['name']
        pmodel = request.POST['model']
        pprice = request.POST['price']
        ptype = request.POST['type']
        category = Category.objects.get(id=request.POST['category'])

        if 'image' in request.FILES:
            pimage = request.FILES['image']
            product.objects.filter(id=id).update(name=pname, price=pprice, model=pmodel, type=ptype, image=pimage,
                                                 category=category)
        else:
            product.objects.filter(id=id).update(name=pname, price=pprice, model=pmodel, type=ptype, category=category)

        return HttpResponseRedirect(reverse('list'))

    context = {'product': product.objects.get(id=id), 'categories': Category.objects.all()}
    return render(request, 'updateform.html', context)
