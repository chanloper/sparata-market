
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Product
from .serializers import ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # 현재 로그인한 사용자를 가져와서 serializer에 저장
        serializer.save(user=self.request.user)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        product = self.get_object()
        if product.user != self.request.user:
            raise PermissionDenied("해당 제품을 수정할 수 있는 권한이 없습니다.")
        serializer.save()


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        # 작성자가 맞는지 확인
        if instance.user != self.request.user:
            raise PermissionDenied("해당 제품을 삭제할 수 있는 권한이 없습니다.")
        instance.delete()
