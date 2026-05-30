from collections import Counter
import re

from flask import Flask, abort, render_template, request

from recipes import get_recipes

app = Flask(__name__)


def normalize_text(text):
    text = str(text or "").lower().strip()
    text = re.sub(r"[^a-z0-9\s\-]", " ", text)
    text = text.replace("-", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def singularize(word):
    word = normalize_text(word)
    if len(word) > 3 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 3 and word.endswith("es"):
        return word[:-2]
    if len(word) > 3 and word.endswith("s"):
        return word[:-1]
    return word


def slugify(text):
    text = normalize_text(text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def normalize_diet(value):
    value = normalize_text(value)
    if value in {"non veg", "nonveg", "non vegetarian", "nonvegetarian", "non-veg"}:
        return "non-veg"
    if value in {"veg", "vegetarian"}:
        return "veg"
    if value in {"", "all", "any"}:
        return "all"
    return value


def ensure_list(value):
    if not value:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        if "|" in value:
            parts = value.split("|")
        elif "\n" in value:
            parts = value.splitlines()
        elif "," in value and len(value.split(",")) > 1:
            parts = value.split(",")
        else:
            parts = [value]
        return [part.strip() for part in parts if str(part).strip()]
    return [str(value).strip()]


def parse_user_ingredients(text):
    if not text:
        return []

    items = re.split(r"[,\n]", text)
    tokens = []

    for item in items:
        item = normalize_text(item)
        if not item:
            continue

        for token in item.split():
            token = singularize(token)
            if token and token not in tokens:
                tokens.append(token)

    return tokens


def recipe_defaults(recipe):
    recipe = dict(recipe or {})
    name = str(recipe.get("name", "Unknown Recipe")).strip() or "Unknown Recipe"

    recipe["name"] = name
    recipe["slug"] = slugify(name)
    recipe["diet"] = normalize_diet(recipe.get("diet", "veg"))
    recipe["time"] = int(float(recipe.get("time", 20) or 20))
    recipe["rating"] = round(float(recipe.get("rating", 4.5) or 4.5), 1)
    recipe["difficulty"] = str(recipe.get("difficulty", "Easy")).strip() or "Easy"
    recipe["description"] = str(recipe.get("description", "A simple homemade recipe.")).strip()

    recipe["emoji"] = str(recipe.get("emoji", "🍲")).strip() or "🍲"
    recipe["category"] = str(recipe.get("category", "general")).strip() or "general"

    recipe["ingredients"] = ensure_list(recipe.get("ingredients"))
    recipe["resources"] = ensure_list(recipe.get("resources")) or ["stove"]
    recipe["tags"] = ensure_list(recipe.get("tags"))
    recipe["steps"] = ensure_list(recipe.get("steps"))
    recipe["tips"] = ensure_list(recipe.get("tips"))
    recipe["notes"] = ensure_list(recipe.get("notes"))
    recipe["serving"] = ensure_list(recipe.get("serving"))
    recipe["avoid"] = ensure_list(recipe.get("avoid"))

    return recipe


def mode_matches(recipe, selected_mode):
    mode = normalize_text(selected_mode)
    if mode in {"", "all", "any"}:
        return True

    tags = {normalize_text(tag) for tag in recipe.get("tags", [])}
    time_value = int(recipe.get("time", 999) or 999)
    resource_set = {normalize_text(r) for r in recipe.get("resources", [])}

    if mode == "quick":
        return time_value <= 15 or "quick" in tags
    if mode == "healthy":
        return "healthy" in tags
    if mode == "air fryer":
        return "air fryer" in tags or "air fryer" in resource_set
    if mode == "microwave":
        return "microwave" in tags or "microwave" in resource_set

    return mode in tags


def calculate_match(user_ingredients, recipe):
    recipe_tokens = set()

    for ingredient in recipe.get("ingredients", []):
        for token in normalize_text(ingredient).split():
            recipe_tokens.add(singularize(token))

    for token in normalize_text(recipe.get("name", "")).split():
        recipe_tokens.add(singularize(token))

    user_tokens = set(user_ingredients)
    matched = sorted(user_tokens & recipe_tokens)
    missing = sorted(user_tokens - recipe_tokens)

    if not user_tokens:
        return round(recipe.get("rating", 0) * 20, 1), matched, missing

    score = round((len(matched) / max(len(user_tokens), 1)) * 100, 1)
    return score, matched, missing


def default_steps(recipe):
    name = recipe.get("name", "this recipe")
    return [
        f"Gather and measure all ingredients for {name}.",
        "Wash, chop, and prep the ingredients before cooking.",
        "Heat the pan, tawa, or appliance on medium heat.",
        "Cook the main ingredients slowly and keep stirring when needed.",
        "Add spices, sauces, or seasoning gradually and taste in between.",
        "Cook until the texture looks right and the flavour is balanced.",
        f"Serve {name} hot and fresh for the best taste.",
    ]


def default_tips(recipe):
    tips = [
        "Use fresh ingredients whenever possible.",
        "Keep the flame medium unless the recipe says otherwise.",
        "Taste before serving and adjust salt or spice carefully.",
        "Do not overcook or overmix the dish.",
    ]

    slug = recipe.get("slug", "")
    if any(key in slug for key in ["pasta", "noodles", "fried-rice"]):
        tips.append("Reserve a little sauce or water so the dish stays moist.")
    if any(key in slug for key in ["shake", "smoothie", "coffee"]):
        tips.append("Chill the ingredients first for a better texture.")
    if any(key in slug for key in ["paratha", "dosa", "pancake", "waffle"]):
        tips.append("Brush a little butter or ghee for better colour and aroma.")

    return tips


def default_notes(recipe):
    notes = [
        "Read the full recipe once before you start cooking.",
        "Prep everything first so the cooking process feels easy.",
    ]
    if "healthy" in {normalize_text(t) for t in recipe.get("tags", [])}:
        notes.append("This recipe is a good option for a lighter meal.")
    if any(key in recipe.get("slug", "") for key in ["paneer", "chicken", "egg"]):
        notes.append("Do not overcook the main protein so it stays soft and tender.")
    return notes


def default_serving(recipe):
    slug = recipe.get("slug", "")
    if any(key in slug for key in ["shake", "smoothie", "coffee"]):
        return [
            "Serve chilled in a tall glass.",
            "Add ice cream or whipped cream for a richer finish.",
        ]
    if any(key in slug for key in ["paratha", "dosa", "idli", "pancake", "waffle"]):
        return [
            "Serve hot with chutney, curd, syrup, or pickle.",
            "Best enjoyed fresh off the tawa or pan.",
        ]
    if any(key in slug for key in ["pasta", "noodles", "fried-rice"]):
        return [
            "Serve hot with grated cheese or herbs on top.",
            "Pair with garlic bread or a simple salad.",
        ]
    return [
        "Serve immediately after cooking.",
        "Pair with chutney, salad, curd, or a side dish as needed.",
    ]


def default_avoid(recipe):
    return [
        "Do not rush the cooking step.",
        "Avoid using too much oil, water, or spice at once.",
        "Do not serve before checking seasoning.",
    ]


RAW_RECIPES = get_recipes() if callable(get_recipes) else []
ALL_RECIPES = [recipe_defaults(recipe) for recipe in RAW_RECIPES]

def build_nutrition(name, recipe):
    n = normalize_text(name)
    tags = {normalize_text(t) for t in recipe.get("tags", [])}
    ingredients = {normalize_text(i) for i in recipe.get("ingredients", [])}

    base = {
        "calories": "280 kcal",
        "protein": "9 g",
        "fat": "10 g",
        "carbs": "34 g",
        "fiber": "4 g",
        "sugar": "3 g",
        "sodium": "420 mg",
        "vitamin_a": "90 mcg",
        "vitamin_c": "8 mg",
        "calcium": "120 mg",
        "iron": "2.0 mg",
        "potassium": "360 mg",
        "magnesium": "32 mg",
        "zinc": "1.0 mg",
        "health_score": 76,
        "best_for": "Balanced meal",
        "allergens": "Varies by ingredients",
        "storage": "Best fresh, refrigerate for 1 day",
        "good_for": "Everyday meal",
        "gi_index": "Medium",
        "best_time": "Lunch",
        "summary": "A balanced homemade recipe with moderate calories and useful nutrition.",
    }

    def update(values):
        base.update(values)

    # Breakfast / bread / flatbread
    if "paratha" in n:
        update({
            "calories": "320 kcal",
            "protein": "9 g",
            "fat": "12 g",
            "carbs": "42 g",
            "fiber": "5 g",
            "sugar": "3 g",
            "sodium": "480 mg",
            "vitamin_a": "110 mcg",
            "vitamin_c": "8 mg",
            "calcium": "140 mg",
            "iron": "2.4 mg",
            "potassium": "410 mg",
            "magnesium": "38 mg",
            "zinc": "1.1 mg",
            "health_score": 78,
            "best_for": "Breakfast",
            "allergens": "Gluten, Dairy",
            "storage": "Best fresh, refrigerate for 1 day",
            "good_for": "Balanced meal",
            "gi_index": "Medium",
            "best_time": "Breakfast",
            "summary": "Stuffed paratha with moderate calories and satisfying energy.",
        })
        if "paneer" in n:
            base["calories"] = "350 kcal"
            base["protein"] = "14 g"
            base["fat"] = "15 g"
            base["calcium"] = "220 mg"
            base["health_score"] = 82
            base["good_for"] = "High protein meal"
            base["summary"] = "Protein-rich paneer paratha with good calcium and filling nutrition."
        if "aloo" in n:
            base["calories"] = "320 kcal"
            base["protein"] = "9 g"
            base["health_score"] = 78
        if "gobi" in n:
            base["calories"] = "300 kcal"
            base["protein"] = "8 g"
            base["fiber"] = "6 g"
            base["health_score"] = 80
        if "methi" in n:
            base["calories"] = "285 kcal"
            base["fiber"] = "5 g"
            base["health_score"] = 83

    elif "poha" in n:
        update({
            "calories": "220 kcal",
            "protein": "5 g",
            "fat": "7 g",
            "carbs": "35 g",
            "fiber": "4 g",
            "sugar": "2 g",
            "sodium": "310 mg",
            "vitamin_a": "60 mcg",
            "vitamin_c": "12 mg",
            "calcium": "60 mg",
            "iron": "1.4 mg",
            "potassium": "220 mg",
            "magnesium": "24 mg",
            "zinc": "0.8 mg",
            "health_score": 86,
            "best_for": "Breakfast",
            "allergens": "Peanuts (optional)",
            "storage": "Best fresh",
            "good_for": "Light meal",
            "gi_index": "Medium",
            "best_time": "Breakfast",
            "summary": "Light, quick, and easy breakfast with decent fiber and low fat.",
        })

    elif "upma" in n:
        update({
            "calories": "240 kcal",
            "protein": "6 g",
            "fat": "8 g",
            "carbs": "36 g",
            "fiber": "4 g",
            "sugar": "2 g",
            "sodium": "330 mg",
            "vitamin_a": "55 mcg",
            "vitamin_c": "10 mg",
            "calcium": "65 mg",
            "iron": "1.6 mg",
            "potassium": "240 mg",
            "magnesium": "26 mg",
            "zinc": "0.9 mg",
            "health_score": 84,
            "best_for": "Breakfast",
            "allergens": "Gluten",
            "storage": "Best fresh",
            "good_for": "Light breakfast",
            "gi_index": "Medium",
            "best_time": "Breakfast",
            "summary": "Comforting semolina breakfast with light nutrition and steady energy.",
        })

    elif any(x in n for x in ["idli", "dosa", "uttapam", "rava dosa", "neer dosa", "pesarattu"]):
        update({
            "calories": "250 kcal",
            "protein": "7 g",
            "fat": "7 g",
            "carbs": "38 g",
            "fiber": "3 g",
            "sugar": "2 g",
            "sodium": "360 mg",
            "vitamin_a": "50 mcg",
            "vitamin_c": "8 mg",
            "calcium": "80 mg",
            "iron": "1.8 mg",
            "potassium": "280 mg",
            "magnesium": "30 mg",
            "zinc": "0.9 mg",
            "health_score": 85,
            "best_for": "Breakfast",
            "allergens": "Varies by batter",
            "storage": "Best fresh",
            "good_for": "Light breakfast",
            "gi_index": "Medium",
            "best_time": "Breakfast",
            "summary": "South Indian breakfast with balanced carbs and light protein.",
        })

    # Sandwich / snacks
    elif any(x in n for x in ["sandwich", "toast", "burger", "wrap", "roll"]):
        update({
            "calories": "290 kcal",
            "protein": "9 g",
            "fat": "11 g",
            "carbs": "36 g",
            "fiber": "4 g",
            "sugar": "3 g",
            "sodium": "500 mg",
            "vitamin_a": "85 mcg",
            "vitamin_c": "6 mg",
            "calcium": "110 mg",
            "iron": "2.0 mg",
            "potassium": "330 mg",
            "magnesium": "28 mg",
            "zinc": "1.0 mg",
            "health_score": 74,
            "best_for": "Snack / Lunch",
            "allergens": "Gluten, Dairy",
            "storage": "Best fresh",
            "good_for": "Quick snack",
            "gi_index": "Medium",
            "best_time": "Evening",
            "summary": "Quick snack with moderate calories and easy serving.",
        })
        if "paneer" in n:
            base["protein"] = "14 g"
            base["calcium"] = "200 mg"
            base["health_score"] = 80
            base["summary"] = "Paneer-based sandwich or wrap with strong protein and calcium value."
        if "egg" in n:
            base["protein"] = "13 g"
            base["health_score"] = 79
        if "chicken" in n:
            base["protein"] = "18 g"
            base["health_score"] = 82

    # Rice / grain dishes
    elif any(x in n for x in ["rice", "pulao", "biryani", "khichdi", "chawal", "fried rice", "sambar rice", "jeera rice", "lemon rice"]):
        update({
            "calories": "360 kcal",
            "protein": "10 g",
            "fat": "9 g",
            "carbs": "58 g",
            "fiber": "5 g",
            "sugar": "3 g",
            "sodium": "450 mg",
            "vitamin_a": "75 mcg",
            "vitamin_c": "10 mg",
            "calcium": "90 mg",
            "iron": "2.4 mg",
            "potassium": "380 mg",
            "magnesium": "34 mg",
            "zinc": "1.0 mg",
            "health_score": 79,
            "best_for": "Lunch",
            "allergens": "Varies by recipe",
            "storage": "Refrigerate for 1 day",
            "good_for": "Filling meal",
            "gi_index": "Medium",
            "best_time": "Lunch",
            "summary": "Rice-based meal with steady energy and balanced satiety.",
        })
        if "rajma" in n:
            base["calories"] = "410 kcal"
            base["protein"] = "16 g"
            base["fiber"] = "10 g"
            base["iron"] = "4.8 mg"
            base["health_score"] = 84
            base["summary"] = "Hearty rajma chawal with good protein, fiber, and long-lasting energy."
        if "chole" in n:
            base["calories"] = "400 kcal"
            base["protein"] = "15 g"
            base["fiber"] = "9 g"
            base["health_score"] = 83
        if "khichdi" in n:
            base["calories"] = "300 kcal"
            base["protein"] = "11 g"
            base["fat"] = "7 g"
            base["fiber"] = "6 g"
            base["health_score"] = 87
            base["good_for"] = "Light meal"
            base["summary"] = "Comforting khichdi with lighter calories and balanced nutrition."
        if "fried rice" in n or "noodles" in n:
            base["calories"] = "380 kcal"
            base["protein"] = "11 g"
            base["health_score"] = 76

    # Curries / paneer / gravies
    elif any(x in n for x in ["curry", "masala", "bhurji", "paneer", "palak", "bhindi", "aloo gobi", "mushroom", "dal", "chole", "rajma"]):
        update({
            "calories": "330 kcal",
            "protein": "13 g",
            "fat": "14 g",
            "carbs": "28 g",
            "fiber": "5 g",
            "sugar": "5 g",
            "sodium": "540 mg",
            "vitamin_a": "120 mcg",
            "vitamin_c": "14 mg",
            "calcium": "160 mg",
            "iron": "2.9 mg",
            "potassium": "420 mg",
            "magnesium": "36 mg",
            "zinc": "1.2 mg",
            "health_score": 81,
            "best_for": "Lunch / Dinner",
            "allergens": "Dairy, Spices",
            "storage": "Refrigerate for 1 day",
            "good_for": "Protein / Balanced meal",
            "gi_index": "Medium",
            "best_time": "Lunch / Dinner",
            "summary": "Home-style curry with balanced nutrition and good satiety.",
        })
        if "paneer" in n:
            base["protein"] = "15 g"
            base["calcium"] = "220 mg"
            base["health_score"] = 84
        if "palak" in n:
            base["vitamin_a"] = "280 mcg"
            base["iron"] = "4.0 mg"
            base["health_score"] = 88
            base["summary"] = "Spinach-based dish with strong iron and vitamin A value."
        if "bhindi" in n:
            base["fiber"] = "7 g"
            base["health_score"] = 86
        if "dal" in n:
            base["protein"] = "15 g"
            base["fiber"] = "8 g"
            base["health_score"] = 87
        if "rajma" in n or "chole" in n:
            base["protein"] = "16 g"
            base["fiber"] = "9 g"
            base["health_score"] = 84

    # Drinks / shakes / tea / coffee
    elif any(x in n for x in ["shake", "coffee", "tea", "lassi", "chaas", "water", "juice", "smoothie", "drink"]):
        update({
            "calories": "180 kcal",
            "protein": "6 g",
            "fat": "5 g",
            "carbs": "24 g",
            "fiber": "1 g",
            "sugar": "16 g",
            "sodium": "110 mg",
            "vitamin_a": "40 mcg",
            "vitamin_c": "4 mg",
            "calcium": "120 mg",
            "iron": "0.8 mg",
            "potassium": "240 mg",
            "magnesium": "16 mg",
            "zinc": "0.5 mg",
            "health_score": 70,
            "best_for": "Drink",
            "allergens": "Dairy",
            "storage": "Serve immediately",
            "good_for": "Quick refreshment",
            "gi_index": "Medium",
            "best_time": "Anytime",
            "summary": "Refreshing drink with moderate calories and quick preparation.",
        })
        if "milk" in ingredients or "milk" in n:
            base["calcium"] = "180 mg"
            base["protein"] = "7 g"
        if "coffee" in n:
            base["summary"] = "Coffee-based drink with milk and light energy value."
        if "tea" in n:
            base["summary"] = "Classic tea with moderate calories and daily refreshment value."

    # Desserts
    elif any(x in n for x in ["halwa", "kheer", "gulab jamun", "rasgulla", "dessert", "sweet", "pudding"]):
        update({
            "calories": "260 kcal",
            "protein": "5 g",
            "fat": "8 g",
            "carbs": "44 g",
            "fiber": "1 g",
            "sugar": "24 g",
            "sodium": "120 mg",
            "vitamin_a": "55 mcg",
            "vitamin_c": "2 mg",
            "calcium": "90 mg",
            "iron": "1.0 mg",
            "potassium": "180 mg",
            "magnesium": "18 mg",
            "zinc": "0.5 mg",
            "health_score": 62,
            "best_for": "Dessert",
            "allergens": "Dairy, Gluten",
            "storage": "Refrigerate for 1 day",
            "good_for": "Sweet craving",
            "gi_index": "High",
            "best_time": "After meal",
            "summary": "Sweet dish with higher sugar and moderate energy value.",
        })
        if "kheer" in n:
            base["calories"] = "290 kcal"
            base["calcium"] = "130 mg"
            base["summary"] = "Milk-based kheer with comforting sweetness and good calcium."
        if "gulab jamun" in n:
            base["calories"] = "330 kcal"
            base["sugar"] = "28 g"
            base["health_score"] = 58
        if "rasgulla" in n:
            base["calories"] = "300 kcal"
            base["sugar"] = "26 g"
            base["health_score"] = 60

    # Snacks / fried / air fryer
    elif any(x in n for x in ["samosa", "pakora", "cutlet", "tikki", "fries", "wedge", "kebab", "chaat", "manchurian", "fry"]):
        update({
            "calories": "240 kcal",
            "protein": "6 g",
            "fat": "10 g",
            "carbs": "30 g",
            "fiber": "4 g",
            "sugar": "3 g",
            "sodium": "390 mg",
            "vitamin_a": "70 mcg",
            "vitamin_c": "6 mg",
            "calcium": "70 mg",
            "iron": "1.6 mg",
            "potassium": "260 mg",
            "magnesium": "22 mg",
            "zinc": "0.8 mg",
            "health_score": 73,
            "best_for": "Snack",
            "allergens": "Varies",
            "storage": "Best fresh",
            "good_for": "Evening snack",
            "gi_index": "Medium",
            "best_time": "Evening",
            "summary": "Crunchy snack with moderate calories and tasty street-style appeal.",
        })
        if "air fryer" in tags or "air fryer" in n:
            base["fat"] = "7 g"
            base["health_score"] = 80
            base["summary"] = "Air fryer snack with lower oil use and a crisp texture."

    return base


for r in ALL_RECIPES:
    r["nutrition"] = build_nutrition(r["name"], r)

@app.route("/", methods=["GET", "POST"])
def home():
    recipes = [dict(recipe) for recipe in ALL_RECIPES]

    entered_ingredients = ""
    selected_diet = "all"
    selected_mode = "all"
    selected_resources = ["stove"]

    if request.method == "POST":
        entered_ingredients = request.form.get("ingredients", "").strip()
        selected_diet = normalize_diet(request.form.get("diet", "all"))
        selected_mode = normalize_text(request.form.get("filter_mode", "all")) or "all"
        selected_resources = request.form.getlist("resources") or ["stove"]

        user_ingredients = parse_user_ingredients(entered_ingredients)

        filtered = []
        for recipe in recipes:
            if selected_diet != "all" and normalize_diet(recipe.get("diet")) != selected_diet:
                continue

            if not mode_matches(recipe, selected_mode):
                continue

            recipe_resources = {normalize_text(item) for item in recipe.get("resources", [])}
            if selected_resources and not any(normalize_text(item) in recipe_resources for item in selected_resources):
                continue

            score, matched, missing = calculate_match(user_ingredients, recipe)

            if user_ingredients and len(matched) == 0:
                continue

            recipe_copy = dict(recipe)
            recipe_copy["match_percent"] = score
            recipe_copy["matched"] = matched[:3]
            recipe_copy["missing"] = missing[:3]
            filtered.append(recipe_copy)

        if filtered:
            filtered.sort(
                key=lambda item: (item["match_percent"], item.get("rating", 0)),
                reverse=True,
            )
            recipes = filtered
        else:
            recipes = []

    else:
        for recipe in recipes:
            recipe["match_percent"] = round(float(recipe.get("rating", 0)) * 20, 1)
            recipe["matched"] = []
            recipe["missing"] = []

        recipes.sort(
            key=lambda item: (item.get("rating", 0), -int(item.get("time", 0))),
            reverse=True,
        )

    recommended_recipes = recipes[:8]
    trending_recipes = sorted(
        ALL_RECIPES,
        key=lambda item: (item.get("rating", 0), -int(item.get("time", 0))),
        reverse=True,
    )[:4]

    ingredient_counter = Counter()
    for recipe in ALL_RECIPES:
        for ingredient in recipe.get("ingredients", []):
            ingredient_counter[normalize_text(ingredient)] += 1

    top_ingredients = [
        ingredient.title() for ingredient, _ in ingredient_counter.most_common(12)
    ]

    stats = {
        "total_recipes": len(ALL_RECIPES),
        "shown_recipes": len(recipes[:24]),
        "avg_rating": round(
            sum(float(recipe.get("rating", 0)) for recipe in ALL_RECIPES) / len(ALL_RECIPES), 1
        ) if ALL_RECIPES else 0,
        "healthy_recipes": sum(
            1 for recipe in ALL_RECIPES if "healthy" in {normalize_text(tag) for tag in recipe.get("tags", [])}
        ),
        "quick_recipes": sum(1 for recipe in ALL_RECIPES if int(recipe.get("time", 999)) <= 15),
    }

    return render_template(
        "index.html",
        recipes=recipes[:24],
        recommended_recipes=recommended_recipes,
        trending_recipes=trending_recipes,
        top_ingredients=top_ingredients,
        stats=stats,
        total=len(ALL_RECIPES),
        entered_ingredients=entered_ingredients,
        selected_diet=selected_diet,
        selected_mode=selected_mode,
        selected_resources=selected_resources,
    )

@app.route("/recipe/<slug>")
def recipe_detail(slug):
    recipe = next(
        (dict(item) for item in ALL_RECIPES if item.get("slug") == slug),
        None
    )

    if not recipe:
        abort(404)

    recipe["steps"] = recipe.get("steps", [])
    recipe["tips"] = recipe.get("tips", [])
    recipe["notes"] = recipe.get("notes", [])
    recipe["serving"] = recipe.get("serving", [])
    recipe["avoid"] = recipe.get("avoid", [])

    return render_template("recipe.html", recipe=recipe)


if __name__ == "__main__":
    app.run(debug=True, port=5000)