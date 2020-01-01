from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django import forms

from dashboard.models import Umuryango, Cell, KPI


class FamilyForm(forms.ModelForm):
    name = forms.CharField(label='Uhagarariye Umuryango',
                           widget=forms.TextInput(attrs={'placeholder': 'Uhagaririrye Umuryango'}))
    number_of_member = forms.CharField(label='Umubare Wabagize Umuryango',
                                       widget=forms.TextInput(attrs={'placeholder': 'urugero: 10'}))

    class Meta:
        model = Umuryango
        fields = [
            'name',
            'number_of_member',
            'icyiciro',
            'irangamuntu',
            'kpi',
            'sector',
            'cell',
            'umudugudu']
        widgets = {
            'name': forms.TextInput(),
            'number_of_member': forms.TextInput(),

        }


class AddKpiForm(forms.ModelForm):
    class Meta:
        model = KPI
        fields = [
            'name'
        ]
