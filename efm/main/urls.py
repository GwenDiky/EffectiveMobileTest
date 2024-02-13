from django.urls import path

from .views import CatalogList, CatalogCreateView, CatalogUpdateView, SearchResultsView

urlpatterns = [
    path('', CatalogList.as_view(template_name="catalog_list.html"), name='catalog'),
    path('add', CatalogCreateView.as_view(template_name='add_catalog.html'), name='addition'),
    path('<int:pk>/update', CatalogUpdateView.as_view(template_name='update_catalog.html'), name='updation'),
    path('search', SearchResultsView.as_view(template_name="catalog_list.html"),
         name='search'),
]
