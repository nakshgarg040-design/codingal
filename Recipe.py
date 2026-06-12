pasta = ("Pasta", "Italian", "20", "Easy")
Biryani = ("Biryani", "Indian", "30", "Hard")
print("Recipe:"[1])
print("Cuisine:"[-1])

all_recipes = [pasta, Biryani]
print("\nFirst recipe name:", all_recipes[0][0])
print("Second recipe time:", all_recipes[1][2], "mins")
print("pasta details(sliced):", pasta[1:3])
Pasta_ingredients = {"Pasta", "Tomato Sauce", "Cheese", "Basil"}
Biryani_ingredients = {"Rice", "Chicken", "Spices", "Yogurt"}
print("\n pasta details:", pasta[1:3])
print("Biryani_Ingredients:", Biryani_ingredients)
print("Total ingredients for both recipes:", len(Pasta_ingredients) + len(Biryani_ingredients))

Pasta_ingredients.add("Garlic")
Pasta_ingredients.discard("Basil")
print("\nUpdated pasta ingredients:", Pasta_ingredients)

all_ingredients = Pasta_ingredients.union(Biryani_ingredients)
common_ingredients = Pasta_ingredients.intersection(Biryani_ingredients)
pasta_unique_ingredients = Pasta_ingredients.difference(Biryani_ingredients)
unique = Biryani_ingredients.difference(Pasta_ingredients)
print("\nAll ingredients:", all_ingredients)
print("Common ingredients:", common_ingredients)
print("Pasta unique ingredients:", pasta_unique_ingredients)
print("Biryani unique ingredients:", unique)