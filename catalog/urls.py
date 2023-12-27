from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('categories/<category_id>', views.get_category, name='category'),
    path('<brand_id>/<product_id>', views.get_product_with_offers, name='offer'),
]
