# Generated by Django 2.0 on 2020-06-28 16:33

from django.db import migrations
from db_tools.data import category_data, product_data
from goods.models import GoodsCategory, Goods, GoodsImage


def import_category(apps, schema_editor):
    for lev1_cat in category_data.row_data:
        lev1_instance = GoodsCategory()
        lev1_instance.code = lev1_cat['code']
        lev1_instance.name = lev1_cat['name']
        lev1_instance.category_type = 1
        lev1_instance.save()

        for lev2_cat in lev1_cat['sub_categorys']:
            lev2_instance = GoodsCategory()
            lev2_instance.code = lev2_cat['code']
            lev2_instance.name = lev2_cat['name']
            lev2_instance.category_type = 2
            lev2_instance.parent_category = lev1_instance
            lev2_instance.save()

            for lev3_cat in lev2_cat['sub_categorys']:
                lev3_instance = GoodsCategory()
                lev3_instance.code = lev3_cat['code']
                lev3_instance.name = lev3_cat['name']
                lev3_instance.category_type = 3
                lev3_instance.parent_category = lev2_instance
                lev3_instance.save()


def import_goods(apps, schema_editor):
    from goods.models import Goods, GoodsCategory, GoodsImage

    for goods_detail in product_data.row_data:
        goods = Goods()
        goods.name = goods_detail['name']
        goods.market_price = float(goods_detail['market_price'].replace('￥', '').replace('元', ''))
        goods.shop_price = float(goods_detail['sale_price'].replace('￥', '').replace('元', ''))
        goods.goods_brief = goods_detail['desc'] if goods_detail['desc'] is not None else ''
        goods.goods_desc = goods_detail['goods_desc'] if goods_detail['goods_desc'] is not None else ''
        goods.goods_front_image = goods_detail['images'][0] if goods_detail['images'] else ''

        category_name = goods_detail['categorys'][-1]
        category = GoodsCategory.objects.filter(name=category_name)
        if category:
            goods.category = category[0]
        goods.save()

        for goods_image in goods_detail['images']:
            goods_image_instance = GoodsImage()
            goods_image_instance.image = goods_image
            goods_image_instance.goods = goods
            goods_image_instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20200609_1706'),
    ]

    operations = [
        migrations.RunPython(import_category),
        migrations.RunPython(import_goods)
    ]