from django.urls import path

from .views import (DistrictView, ShapeListView, ShapeView, approve_request,
                    delete_request_view, delete_shape_request, home,
                    map_rulindo, request_for_multiple, search_shape,
                    shape_view, single_map)

urlpatterns = [
    path('', home, name="home"),
    path('map/', map_rulindo, name='print-map'),
    path('multiple/maps/', request_for_multiple, name="multiple-maps"),
    path('single/map/', single_map, name="single-map"),
    path('map-view/<slug>/', shape_view, name="shape-image"),
    path('district/view/<pk>/', DistrictView, name="district-view"),
    path('list/shapes/', ShapeListView.as_view(), name="shape-list"),
    path('search/results/', search_shape, name='search-shape'),
    path('shape/delete/<pk>/', delete_shape_request, name='delete-shape-request'),
    path('shape-delete/list/', delete_request_view, name='delete-request-list'),
    path('request/approve/<pk>/', approve_request, name='approve-request')
]
