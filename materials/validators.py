from rest_framework import serializers


class URLValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('url', False) and 'youtube.com' not in value['url']:
            raise serializers.ValidationError('Разрешён только ресурс youtube')