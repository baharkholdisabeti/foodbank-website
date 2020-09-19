from django import forms

class SearchForm(forms.Form):
    branch_form = forms.CharField(label='', max_length=100)