from django.contrib import admin
from .models import (
    Nutrient,
    Edible,
    Recipe,
    EdibleIngredients,
    NutrientContent,
)


admin.site.register(Nutrient)
admin.site.register(Edible)
admin.site.register(Recipe)
admin.site.register(EdibleIngredients)
admin.site.register(NutrientContent)
