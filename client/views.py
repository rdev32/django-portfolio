from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from administrator.models import OwnerProxy, Project, ProjectProxy
import requests

class ManageView(LoginRequiredMixin, TemplateView):
    template_name = "manage.html"

    # owner_data = list(OwnerProxy.objects.all())[0].get_json()
    # project_data = list(i.get_json() for i in ProjectProxy.objects.all())
    
    # extra_context = {
    #     'owner': owner_data,
    #     'projects': project_data
    # }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["owner"] = self.owner_data
    #     context["projects"] = list(i.get_json() for i in ProjectProxy.objects.all())
    #     return context

class IndexView(TemplateView):
    template_name = "index.html"
    # owner_data = list(OwnerProxy.objects.all())[0].get_json()
    # project_data = list(i.get_json() for i in ProjectProxy.objects.all())
    
    # extra_context = {
    #     'owner': owner_data,
    #     'projects': project_data
    # }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["owner"] = self.owner_data
    #     context["projects"] = list(i.get_json() for i in ProjectProxy.objects.all())
    #     return context

# def proyects_request(data):
#     for item in data:
#         yield {
#             'name': item['name'],
#             'description': item['description'],
#             'url': item['html_url']
#         }

# @login_required
# def load(request):
#     token = "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"
#     headers = {
#         'Accept': 'application/vnd.github+json',
#         'Authorization': f'Bearer {token}',
#         'X-GitHub-Api-Version': '2022-11-28'
#     }

#     with requests.get(url='https://api.github.com/users/rdev32/repos', headers=headers) as req:
#         json =req.json()
#         data = list(proyects_request(json))
#         for item in data:
#             p = Project(name=item['name'], description=item['description'], url=item['url'])
#             p.save()

#     return redirect('manage')
