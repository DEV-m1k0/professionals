from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={
        "placeholder": "поиск...",
        "class": "form-control",
        "type": "search"
    }))