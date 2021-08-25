from rest_framework import serializers

from authentication.models import Chat


class RequestRoomAccessSerializer(serializers.ModelSerializer):
    title = serializers.CharField()

    class Meta:
        model = Chat
        fields = ['title', ]

    def validate(self, data):
        try:
            verified = Chat.objects.get(title=data['title'])
            user = self.context['request'].user
        except:
            raise serializers.ValidationError("Unauthorized Access")
        if user not in verified.users.all():
            raise serializers.ValidationError("Unauthorized Access")
        return data
