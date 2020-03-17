from django.shortcuts import render
from django.http import HttpResponse
from .models import Furniture
from django.core import serializers
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from collections.abc import Iterable
from . forms import FurnitureForm
from django.shortcuts import render


# Create your views here.


def serialize_data(queryset):
    if isinstance(queryset, Iterable):
        return serializers.serialize('json', queryset)
    else:
        return serializers.serialize('json', [ queryset ])


def create_furniture(request):
    make = request.GET.get('make')
    model = request.GET.get('model')
    description = request.GET.get('description ')
    price = request.GET.get('price')
    image_url = request.GET.get('image_url')
    material = request.GET.get('material')

    furniture = Furniture('make=make','model=model', 'description=description', 'price=price', 'image_url=image_url', 'material=material')
    furniture.save()
    return HttpResponse('create')

def edit_furniture(request, furniture_id):
    furniture = Furniture.objects.get(pk=furniture_id)
    make = request.GET.get('make')
    furniture.make = make
    return HttpResponse('created')

def delete_furniture(request, furniture_id):
    Furniture.objects.get(pk=furniture_id).delete()

def get_all_furniture(request):
    make = request.GET.get('make')
    if make:
        furnitures = Furniture.objects.all().filter(make=make)
        return HttpResponse(serialize_data(furnitures))
    furnitures = Furniture.objects.all()
    return HttpResponse(serialize_data(furnitures))


def get_furniture(request, furniture_id):
    furniture = Furniture.objects.get(pk=furniture_id)
    return HttpResponse(serialize_data(furniture))


def get_all_wooden(request):
    wooden = Furniture.objects.filter(material='W')
    return HttpResponse(serialize_data(wooden))


def order_furniture(request):
    furniture = Furniture.objects.all().order_by('model')
    return HttpResponse(serialize_data(furniture))

def create_furniture_form(request):

    if request.method == 'GET':
        form = FurnitureForm()
        context = {'form': form}
        return render(request, 'create.html', context)

    elif request.method == 'POST':
        form = FurnitureForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('saved')
        else:
            print(form.is_valid())
            return HttpResponse('not valid')


def read_furniture_data(request, furniture_id=None):
    if furniture_id:
        return get_furniture(request, furniture_id)
    furnitures = Furniture.objects.all()
    return render(request, 'furniture_list.html', {'furniture': furnitures})


class FurnitureList(ListView):
    model = Furniture
    template_name = 'furniture_list.html'
    context_object_name = "furnitures"


class FurnitureCreate(CreateView):
    model = Furniture
    form_class = FurnitureForm
    template_name = 'create.html'
    success_url = '/furniture/all/'


class FurnitureDetail(DetailView):
    model = Furniture
    template_name = 'furniture_detail.html'


class FurnitureUpdate(UpdateView):
    model = Furniture
    template_name = 'create.html'
    form_class = FurnitureForm
    success_url = '/furniture/all/'


class DeleteFurniture(DeleteView):
    model = Furniture
    template_name = 'furniture_delete.html'
    success_url = '/furniture/all/'