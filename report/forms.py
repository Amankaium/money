from django import forms

class ReportFilterForm(forms.Form):

    min_date = forms.DateTimeField(widget=forms.SelectDateWidget(), label='Дата с', required=False)
    max_date = forms.DateTimeField(widget=forms.SelectDateWidget(), label='до', required=False)

    min_money = forms.IntegerField(label='Сумма от', required=False)
    max_money = forms.IntegerField(label='до', required=False)
