from datetime import datetime, timedelta

from rest_framework import serializers

from links.models import Link


class LinkSerializer(serializers.ModelSerializer):



    class Meta:
        model = Link
        fields = ('original_link', 'lifetime', 'short_link')




