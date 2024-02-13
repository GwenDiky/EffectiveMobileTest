from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Catalog
from .forms import CatalogForm
# Create your views here.

class CatalogList(ListView):
    model = Catalog
    paginate_by = 1
    context_object_name = "catalogs"

class CatalogCreateView(CreateView):
    model = Catalog
    form_class = CatalogForm
    success_url = reverse_lazy("catalog")

class CatalogCreateView(CreateView):
    model = Catalog
    form_class = CatalogForm
    success_url = reverse_lazy("catalog")


class CatalogUpdateView(UpdateView):
    model = Catalog
    form_class = CatalogForm
    success_url = reverse_lazy("catalog")


class SearchResultsView(ListView):
    model = Catalog
    context_object_name = "catalogs"

    def get_queryset(self):
        query = self.request.GET.get("title")
        if query:
            object_list = Catalog.objects.filter(
                Q(surname__icontains=query) |
                Q(name__icontains=query) |
                Q(patronymic__icontains=query) |
                Q(organisation__icontains=query) |
                Q(work_phone__icontains=query) |
                Q(personal_phone__icontains=query)
            )
            return object_list
        else:
            return Catalog.objects.all()