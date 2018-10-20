from django.contrib import admin

# Register your models here.

from .models import Member, Web, Game, Bundle, GameKey


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )


@admin.register(Web)
class WebAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'access_key',
    )
    search_fields = (
        'name',
    )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'company',
    )
    search_fields = (
        'name',
        'company',
    )


@admin.register(Bundle)
class BundleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )


@admin.register(GameKey)
class GameKeyAdmin(admin.ModelAdmin):
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
    readonly_fields = ('profit', 'profit_pct', )
    search_fields = (
        'game__name',
        'buyer__name'
    )
