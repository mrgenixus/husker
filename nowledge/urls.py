from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^solutions/(?P<solution_id>[0-9]+)/?$', views.SolutionView.as_view(), name="solution"),
    url(r'^solutions/?$', views.SolutionsView.as_view()),
    url('', TemplateView.as_view(template_name="layouts/app.html")),
]
