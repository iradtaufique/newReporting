from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from .models import Sector, KPI, Umuryango
from django.db.models import Sum, Count, F


class DashboardView(ListView):
    model = Umuryango
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['kpis'] = KPI.objects.all()
        # context['results'] = Result.objects.filter(sector=self.request.user.user_profile.sector)
        # context['achieved_results'] = Result.objects.filter(achieved=0, sector=self.request.user.user_profile.sector)
        # context['pending_results'] = Result.objects.filter(pending=0, sector=self.request.user.user_profile.sector)
        context['sectors'] = Sector.objects.all()

        context['achieved_total'] = Umuryango.objects.values('kpi__name', 'kpi_id') \
                                                     .annotate(achieved=Sum('achieved')) \
                                                     .annotate(target=Sum('target'))

        context['achieved_sector'] = Umuryango.objects.values('kpi__name', 'kpi_id')\
                                                  .annotate(achieved=Sum('achieved'))\
                                                  .annotate(target=Sum('target'))\
                                                  .filter(sector=self.request.user.user_profile.sector)


        # context['kpizose'] = Umuryang.objects.values('kpi__name', 'status').filter(status=False).annotate(Count('status'))
        # context['ibisigay'] = Umuryango.objects.filter(kpi__name='kpi_name').count()
        # Entry.objects.filter(authors__name=F('blog__name'))
        # context['ibisigaye'] = Umuryango.objects.filter(kpi__name=F('kpi1__name')).filter(status=True).distinct().count()
        # context['ibyakozw'] = Umuryango.objects.filter(status="True").filter(kpi__name=self.kwargs['kpi__name']).count()
        # context['ibyakozw'] = Umuryango.objects.values('kpi__name', 'kpi_id').filter(kpi__name=F('kpi__name'), status=True).annotate(status=Sum('status'))
        # context['ibisi'] = Umuryango.objects.values('kpi__name', 'kpi_id').filter(kpi__name='kpi__name', status=False).annotate(Count('status',distinct=True))





        return context


class KPIDetailView(DetailView):
    model = KPI
    template_name = "dashboard/kpi_detail.html"

    def get_context_data(self, **kwargs):
        context = super(KPIDetailView, self).get_context_data(**kwargs)
        context['kpis'] = KPI.objects.all()
        context['current_kpi'] = Umuryango.objects.filter(kpi_id=self.kwargs['pk'])\
                                          .values('kpi__name').annotate(targ=Sum('target'))\
                                          .annotate(achiev=Sum('achieved'))\
                                          .distinct()

        return context


class Ibyakozwe(ListView):
    model = KPI
    template_name = "umuryango/ibyakozwe.html"

    def get_context_data(self, **kwargs):
        context = super(Ibyakozwe, self).get_context_data(**kwargs)
        context['ibyakozwe'] = Umuryango.objects.filter(achieved=1).filter(kpi_id=self.kwargs['pk'])
        context['ibisigaye'] = Umuryango.objects.filter(achieved=0).filter(kpi_id=self.kwargs['pk'])

        context['ibyakozwe_sector'] = Umuryango.objects.filter(achieved=1, sector=self.request.user.user_profile.sector).filter(kpi_id=self.kwargs['pk'])
        context['ibisigaye_sector'] = Umuryango.objects.filter(achieved=0, sector=self.request.user.user_profile.sector).filter(kpi_id=self.kwargs['pk'])

        return context


class District_chartView(View):
    def get(self, request, pk):
        dataset = Umuryango.objects.values('kpi__name', 'sector__name').annotate(targ=Sum('target')) \
                           .annotate(achiev=Sum('achieved'))\
                           .filter(kpi_id=self.kwargs['pk'])\
                           .order_by('target')
        return render(request, 'dashboard/kpi_detail.html', {'dataset': dataset})


class Sector_chartView(View):
    def get(self, request):
        dataset = Umuryango.objects.values('kpi__name').annotate(targ=Sum('target')) \
                           .annotate(achiev=Sum('achieved')) \
                           .filter(sector=self.request.user.user_profile.sector) \
                           .order_by('target')

        return render(request, 'dashboard/kpi_detail.html', {'dataset': dataset})
