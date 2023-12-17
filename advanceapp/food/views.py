from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.views.generic import ListView, DetailView, CreateView
from .form import ItemForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from rest_framework import viewsets
from .serializers import ItemSerializer
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    item_list = Item.objects.all().order_by("-item_price")

    search_query = request.GET.get("item_name")

    if search_query != "" and search_query is not None:
        item_list = item_list.filter(name__icontains=search_query)

    paginator = Paginator(item_list, 2)
    page = request.GET.get("page")
    item_list = paginator.get_page(page)

    return render(request, "food/index.html", {"item_list": item_list})
    # return HttpResponse("Hello World !")


class IndexView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "item_list"


def details(request, item_id):
    item = Item.objects.get(pk=item_id)

    return render(request, "food/details.html", {"item": item})


class DetailItemView(DetailView):
    model = Item
    template_name = "food/details.html"


def add(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request, "food/add.html", {"form": form})


class AddItemView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "food/add.html"
    success_url = reverse_lazy("food:index")

@login_required
def update(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request, "food/add.html", {"item": item, "form": form})


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "food/add.html"
    success_url = reverse_lazy("food:index")


def delete(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    return render(request, "food/delete.html", {"item": item})


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "food/delete.html"
    success_url = reverse_lazy("food:index")


class IndexViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
