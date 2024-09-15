from django.shortcuts import render
from rest_framework import viewsets, generics, mixins
from rest_framework.decorators import action
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response 
from django.utils import timezone

   
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    #get all completed todos
    def get_completed_todos(self, request, *args, **kwargs):
        completed_todos = Todo.objects.filter(completed=True)
        serializer = TodoSerializer(completed_todos, many=True)
        return Response(serializer.data)
    
    # get pending todos
    def get_pending_todos(self, request, *args, **kwargs):
        pending_todos = Todo.objects.filter(completed=False)
        serializer = TodoSerializer(pending_todos, many=True)
        return Response(serializer.data)

    # search todos by title or description
    def search_todos(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')
        todos = Todo.objects.filter(title__icontains=query) | Todo.objects.filter(description__icontains=query)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    # get long pending todos
    def get_long_pending_todos(self, request, *args, **kwargs):
        long_pending_todos = Todo.objects.filter(updated_at__date__lt=timezone.now().date())
        serializer = TodoSerializer(long_pending_todos, many=True)
        return Response(serializer.data)
    
