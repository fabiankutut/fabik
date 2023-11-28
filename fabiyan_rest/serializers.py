from rest_framework import serializers


class ProfileRestSerializers(serializers.Serializers):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
