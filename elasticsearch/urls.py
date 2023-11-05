from django.urls import path
from .views import VerbVListView, VerbDetailView



urlpatterns = [
    path('verbs/', VerbVListView.as_view(), name='list_view'),
    path('verb_detail/<int:pk>/',VerbDetailView.as_view(), name='detail_view' ),
  
]
