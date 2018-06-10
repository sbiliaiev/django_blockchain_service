from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import Http404
from .models import Device, DeviceData
from .serializers import DeviceSerializer, DeviceDataSerializer


class DeviceView(views.APIView):

    def get(self, request, *args, **kwargs):
        devices = Device.objects.all()
        return Response(DeviceSerializer(devices, many=True).data)
    
    def post(self, request, *args, **kwargs):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceDetailView(views.APIView):
    def get_object(self, *args, **kwargs):
        try:
            return Device.objects.get(pk=kwargs['pk'])
        except Device.DoesNotExist as e:
            raise Http404
    
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        device = self.get_object(**kwargs)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        device = self.get_object(**kwargs)
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        device = self.get_object(**kwargs)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class DeviceDataView(views.APIView):
    
#     def get(self, request, *args, **kwargs):
#         devices = DeviceData.objects.all()
#         return Response(DeviceDataSerializer(devices, many=True).data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = DeviceDataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceDataView(generics.ListCreateAPIView):
    queryset = DeviceData.objects.all()
    serializer_class = DeviceDataSerializer

class DeviceDataDetailView(views.APIView):
    def get_object(self, *args, **kwargs):
        try:
            return DeviceData.objects.get(id=kwargs['pk'])
        except DeviceData.DoesNotExist as e:
            raise Http404
    
    def get(self, request, *args, **kwargs):
        device_data = self.get_object(**kwargs)
        serializer = DeviceDataSerializer(device_data)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        device_data = self.get_object(**kwargs)
        serializer = DeviceDataSerializer(device_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        device_data = self.get_object(**kwargs)
        device_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)