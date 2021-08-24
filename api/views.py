from rest_framework import generics, authentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *


# Create your views here.
class Fr_Request(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = Fr_RequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        r = serializer.save()
        return Response({'message': 'Success'})




class Fr_Response(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = Fr_ResponseSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        r = serializer.save()
        return Response({'message': 'Success'})




class Fr_Remove(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = Fr_RemoveSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        r = serializer.save()
        return Response({'message': 'Success'})


class Grp_Request(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = Grp_RequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        r = serializer.save()
        return Response({'message': 'Success'})





class Grp_Response(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = Grp_ResponseSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        r = serializer.save()
        return Response({'message': 'Success'})



class Grp_Create(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = Grp_CreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        r = serializer.save()
        return Response({'message': 'Success'})


class Grp_Exit(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = Grp_ExitSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        r = serializer.save()
        return Response({'message': 'Success'})





class Make_Admin(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = NewAdminSerializer


    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data,context={'user':user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})

class Remove_Admin(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = RemoveAdminSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data,context={'user':user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})

class Remove_Member(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = RemoveMemberSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data,context={'user':user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})

class RetrieveMessage(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = RetrieveMessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        r = serializer.save()
        return Response(r)


