from django import forms

class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Buscar Produto', max_length=100)