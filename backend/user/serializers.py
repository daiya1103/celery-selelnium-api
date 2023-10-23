from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.utils.html import linebreaks, urlize

from scrape.models import (
    Amazon,
    Mercari,
    Rakuma,
    Yahoo,
    Paypay,
    Recipe,
    Keyword,
    Common,
)


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value: str) -> str:
        return make_password(value)


class AmazonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amazon
        fields = "__all__"


class MercariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercari
        fields = "__all__"


class YahooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yahoo
        fields = "__all__"


class RakumaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rakuma
        fields = "__all__"


class PaypaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Paypay
        fields = "__all__"


class UserSerializer(WritableNestedModelSerializer):
    amazon = AmazonSerializer()
    mercari = MercariSerializer()
    amazon = AmazonSerializer()
    amazon = AmazonSerializer()

    class Meta:
        model = get_user_model()
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
            "mercari": {"read_only": True},
        }


class KeywordSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Keyword
        fields = (
            "id",
            "keyword",
            "bool",
            "site",
            "category_1",
            "category_2",
            "search_amount",
            "second_keyword_1",
            "second_keyword_2",
            "second_keyword_3",
            "second_keyword_4",
            "second_keyword_5",
            "row",
        )
        extra_kwargs = {
            "keyword": {"required": False},
            "bool": {"required": False},
            "site": {"required": False},
            "category_1": {"required": False},
            "category_2": {"required": False},
            "search_amount": {"required": False},
            "second_keyword_1": {"required": False},
            "second_keyword_2": {"required": False},
            "second_keyword_3": {"required": False},
            "second_keyword_4": {"required": False},
            "second_keyword_5": {"required": False},
        }


class KeywordPostSerializer(WritableNestedModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())

    class Meta:
        model = Keyword
        fields = "__all__"


class RecipeSerializer(WritableNestedModelSerializer):
    keywords = KeywordSerializer(many=True)

    class Meta:
        model = Recipe
        fields = "__all__"
        extra_keywargs = {"user": {"read_only": True}}


class CommonSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common
        fields = "__all__"
        extra_keywargs = {"user": {"read_only": True}}
