from django.test import TestCase
from django.urls import reverse

from .models import Todo


class TodoTests(TestCase):
    def test_create_and_list(self):
        res = self.client.post(reverse("todos:create"), {"title": "공부하기", "content": "Django"})
        self.assertRedirects(res, reverse("todos:list"))
        res = self.client.get(reverse("todos:list"))
        self.assertContains(res, "공부하기")

    def test_validation_error(self):
        res = self.client.post(reverse("todos:create"), {"title": ""})
        self.assertContains(res, "제목은 필수 입력 항목입니다.")
        res = self.client.post(reverse("todos:create"), {"title": "a"})
        self.assertContains(res, "제목은 2자 이상 입력하세요.")
        self.assertEqual(Todo.objects.count(), 0)

    def test_update_toggle_delete(self):
        t = Todo.objects.create(title="원래 제목")
        self.client.post(reverse("todos:update", args=[t.pk]), {"title": "바뀐 제목"})
        t.refresh_from_db()
        self.assertEqual(t.title, "바뀐 제목")
        self.client.post(reverse("todos:toggle", args=[t.pk]))
        t.refresh_from_db()
        self.assertTrue(t.is_completed)
        res = self.client.get(reverse("todos:list"))
        self.assertContains(res, "todo-item completed")
        self.client.post(reverse("todos:delete", args=[t.pk]))
        self.assertFalse(Todo.objects.exists())

    def test_admin_registered(self):
        from django.contrib import admin
        self.assertIn(Todo, admin.site._registry)
