from django.urls import path
from core import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('/reviews', views.reviews_view, name='reviews'),
    path('/features', views.features_view, name='features'),
    path('/notes', views.notes_view, name='notes'),
]