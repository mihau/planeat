from django.db import models


class Nutrient(models.Model):
    """ This class describes a nutrient.

    This can be a macronutrient or any vitamin, basically anything on sub
    ingredient level

    """
    name = models.CharField(max_length=30)
    description = models.TextField()


class Edible(models.Model):
    """ This class describes anything that can be eaten.

    """
    name = models.CharField(max_length=30)
    description = models.TextField()
    _calories = models.IntegerField(blank=True, null=True)


class Recipe(Edible):
    servings = models.IntegerField(default=1)


class EdibleIngredients(models.Model):
    """ Objects of this class allow to define an Edible consisting of multiple
    other ingredients (which are Edibles as well).

    By default the amount is expressed in grams.

    """
    product = models.ForeignKey(
        'Edible',
        on_delete=models.CASCADE,
        related_name='ingredients',
    )
    ingredient = models.ForeignKey(
        'Edible',
        on_delete=models.CASCADE,
        related_name='products',
    )
    amount = models.FloatField()


class NutrientContent(models.Model):
    """ Objects of this class store information about content of nutrients
    in a given Edible.

    """
    edible = models.ForeignKey('Edible', on_delete=models.CASCADE)
    nutrient = models.ForeignKey('Nutrient', on_delete=models.CASCADE)
    content = models.FloatField()
