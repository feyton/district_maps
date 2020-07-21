from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'index.html')


home = HomeView.as_view()
