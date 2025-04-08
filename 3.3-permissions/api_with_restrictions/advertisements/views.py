from rest_framework import status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter


class AdvertisementUserThrottle(UserRateThrottle):
    scope = "advertisement_user"


class AdvertisementAnonThrottle(AnonRateThrottle):
    scope = "advertisement_anon"


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AdvertisementThrottle]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        """Запрещаем удаление чужих объявлений."""
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                {"detail": "Удаление чужого объявления запрещено."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Запрещаем обновление чужих объявлений."""
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                {"detail": "Обновление чужого объявления запрещено."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Запрещаем частичное обновление чужих объявлений."""
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                {"detail": "Обновление чужого объявления запрещено."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().partial_update(request, *args, **kwargs)
