# During dispatch, the following attributes are available on the ViewSet.
# basename - the base to use for the URL names that are created.
# action - the name of the current action (e.g., list, create).
# detail - boolean indicating if the current action is configured for a list or detail view.
# suffix - the display suffix for the viewset type - mirrors the detail attribute.
# name - the display name for the viewset. This argument is mutually exclusive to suffix.
# description - the display description for the individual view of a viewset.

from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import Movie
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404

class MovieViewSet(viewsets.ViewSet):
    def list(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)
