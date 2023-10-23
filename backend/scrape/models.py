from django.db import models
from django.contrib.auth import get_user_model
import json


class Amazon(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    # amazonの出品設定
    condition = models.TextField(default="")

    days_shipping = models.PositiveIntegerField(default=10)

    point = models.PositiveIntegerField(default=2)

    amount = models.PositiveIntegerField(default=2)

    brand_name = models.CharField(max_length=255, default="ノーブランド")

    maker = models.CharField(max_length=255, default="ノーブランド")

    type_of_product = models.CharField(max_length=255, default="Hobbies")

    contidion_of_product = models.CharField(max_length=255, default="新品")

    browse_node = models.PositiveIntegerField(default=2189388051)

    random_charactor = models.PositiveIntegerField(default=1)

    prefix = models.CharField(max_length=255, default="")

    csv_bool = models.BooleanField(default=False, verbose_name="リサーチ完了後、csvを出力する")

    get_bool = models.BooleanField(default=False, verbose_name="リサーチ完了後、そのまま商品情報を取得する")

    csv_bool = models.BooleanField(
        default=False, verbose_name="第1キーワードを含まない商品を検索結果から除外する"
    )


class Mercari(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    price_min = models.PositiveIntegerField(default=2999)

    price_max = models.PositiveIntegerField(default=40000)

    # 商品の状態
    # 新品未使用
    condition_new = models.BooleanField(default=False)

    # 未使用に近い
    condition_close_to_new = models.BooleanField(default=False)

    # 目立った傷や汚れなし
    condition_ok = models.BooleanField(default=False)

    # やや傷や汚れあり
    condition_soso = models.BooleanField(default=False)

    # 傷や汚れあり
    condition_not_ok = models.BooleanField(default=False)

    # 全体的に状態が悪い
    condition_bad = models.BooleanField(default=False)

    order = models.CharField(max_length=255, default="すべて")

    on_sale = models.BooleanField(default=False)

    sold_out = models.BooleanField(default=False)


class Yahoo(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    # レシピ > 設定 > ヤフオク
    price_type = models.CharField(max_length=255, default="bidorbuyprice")

    price_min = models.PositiveIntegerField(default=2999)

    price_max = models.PositiveIntegerField(default=30000)
    # 商品の状態
    # 未使用
    condition_new = models.BooleanField(default=False)

    # 中古
    condition_used = models.BooleanField(default=False)

    # 未使用品に近い
    condition_close_to_new = models.BooleanField(default=False)

    # 目立った傷や汚れなし
    condition_ok = models.BooleanField(default=False)

    # やや傷や汚れあり
    condition_soso = models.BooleanField(default=False)

    # 傷や汚れあり
    condition_not_ok = models.BooleanField(default=False)

    # 全体的に状態が悪い
    condition_bad = models.BooleanField(default=False)

    order = models.CharField(max_length=255, default="new")

    status = models.CharField(max_length=255, default="販売中")

    # 出品者
    abatch = models.CharField(max_length=255, default="")

    option_delivery = models.BooleanField(default=False)

    option_new = models.BooleanField(default=False)

    option_end = models.BooleanField(default=False)

    option_anon = models.BooleanField(default=False)

    option_konbini = models.BooleanField(default=False)


class Rakuma(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    price_min = models.PositiveIntegerField(default=2999)

    price_max = models.PositiveIntegerField(default=30000)

    condition = models.CharField(max_length=255, default="new")

    official_item_type = models.CharField(max_length=255, default="")

    anonymous_shipping = models.BooleanField(default=False)

    # 配送料の負担
    carriage = models.BooleanField(default=False)

    # 販売状況
    transaction = models.CharField(max_length=255, default="selling")


class Paypay(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    price_min = models.PositiveIntegerField(default=2999)

    price_max = models.PositiveIntegerField(default=10000)

    # 未使用
    condition_new = models.BooleanField(default=False)

    # 未使用品に近い
    condition_close_to_new = models.BooleanField(default=False)

    # 目立った傷や汚れなし
    condition_ok = models.BooleanField(default=False)

    # やや傷や汚れあり
    condition_soso = models.BooleanField(default=False)

    # 傷や汚れあり
    condition_not_ok = models.BooleanField(default=False)

    order = models.CharField(max_length=255, default="openTime")


class Common(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    csv = models.BooleanField(default=False)

    get_info = models.BooleanField(default=False)

    exclusion = models.BooleanField(default=False)

    exclusion_size = models.PositiveIntegerField(default=10)


class Recipe(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="recipes"
    )

    title = models.CharField(max_length=255)


class Keyword(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="keywords"
    )

    keyword = models.CharField(default="", max_length=255)

    row = models.PositiveIntegerField()

    bool = models.BooleanField(default=False)

    site = models.CharField(default="", max_length=10)

    category_1 = models.CharField(default="", max_length=255)

    category_2 = models.CharField(default="", max_length=255)

    second_keyword_1 = models.CharField(
        default="", max_length=255, null=True, blank=True
    )

    second_keyword_2 = models.CharField(
        default="", max_length=255, null=True, blank=True
    )

    second_keyword_3 = models.CharField(
        default="", max_length=255, null=True, blank=True
    )

    second_keyword_4 = models.CharField(
        default="", max_length=255, null=True, blank=True
    )

    second_keyword_5 = models.CharField(
        default="", max_length=255, null=True, blank=True
    )

    search_amount = models.PositiveIntegerField(default=50)
