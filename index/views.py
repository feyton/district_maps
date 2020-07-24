from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View, ListView
from seaborn.palettes import color_palette

from maps.main import plot_comunas_data, plot_map_fill_multiples_ids_tone, sf

from .forms import ShapeImageForm
from .models import District, ShapeImage, Species, Testimony, Member, Example
from .utils import generate_image_for_shape
from .forms import OptionForm


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
        if form.is_valid():
            shape = form.save(commit=True)
            sh = generate_image_for_shape(shape)
            return redirect(sh)
        messages.error(self.request, 'Error in form')
        return render(self.request, 'pages/multiple-map.html', {'form': form})


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
    queryset = ShapeImage.objects.all()
    context_object_name = 'shapes'
    paginate_by = 10


def shape_view(request, slug):
    img = get_object_or_404(ShapeImage, slug=slug)
    if img:
        context = {'shape': img}
        return render(request, 'pages/shape-view.html', context)
