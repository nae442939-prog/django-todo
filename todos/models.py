from django.db import models


class Todo(models.Model):
    title = models.CharField("제목", max_length=200)
    content = models.TextField("세부 내용", blank=True)
    is_completed = models.BooleanField("완료 여부", default=False)
    created_at = models.DateTimeField("생성 일시", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
