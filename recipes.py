def recipe(
    name, diet, time, rating, difficulty, description,
    ingredients, resources, tags, emoji, category,
    style=None, steps=None, tips=None, notes=None, serving=None, avoid=None
):
    def detail_pack(style_name, recipe_name):
        style_name = (style_name or category or "general").lower()

        if style_name == "paratha":
            return {
                "steps": [
                    f"Prepare the stuffing for {recipe_name}.",
                    "Make soft dough with wheat flour, salt, and a little water.",
                    "Stuff the filling carefully and seal it well.",
                    "Roll gently and cook on tawa with ghee on both sides.",
                    "Serve hot when the paratha is golden and soft.",
                ],
                "tips": [
                    "Keep the stuffing dry so rolling becomes easy.",
                    "Cook on medium flame for even browning.",
                    "Brush a little ghee for better taste and texture.",
                ],
                "notes": [
                    "Rest the dough for a few minutes before rolling.",
                    "Use fresh stuffing for the best flavour.",
                ],
                "serving": [
                    "Serve with curd, pickle, or butter.",
                    "Tastes best fresh from the tawa.",
                ],
                "avoid": [
                    "Do not overfill the paratha.",
                    "Do not cook on very high flame.",
                ],
            }

        if style_name == "breakfast":
            return {
                "steps": [
                    f"Prepare the main batter or mixture for {recipe_name}.",
                    "Heat the pan or tawa properly before cooking.",
                    "Cook the dish on medium flame until done.",
                    "Finish with garnish and serve while hot.",
                ],
                "tips": [
                    "Keep all ingredients ready before starting.",
                    "Do not rush the cooking step.",
                    "Serve immediately for the best breakfast taste.",
                ],
                "notes": [
                    "Breakfast dishes taste better when served fresh.",
                    "Adjust spice level based on preference.",
                ],
                "serving": [
                    "Serve with chutney, curd, butter, or tea.",
                    "Best enjoyed fresh and warm.",
                ],
                "avoid": [
                    "Do not overcook the batter or filling.",
                    "Do not let the dish dry out.",
                ],
            }

        if style_name == "sandwich":
            return {
                "steps": [
                    f"Prepare the filling or spread for {recipe_name}.",
                    "Layer the ingredients evenly on bread or bun.",
                    "Toast, grill, or heat until crisp and golden.",
                    "Cut and serve immediately while warm.",
                ],
                "tips": [
                    "Use fresh bread for better texture.",
                    "Do not add too much wet filling.",
                    "Toast lightly so the bread stays crisp.",
                ],
                "notes": [
                    "Sandwiches are best when served immediately.",
                    "You can add a little cheese for extra flavour.",
                ],
                "serving": [
                    "Serve with ketchup, chutney, or dip.",
                    "Pair with tea, coffee, or a cold drink.",
                ],
                "avoid": [
                    "Do not add watery filling.",
                    "Do not over-toast the bread.",
                ],
            }

        if style_name == "rice":
            return {
                "steps": [
                    f"Wash and prepare the rice for {recipe_name}.",
                    "Cook the base ingredients or temper the spices first.",
                    "Mix everything gently without breaking the rice.",
                    "Finish with garnish and serve hot.",
                ],
                "tips": [
                    "Keep the rice grains separate and fluffy.",
                    "Use the right amount of water.",
                    "Cook on low flame after mixing for better flavour.",
                ],
                "notes": [
                    "Rice dishes taste better when freshly cooked.",
                    "Avoid overmixing to keep the texture nice.",
                ],
                "serving": [
                    "Serve hot with curry, raita, or salad.",
                    "Pair with papad or pickle if needed.",
                ],
                "avoid": [
                    "Do not overcook the rice.",
                    "Do not make the dish too wet.",
                ],
            }

        if style_name == "curry":
            return {
                "steps": [
                    f"Prepare the main ingredient for {recipe_name}.",
                    "Cook onion, tomato, ginger, and garlic with spices.",
                    "Add the main ingredient and simmer with the gravy.",
                    "Finish with garnish and serve hot.",
                ],
                "tips": [
                    "Cook the masala well for a richer taste.",
                    "Use medium flame so the gravy does not burn.",
                    "Taste before serving and adjust seasoning carefully.",
                ],
                "notes": [
                    "Curries taste better after a few minutes of resting.",
                    "Do not add too much water at once.",
                ],
                "serving": [
                    "Serve with roti, naan, or rice.",
                    "Best enjoyed hot with a side dish.",
                ],
                "avoid": [
                    "Do not rush the masala cooking stage.",
                    "Do not let the gravy become too thin.",
                ],
            }

        if style_name == "snack":
            return {
                "steps": [
                    f"Prepare the snack mixture for {recipe_name}.",
                    "Shape, fill, or assemble the snack carefully.",
                    "Fry, bake, toast, or air fry as needed.",
                    "Serve hot with chutney, sauce, or dip.",
                ],
                "tips": [
                    "Keep the snack crispy and fresh.",
                    "Do not overcrowd the pan or basket.",
                    "Serve immediately for the best texture.",
                ],
                "notes": [
                    "Snacks usually taste best when hot.",
                    "Adjust spices based on your taste.",
                ],
                "serving": [
                    "Serve with chutney, ketchup, or mint dip.",
                    "Great with evening tea or coffee.",
                ],
                "avoid": [
                    "Do not use too much oil.",
                    "Do not overcook the snack.",
                ],
            }

        if style_name == "chaat":
            return {
                "steps": [
                    f"Prepare all chaat ingredients for {recipe_name}.",
                    "Mix the base ingredients and add chutneys or curd.",
                    "Top with sev, masala, and garnish.",
                    "Serve immediately to keep it crunchy.",
                ],
                "tips": [
                    "Add chutney just before serving.",
                    "Keep the chaat crunchy and fresh.",
                    "Balance sweet, sour, and spicy flavours well.",
                ],
                "notes": [
                    "Chaat is best served immediately.",
                    "Do not let it sit for too long after mixing.",
                ],
                "serving": [
                    "Serve as a quick evening snack.",
                    "Best enjoyed fresh and crunchy.",
                ],
                "avoid": [
                    "Do not make the chaat soggy.",
                    "Do not add too much curd too early.",
                ],
            }

        if style_name == "pasta":
            return {
                "steps": [
                    f"Boil the pasta for {recipe_name} until al dente.",
                    "Prepare the sauce with butter, garlic, tomato, or milk as needed.",
                    "Add the pasta and toss until evenly coated.",
                    "Serve hot with herbs or cheese on top.",
                ],
                "tips": [
                    "Do not overcook the pasta.",
                    "Keep a little pasta water to adjust sauce.",
                    "Serve immediately for the best creamy texture.",
                ],
                "notes": [
                    "Pasta tastes best when served fresh and warm.",
                    "Choose sauce consistency based on preference.",
                ],
                "serving": [
                    "Serve with garlic bread or salad.",
                    "Top with cheese, oregano, or chilli flakes.",
                ],
                "avoid": [
                    "Do not overboil the pasta.",
                    "Do not make the sauce too dry.",
                ],
            }

        if style_name == "noodles":
            return {
                "steps": [
                    f"Prepare the noodles and vegetables for {recipe_name}.",
                    "Stir-fry onions, veggies, and sauces on high flame.",
                    "Add noodles and toss everything together.",
                    "Serve hot with extra sauce if needed.",
                ],
                "tips": [
                    "Use high flame for a better stir-fry taste.",
                    "Do not overcook the noodles.",
                    "Keep the veggies slightly crunchy.",
                ],
                "notes": [
                    "Quick cooking gives the best noodle texture.",
                    "Toss gently so the noodles do not break.",
                ],
                "serving": [
                    "Serve hot with chilli sauce or schezwan sauce.",
                    "Add spring onion on top if available.",
                ],
                "avoid": [
                    "Do not make the noodles soggy.",
                    "Do not overload with water.",
                ],
            }

        if style_name == "dessert":
            return {
                "steps": [
                    f"Prepare the sweet mixture for {recipe_name}.",
                    "Cook or set it slowly with proper stirring or resting.",
                    "Check the texture and sweetness carefully.",
                    "Serve after cooling or when set properly.",
                ],
                "tips": [
                    "Use the right amount of sugar.",
                    "Keep stirring where needed to avoid lumps.",
                    "Let the dessert set properly before serving.",
                ],
                "notes": [
                    "Desserts taste best when made patiently.",
                    "Cooling time is important for many sweets.",
                ],
                "serving": [
                    "Serve chilled or warm depending on the dessert.",
                    "Garnish with nuts, chocolate, or cream if desired.",
                ],
                "avoid": [
                    "Do not overcook sweet mixtures.",
                    "Do not serve before the texture is ready.",
                ],
            }

        if style_name == "drink":
            return {
                "steps": [
                    f"Prepare the ingredients for {recipe_name}.",
                    "Blend or mix everything until smooth.",
                    "Chill if needed and pour into a serving glass.",
                    "Serve immediately with ice or garnish.",
                ],
                "tips": [
                    "Use chilled ingredients for a better drink.",
                    "Blend until smooth and creamy.",
                    "Serve immediately so the taste stays fresh.",
                ],
                "notes": [
                    "Drinks are best when served cold and fresh.",
                    "Adjust sweetness before serving.",
                ],
                "serving": [
                    "Serve in a tall glass with ice.",
                    "Top with whipped cream or nuts if you like.",
                ],
                "avoid": [
                    "Do not over-dilute the drink.",
                    "Do not keep it standing for too long.",
                ],
            }

        if style_name == "healthy":
            return {
                "steps": [
                    f"Prepare fresh ingredients for {recipe_name}.",
                    "Mix or assemble the ingredients carefully.",
                    "Keep the seasoning light and balanced.",
                    "Serve fresh for the best healthy taste.",
                ],
                "tips": [
                    "Use fresh fruits, vegetables, or oats.",
                    "Keep the oil and sugar low.",
                    "Serve soon after preparation for freshness.",
                ],
                "notes": [
                    "Healthy dishes work best with fresh ingredients.",
                    "Simple seasoning keeps the flavour clean.",
                ],
                "serving": [
                    "Serve as breakfast or a light meal.",
                    "Add nuts or seeds if needed.",
                ],
                "avoid": [
                    "Do not overuse sugar or oil.",
                    "Do not overcook fresh ingredients.",
                ],
            }

        if style_name == "airfryer":
            return {
                "steps": [
                    f"Prepare the ingredients for {recipe_name}.",
                    "Preheat the air fryer and arrange items in one layer.",
                    "Cook until crispy or evenly done.",
                    "Serve hot with dip or garnish.",
                ],
                "tips": [
                    "Do not overcrowd the basket.",
                    "Flip halfway if needed for even cooking.",
                    "Preheat the air fryer for better results.",
                ],
                "notes": [
                    "Air fryer recipes are best when arranged in a single layer.",
                    "Brush a small amount of oil if needed.",
                ],
                "serving": [
                    "Serve immediately while crispy.",
                    "Pair with ketchup or dip.",
                ],
                "avoid": [
                    "Do not fill the basket too much.",
                    "Do not overcook.",
                ],
            }

        if style_name == "pizza":
            return {
                "steps": [
                    f"Prepare the base for {recipe_name}.",
                    "Spread sauce and add toppings evenly.",
                    "Bake or toast until the base is crisp and the cheese melts.",
                    "Slice and serve hot.",
                ],
                "tips": [
                    "Do not overload toppings.",
                    "Bake until the cheese is properly melted.",
                    "Serve fresh for the best pizza taste.",
                ],
                "notes": [
                    "A crisp base gives the best result.",
                    "Balance toppings so the pizza stays light.",
                ],
                "serving": [
                    "Serve with chilli flakes and oregano.",
                    "Best with a dip or soft drink.",
                ],
                "avoid": [
                    "Do not make the base soggy.",
                    "Do not add too much sauce.",
                ],
            }

        if style_name == "nonveg":
            return {
                "steps": [
                    f"Prepare the non-veg ingredient for {recipe_name}.",
                    "Cook it with onion, garlic, ginger, and spices.",
                    "Make sure it is cooked through and tender.",
                    "Serve hot with your favourite side.",
                ],
                "tips": [
                    "Cook the protein properly for best taste and safety.",
                    "Use fresh spices for better flavour.",
                    "Do not overcook or it may become dry.",
                ],
                "notes": [
                    "Non-veg recipes taste better when handled carefully.",
                    "Keep the seasoning balanced.",
                ],
                "serving": [
                    "Serve with rice, bread, or roti.",
                    "Best enjoyed hot and fresh.",
                ],
                "avoid": [
                    "Do not undercook the protein.",
                    "Do not use too much heat all at once.",
                ],
            }

        return {
            "steps": [
                f"Prepare the ingredients for {recipe_name}.",
                "Cook everything step by step with care.",
                "Taste and adjust the seasoning.",
                "Serve warm and enjoy.",
            ],
            "tips": [
                "Keep ingredients ready before you start.",
                "Taste before serving.",
                "Use medium heat unless needed otherwise.",
            ],
            "notes": [
                "Simple recipes taste best when cooked patiently.",
                "Fresh ingredients improve flavour.",
            ],
            "serving": [
                "Serve hot and fresh.",
                "Pair with a side if needed.",
            ],
            "avoid": [
                "Do not rush the cooking.",
                "Do not over-season.",
            ],
        }

    pack = detail_pack(style or category, name)

    return {
        "name": name,
        "diet": diet,
        "time": time,
        "rating": rating,
        "difficulty": difficulty,
        "description": description,
        "ingredients": ingredients,
        "resources": resources,
        "tags": tags,
        "emoji": emoji,
        "category": category,
        "steps": steps or pack["steps"],
        "tips": tips or pack["tips"],
        "notes": notes or pack["notes"],
        "serving": serving or pack["serving"],
        "avoid": avoid or pack["avoid"],
    }


