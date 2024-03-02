from django.urls import path
from.views import *

urlpatterns = [
    path("", show_categories, name="categories"),
    path("addcategory/",  add_category, name='addcategory'),
    path("category/<int:id>/", show_category, name="category"),
    path("deletecategory/<int:id>/", delete_category, name="deletecategory"),
    path("updatecategory/<int:id>/", update_category, name="updatecategory"),
]