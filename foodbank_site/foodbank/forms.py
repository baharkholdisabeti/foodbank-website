from django import forms

class SearchForm(forms.Form):
    branch_form = forms.CharField(label='', max_length=100)

class FilterForm(forms.Form):
    categories = [zip("Milk", 'media/milk.png'), zip("Dairy", 'media/dairy.jpg')]
    needs = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=categories,
    )