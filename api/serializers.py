from rest_framework import serializers

class ReplacerSerializer(serializers.Serializer):
    first_operand = serializers.CharField()
    result = serializers.CharField()
    operation = serializers.CharField(max_length=20)
    