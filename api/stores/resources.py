# stores/resources.py

from tastypie.resources import ModelResource
from tastypie import fields
from stores.models import Store, StoreType, OpeningHours

class StoreTypeResource(ModelResource):
    class Meta:
        queryset = StoreType.objects.all()
        allowed_methods = ['get']
        excludes = ['id', 'resource_uri']
        include_resource_uri = False

class OpeningHoursResource(ModelResource):
    class Meta:
        queryset = OpeningHours.objects.all()
        allowed_methods = ['get']
        excludes = ['resource_uri', 'id']
        include_resource_uri = False

class StoreResource(ModelResource):
    types = fields.ForeignKey(StoreTypeResource, 'type', full=True)
    openingHours = fields.ToManyField(OpeningHoursResource, 'OpeningHours', full=True, null=True)
    class Meta:
        queryset = Store.objects.all()
        allowed_methods = ['get']
        include_resource_uri = False
