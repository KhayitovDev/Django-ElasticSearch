from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import filters
from django.db.models import Q
from django.http import HttpResponseNotFound



from .serializers import VerbSerializer
from .models import Verb



class VerbVListView(ListAPIView):
    serializer_class=VerbSerializer
    queryset=Verb.objects.all()
    filter_backends=[filters.SearchFilter]
    search_fields=['first_form', 'second_form', 'third_form', 'translation_to_uzbek']
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({'detail': 'Not  results found'}, status=404)


class VerbDetailView(RetrieveAPIView):
    serializer_class=VerbSerializer
    queryset=Verb.objects.all()
    lookup_field='pk'

