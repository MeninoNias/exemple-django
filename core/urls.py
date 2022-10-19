from django.urls import path

from core.views import Home, HomeForm, HomeUpdateForm

urlpatterns = [
    path('', Home.as_view(), name='teste'),
    path('create/', HomeForm.as_view(), name='create'),
    path('update/<str:pk>/', HomeUpdateForm.as_view(), name='update'),
]
