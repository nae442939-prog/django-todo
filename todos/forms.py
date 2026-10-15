from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "content", "is_completed"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "할 일을 입력하세요"}),
            "content": forms.Textarea(attrs={"rows": 4, "placeholder": "세부 내용 (선택)"}),
        }
        error_messages = {
            "title": {
                "required": "제목은 필수 입력 항목입니다.",
                "max_length": "제목은 200자 이내로 입력하세요.",
            },
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 2:
            raise forms.ValidationError("제목은 2자 이상 입력하세요.")
        return title
