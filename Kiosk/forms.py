from django import forms
from .models import Customer,Food,OrderLine,Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields='__all__'

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields='name','description','price'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields='cust_order','mode_payment'

class OrderLineForm(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields=('food','quantity')

    #def __init__(self, *args, **kwargs):
        #super(OrderLineForm, self).__init__(*args, **kwargs)
        #self.fields['cust_order']=forms.MultipleChoiceField(queryset=Order.objects.filter())
    


