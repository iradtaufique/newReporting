from django.shortcuts import render
from .forms import ReportForm

from .models import ReportType


def generate_report(request):
    report_form = ReportForm(request.POST, request.FILES,request=request)

    report_form.fields['report_type'].queryset = ReportType.objects.filter(owner=1)

    if report_form.is_valid():
        report_form.save()
    else:
        report_form = ReportForm(request=request)
    template_name = 'report/create_report.html'
    context       =  {'form':report_form}
    return render(request, template_name, context)


