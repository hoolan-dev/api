from django.urls import path

from property.views import PropertyListView, PropertyCreateView

urlpatterns = [
    path('property/list', PropertyListView.as_view(),
         name="property-list"),
    path('property/create', PropertyCreateView.as_view(),
         name="property-list"),
]
