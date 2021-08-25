from rest_framework import generics, authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chat.serializers import RequestRoomAccessSerializer


class RequestRoomAccessView(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = RequestRoomAccessSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Access Granted'})




