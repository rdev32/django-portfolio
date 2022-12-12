from django.shortcuts import redirect
from django.views.generic import TemplateView
from control.models import OwnerProxy, ProjectProxy

class IndexView(TemplateView):
    template_name = "index.html"

    extra_context = {
        'owner': OwnerProxy.objects.first().get_json(),
        'projects': list(item.get_json() for item in ProjectProxy.objects.all())
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = OwnerProxy.objects.first().get_json()
        context["projects"] = list(item.get_json() for item in ProjectProxy.objects.all())
        return context
