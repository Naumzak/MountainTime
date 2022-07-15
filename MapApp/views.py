from django.http import JsonResponse
from django.shortcuts import render, redirect
from .update_map_db import UpdateMarker
import json
from  .models import Map
from django.template.defaultfilters import slugify
# Create your views here.
from django.views.generic import CreateView, View, ListView, UpdateView, TemplateView


class CreateMapView(View):
    def get(self, request):
        name = request.GET['name']
        m = Map(name=name)
        m.save()
        m.users.add(request.user)
        return redirect('maps_list')


class ListMap(View):
    def get(self, request):
        maps = Map.objects.filter(users=request.user)
        return render(request, 'list_map.html', context={'maps': maps})



class OpenMap(View):
    def get(self, request):
        map_id = request.GET['map']
        markers = Map.objects.get(pk=map_id).markers.all()
        return render(request, 'osm_version.html', context={'map_id': map_id, 'markers': markers, 'center': [1, 2, 3]})


class UpdateView(View):
    def post(self, request):
        params = json.loads(request.body)
        marker = UpdateMarker(latitude=params['latitude'],
                              longitude=params['longitude'],
                              user_id=request.user.id,
                              map_id=params['map_id'],
                              type_request=params['type'])
        marker.update()
        return JsonResponse({"123": "123"})


def test(request):
    return render()
