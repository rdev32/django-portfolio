from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from control.models import OwnerProxy, ProjectProxy
import requests
import ast

class ControlView(LoginRequiredMixin, TemplateView):
    template_name = "panel.html"
    
    extra_context = {
        'owner': OwnerProxy.objects.first().get_json(),
        'projects': list(item.get_json() for item in ProjectProxy.objects.all())
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = OwnerProxy.objects.first().get_json()
        context["projects"] = list(item.get_json() for item in ProjectProxy.objects.all())
        return context

@login_required
def gh_loader(request):
    token = "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"
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    def proyects_request(data):
        for item in data:
            yield {
                'name': item['name'],
                'description': item['description'],
                'url': item['html_url']
            }

    req = requests.get(url='https://api.github.com/users/rdev32/repos', headers=headers)
    json = req.json()
    data = proyects_request(json)
    for item in data:
        p = ProjectProxy.objects.create(name=item['name'], description=item['description'], url=item['url'])
        p.save()

    return redirect('control')