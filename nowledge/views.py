from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View

from .models import Solution


class SolutionsView(View):
    def get(self, request):
        context = {
            'solutions': Solution.objects.all()
        }

        return render(request, 'solutions/index.html', context)


class SolutionView(View):
    def get(self, request, solution_id):

        solution =get_object_or_404(Solution, pk=solution_id)

        context = {
            'solution': solution
        }

        return render(request, 'solutions/show.html', context)
