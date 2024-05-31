from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search for a movie...'}))