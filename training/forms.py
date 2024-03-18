from django import forms

class MeterReadingForm(forms.Form):
    start_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'step': '900'}),
        required=True
    )
    end_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'step': '900'}),
        required=True
    )