from django.contrib import admin
from .models import (
    Nutrient,
    Edible,
    Recipe,
    EdibleIngredients,
    NutrientContent,
    WeightMeasure,
)


class NutrientContentInline(admin.TabularInline):
    model = NutrientContent
    extra = 3


class EdibleAdmin(admin.ModelAdmin):
    inlines = [NutrientContentInline]


class EdibleIngredientsInline(admin.TabularInline):
    model = EdibleIngredients
    fk_name = 'product'
    extra = 8


class RecipeAdmin(admin.ModelAdmin):
    inlines = [EdibleIngredientsInline]


admin.site.register(Nutrient)
admin.site.register(Edible, EdibleAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(EdibleIngredients)
admin.site.register(NutrientContent)
admin.site.register(WeightMeasure)
