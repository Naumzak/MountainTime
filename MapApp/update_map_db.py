from .models import *


class UpdateMarker:
    def __init__(self, latitude, longitude, user_id, map_id, type_request):
        self.latitude = latitude
        self.longitude = longitude
        self.user_id = user_id
        self.map = Map.objects.get(pk=map_id)
        self.type_request = type_request

    def access_check(self):
        users = self.map.users.all()
        for user in users:
            if user.pk == self.user_id:
                return True
        return False

    def save_marker(self):
        marker_name = 'lat' + self.latitude + 'lng' + self.longitude + self.map.name
        marker = Marker(latitude=self.latitude, longitude=self.longitude, name=marker_name)
        marker.save()
        self.map.markers.add(marker)

    def delete_marker(self):
        marker = Marker.objects.get(latitude=self.latitude, longitude=self.longitude)
        Marker.delete(marker)

    def update(self):
        if self.access_check():
            if self.type_request == 'add':
                self.save_marker()
            elif self.type_request == 'delete':
                self.delete_marker()