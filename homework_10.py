from datetime import datetime, timedelta
from myapp.models import Task, SubTask

task = Task.objects.create(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status="New",
    deadline=datetime.now() + timedelta(days=3)
)

subtask1 = SubTask.objects.create(
    task=task,
    title="Gather information",
    description="Find necessary information for the presentation",
    status="New",
    deadline=datetime.now() + timedelta(days=2)
)

subtask2 = SubTask.objects.create(
    task=task,
    title="Create slides",
    description="Create presentation slides",
    status="New",
    deadline=datetime.now() + timedelta(days=1)
)

print(f"Task and SubTasks created: {task}, {subtask1}, {subtask2}")

new_tasks = Task.objects.filter(status="New")
for task in new_tasks:
    print(task)

overdue_done_subtasks = SubTask.objects.filter(status="Done", deadline__lt=datetime.now())
for subtask in overdue_done_subtasks:
    print(subtask)

task.status = "In progress"
task.save()
print(f"Updated task: {task}")

subtask1.deadline = datetime.now() - timedelta(days=2)
subtask1.save()
print(f"Updated subtask deadline: {subtask1}")

subtask2.description = "Create and format presentation slides"
subtask2.save()
print(f"Updated subtask description: {subtask2}")

task.delete()
print(f"Deleted task and its subtasks: {task}")
