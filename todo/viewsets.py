from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from todo.models import Todo, Category
from todo.serializers import TodoSerializer, CategorySerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False)
    def Done(self, request):
        done_todos = Todo.objects.filter(completed=True)
        serializer = self.get_serializer(done_todos, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def NotDone(self, request):
        not_done_todos = Todo.objects.filter(completed=False)
        serializer = self.get_serializer(not_done_todos, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
