from django import forms
from .models import *


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('report_type', 'report_file')
        widgets = {
            'report_file': forms.FileInput(attrs={'style': ' border-radius:2px;);'}),
           
        }
        labels={
            'report_type':'Raporo Itanzwe',
            'report_file':' Dosiye ya Raporo Itanzwe'
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields["report_type"].queryset = ReportType.objects.filter(owner=self.request.user.user_profile)
        # self.fields['report_type'].help_text = "urugero: raporo y' imari ni igena migambi"
        # self.fields['report_file'].help_text = 'urugero:  file igaragaza raporo utanze '


