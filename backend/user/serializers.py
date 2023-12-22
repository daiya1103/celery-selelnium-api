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
    Ngword,
    Exclusion,
    Delete,
    Replace,
    Margin,
    DefaultMargin,
    ResearchResult,
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
            "row",
        )
        extra_kwargs = {
            "keyword": {"required": False},
            "bool": {"required": False},
            "site": {"required": False},
            "category_1": {"required": False},
            "category_2": {"required": False},
            "search_amount": {"required": False},
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


class NgwordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ngword
        fields = "__all__"
        extra_keywargs = {"user": {"read_only": True}}


class ExclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exclusion
        fields = "__all__"
        extra_keywargs = {"user": {"read_only": True}}


class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delete
        fields = "__all__"
        extra_keywargs = {"user": {"read_only": True}}


class ReplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replace
        fields = "__all__"
        extra_keywargs = {"user": {"read_only": True}}


class DefaultMarginSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultMargin
        fields = "__all__"
        extra_keywargs = {"user": {"read_only": True}}


class MarginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Margin
        fields = "__all__"
        extra_keywargs = {"user": {"read_only": True}, 'max_price': {'required': False}}


class NgSettingSerializer(WritableNestedModelSerializer):
    ngwords = NgwordSerializer(many=True)
    exclusions = ExclusionSerializer(many=True)
    deletes = DeleteSerializer(many=True)
    replaces = ReplaceSerializer(many=True)
    margins = MarginSerializer(many=True)
    margin = DefaultMarginSerializer()
    amazon = AmazonSerializer()

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "ngwords",
            "exclusions",
            "deletes",
            "replaces",
            "margins",
            "margin",
            "amazon",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "mercari": {"read_only": True},
        }


class MainInfomationSerializer(WritableNestedModelSerializer):
    ngwords = NgwordSerializer(many=True)
    exclusions = ExclusionSerializer(many=True)
    deletes = DeleteSerializer(many=True)
    replaces = ReplaceSerializer(many=True)
    margins = MarginSerializer(many=True)
    margin = DefaultMarginSerializer()
    amazon = AmazonSerializer()
    mercari = MercariSerializer()
    yahoo = YahooSerializer()
    recipes = RecipeSerializer(many=True)
    common = CommonSettingSerializer()

    class Meta:
        model = get_user_model()
        fields = (
            "ngwords",
            "exclusions",
            "deletes",
            "replaces",
            "margins",
            "margin",
            "amazon",
            "mercari",
            "recipes",
            "common",
            "yahoo",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "mercari": {"read_only": True},
        }


class ResearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchResult
        fields = "__all__"
        extra_kwargs = {
            "product_img2": {"required": False},
            "product_img3": {"required": False},
        }
