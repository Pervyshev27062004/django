from rest_framework import serializers

from products.models import Product


class ProductModelSerializer(serializers.HyperlinkedModelSerializer):
    has_image = serializers.SerializerMethodField()

    purchases_count = serializers.IntegerField()
    purchases_total = serializers.IntegerField()

    def get_has_image(self, obj: Product) -> bool:
        return bool(obj.image)

    def get_purchases_count(self, obj: Product) -> int:
        return obj.purchases.count()

    def get_purchases_total(self, obj: Product) -> int:
        return 0

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "has_image",
            "purchases_count",
            "purchases_total",
            "image",
            "color",
            "price",
            "created_at",
            "description",
        ]


class ProductSerializer(serializers.Serializer):
    external_id = serializers.CharField(
        max_length=255, allow_blank=True, allow_null=True
    )
    title = serializers.CharField(max_length=255)
    image = serializers.ImageField(allow_empty_file=True)
    color = serializers.CharField(max_length=32)
    price = serializers.DecimalField(decimal_places=5, max_digits=10)
    price_eur = serializers.DecimalField(decimal_places=5, max_digits=10)
    excerpt = serializers.CharField(allow_blank=True, allow_null=True)
    description = serializers.CharField(allow_blank=True, allow_null=True)
    purchases_total = serializers.DecimalField(decimal_places=5, max_digits=10)
    created_at = serializers.DateTimeField()
