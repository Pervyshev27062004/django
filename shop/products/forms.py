from django import forms


class ProductsForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)
    price = forms.IntegerField()
    color = forms.CharField(max_length=32, required=False)
    excerpt = forms.CharField()
    description = forms.CharField()