RECIPES = [
    recipe("Aloo Paratha", "veg", 20, 4.6, "Easy", "Classic aloo paratha with homemade spices.", ["potato", "wheat flour", "ghee", "salt", "spices"], ["stove"], ["breakfast", "filling", "quick"], "🫓", "breakfast", style="paratha"),
    recipe("Gobi Paratha", "veg", 20, 4.6, "Easy", "Soft gobi paratha with a simple stuffing.", ["cauliflower", "wheat flour", "ghee", "salt", "spices"], ["stove"], ["breakfast", "filling", "quick"], "🫓", "breakfast", style="paratha"),
    recipe("Paneer Paratha", "veg", 20, 4.6, "Easy", "Paneer stuffed paratha, rich and filling.", ["paneer", "wheat flour", "ghee", "salt", "spices"], ["stove"], ["breakfast", "filling", "quick"], "🫓", "breakfast", style="paratha"),
    recipe("Methi Paratha", "veg", 20, 4.5, "Easy", "Healthy methi paratha for breakfast.", ["fenugreek leaves", "wheat flour", "ghee", "salt", "spices"], ["stove"], ["breakfast", "healthy", "quick"], "🫓", "breakfast", style="paratha"),
    recipe("Onion Paratha", "veg", 20, 4.5, "Easy", "Quick onion paratha with a tasty filling.", ["onion", "wheat flour", "ghee", "salt", "spices"], ["stove"], ["breakfast", "quick"], "🫓", "breakfast", style="paratha"),
    recipe("Besan Chilla", "veg", 15, 4.6, "Easy", "Savory gram flour chilla for breakfast.", ["besan", "onion", "tomato", "green chilli", "spices"], ["stove"], ["breakfast", "healthy", "quick"], "🥞", "breakfast", style="breakfast"),
    recipe("Poha", "veg", 15, 4.6, "Easy", "Light and fluffy poha with peanuts and lemon.", ["poha", "onion", "peanuts", "lemon", "mustard seeds"], ["stove"], ["breakfast", "quick", "healthy"], "🍛", "breakfast", style="breakfast"),
    recipe("Upma", "veg", 15, 4.5, "Easy", "Warm and comforting semolina upma.", ["rava", "onion", "curry leaves", "mustard seeds", "green chilli"], ["stove"], ["breakfast", "quick"], "🥣", "breakfast", style="breakfast"),
    recipe("Idli", "veg", 20, 4.7, "Easy", "Soft idli served with chutney and sambar.", ["idli batter", "coconut chutney", "sambar"], ["stove"], ["breakfast", "classic"], "🥞", "breakfast", style="breakfast"),
    recipe("Masala Dosa", "veg", 25, 4.7, "Medium", "Crispy dosa with potato masala filling.", ["rice batter", "urad dal", "potato", "sambar", "chutney"], ["stove"], ["breakfast", "classic"], "🥞", "breakfast", style="breakfast"),
    recipe("Uttapam", "veg", 20, 4.6, "Easy", "Soft uttapam topped with onion and tomato.", ["rice batter", "onion", "tomato", "chutney", "sambar"], ["stove"], ["breakfast", "classic"], "🥞", "breakfast", style="breakfast"),
    recipe("Bread Omelette", "non-veg", 10, 4.6, "Easy", "Quick bread omelette for breakfast.", ["bread", "egg", "onion", "butter", "spices"], ["stove"], ["breakfast", "quick"], "🍳", "breakfast", style="breakfast"),
    recipe("Egg Sandwich", "non-veg", 12, 4.6, "Easy", "Simple egg sandwich for a quick bite.", ["bread", "egg", "butter", "onion", "mayo"], ["stove"], ["snack", "quick"], "🥪", "snack", style="sandwich"),
    recipe("Veg Sandwich", "veg", 12, 4.6, "Easy", "Fresh and simple vegetable sandwich.", ["bread", "cucumber", "tomato", "onion", "butter"], ["stove"], ["snack", "quick"], "🥪", "snack", style="sandwich"),
    recipe("Cheese Sandwich", "veg", 12, 4.6, "Easy", "Melty cheese sandwich for a quick snack.", ["bread", "cheese", "butter", "tomato", "onion"], ["stove"], ["snack", "quick"], "🥪", "snack", style="sandwich"),
    recipe("Grilled Veg Sandwich", "veg", 15, 4.6, "Easy", "Grilled sandwich loaded with vegetables.", ["bread", "cucumber", "tomato", "onion", "cheese"], ["stove"], ["snack", "quick"], "🥪", "snack", style="sandwich"),
    recipe("Paneer Sandwich", "veg", 15, 4.6, "Easy", "Paneer-filled sandwich for a quick bite.", ["bread", "paneer", "onion", "capsicum", "butter"], ["stove"], ["snack", "quick"], "🥪", "snack", style="sandwich"),
    recipe("Corn Sandwich", "veg", 15, 4.5, "Easy", "Sweet corn sandwich with a creamy filling.", ["bread", "corn", "butter", "cheese", "onion"], ["stove"], ["snack", "quick"], "🥪", "snack", style="sandwich"),
    recipe("Cheese Garlic Bread", "veg", 15, 4.7, "Easy", "Cheesy garlic bread with a crispy bite.", ["bread", "garlic", "butter", "cheese", "oregano"], ["stove"], ["snack", "quick"], "🧄", "snack", style="sandwich"),
    recipe("Jeera Rice", "veg", 20, 4.6, "Easy", "Simple and fragrant jeera rice.", ["rice", "cumin", "ghee", "salt"], ["stove"], ["lunch", "quick"], "🍚", "rice", style="rice"),
    recipe("Lemon Rice", "veg", 20, 4.6, "Easy", "Tangy lemon rice with a South Indian touch.", ["rice", "lemon", "peanuts", "mustard seeds", "curry leaves"], ["stove"], ["lunch", "quick"], "🍚", "rice", style="rice"),
    recipe("Veg Pulao", "veg", 25, 4.7, "Easy", "Easy vegetable pulao cooked in one pot.", ["rice", "peas", "carrot", "beans", "spices"], ["stove"], ["lunch", "one pot"], "🍚", "rice", style="rice"),
    recipe("Veg Biryani", "veg", 30, 4.7, "Medium", "Homestyle vegetarian biryani.", ["rice", "vegetables", "curd", "biryani masala", "onion"], ["stove"], ["special", "lunch"], "🍚", "rice", style="rice"),
    recipe("Khichdi", "veg", 25, 4.7, "Easy", "Comforting khichdi for a light meal.", ["rice", "moong dal", "ghee", "cumin", "salt"], ["stove"], ["healthy", "lunch"], "🍚", "rice", style="rice"),
    recipe("Dal Tadka", "veg", 25, 4.7, "Easy", "Classic dal tadka with tempered spices.", ["dal", "onion", "tomato", "ginger", "garlic"], ["stove"], ["protein", "lunch"], "🍲", "curry", style="curry"),
    recipe("Rajma Chawal", "veg", 30, 4.7, "Easy", "Rajma chawal, a hearty lunch favorite.", ["rajma", "rice", "onion", "tomato", "spices"], ["stove"], ["lunch", "filling"], "🍚", "rice", style="rice"),
    recipe("Chole Chawal", "veg", 30, 4.7, "Easy", "Chole chawal with rich flavours.", ["chole", "rice", "onion", "tomato", "spices"], ["stove"], ["lunch", "filling"], "🍚", "rice", style="rice"),
    recipe("Curd Rice", "veg", 15, 4.6, "Easy", "Cooling curd rice for a light meal.", ["rice", "curd", "mustard seeds", "curry leaves"], ["stove"], ["healthy", "lunch"], "🍚", "rice", style="rice"),
    recipe("Sambar Rice", "veg", 30, 4.6, "Medium", "Flavorful sambar rice with vegetables.", ["rice", "dal", "mixed vegetables", "sambar powder"], ["stove"], ["lunch", "one pot"], "🍚", "rice", style="rice"),
    recipe("Paneer Butter Masala", "veg", 30, 4.8, "Medium", "Creamy paneer butter masala for dinner.", ["paneer", "butter", "tomato", "cream", "spices"], ["stove"], ["dinner", "special"], "🥘", "curry", style="curry"),
    recipe("Paneer Bhurji", "veg", 15, 4.7, "Easy", "Quick paneer bhurji for a filling meal.", ["paneer", "onion", "tomato", "capsicum", "spices"], ["stove"], ["quick", "protein"], "🥘", "curry", style="curry"),
    recipe("Palak Paneer", "veg", 25, 4.7, "Medium", "Nutritious palak paneer with spinach gravy.", ["paneer", "spinach", "onion", "tomato", "spices"], ["stove"], ["healthy", "dinner"], "🥘", "curry", style="curry"),
    recipe("Matar Paneer", "veg", 25, 4.7, "Medium", "Classic matar paneer with peas.", ["paneer", "peas", "onion", "tomato", "spices"], ["stove"], ["dinner", "special"], "🥘", "curry", style="curry"),
    recipe("Aloo Gobi", "veg", 25, 4.6, "Easy", "Dry aloo gobi, simple and satisfying.", ["potato", "cauliflower", "onion", "tomato", "spices"], ["stove"], ["dinner", "healthy"], "🥘", "curry", style="curry"),
    recipe("Bhindi Masala", "veg", 25, 4.6, "Easy", "Bhindi masala cooked with Indian spices.", ["bhindi", "onion", "tomato", "spices", "oil"], ["stove"], ["dinner", "healthy"], "🥘", "curry", style="curry"),
    recipe("Mixed Veg Curry", "veg", 25, 4.6, "Easy", "Mixed vegetable curry for lunch or dinner.", ["carrot", "beans", "peas", "potato", "spices"], ["stove"], ["healthy", "dinner"], "🥘", "curry", style="curry"),
    recipe("Baingan Bharta", "veg", 25, 4.6, "Easy", "Smoky baingan bharta with rustic flavour.", ["brinjal", "onion", "tomato", "garlic", "spices"], ["stove"], ["dinner", "healthy"], "🥘", "curry", style="curry"),
    recipe("Mushroom Masala", "veg", 25, 4.7, "Easy", "Mushroom masala with rich gravy.", ["mushroom", "onion", "tomato", "cream", "spices"], ["stove"], ["dinner", "special"], "🥘", "curry", style="curry"),
    recipe("Dum Aloo", "veg", 25, 4.7, "Easy", "Soft dum aloo in a spiced gravy.", ["potato", "yogurt", "onion", "tomato", "spices"], ["stove"], ["dinner", "special"], "🥘", "curry", style="curry"),
    recipe(
    "Coffee",
    "veg",
    5,
    4.4,
    "Easy",
    "Simple hot coffee with milk and sugar.",
    ["milk", "coffee", "sugar", "water"],
    ["stove"],
    ["drink", "quick"],
    "☕",
    "drink",
    style="drink",
),
recipe(
    "Tea",
    "veg",
    5,
    4.4,
    "Easy",
    "Classic Indian milk tea.",
    ["milk", "tea leaves", "sugar", "ginger"],
    ["stove"],
    ["drink", "quick"],
    "🍵",
    "drink",
    style="drink",
),
recipe(
    "Pancake",
    "veg",
    12,
    4.6,
    "Easy",
    "Soft pancakes made with milk and flour.",
    ["milk", "flour", "egg", "sugar", "butter"],
    ["stove"],
    ["breakfast", "sweet", "quick"],
    "🥞",
    "breakfast",
    style="breakfast",
),
recipe(
    "Waffle",
    "veg",
    12,
    4.6,
    "Easy",
    "Crisp waffle served warm with milk batter.",
    ["milk", "flour", "egg", "sugar", "butter"],
    ["stove"],
    ["breakfast", "sweet", "quick"],
    "🧇",
    "breakfast",
    style="breakfast",
),
recipe(
    "White Sauce Pasta",
    "veg",
    20,
    4.7,
    "Easy",
    "Creamy white sauce pasta made with milk.",
    ["pasta", "milk", "butter", "flour", "cheese", "garlic"],
    ["stove"],
    ["dinner", "comfort food"],
    "🍝",
    "pasta",
    style="pasta",
),
recipe(
    "Pink Sauce Pasta",
    "veg",
    20,
    4.7,
    "Easy",
    "Creamy pink sauce pasta with milk and tomato.",
    ["pasta", "milk", "tomato", "butter", "cream", "cheese"],
    ["stove"],
    ["dinner", "comfort food"],
    "🍝",
    "pasta",
    style="pasta",
),
recipe(
    "Kheer",
    "veg",
    30,
    4.7,
    "Easy",
    "Classic rice kheer made with milk.",
    ["milk", "rice", "sugar", "cardamom", "almonds"],
    ["stove"],
    ["dessert", "sweet"],
    "🍚",
    "dessert",
    style="dessert",
),
recipe(
    "Besan Halwa",
    "veg",
    20,
    4.6,
    "Easy",
    "Warm besan halwa made with milk and ghee.",
    ["milk", "besan", "ghee", "sugar", "cardamom"],
    ["stove"],
    ["dessert", "sweet"],
    "🍯",
    "dessert",
    style="dessert",),

 recipe("Milk Shake", "veg", 8, 4.5, "Easy", "Classic milk shake for a quick cool drink.", ["milk", "sugar", "ice cream"], ["blender"], ["drink", "sweet", "quick"], "🥤", "drink", style="drink"),
recipe("Banana Milkshake", "veg", 8, 4.6, "Easy", "Creamy banana milkshake made at home.", ["banana", "milk", "sugar", "ice cream"], ["blender"], ["drink", "sweet", "quick"], "🥤", "drink", style="drink"),
recipe("Mango Lassi", "veg", 8, 4.6, "Easy", "Sweet mango lassi with a creamy texture.", ["mango", "curd", "sugar", "cardamom"], ["blender"], ["drink", "sweet", "quick"], "🥛", "drink", style="drink"),
recipe("Oreo Shake", "veg", 8, 4.7, "Easy", "Thick oreo shake for a dessert-style drink.", ["oreo", "milk", "sugar", "ice cream"], ["blender"], ["drink", "sweet"], "🥤", "drink", style="drink"),
recipe("Cold Coffee", "veg", 8, 4.6, "Easy", "Chilled cold coffee with milk and sugar.", ["coffee", "milk", "sugar", "ice"], ["blender"], ["drink", "quick"], "☕", "drink", style="drink"),
recipe("Hot Chocolate", "veg", 8, 4.6, "Easy", "Warm hot chocolate with milk and cocoa.", ["milk", "cocoa", "sugar", "chocolate"], ["stove"], ["drink", "sweet"], "☕", "drink", style="drink"),
recipe("Masala Chai", "veg", 5, 4.5, "Easy", "Classic Indian masala chai.", ["tea leaves", "milk", "sugar", "ginger", "cardamom"], ["stove"], ["drink", "quick"], "🍵", "drink", style="drink"),

recipe("Poha Cutlet", "veg", 20, 4.6, "Easy", "Crispy poha cutlet for evening snack.", ["poha", "potato", "peas", "spices", "breadcrumbs"], ["stove"], ["snack", "quick"], "🥔", "snack", style="snack"),
recipe("Aloo Tikki", "veg", 20, 4.6, "Easy", "Simple potato tikki with crisp edges.", ["potato", "peas", "spices", "breadcrumbs", "oil"], ["stove"], ["snack", "street food"], "🥔", "snack", style="snack"),
recipe("Veg Cutlet", "veg", 20, 4.6, "Easy", "Mixed vegetable cutlet for a quick bite.", ["potato", "carrot", "peas", "breadcrumbs", "spices"], ["stove"], ["snack", "quick"], "🥟", "snack", style="snack"),
recipe("Paneer Tikka", "veg", 25, 4.8, "Medium", "Juicy paneer tikka with grilled spices.", ["paneer", "curd", "capsicum", "onion", "spices", "lemon"], ["oven", "stove"], ["snack", "protein"], "🍢", "snack", style="snack"),
recipe("Paneer Roll", "veg", 20, 4.7, "Easy", "Paneer roll wrapped in soft roti.", ["roti", "paneer", "onion", "capsicum", "spices"], ["stove"], ["snack", "quick"], "🌯", "snack", style="snack"),
recipe("Veg Roll", "veg", 15, 4.6, "Easy", "Vegetable roll for a fast snack.", ["roti", "potato", "capsicum", "onion", "spices"], ["stove"], ["snack", "quick"], "🌯", "snack", style="snack"),
recipe("Chicken Roll", "non-veg", 20, 4.7, "Easy", "Chicken roll with spicy filling.", ["roti", "chicken", "onion", "capsicum", "spices"], ["stove"], ["snack", "protein"], "🌯", "snack", style="snack"),
recipe("Chicken Curry", "non-veg", 35, 4.8, "Medium", "Homestyle chicken curry with rich gravy.", ["chicken", "onion", "tomato", "ginger", "garlic", "spices"], ["stove"], ["protein", "dinner"], "🍗", "dinner", style="curry"),
recipe("Chicken Fried Rice", "non-veg", 25, 4.7, "Easy", "Chicken fried rice cooked in one pan.", ["rice", "chicken", "egg", "soy sauce", "garlic", "vegetables"], ["stove"], ["protein", "dinner"], "🍚", "dinner", style="rice"),
recipe("Egg Curry", "non-veg", 25, 4.7, "Easy", "Egg curry in a spicy onion-tomato gravy.", ["egg", "onion", "tomato", "ginger", "garlic", "spices"], ["stove"], ["protein", "dinner"], "🍳", "dinner", style="curry"),
recipe("Egg Fried Rice", "non-veg", 20, 4.6, "Easy", "Egg fried rice with vegetables and soy sauce.", ["rice", "egg", "soy sauce", "garlic", "onion", "vegetables"], ["stove"], ["quick", "protein"], "🍚", "dinner", style="rice"),
recipe("Egg Bhurji", "non-veg", 10, 4.6, "Easy", "Quick egg bhurji for breakfast.", ["egg", "onion", "tomato", "spices", "butter"], ["stove"], ["breakfast", "quick"], "🍳", "breakfast", style="breakfast"),
recipe("Anda Paratha", "non-veg", 20, 4.6, "Easy", "Egg stuffed paratha with spices.", ["egg", "wheat flour", "ghee", "salt", "spices"], ["stove"], ["breakfast", "protein"], "🫓", "breakfast", style="paratha"),

recipe("Chole Bhature", "veg", 35, 4.8, "Medium", "Street-style chole bhature at home.", ["chickpeas", "maida", "curd", "onion", "tomato", "spices"], ["stove"], ["street food", "dinner"], "🥙", "snack", style="snack"),
recipe("Chole Kulche", "veg", 30, 4.7, "Easy", "Chole kulche with tangy flavours.", ["chickpeas", "kulcha", "onion", "tomato", "spices"], ["stove"], ["street food", "snack"], "🥙", "snack", style="snack"),
recipe("Pav Bhaji", "veg", 25, 4.8, "Medium", "Classic pav bhaji with buttery masala.", ["pav", "potato", "peas", "cauliflower", "onion", "tomato", "butter", "spices"], ["stove"], ["street food", "dinner"], "🍞", "snack", style="snack"),
recipe("Misal Pav", "veg", 30, 4.7, "Medium", "Spicy misal pav with farsan topping.", ["moth beans", "onion", "tomato", "farsan", "pav", "spices"], ["stove"], ["street food", "snack"], "🍞", "snack", style="snack"),
recipe("Dhokla", "veg", 20, 4.7, "Easy", "Soft steamed dhokla with tempering.", ["besan", "curd", "eno", "oil", "mustard seeds"], ["stove"], ["snack", "healthy"], "🍰", "snack", style="snack"),
recipe("Khaman", "veg", 20, 4.6, "Easy", "Fluffy khaman with a light tempering.", ["besan", "curd", "eno", "oil", "mustard seeds"], ["stove"], ["snack", "healthy"], "🍰", "snack", style="snack"),
recipe("Medu Vada", "veg", 25, 4.7, "Medium", "Crispy medu vada for breakfast.", ["urad dal", "onion", "curry leaves", "green chili", "oil"], ["stove"], ["breakfast", "south indian"], "🍩", "breakfast", style="breakfast"),
recipe("Rava Dosa", "veg", 20, 4.6, "Easy", "Thin and crispy rava dosa.", ["rava", "curd", "rice flour", "onion", "green chili"], ["stove"], ["breakfast", "south indian"], "🥞", "breakfast", style="breakfast"),
recipe("Neer Dosa", "veg", 15, 4.5, "Easy", "Soft neer dosa with a delicate texture.", ["rice", "water", "salt", "oil"], ["stove"], ["breakfast", "south indian"], "🥞", "breakfast", style="breakfast"),
recipe("Pesarattu", "veg", 20, 4.7, "Easy", "Healthy moong dal pesarattu.", ["moong dal", "ginger", "green chili", "onion"], ["stove"], ["breakfast", "protein"], "🥞", "breakfast", style="breakfast"),

recipe("Tomato Soup", "veg", 15, 4.6, "Easy", "Warm tomato soup with pepper.", ["tomato", "butter", "cream", "pepper", "salt"], ["stove"], ["healthy", "quick"], "🍅", "drink", style="drink"),
recipe("Sweet Corn Soup", "veg", 15, 4.6, "Easy", "Creamy sweet corn soup.", ["sweet corn", "carrot", "cornflour", "pepper", "salt"], ["stove"], ["healthy", "quick"], "🌽", "drink", style="drink"),
recipe("Veg Manchurian", "veg", 25, 4.7, "Medium", "Crispy veg manchurian balls.", ["cabbage", "carrot", "flour", "soy sauce", "garlic"], ["stove"], ["snack", "indochinese"], "🥟", "snack", style="snack"),
recipe("Veg Manchurian Fried Rice", "veg", 25, 4.7, "Medium", "Spicy veg manchurian with fried rice.", ["rice", "cabbage", "carrot", "soy sauce", "garlic"], ["stove"], ["lunch", "indochinese"], "🍚", "rice", style="rice"),
recipe("Schezwan Noodles", "veg", 20, 4.7, "Easy", "Spicy schezwan noodles.", ["noodles", "schezwan sauce", "capsicum", "onion", "carrot"], ["stove"], ["quick", "lunch"], "🍜", "noodles", style="noodles"),
recipe("Hakka Noodles", "veg", 20, 4.6, "Easy", "Classic hakka noodles with vegetables.", ["noodles", "cabbage", "carrot", "capsicum", "soy sauce"], ["stove"], ["quick", "lunch"], "🍜", "noodles", style="noodles"),
recipe("Mac and Cheese", "veg", 20, 4.7, "Easy", "Creamy mac and cheese.", ["macaroni", "milk", "butter", "cheese", "flour"], ["stove"], ["comfort food", "dinner"], "🧀", "pasta", style="pasta"),
recipe("Red Sauce Pasta", "veg", 20, 4.6, "Easy", "Simple red sauce pasta.", ["pasta", "tomato", "garlic", "onion", "olive oil", "cheese"], ["stove"], ["quick", "comfort food"], "🍝", "pasta", style="pasta"),
recipe("Lasagna", "veg", 35, 4.8, "Medium", "Baked lasagna with cheese layers.", ["pasta sheets", "tomato", "cheese", "milk", "butter"], ["oven", "stove"], ["special", "dinner"], "🍝", "pasta", style="pasta"),
recipe("Pizza Margherita", "veg", 25, 4.7, "Medium", "Classic margherita pizza.", ["pizza base", "tomato", "cheese", "basil", "olive oil"], ["oven"], ["pizza", "special"], "🍕", "pizza", style="pizza"),
recipe("Veg Pizza", "veg", 25, 4.7, "Medium", "Vegetable loaded pizza.", ["pizza base", "cheese", "capsicum", "onion", "tomato"], ["oven"], ["pizza", "special"], "🍕", "pizza", style="pizza"),

recipe("French Fries", "veg", 20, 4.6, "Easy", "Crispy french fries.", ["potato", "oil", "salt"], ["stove"], ["snack", "quick"], "🍟", "snack", style="snack"),
recipe("Potato Wedges", "veg", 20, 4.6, "Easy", "Baked style potato wedges.", ["potato", "oil", "salt", "paprika", "herbs"], ["oven", "air fryer"], ["snack", "quick"], "🍟", "air fryer", style="airfryer"),
recipe("Bread Pakora", "veg", 20, 4.6, "Easy", "Street-style bread pakora.", ["bread", "potato", "besan", "spices", "oil"], ["stove"], ["snack", "street food"], "🍞", "snack", style="snack"),
recipe("Onion Rings", "veg", 15, 4.5, "Easy", "Crunchy onion rings.", ["onion", "maida", "cornflour", "oil"], ["stove"], ["snack", "quick"], "🧅", "snack", style="snack"),
recipe("Cheese Balls", "veg", 20, 4.7, "Easy", "Golden cheese balls.", ["cheese", "potato", "breadcrumbs", "oil"], ["stove"], ["snack", "quick"], "🧀", "snack", style="snack"),
recipe("Samosa", "veg", 25, 4.7, "Medium", "Crispy samosa with potato filling.", ["maida", "potato", "peas", "spices", "oil"], ["stove"], ["snack", "street food"], "🥟", "snack", style="snack"),
recipe("Kachori", "veg", 25, 4.6, "Medium", "Spicy kachori snack.", ["maida", "moong dal", "spices", "oil"], ["stove"], ["snack", "street food"], "🥟", "snack", style="snack"),
recipe("Gulab Jamun", "veg", 30, 4.8, "Medium", "Soft gulab jamun in sugar syrup.", ["milk powder", "maida", "ghee", "sugar", "cardamom"], ["stove"], ["sweet", "dessert"], "🍮", "dessert", style="dessert"),
recipe("Rasgulla", "veg", 30, 4.8, "Medium", "Soft and spongy rasgulla.", ["chenna", "sugar", "cardamom"], ["stove"], ["sweet", "dessert"], "🍮", "dessert", style="dessert"),
recipe("Gajar Halwa", "veg", 30, 4.7, "Easy", "Rich gajar halwa with milk and ghee.", ["carrot", "milk", "sugar", "ghee", "cardamom"], ["stove"], ["sweet", "dessert"], "🍯", "dessert", style="dessert"),
recipe("Suji Halwa", "veg", 20, 4.6, "Easy", "Warm suji halwa for quick dessert.", ["suji", "ghee", "sugar", "water", "cardamom"], ["stove"], ["sweet", "dessert"], "🍯", "dessert", style="dessert"),
recipe("Kheer", "veg", 30, 4.7, "Easy", "Creamy rice kheer made with milk.", ["milk", "rice", "sugar", "cardamom", "almonds"], ["stove"], ["sweet", "dessert"], "🍚", "dessert", style="dessert"),
    
]


def get_recipes():
    return RECIPES