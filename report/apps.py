from django.apps import AppConfig


class ReportConfig(AppConfig):
    name = 'report'

    def ready(deadline):
        from report import scheduler
        scheduler.start(deadline)
