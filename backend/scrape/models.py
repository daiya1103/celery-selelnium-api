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

    brand_name = models.CharField(max_length=255, default="ノーブランド品")

    maker = models.CharField(max_length=255, default="ノーブランド品")

    type_of_product = models.CharField(max_length=255, default="Hobbies")

    contidion_of_product = models.CharField(max_length=255, default="新品")

    browse_node = models.PositiveIntegerField(default=3113755051)

    random_charactor = models.PositiveIntegerField(default=1)

    prefix = models.CharField(max_length=255, default="")


class Ngword(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="ngwords"
    )

    row = models.PositiveIntegerField()

    value = models.CharField(max_length=255)


class Exclusion(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="exclusions"
    )

    row = models.PositiveIntegerField()

    value = models.CharField(max_length=255)


class Replace(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="replaces"
    )

    row = models.PositiveIntegerField()

    before = models.CharField(max_length=255)

    after = models.CharField(max_length=255)


class Delete(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="deletes"
    )

    row = models.PositiveIntegerField()

    value = models.CharField(max_length=255)


class DefaultMargin(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="margin"
    )

    bool = models.BooleanField(default=True)

    margin = models.PositiveIntegerField(blank=True, null=True)

    delivery = models.PositiveIntegerField(blank=True, null=True)


class Margin(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="margins"
    )

    min_price = models.PositiveIntegerField(blank=True, null=True)

    max_price = models.PositiveIntegerField(blank=True, null=True)

    margin = models.PositiveIntegerField(blank=True, null=True)

    row = models.PositiveIntegerField(blank=True, null=True)


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

    order = models.CharField(max_length=255, default="おすすめ順")

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

    title = models.CharField(max_length=255, default="タイトルなし")

    num = models.PositiveIntegerField()


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

    search_amount = models.PositiveIntegerField(default=50)


class ResearchResult(models.Model):
    product_img1 = models.URLField()

    product_img2 = models.URLField(null=True, blank=True)

    product_img3 = models.URLField(null=True, blank=True)

    url = models.URLField()

    product_name = models.CharField(max_length=255)

    seller_id = models.CharField(max_length=255)

    product_price = models.PositiveIntegerField()

    condition = models.CharField(max_length=255)

    sell_status = models.CharField(max_length=255)

    task_id = models.CharField(max_length=255)
