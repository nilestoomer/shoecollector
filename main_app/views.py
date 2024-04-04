from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Shoe, Wear, Sock
from .serializers import ShoeSerializer, WearSerializer, SockSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the shoe-collector api home route!'}
    return Response(content)
  
class ShoeList(generics.ListCreateAPIView):
  queryset = Shoe.objects.all()
  serializer_class = ShoeSerializer

class ShoeDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Shoe.objects.all()
  serializer_class = ShoeSerializer
  lookup_field = 'id'

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)

    socks_not_associated = Sock.objects.exclude(id__in=instance.socks.all())
    socks_serializer = SockSerializer(socks_not_associated, many=True)

    return Response({
      'shoe': serializer.data,
      'socks_not_associated': socks_serializer.data
    })

class WearListCreate(generics.ListCreateAPIView):
  serializer_class = WearSerializer

  def get_queryset(self):
    shoe_id = self.kwargs['shoe_id']
    return Wear.objects.filter(shoe_id=shoe_id)
  
  def perform_create(self, serializer):
    shoe_id = self.kwargs['shoe_id']
    shoe = Shoe.objects.get(id=shoe_id)
    serializer.save(shoe=shoe)

class WearDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = WearSerializer
  lookup_field = 'id'

  def get_queryset(self):
    shoe_id = self.kwargs['shoe_id']
    return Wear.objects.filter(shoe_id=shoe_id)
  
class SockList(generics.ListCreateAPIView):
  queryset = Sock.objects.all()
  serializer_class = SockSerializer

class SockDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Sock.objects.all()
  serializer_class = SockSerializer
  lookup_field = 'id'

class AddSockToShoe(APIView):
  def post(self, request, shoe_id, sock_id):
    shoe = Shoe.objects.get(id=shoe_id)
    sock = Sock.objects.get(id=sock_id)
    shoe.socks.add(sock)
    return Response({'message': f'Sock {sock.color} added to Shoe {shoe.name}'})