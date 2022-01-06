from django.urls import path, include

from .views import RecordList, RecordCreate

urlpatterns = [
    path('new/', RecordCreate.as_view()),
    path('all/', RecordList.as_view()),
]
