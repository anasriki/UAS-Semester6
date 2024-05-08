from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Pulsa, Transaksi, Pelanggan
from .serializers import PulsaSerializer, TransaksiSerializer, PelangganSerializer

# Create your views here.
@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Pulsa_list(request, format=None):

    if request.method == 'GET':
        Pulsa = Pulsa.objects.all()
        serializer = PulsaSerializer(Pulsa, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PulsaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Pulsa_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Pulsa = Pulsa.objects.get(pk=pk)
    except Pulsa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PulsaSerializer(Pulsa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PulsaSerializer(Pulsa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Pulsa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Transaksi_list(request, format=None):

    if request.method == 'GET':
        Transaksi = Transaksi.objects.all()
        serializer = TransaksiSerializer(Transaksi, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransaksiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Transaksi_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Transaksi = Transaksi.objects.get(pk=pk)
    except Transaksi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransaksiSerializer(Mobil)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TransaksiSerializer(Transaksi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Transaksi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Pelanggan_list(request, format=None):

    if request.method == 'GET':
        Pelanggan = Pelanggan.objects.all()
        serializer = PelangganSerializer(Pelanggan, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PelangganSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Pelanggan_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Pelanggan = Pelanggan.objects.get(pk=pk)
    except Pelanggan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PelangganSerializer(Pelanggan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PelangganSerializer(Pelanggan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Pelanggan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PulsaDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Pulsa.objects.get(pk=pk)
        except Pulsa.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        Pulsa = self.get_object(pk)
        serializer = PulsaSerializer(Pulsa)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Pulsa = self.get_object(pk)
        serializer = PulsaSerializer(Pulsa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Pulsa = self.get_object(pk=pk)
        Pulsa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TransaksiDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Transaksi.objects.get(pk=pk)
        except Transaksi.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        Transaksi = self.get_object(pk)
        serializer = TransaksiSerializer(Transaksi)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Transaksi = self.get_object(pk)
        serializer = TransaksiSerializer(Transaksi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Transaksi = self.get_object(pk=pk)
        Transaksi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PelangganDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Pelanggan.objects.get(pk=pk)
        except Pelanggan.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        Pelanggan = self.get_object(pk)
        serializer = PelangganSerializer(Pelanggan)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Pelanggan = self.get_object(pk)
        serializer = PelangganSerializer(Pelanggan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Pelanggan = self.get_object(pk=pk)
        Pelanggan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)