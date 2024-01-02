from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializer import CarSpecsSerializer
from first_app.models import CarSpecs

@api_view()
@permission_classes([AllowAny]) # togliendo questo. Entriamo senza il token 
def firstFunction(request):
    print ( request.query_params )
    # print ( request.query_params['id'] ) # http://127.0.0.1:8000/first-app/first/?id=12345
    # print ( request.query_params['id'] ) # http://127.0.0.1:8000/first-app/first/?id=12345
    # print ( request.query_params['key'] ) # http://127.0.0.1:8000/first-app/first/?id=12345&key=999
    number = request.query_params['num']
    new_number = int(number) * 2
    return Response({'message': "we received your request", " result ": new_number })


class CarSpecsViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecsSerializer
    throttle_scope = "first_app"
    
    def get_queryset(self):
        car_specs = CarSpecs.objects.all()
        return car_specs