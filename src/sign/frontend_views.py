# coding=utf8


from django.views.generic.base import TemplateView
from django_echarts.views.frontend import EChartsFrontView

from .demo_data import FACTORY

class FrontendEchartsTemplate(TemplateView):
    template_name = 'frontend_charts.html'


class SimpleBarView(EChartsFrontView):
    def get_echarts_instance(self, **kwargs):
        return FACTORY.create('bar')



