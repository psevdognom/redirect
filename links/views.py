

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.http import HttpResponseRedirect
import pytz

from links.models import Link
from links.serializers import LinkSerializer
from redirect.settings import TIME_ZONE
# Create your views here.

from django.http import Http404

from datetime import datetime, timezone

class CreateLinkView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    serializer_class = LinkSerializer
    queryset = Link.objects.all()



class RedirectView(RetrieveAPIView):

    lookup_url_kwarg = 'short_link'
    lookup_field = 'short_link'

    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def get_object(self):
        obj = super().get_object()
        if obj.lifetime:
            if obj.lifetime < datetime.now(pytz.timezone(TIME_ZONE)):
                raise Http404
            else:
                return obj
        else:
            return obj

    def retrieve(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.get_object().original_link)

