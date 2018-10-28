from django.contrib import admin

from import_export import resources, fields
from import_export.admin import (
    ImportExportModelAdmin,
    ImportExportActionModelAdmin,
)

# Register your models here.
from import_export.widgets import ForeignKeyWidget

from .models import Member, Web, Game, Bundle, GameKey


class MemberResource(resources.ModelResource):
    class Meta:
        model = Member
        skip_unchanged = True
        report_skipped = False


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin,
                  ImportExportActionModelAdmin,
                  admin.ModelAdmin):
    resource_class = MemberResource
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )


class WebResource(resources.ModelResource):
    class Meta:
        model = Web
        skip_unchanged = True
        report_skipped = False


@admin.register(Web)
class WebAdmin(ImportExportModelAdmin,
               ImportExportActionModelAdmin,
               admin.ModelAdmin):
    resource_class = WebResource
    list_display = (
        'name', 'access_key',
    )
    search_fields = (
        'name',
    )


class GameResource(resources.ModelResource):
    class Meta:
        model = Game
        skip_unchanged = True
        report_skipped = False


@admin.register(Game)
class GameAdmin(ImportExportModelAdmin,
                ImportExportActionModelAdmin,
                admin.ModelAdmin):
    resource_class = GameResource
    list_display = (
        'name', 'company',
    )
    search_fields = (
        'name',
        'company',
    )


class BundleResource(resources.ModelResource):
    class Meta:
        model = Bundle
        skip_unchanged = True
        report_skipped = False


@admin.register(Bundle)
class BundleAdmin(ImportExportModelAdmin,
                  ImportExportActionModelAdmin,
                  admin.ModelAdmin):
    resource_class = BundleResource
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )


class GameKeyResource(resources.ModelResource):
    game = fields.Field(
        column_name='game',
        attribute='game',
        widget=ForeignKeyWidget(Game, 'name'))

    buyer = fields.Field(
        column_name='buyer',
        attribute='buyer',
        widget=ForeignKeyWidget(Member, 'name'))

    sell_web = fields.Field(
        column_name='sell_web',
        attribute='sell_web',
        widget=ForeignKeyWidget(Web, 'name'))

    class Meta:
        model = GameKey
        skip_unchanged = True
        report_skipped = False
        fields = (
            'id',
            'game',
            'key',
            'buyer',
            'buy_date',
            'buy_price',
            'minimum_sell_price',
            'sell_date',
            'sell_price',
            'sell_web',
        )


@admin.register(GameKey)
class GameKeyAdmin(ImportExportModelAdmin,
                   ImportExportActionModelAdmin,
                   admin.ModelAdmin):
    resource_class = GameKeyResource
    list_display = (
        'game',
        'key',
        'buyer',
        'buy_date',
        'buy_price',
        'minimum_sell_price',
        'sell_date',
        'sell_price',
        'sell_web',
    )
    readonly_fields = ('profit', 'profit_pct',)
    search_fields = (
        'game__name',
        'buyer__name'
    )
