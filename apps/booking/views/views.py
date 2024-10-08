from django.core.serializers import serialize
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import Request
from ..models.apartments import Apartment
from ..serializers.serializer_apartment import ApartmentSerializer


class ApartmentCreateView(APIView):
    def post(self, request):
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"House for rent: '{serializer.validated_data['title']}' successfully created.",
                'housing': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApartmentListView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                apartment = Apartment.objects.get(pk=pk)  # Изменено на стандартный метод получения объекта
                serializer = ApartmentSerializer(apartment)
                return Response(serializer.data)
            except Apartment.DoesNotExist:
                return Response({"error": "Apartment not found"}, status=404)
        else:
            apartments = Apartment.objects.filter(is_active=True).values(
                'title', 'description', 'street', 'house_number', 'amount_of_rooms', 'price', 'type_of_housing'
                # Исправлено имя поля
            )
            return JsonResponse(list(apartments), safe=False)


class ApartmentUpdateView(APIView):
    def put(self, request, pk=None):
        apartment = Apartment.objects.get(pk=pk)
        serializer = ApartmentSerializer(apartment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        apartment = Apartment.objects.get(pk=pk)
        apartment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApartmentChangeActiveView(APIView):
    def put(self, request, pk=None):
        apartment = Apartment.objects.get(pk=pk)
        data = request.data.copy()

        if 'activate' in data and data['activate'] == True:
            data['is_active'] = True  # Булевое значение True для поля is_active
        else:
            data['is_active'] = False  # Булевое значение False для поля is_active

        serializer = ApartmentSerializer(apartment, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
