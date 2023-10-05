from django.urls import path
from . import views

urlpatterns = [
    # will add stuff
    path("validate/", views.tokenValidation, name="validate"),
    path("categories/", views.categoryView, name="categories"),
    path("productList/<str:cat_id>/", views.productListView, name="productList"),
    path("product/<str:prod_id>/", views.productView, name="product"),
]