from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SearchParamsSerializer
from .models import SearchQuery


@api_view(['GET'])
def search_view(request):
    serializer = SearchParamsSerializer(data=request.query_params)
    if serializer.is_valid():
        from_city = serializer.validated_data['from_city']
        to_city = serializer.validated_data['to_city']
        max_capacity = serializer.validated_data.get('max_capacity')
        start_date = serializer.validated_data.get('start_date')
        end_date = serializer.validated_data.get('end_date')
        
        
        search_queries = SearchQuery.objects.filter(
            from_city=from_city,
            to_city=to_city,
            max_capacity__lte=max_capacity if max_capacity else SearchQuery._meta.get_field('max_capacity').get_max_valid_value(),
            start_date__gte=start_date,
            end_date__lte=end_date
        )
        
        return Response({"message": "Search successful"})
    return Response(serializer.errors, status=400 )





