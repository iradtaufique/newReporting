from django.shortcuts import render
from .forms import ReportForm


def generate_report(request):
    report_form = ReportForm(request.POST, request.FILES)

    if report_form.is_valid():
        report_form.save()
    else:
        report_form = ReportForm()
    template_name = 'report/create_report.html'
    context       =  {'form':report_form}
    return render(request, template_name, context)


