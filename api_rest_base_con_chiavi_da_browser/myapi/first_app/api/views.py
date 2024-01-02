from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import AllowAny, IsAuthenticated

@api_view()
@permission_classes([AllowAny]) # togliendo questo. Entriamo senza il token 
def firstFunction(request):
    print ( request.query_params )
    # print ( request.query_params['id'] ) # http://127.0.0.1:8000/first-app/first/?id=12345
    # print ( request.query_params['id'] ) # http://127.0.0.1:8000/first-app/first/?id=12345
    # print ( request.query_params['key'] ) # http://127.0.0.1:8000/first-app/first/?id=12345&key=999
    return Response({'message': "we received your request"})