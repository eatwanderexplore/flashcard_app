from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        view.CardListView.as_view(),
        name="card-list"
    ),
]