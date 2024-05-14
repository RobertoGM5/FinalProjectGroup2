from rest_framework import serializers


class SearchParamsSerializer(serializers.Serializer):
    from_city = serializers.CharField(required=True)
    to_city = serializers.Charfield(required=True)
    max_capacity = serializers.IntegerField(required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)