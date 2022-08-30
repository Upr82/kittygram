from functools import partial
from pickle import TRUE
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework import generics
from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer, CatSerializerFull

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializerFull

# class CatList(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer

# class CatDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializerFull



# class APICat(APIView):
#     def get(self, request):
#         cats = Cat.objects.all()
#         serializer = CatSerializerFull(cats, many=TRUE)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class APICatDetail(APIView):
#     def get(self, request, pk):
#         cat = get_object_or_404(Cat, id=pk)
#         serializer = CatSerializer(cat)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def patch(self, request, pk):
#         cat = get_object_or_404(Cat, id=pk)
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         cat = get_object_or_404(Cat, id=pk)
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         serializer = CatSerializer(data=request.data, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "ПОлучены данные", "data": request.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def cat_detail(request, pk):
#     cat = get_object_or_404(Cat, pk=pk)
#     if request.method == 'PATCH' or request.method == 'PUT':
#         serializer = CatSerializer(cat, data=request.data, partial=True) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     cat = get_object_or_404(Cat, id=pk)
#     serializer = CatSerializer(cat)
#     return Response(serializer.data)