from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, View
from seaborn.palettes import color_palette
from django.http import JsonResponse
from maps.main import plot_comunas_data, plot_map_fill_multiples_ids_tone, sf

from .forms import DeleteShapeForm, OptionForm, ShapeImageForm
from .models import District, Example, Member, ShapeImage, Species, Testimony, Subscriber, ShapeDeleteRequest
from .utils import generate_image_for_shape
from rest_framework.views import APIView

class HomeView(View):
    def get(self, *args, **kwargs):
        context = {
            'members': Member.objects.all(),
            'testimonies': Testimony.objects.all(),
            'posts': Example.objects.all()
        }

        return render(self.request, 'index.html', context)


home = HomeView.as_view()


class PrintMap(View):
    def get(self, *args, **kwargs):
        # districts = []
        # for i in range(1, 5):
        #     d = District.objects.get(id=i)
        #     districts.append(d.name)
        # # print(districts)
        # data = [100, 300, 400, 45]
        # plot_comunas_data(sf, "Mapping", districts, data, 3, True)

        context = {
            'sp': Species.objects.all()
        }

        return render(self.request, 'map.html', context)


map_rulindo = PrintMap.as_view()


class RequestMapMultiple(View):
    def get(self, *args, **kwargs):
        form = ShapeImageForm
        context = {"form": form, "option_form": OptionForm}

        return render(self.request, 'pages/multiple-map.html', context)

    def post(self, *args, **kwargs):
        form = ShapeImageForm(self.request.POST)
        options = OptionForm(self.request.POST)
        if form.is_valid() and options.is_valid():
            color = options.cleaned_data['color']
            show_title = options.cleaned_data['show_title']
            add_name = options.cleaned_data['add_name']
            shape = form.save(commit=True)
            sh = generate_image_for_shape(
                shape, color=color, show_title=show_title, add_name=add_name)
            return redirect(sh)
        messages.error(self.request, 'Error in form')
        return render(self.request, 'pages/multiple-map.html', {'form': form, 'option_form': options})


request_for_multiple = RequestMapMultiple.as_view()


class SingleMapView(View):
    def get(self, *args, **kwargs):
        return redirect("multiple-maps")
        # return render(self.request, 'pages/single-map.html')


single_map = SingleMapView.as_view()


class ShapeView(View):
    def get(self, *args, **kwargs):
        pk = kwargs['slug']
        # slug = self.kwargs['slug']
        img = get_object_or_404(ShapeImage, slug=pk)
        if img:
            context = {'shape': img}
            return render(self.request, 'pages/shape-view.html', context)


class DistrictView(View):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        dist = get_object_or_404(District, pk=pk)
        if dist:
            context = {'district': dist}
            return render(self.request, 'pages/district-view.html', context)


class ShapeListView(ListView):
    model = ShapeImage
    template_name = "pages/shape-list.html"
    queryset = ShapeImage.objects.all().order_by('-created')
    context_object_name = 'shapes'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ShapeListView, self).get_context_data(**kwargs)
        context['form'] = DeleteShapeForm()
        return context


def shape_view(request, slug):
    img = get_object_or_404(ShapeImage, slug=slug)
    if img:
        context = {'shape': img}
        return render(request, 'pages/shape-view.html', context)


def search_shape(request):
    query_set = ShapeImage.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = query_set.filter(
            Q(code__iexact=query)).distinct()
    else:
        messages.error(request, "Type a valid term")
        return redirect('home')
    context = {
        'shape': queryset,
        'query': query,
    }

    return render(request, 'pages/search.html', context)


def delete_shape_request(request, pk):
    shape = get_object_or_404(ShapeImage, slug=pk)
    form = DeleteShapeForm(request.POST)
    if form.is_valid():
        req = form.save(commit=False)
        req.shape = shape
        req.save()
        return JsonResponse({'message': 'Shape Deletion request successfully logged'})
    return JsonResponse({'message': 'Something went wrong'})


def delete_request_view(request):
    return render(request, 'pages/delete-request.html', {'reqs': ShapeDeleteRequest.objects.all()})


def approve_request(request, pk):
    req = get_object_or_404(ShapeDeleteRequest, pk=pk)
    req.approve()
    return redirect('delete-request-list')
