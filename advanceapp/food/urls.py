from django.urls import path
from . import views

app_name = "food"
urlpatterns = [
    path("", views.index, name="index"),
    # path("", views.IndexView.as_view(), name="index"),
    # path("details/<int:item_id>/", views.details, name="details"),
    path("details/<int:pk>/", views.DetailItemView.as_view(), name="details"),
    # path("add/", views.add, name="add"),
    path("add/", views.AddItemView.as_view(), name="add"),
    path("update/<int:item_id>/", views.update, name="update"),
    # path("update/<int:pk>/", views.ItemUpdateView.as_view(), name="update"),
    # path("delete/<int:item_id>", views.delete, name="delete"),
    path("delete/<int:pk>/", views.ItemDeleteView.as_view(), name="delete")
]