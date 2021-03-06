from rest_framework import filters
from rest_framework import viewsets

from time_tracker.models import Profile
from time_tracker.serializers import ProfileSerializer
from time_tracker.permissions import ProfilePermission


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (ProfilePermission,)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('user__id',)
    ordering_fields = ('first_name', 'last_name')
    ordering = ('-first_name', '-last_name')
    
    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.filter(is_active=True)
        return profile
