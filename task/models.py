from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class TaskModel(models.Model):
    PRIORITIES = (
        [1, 'Low'],
        [2, 'Medium'],
        [3, 'High'],
    )
    STATUSES = (
        [True, 'Done'],
        [False, 'In Progress'],
    )
    name = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORITIES, default=1)
    status = models.BooleanField(choices=STATUSES, default=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
        ordering = 'status', 'deadline', '-priority'

    def __str__(self) -> str:
        return f"{self.deadline:%d.%m.%Y}"

    def get_absolute_url(self):
        return reverse("task", kwargs={"pk": self.pk})
