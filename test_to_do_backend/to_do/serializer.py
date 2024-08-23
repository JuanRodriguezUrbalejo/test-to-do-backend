from rest_framework import serializers
from .models import Tasks, Lists


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class ListsSerializer(serializers.ModelSerializer):
    tasks = TasksSerializer(many=True, read_only=True, source='tasks_set')

    class Meta:
        model = Lists
        fields = '__all__'

