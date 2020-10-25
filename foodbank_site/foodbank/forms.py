from django import forms

class SearchForm(forms.Form):
    branch_form = forms.CharField(label='', max_length=100)

categories = [
        ("media/milk.png", "Milk"),
        ("media/bread.jpg", "Bread"),
    ]
    
class FilterForm(forms.Form):
    needs = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=categories,
    )
