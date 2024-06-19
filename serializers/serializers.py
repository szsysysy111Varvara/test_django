from django.utils import timezone
from rest_framework import serializers
from myapp.models import SubTask, Category, Task

class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'
        read_only_fields = ['created_at']

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        if Category.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError("Category with this name already exists")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if Category.objects.filter(name=validated_data['name']).exclude(pk=instance.pk).exists():
            raise serializers.ValidationError("Category with this name already exists")
        return super().update(instance, validated_data)


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'task', 'title', 'description', 'status', 'deadline', 'created_at']

class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at']

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Deadline cannot be in the past.")
        return value