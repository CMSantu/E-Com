from django import forms
from .models import OrderItem,Category

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)


class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    state = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'State'}))
    zip_code = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Zip Code'}))
    payment_method = forms.ChoiceField(choices=[('credit_card', 'Credit Card'), ('COD', 'Cash-On-Delivery')])


class CartForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields=('quantity',)

class CategoryForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'category-dropdown'})
    )