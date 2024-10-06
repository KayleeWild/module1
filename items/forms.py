from django import forms

class CheckoutForm(forms.Form):
    # Address stuff
    street = forms.CharField(max_length=100, label='Street Address')
    city = forms.CharField(max_length=100, label='City')
    state = forms.CharField(max_length=40, label='State')
    zipcode = forms.CharField(max_length=10, label='Zip Code')
    # Payment stuff
    card_name = forms.CharField(max_length=100, label='Name on Card')
    card_number = forms.CharField(max_length=20, label='Card Number')
    expiration_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2024, 2030)), label='Expiration Date')
    cvv = forms.CharField(max_length=3, label='CVV')