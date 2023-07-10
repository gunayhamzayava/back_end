from typing import Any, Dict
from django import forms
from .models import Product
from .validators import validate_timestamp

# modelleri html input formatina cevirmek ucun ist. olunur

# class ProductForm(forms.Form):
#     name = forms.CharField() #max_length-e ehtiyac yoxdu
#     description = forms.CharField()
#     price = forms.FloatField()


# adi ve ya modelden inherit formlar islede bilerik


class ProductForm(forms.ModelForm):
    # category = forms.CharField()  ozumuzden de elave ede bilerik

    timestamp = forms.CharField(
        widget=forms.DateInput(attrs={"type": "date"}),
        # validators=[validate_timestamp]
    )  # inputu date'e cevirmek,claass'i fln da deyise bilerik

    class Meta:
        model = Product
        # fields  = ('name', 'description', 'price','discount_price')  #yalniz bunlar ekranda gorunur
        # exclude = ('created_at', 'updated_at')  #bunlardan basqa hamisi ekranda gorunur
        fields = "__all__"  # butun fieldsler

    # hamisinin birlikde type,classini deyismek ucun:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "form-control"}
            )  # key'leri(inputlari) gotururuk ve hamsina class birden veririk

        # print(self.fields.keys())

        # self.fields['name'].widget.attrs.update({"class": "underline"})
        self.fields['name'].widget.attrs['class'] +=' underline'  #var olan class'in yanina underline da elave edir.

    def clean(self):
        # print(self.cleaned_data)  #errorlari terminalda gosterir

        price = self.cleaned_data.get('price',None)
        discount_price = self.cleaned_data.get('discount_price',None)

        if not price:
            raise forms.ValidationError("Price is required")
        
        if price==discount_price:
            raise forms.ValidationError("Discount price must be lower than price.")

        return super().clean()