from rest_framework import serializers

from conduccion.experto.models import FieldType, Field, FieldOption, FieldCondition, Result

class FieldTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldType
        fields = ('id', 'name')

class FieldOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOption
        fields = ('key', 'value')

class FieldSerializer(serializers.ModelSerializer):
    options = FieldOptionSerializer(source='field_option', many=True, read_only=True)
    type = FieldTypeSerializer(source='field_type')
    class Meta:
        model = Field
        fields = ('id', 'label', 'options', 'type')

class FieldConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldCondition
        fields = ('id', 'name', 'field')

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'name', 'razon', 'conditions')
