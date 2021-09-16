

from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="MedhubHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUS"),
    path("tracker/", views.tracker, name="TrakingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="Productview"),
    path("checkout/", views.checkout, name="Checkout"),
    path("footer/", views.footer, name="Footer"),


]
