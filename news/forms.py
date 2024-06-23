from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=150,
        label='Title',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'})
    )
    content = forms.CharField(
        label='Content',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'rows': 5}),
    )
    is_published = forms.BooleanField(
        label='Published',
        initial=True,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input mb-2'})
    )
    category = forms.ModelChoiceField(
        empty_label=None,
        label='Choose category',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mb-2'})
    )
