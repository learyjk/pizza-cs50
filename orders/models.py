from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=16, blank=False)

    def __str__(self):
        return f"{self.name}"


class Size(models.Model):
    name = models.CharField(max_length=16, blank=False)

    def __str__(self):
        return self.name


class PizzaStyle(models.Model):
    name = models.CharField(max_length=16, blank=False)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Extra(models.Model):
    name = models.CharField(max_length=64)
    added_cost = models.DecimalField(max_digits=5, default=0.50, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class PastaStyle(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class SaladStyle(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class DinnerPlatterStyle(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="pizza")
    style = models.ForeignKey(PizzaStyle, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    num_toppings = models.IntegerField()
    toppings = models.ManyToManyField(Topping, blank=True)
    price = models.DecimalField(max_digits=5, default=0.00, decimal_places=2)

    def toppings_list(self):
        return "\n".join([p.name for p in self.toppings.all()])

    def special(self):
        if self.is_special:
            return "Yes"
        else:
            return "No"

    def __str__(self):
        return f"{self.menu}: {self.style} | {self.size} | Special?: {self.special()} | "


class Sub(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="sub")
    ingredients = models.ForeignKey(Ingredient, blank=False, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    extras = models.ManyToManyField(Extra, blank=True)
    price = models.DecimalField(max_digits=5, default=0.00, decimal_places=2)

    def extras_list(self):
        query_set = self.extras.all()
        if not query_set:
            return "No extras"
        else:
            return "\n".join([p.name for p in query_set])

    def __str__(self):
        extras = self.extras_list()
        return f"{self.menu}: {self.ingredients} | {self.size} | {self.price} | Extras: {extras}"


class Pasta(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="pasta")
    style = models.ForeignKey(PastaStyle, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, default=0.00, decimal_places=2)

    def __str__(self):
        return f"{self.menu} | {self.style} | {self.price}"


class Salad(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="salad")
    style = models.ForeignKey(SaladStyle, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, default=0.00, decimal_places=2)

    def __str__(self):
        return f"{self.menu} | {self.style} | {self.price}"


class DinnerPlatter(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="dinner_platter")
    style = models.ForeignKey(DinnerPlatterStyle, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, default=0.00, decimal_places=2)

    def __str__(self):
        return f"{self.menu} | {self.style} | {self.price}"
