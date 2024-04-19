from django import forms
from django.contrib.auth.models import User

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "email", "coffee", "count", "user"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].queryset = User.objects.filter(id=user.id, is_active=True)
        self.fields['coffee'].widget.attrs.update({'class': 'form-control'})