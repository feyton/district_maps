from django.urls import path

from .views import (DistrictView, ShapeListView, ShapeView, home, map_rulindo,
                    request_for_multiple, shape_view, single_map)

urlpatterns = [
    path('', home, name="home"),
    path('map/', map_rulindo, name='print-map'),
    path('multiple/maps/', request_for_multiple, name="multiple-maps"),
    path('single/map/', single_map, name="single-map"),
    path('map-view/<slug>/', shape_view, name="shape-image"),
    path('district/view/<pk>/', DistrictView, name="district-view"),
    path('list/shapes/', ShapeListView.as_view(), name="shape-list")
]
