from restaurants.models import Restaurant
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
    RestaurantListSerializer,
    RestaurantDetailSerializer,
    RestaurantCreateUpdateSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner
from rest_framework.filters import SearchFilter,OrderingFilter

class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    permission_classes = [AllowAny,]
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name','description']



class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'
    permission_classes = [AllowAny,]


class RestaurantCreateView(CreateAPIView):
    serializer_class = RestaurantCreateUpdateSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RestaurantUpdateView(RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'
    permission_classes = [IsAuthenticated,IsOwner]


class RestaurantDeleteView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'
    permission_classes = [IsAuthenticated,IsAdminUser]