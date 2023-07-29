from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=500)
    important = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __repr__(self) -> str:
        return f"Task(title={self.title!r}, important={self.important!r}, completed={self.completed!r}"
