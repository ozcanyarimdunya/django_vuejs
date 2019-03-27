from rest_framework import permissions, filters
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from . import models
from . import serializers


# Views with Generic Class Based Views
class TodoList(ListAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    ordering_fields = ('name', 'completed', 'created', 'updated')
    search_fields = ('name',)


class TodoCreate(CreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # serializer.instance.user = self.request.user
        super().perform_create(serializer=serializer)


class TodoDetail(RetrieveAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoUpdate(UpdateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoToggle(UpdateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.instance.completed = not serializer.instance.completed
        super().perform_update(serializer=serializer)


class TodoDelete(DestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated]


# Views with ModelViewSet
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

    def perform_create(self, serializer):
        # serializer.instance.user = self.request.user
        super().perform_create(serializer=serializer)

    def perform_update(self, serializer):
        serializer.instance.completed = not serializer.instance.completed
        super().perform_update(serializer=serializer)

    @action(methods=['GET'], detail=False, url_path='completed-todos', url_name='completed-todos')
    def completed_todos(self, request):
        queryset = self.queryset.filter(completed=True)
        serialized = self.serializer_class(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(methods=['POST'], detail=True, url_path='toggle-todo', url_name='toggle-todo')
    def toggle_todo(self, request, pk):
        obj = self.get_object()
        obj.completed = not obj.completed
        obj.save()
        serialized = self.serializer_class(obj)
        return Response(status=status.HTTP_202_ACCEPTED, data=serialized.data)
