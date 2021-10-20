from rest_framework import generics, authentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *


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
        serializer = self.get_serializer(data=request.data, context={'user': user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})


class Remove_Admin(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = RemoveAdminSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data, context={'user': user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})


class Remove_Member(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = RemoveMemberSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data, context={'user': user})
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


class GetFriends(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = request.user
        friends = user.friends.all()
        data = []
        for fr in friends:
            a1 = fr.chats.msgs.last()
            a = '1970-01-01 00:00:00.430294+00:00' if a1 == None else str(a1.dttime)

            data.append({
                'id': fr.user.id,
                'username': fr.user.username,
                'first_name': fr.user.first_name,
                'last_name': fr.user.last_name,
                'status': fr.user.status,
                'last_act': a
            })
        data.sort(key=lambda fr: fr['last_act'], reverse=True)
        return Response(data)


class GetGroups(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = request.user
        groups = user.groups.all()
        data = []
        for gr in groups:
            a1 = gr.chats.msgs.last()
            a = '1970-01-01 00:00:00.430294+00:00' if a1 == None else str(a1.dttime)

            data.append({
                'id': gr.id,
                'name': gr.name,
                'description': gr.description,
                'last_act': a
            })
        data.sort(key=lambda gr: gr['last_act'], reverse=True)
        return Response(data)


class GetRequests(generics.GenericAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = request.user
        groups = user.group_requests.all()
        data = []
        for gr in groups:
            data.append({
                'id': gr.id,
                'name': gr.name,
                'type': 1,
                'description': gr.description
            })
        friends = user.friend_requests.all()
        for fr in friends:
            data.append({
                'username': fr.username,
                'first_name': fr.first_name,
                'last_name': fr.last_name,
                'type': 0
            })
        return Response(data)
