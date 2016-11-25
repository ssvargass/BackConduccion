from rest_framework import generics
from django.db.models import Count
from conduccion.experto.serializers import FieldTypeSerializer, FieldSerializer, FieldConditionSerializer, ResultSerializer
from conduccion.experto.models import FieldType, Field, FieldCondition, Result
# Create your views here.


class FieldTypeView(generics.ListAPIView):
    serializer_class = FieldTypeSerializer

    def get_queryset(self):
        queryset = FieldType.objects.all()
        name = self.request.GET.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name).distinct()
        return queryset

class FieldView(generics.ListAPIView):
    serializer_class = FieldSerializer

    def get_queryset(self):
        queryset = Field.objects.all()
        pk = self.request.GET.get('pk', None)
        if pk is not None:
            queryset = queryset.filter(id=pk)
        return queryset

class FieldConditionView(generics.ListAPIView):
    serializer_class = FieldConditionSerializer

    def get_queryset(self):
        queryset = FieldCondition.objects.all()
        field = self.request.GET.get('field', None)
        if field is not None:
            queryset = queryset.filter(field=field)
        return queryset

class ResultView(generics.ListAPIView):
    serializer_class = ResultSerializer

    def get_queryset(self):
        queryset = Result.objects.all()
        conditions = self.request.GET.get('conditions', None)
        if conditions is not None:
            conditionList = conditions.split(',')
            queryset = queryset.filter(conditions__in=conditionList).annotate(num_attr=Count('conditions')).filter(num_attr=len(conditionList))
        return queryset
