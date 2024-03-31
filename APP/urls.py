from django.urls import path 
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path("cart/", views.cart),
    path("",views.home),
    path("about",views.about),
    path("contact",views.contact),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(),name="product-detail")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)