from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def toggle_complete(self, request, pk=None):
        """
        Toggle the completion status of a task.
        """
        task = self.get_object()
        task.completed = not task.completed
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)
