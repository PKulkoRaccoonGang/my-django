from django import forms
from .models import News

import re


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control mb-2'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise forms.ValidationError('Title should not contain numbers')
        return title
