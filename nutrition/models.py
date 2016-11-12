from django.db import models


class Nutrient(models.Model):
    """ This class describes a nutrient.

    This can be a macronutrient or any vitamin, basically anything on sub
    ingredient level. Corresponding table in USDA database is nutr_def.

    """
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name


class Edible(models.Model):
    """ This class describes anything that can be eaten.

    Corresponding table in USDA database is food_des.

    """
    name = models.CharField(max_length=30)
    description = models.TextField()
    _calories = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def calories(self):
        """ Calories per 100g.

        It's either the self._calories if assinged or a sum of calories of all
        the ingredients.

        """
        return self._calories or sum(
            [
                (i.ingredient.calories / i.amount)
                for i in self.ingredients.all()
            ]
        )


class Recipe(Edible):
    servings = models.IntegerField(default=1)

    @property
    def mass(self):
        return sum([i.amount for i in self.igredients])

    @property
    def serving_mass(self):
        return self.mass / self.servings


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

    def __str__(self):
        return "{} grams of {}".format(self.amount, self.ingredient.name)


class NutrientContent(models.Model):
    """ Objects of this class store information about content of nutrients
    in a given Edible.

    Corresponding table in USDA database is nut_data.

    """
    edible = models.ForeignKey('Edible', on_delete=models.CASCADE)
    nutrient = models.ForeignKey('Nutrient', on_delete=models.CASCADE)
    content = models.FloatField()

    def __str__(self):
        return "{} grams of {}".format(self.content, self.nutrient.name)


class WeightMeasure(models.Model):
    """ Objects of this class represent the amount of a given Edible contained
    by household measures.

    Corresponding table in USDA database is weight.

    """
    edible = models.ForeignKey('Edible', on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.CharField(max_length=200)
    weight = models.FloatField()
