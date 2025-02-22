import streamlit as st
import pandas as pd

# Sample recipe data from NYT Cooking, Bon Appétit, and Tasty
recipes = {
    'breakfast': [
        {
            'name': 'Buttery Breakfast Casserole',
            'ingredients': ['croissants', 'olive oil', 'scallions', 'sweet Italian sausage', 'fresh sage', 'eggs', 'milk', 'heavy cream', 'gruyère cheese', 'salt', 'black pepper'],
            'allergens': ['dairy', 'eggs', 'gluten'],
            'instructions': 'Layer split croissants in buttered baking dish. Cook sausage with scallions and sage. Mix eggs, milk, cream, and seasonings. Pour over croissants, top with cheese. Bake until golden.',
            'source': 'https://cooking.nytimes.com/recipes/1017894-buttery-breakfast-casserole'
        },
        {
            'name': 'Açaí Bowl',
            'ingredients': ['frozen açaí puree', 'banana', 'mixed berries', 'almond milk', 'granola', 'honey'],
            'allergens': ['tree nuts'],
            'instructions': 'Blend açaí, banana, berries, and almond milk. Top with granola and honey.',
            'source': 'https://cooking.nytimes.com/68861692-nyt-cooking/112038332-best-breakfast-recipes'
        },
        {
            'name': 'Matcha Chia Pudding',
            'ingredients': ['chia seeds', 'matcha powder', 'coconut milk', 'maple syrup', 'vanilla extract', 'fresh fruit'],
            'allergens': [],
            'instructions': 'Mix chia seeds, matcha, coconut milk, maple syrup, and vanilla. Refrigerate overnight. Top with fresh fruit.',
            'source': 'https://www.bonappetit.com/gallery/make-ahead-breakfast-ideas'
        },
        {
            'name': 'Loaded Carrot Muffins',
            'ingredients': ['carrots', 'flour', 'eggs', 'brown sugar', 'vegetable oil', 'cinnamon', 'walnuts', 'raisins'],
            'allergens': ['eggs', 'gluten', 'tree nuts'],
            'instructions': 'Mix wet and dry ingredients separately, combine with shredded carrots. Fold in nuts and raisins. Bake until golden.',
            'source': 'https://www.bonappetit.com/gallery/healthy-breakfast-recipes'
        },
        {
            'name': 'Creme Brulee French Toast',
            'ingredients': ['thick bread slices', 'eggs', 'heavy cream', 'vanilla extract', 'brown sugar', 'butter', 'cinnamon'],
            'allergens': ['eggs', 'dairy', 'gluten'],
            'instructions': 'Make custard with eggs, cream, and vanilla. Soak bread. Caramelize brown sugar in pan, add bread, cook until golden.',
            'source': 'https://tasty.co/compilation/tasty-s-top-25-breakfasts'
        },
        {
            'name': 'Whipped Ricotta Berry Bagel',
            'ingredients': ['bagel', 'ricotta cheese', 'honey', 'mixed berries', 'mint leaves'],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Toast bagel. Whip ricotta with honey until fluffy. Spread on bagel and top with fresh berries and mint.',
            'source': 'https://tasty.co/article/salimahmccullough/best-breakfast-ideas'
        },
        {
            'name': 'Vegan Carrot Muffins',
            'ingredients': ['flax meal', 'coconut oil', 'dark brown sugar', 'plant based milk', 'vanilla extract', 'carrots', 'all-purpose flour', 'baking soda', 'kosher salt', 'cinnamon', 'ginger', 'turbinado sugar'],
            'allergens': ['gluten'],
            'instructions': 'Mix flax meal with water, combine with wet ingredients and grated carrots. Add dry ingredients. Top with ginger sugar. Bake at 375°F for 18-24 minutes.',
            'source': 'https://justinesnacks.com/vegan-carrot-muffins-for-two/'
        },
        {
            'name': 'Salted Date & Brown Butter Carrot Bread',
            'ingredients': ['carrots', 'salted butter', 'dark brown sugar', 'eggs', 'vanilla extract', 'flour', 'cardamom', 'cinnamon', 'baking powder', 'baking soda', 'dates', 'cream cheese', 'powdered sugar'],
            'allergens': ['dairy', 'eggs', 'gluten'],
            'instructions': 'Brown butter, mix with processed carrots and wet ingredients. Add dry ingredients and dates. Bake and top with cardamom cream cheese frosting.',
            'source': 'https://justinesnacks.com/salted-date-brown-butter-carrot-bread/'
        },
        {
            'name': 'Bananas Foster Overnight Oats',
            'ingredients': ['banana', 'cinnamon', 'rolled oats', 'plant milk', 'chia seeds', 'protein powder', 'flaxmeal', 'almond butter', 'coconut oil'],
            'allergens': ['tree nuts'],
            'instructions': 'Mix mashed banana, oats, milk and chia seeds. Chill overnight. Top with grilled bananas and flax-almond crumble.',
            'source': 'https://justinesnacks.com/bananas-foster-overnight-oats/'
        },
        {
            'name': 'Light and Fluffy Buttermilk Pancakes',
            'ingredients': ['all-purpose flour', 'baking powder', 'baking soda', 'kosher salt', 'sugar', 'eggs', 'buttermilk', 'sour cream', 'unsalted butter', 'maple syrup'],
            'allergens': ['dairy', 'eggs', 'gluten'],
            'instructions': 'Make dry mix. Whip egg whites separately. Mix wet ingredients with yolks. Fold together and cook on griddle until golden brown.',
            'source': 'https://www.seriouseats.com/light-and-fluffy-pancakes-recipe'
        },
        {
            'name': 'Overnight French Toast Casserole',
            'ingredients': ['brioche bread', 'eggs', 'milk', 'heavy cream', 'vanilla extract', 'cinnamon', 'nutmeg', 'brown sugar', 'butter', 'maple syrup'],
            'allergens': ['dairy', 'eggs', 'gluten'],
            'instructions': 'Layer bread in baking dish. Mix wet ingredients and pour over bread. Refrigerate overnight. Top with streusel and bake until golden.',
            'source': 'https://www.foodnetwork.com/recipes/overnight-french-toast-casserole'
        },
        {
            'name': 'Sheet Pan Breakfast Hash',
            'ingredients': ['potatoes', 'bell peppers', 'onions', 'bacon', 'eggs', 'olive oil', 'paprika', 'garlic powder', 'salt', 'pepper'],
            'allergens': ['eggs'],
            'instructions': 'Roast vegetables and bacon on sheet pan. Create wells and crack eggs into them. Bake until eggs are set.',
            'source': 'https://www.foodnetwork.com/recipes/sheet-pan-hash'
        },
        {
            'name': 'Classic Egg Salad Sandwich',
            'ingredients': ['hard boiled eggs', 'mayonnaise', 'lemon', 'celery', 'scallions', 'parsley', 'bread', 'lettuce', 'radishes'],
            'allergens': ['eggs', 'gluten'],
            'instructions': 'Combine eggs, mayo, lemon juice, celery, scallions, and parsley. Mix to desired consistency. Season with salt and pepper. Serve on bread with lettuce and radishes.',
            'source': 'https://www.seriouseats.com/the-best-egg-salad-recipe'
        },
        {
            'name': 'Tahini Banana Bread',
            'ingredients': ['ripe bananas', 'tahini', 'eggs', 'vanilla extract', 'all-purpose flour', 'baking soda', 'cinnamon', 'salt', 'sesame seeds'],
            'allergens': ['eggs', 'gluten', 'sesame'],
            'instructions': 'Mix wet ingredients. Combine dry ingredients separately. Fold together, top with sesame seeds, and bake until golden.',
            'source': 'https://carolinagelen.com/tahini-banana-bread/'
        },
        {
            'name': 'Crispy Potato Latkes',
            'ingredients': ['potatoes', 'onion', 'eggs', 'all-purpose flour', 'baking powder', 'salt', 'black pepper', 'vegetable oil', 'sour cream', 'applesauce'],
            'allergens': ['eggs', 'gluten', 'dairy'],
            'instructions': 'Grate potatoes and onion, drain well. Mix with other ingredients. Fry until golden and crispy. Serve with sour cream and applesauce.',
            'source': 'https://carolinagelen.com/crispy-potato-latkes/'
        },
    ],
    'lunch': [
        {
            'name': 'Grain Bowl With Sardines',
            'ingredients': ['quinoa', 'sardines', 'cucumber', 'tomatoes', 'olive oil', 'lemon', 'herbs'],
            'allergens': ['fish'],
            'instructions': 'Cook quinoa, arrange with sardines and vegetables. Dress with olive oil, lemon, and herbs.',
            'source': 'https://cooking.nytimes.com/68861692-nyt-cooking/20404912-lunch-ideas'
        },
        {
            'name': 'Healthy Mediterranean Salad',
            'ingredients': ['mixed greens', 'chickpeas', 'feta cheese', 'olives', 'cucumber', 'red onion', 'olive oil', 'lemon juice'],
            'allergens': ['dairy'],
            'instructions': 'Combine greens, chickpeas, and vegetables. Top with feta and dress with olive oil and lemon.',
            'source': 'https://cooking.nytimes.com/68861692-nyt-cooking/2110355-healthy-weekday-lunches'
        },
        {
            'name': 'Apple Som Tam',
            'ingredients': ['crisp apples', 'chili', 'lime juice', 'fish sauce', 'palm sugar', 'peanuts', 'cherry tomatoes'],
            'allergens': ['peanuts', 'fish'],
            'instructions': 'Slice apples into matchsticks. Mix with chili, lime juice, fish sauce, and palm sugar. Top with crushed peanuts and tomatoes.',
            'source': 'https://www.bonappetit.com/meal-time/lunch'
        },
        {
            'name': 'Broccoli Date Salad',
            'ingredients': ['raw broccoli', 'dates', 'pistachios', 'ras-el-hanout', 'olive oil', 'lemon juice'],
            'allergens': ['tree nuts'],
            'instructions': 'Chop broccoli finely, mix with chopped dates and pistachios. Season with ras-el-hanout, olive oil, and lemon juice.',
            'source': 'https://www.bonappetit.com/gallery/healthy-lunch-recipes'
        },
        {
            'name': 'Butternut Squash Al Pastor Tacos',
            'ingredients': ['butternut squash', 'al pastor seasoning', 'corn tortillas', 'avocado', 'cilantro', 'lime'],
            'allergens': [],
            'instructions': 'Roast seasoned butternut squash until tender. Warm tortillas, fill with squash, top with avocado, cilantro, and lime.',
            'source': 'https://tasty.co/article/michelleno/healthy-lunch-ideas'
        },
        {
            'name': 'Meal Prep Salmon Bowl',
            'ingredients': ['salmon fillet', 'brown rice', 'broccoli', 'carrots', 'edamame', 'soy sauce', 'sesame oil'],
            'allergens': ['fish', 'soy'],
            'instructions': 'Cook rice and roast salmon and vegetables. Portion into containers, drizzle with soy sauce and sesame oil.',
            'source': 'https://tasty.co/article/jesseszewczyk/meal-prep-lunch-recipes'
        },
        {
            'name': 'Kabocha Squash Bowl with Golden Raisin & Olive Dressing',
            'ingredients': ['kabocha squash', 'rice', 'olive oil', 'red onion', 'garlic', 'kalamata olives', 'golden raisins', 'red chili flakes', 'red wine vinegar', 'honey', 'chickpeas', 'fresh herbs'],
            'allergens': [],
            'instructions': 'Roast squash, make dressing with olives and raisins, combine with rice and chickpeas. Top with herb salad.',
            'source': 'https://justinesnacks.com/kabocha-squash-bowl-with-golden-raisin-kalamata-olive-dressing/'
        },
        {
            'name': 'Lemon Honey Snap Pea Toast',
            'ingredients': ['lemon', 'garlic', 'honey', 'white wine vinegar', 'snap peas', 'basil', 'mint', 'pecorino romano', 'olive oil', 'sourdough bread'],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Make lemon-honey dressing, slice snap peas, mix with herbs. Top toasted sourdough with the salad and cheese.',
            'source': 'https://justinesnacks.com/lemon-honey-snap-pea-toast/'
        },
        {
            'name': 'Crab Salad Sandwiches with Honey Dijon',
            'ingredients': ['jumbo lump crab', 'kewpie mayonnaise', 'hot sauce', 'lemon', 'red cabbage', 'dill', 'scallions', 'honey', 'dijon mustard', 'brioche buns', 'butter'],
            'allergens': ['shellfish', 'dairy', 'eggs', 'gluten'],
            'instructions': 'Mix crab salad with mayo and seasonings. Make cabbage slaw and honey dijon dressing. Assemble on toasted brioche buns.',
            'source': 'https://justinesnacks.com/crab-salad-sandwiches-with-honey-dijon-dressing/'
        },
        {
            'name': 'Muffuletta Sandwich',
            'ingredients': ['soppressata', 'capicola', 'mortadella', 'provolone', 'olives', 'capers', 'roasted red peppers', 'giardiniera', 'garlic', 'Italian bread'],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Layer meats and cheese on bread. Make olive salad with olives, capers, peppers, and giardiniera. Add to sandwich and press.',
            'source': 'https://www.seriouseats.com/sandwich-recipes'
        },
        {
            'name': 'Chicken Niçoise Salad',
            'ingredients': ['grilled chicken', 'green beans', 'potatoes', 'hard boiled eggs', 'olives', 'tomatoes', 'lettuce', 'vinaigrette'],
            'allergens': ['eggs'],
            'instructions': 'Grill chicken and arrange with blanched green beans, boiled potatoes, eggs, olives, and tomatoes over lettuce. Dress with vinaigrette.',
            'source': 'https://www.seriouseats.com/grilled-chicken-nicoise-salad-recipe'
        },
        {
            'name': 'Mediterranean Quinoa Bowl',
            'ingredients': ['quinoa', 'cherry tomatoes', 'cucumber', 'kalamata olives', 'feta cheese', 'red onion', 'olive oil', 'lemon juice', 'oregano', 'garlic'],
            'allergens': ['dairy'],
            'instructions': 'Cook quinoa. Combine with fresh vegetables. Dress with olive oil and lemon. Top with feta.',
            'source': 'https://www.foodnetwork.com/recipes/mediterranean-quinoa-bowl'
        },
        {
            'name': 'Grilled Chicken Pesto Wrap',
            'ingredients': ['grilled chicken breast', 'spinach tortilla', 'pesto', 'mozzarella', 'roasted red peppers', 'arugula', 'sun-dried tomatoes'],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Spread pesto on tortilla. Layer with chicken, cheese, and vegetables. Roll tightly and grill until warm.',
            'source': 'https://www.foodnetwork.com/recipes/grilled-chicken-pesto-wrap'
        },
        {
            'name': 'Charred Corn and Feta Salad',
            'ingredients': ['corn', 'feta cheese', 'red onion', 'cherry tomatoes', 'cilantro', 'lime juice', 'olive oil', 'chili powder', 'salt', 'black pepper'],
            'allergens': ['dairy'],
            'instructions': 'Char corn in a cast iron skillet. Mix with crumbled feta, vegetables, and herbs. Dress with lime and olive oil.',
            'source': 'https://carolinagelen.com/charred-corn-and-feta-salad/'
        },
        {
            'name': 'Crispy Chickpea Gyros',
            'ingredients': ['chickpeas', 'pita bread', 'greek yogurt', 'cucumber', 'garlic', 'dill', 'lemon', 'olive oil', 'paprika', 'red onion'],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Crisp chickpeas with spices. Make tzatziki with yogurt, cucumber, and herbs. Assemble in pita with vegetables.',
            'source': 'https://carolinagelen.com/crispy-chickpea-gyros/'
        },
    ],
    'dinner': [
        {
            'name': 'Tofu Larb',
            'ingredients': ['firm tofu', 'shallots', 'lime juice', 'fish sauce', 'chili', 'mint', 'cilantro', 'rice powder'],
            'allergens': ['soy'],
            'instructions': 'Crumble and cook tofu, mix with herbs and seasonings. Serve with rice or lettuce cups.',
            'source': 'https://cooking.nytimes.com/topics/dinner-recipes'
        },
        {
            'name': 'Easy Weeknight Pasta',
            'ingredients': ['pasta', 'olive oil', 'garlic', 'red pepper flakes', 'parmesan', 'parsley'],
            'allergens': ['gluten', 'dairy'],
            'instructions': 'Cook pasta, sauté garlic and pepper flakes in oil. Toss with pasta, cheese, and parsley.',
            'source': 'https://cooking.nytimes.com/68861692-nyt-cooking/1604305-easy-weeknight-dinners'
        },
        {
            'name': 'Roasted Kabocha Squash',
            'ingredients': ['kabocha squash', 'olive oil', 'maple syrup', 'soy sauce', 'ginger', 'sesame seeds', 'scallions'],
            'allergens': ['soy'],
            'instructions': 'Peel and cut squash, toss with oil, maple syrup, and soy sauce. Roast until tender. Top with ginger, sesame seeds, and scallions.',
            'source': 'https://www.bonappetit.com/recipes/slideshow/fast-easy-weeknight-dinner-recipes-ideas'
        },
        {
            'name': 'Spicy Salmon Rice Bowl',
            'ingredients': ['salmon fillet', 'sushi rice', 'gochugaru', 'sesame oil', 'nori', 'cucumber', 'avocado'],
            'allergens': ['fish'],
            'instructions': 'Cook rice. Season salmon with gochugaru, pan-sear. Serve over rice with cucumber, avocado, and nori.',
            'source': 'https://www.bonappetit.com/gallery/22-weeknight-dinners-ba-editors-make-again-and-again'
        },
        {
            'name': 'Sheet-Pan Gnocchi',
            'ingredients': ['potato gnocchi', 'cherry tomatoes', 'garlic', 'olive oil', 'basil', 'parmesan cheese'],
            'allergens': ['gluten', 'dairy'],
            'instructions': 'Toss gnocchi and tomatoes with oil and garlic on sheet pan. Roast until gnocchi is crispy and tomatoes burst. Top with basil and cheese.',
            'source': 'https://tasty.co/article/jesseszewczyk/back-to-school-dinner-recipes'
        },
        {
            'name': 'Healthy Chicken Fajitas',
            'ingredients': ['chicken breast', 'bell peppers', 'onions', 'fajita seasoning', 'lime', 'tortillas', 'avocado'],
            'allergens': ['gluten'],
            'instructions': 'Season and cook chicken with peppers and onions. Serve in warm tortillas with avocado and lime.',
            'source': 'https://tasty.co/article/michelleno/easy-healthy-dinner-recipes'
        },
        {
            'name': 'Edamame Shiitake Dumplings',
            'ingredients': ['shiitake mushrooms', 'scallions', 'chili crisp', 'olive oil', 'edamame', 'rice paper wrappers', 'flour', 'baby bok choy', 'avocado oil', 'black vinegar'],
            'allergens': ['gluten', 'soy'],
            'instructions': 'Make filling with mushrooms, scallions, and edamame. Wrap in rice paper, fry until crispy, create dumpling skirt. Serve with bok choy.',
            'source': 'https://justinesnacks.com/edamame-shitake-dumplings/'
        },
        {
            'name': 'Twice-Baked Japanese Sweet Potatoes',
            'ingredients': ['Japanese sweet potato', 'white miso paste', 'skyr or greek yogurt', 'maple syrup'],
            'allergens': ['dairy'],
            'instructions': 'Bake sweet potato until tender, scoop out interior and mix with miso, yogurt, and maple syrup. Restuff and bake until caramelized.',
            'source': 'https://justinesnacks.com/twice-baked-japanese-sweet-potatoes/'
        },
        {
            'name': 'Kale Tahini Pasta',
            'ingredients': ['kale', 'tahini', 'oregano', 'coriander', 'cumin', 'lemon', 'pasta', 'olive oil', 'red pepper flakes', 'sesame seeds'],
            'allergens': ['gluten'],
            'instructions': 'Blanch kale, blend with tahini and seasonings. Cook pasta, combine with sauce and top with sesame seeds.',
            'source': 'https://justinesnacks.com/kale-tahini-pasta/'
        },
        {
            'name': 'Arugula Orzo with Feta & Mint',
            'ingredients': ['arugula', 'parsley', 'English peas', 'garlic', 'lemon', 'olive oil', 'orzo', 'feta cheese', 'mint leaves'],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Blanch greens and peas, blend arugula sauce. Cook orzo, combine with sauce and peas. Top with feta and mint.',
            'source': 'https://justinesnacks.com/arugula-orzo-with-feta-lemon-mint/'
        },
        {
            'name': 'Pasta al Limone',
            'ingredients': ['spaghetti', 'butter', 'lemon', 'garlic', 'Parmigiano-Reggiano', 'black pepper'],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Cook pasta. Make sauce with butter, lemon zest, and garlic. Toss pasta with sauce, cheese, and pasta water until creamy. Add lemon juice to taste.',
            'source': 'https://www.seriouseats.com/pasta-al-limone'
        },
        {
            'name': 'Slow-Cooked Bolognese Sauce',
            'ingredients': ['ground beef', 'pancetta', 'onion', 'carrot', 'celery', 'garlic', 'tomatoes', 'milk', 'white wine', 'bay leaves'],
            'allergens': ['dairy'],
            'instructions': 'Brown meat and vegetables. Add wine, milk, and tomatoes. Simmer slowly until rich and thick. Serve with pasta.',
            'source': 'https://www.seriouseats.com/the-best-slow-cooked-bolognese-sauce-recipe'
        },
        {
            'name': 'One-Pot Lemon Garlic Shrimp Pasta',
            'ingredients': ['linguine', 'shrimp', 'garlic', 'lemon', 'white wine', 'butter', 'parsley', 'red pepper flakes', 'parmesan cheese'],
            'allergens': ['shellfish', 'dairy', 'gluten'],
            'instructions': 'Cook pasta and shrimp in same pot. Make sauce with garlic, wine, and lemon. Toss together and finish with parmesan.',
            'source': 'https://www.foodnetwork.com/recipes/lemon-garlic-shrimp-pasta'
        },
        {
            'name': 'Herb-Crusted Rack of Lamb',
            'ingredients': ['rack of lamb', 'fresh rosemary', 'fresh thyme', 'garlic', 'dijon mustard', 'breadcrumbs', 'olive oil', 'salt', 'pepper'],
            'allergens': ['gluten'],
            'instructions': 'Coat lamb with mustard and herb-breadcrumb mixture. Roast until desired doneness. Rest before slicing.',
            'source': 'https://www.foodnetwork.com/recipes/herb-crusted-rack-of-lamb'
        },
        {
            'name': 'Caramelized Onion and Mushroom Pasta',
            'ingredients': ['pasta', 'mushrooms', 'onions', 'garlic', 'thyme', 'butter', 'parmesan cheese', 'white wine', 'black pepper', 'olive oil'],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Caramelize onions slowly. Sauté mushrooms until golden. Cook pasta and toss with vegetables, cheese, and pasta water.',
            'source': 'https://carolinagelen.com/caramelized-onion-and-mushroom-pasta/'
        },
        {
            'name': 'Harissa Roasted Chicken',
            'ingredients': ['whole chicken', 'harissa paste', 'honey', 'lemon', 'garlic', 'olive oil', 'carrots', 'potatoes', 'salt', 'cilantro'],
            'allergens': [],
            'instructions': 'Marinate chicken in harissa and honey. Roast with vegetables until chicken is cooked through and vegetables are tender.',
            'source': 'https://carolinagelen.com/harissa-roasted-chicken/'
        },
    ]
}

# Common allergens (capitalized)
allergens = [
    'Dairy',
    'Eggs',
    'Fish',
    'Tree Nuts',
    'Peanuts',
    'Gluten',
    'Soy'
]

# Color palette
colors = {
    'primary': '#7400B8',
    'secondary': '#6930C3',
    'tertiary': '#5E60CE',
    'quaternary': '#5390D9',
    'quinary': '#4EA8DE',
    'senary': '#48BFE3',
    'septenary': '#56CFE1',
    'octonary': '#64DFDF',
    'nonary': '#72EFDD',
    'denary': '#80FFDB'
}

def main():
    # Set page config and custom CSS
    st.set_page_config(page_title='Recipe Browser', layout='wide')
    st.markdown(f"""
        <style>
        .stApp {{
            background: linear-gradient(180deg, {colors['primary']}, {colors['denary']});
        }}
        section[data-testid="stSidebar"] {{
            background-color: white !important;
            padding: 1rem;
        }}
        section[data-testid="stSidebar"] .stMarkdown {{
            color: {colors['primary']} !important;
        }}
        .allergy-title {{
            font-size: 40px !important;
            margin-bottom: 30px !important;
            padding-left: 0 !important;
            color: #7E22CE !important;
        }}
        .allergy-subtitle {{
            font-size: 14px !important;
            margin-bottom: 10px !important;
            padding-left: 0 !important;
            color: #5E60CE !important;
            font-family: "Source Sans Pro", sans-serif !important;
        }}
        div[data-testid="stSidebarContent"] > div > div {{
            padding-left: 0 !important;
        }}
        .stButton>button {{
            background-color: {colors['quaternary']};
            color: white;
        }}
        .stSelectbox>div>div {{
            background-color: {colors['tertiary']} !important;
            border: none !important;
            color: white !important;
        }}
        .stSelectbox>div>div:hover {{
            background-color: {colors['tertiary']} !important;
        }}
        .stMultiSelect>div>div {{
            background-color: white !important;
            border: 2px solid {colors['tertiary']} !important;
            border-radius: 8px !important;
            color: {colors['tertiary']} !important;
        }}
        .stMultiSelect>div>div:hover {{
            background-color: {colors['tertiary']} !important;
            color: white !important;
        }}
        .stMultiSelect span {{
            color: {colors['tertiary']} !important;
        }}
        .stMultiSelect svg {{
            color: {colors['tertiary']} !important;
        }}
        div[role="listbox"] {{
            background-color: {colors['tertiary']} !important;
            max-height: none !important;
            overflow: visible !important;
        }}
        div[role="option"] {{
            background-color: {colors['tertiary']} !important;
            color: white !important;
            margin: -4px !important;
            padding: 8px 12px !important;
        }}
        div[role="option"]:hover {{
            background-color: #80FFDB !important;
            color: {colors['tertiary']} !important;
            margin: -4px !important;
            padding: 8px 12px !important;
        }}
        div[role="option"][aria-selected="true"] {{
            background-color: {colors['tertiary']} !important;
            color: white !important;
            border: none !important;
            outline: none !important;
            box-shadow: none !important;
        }}
        div[data-baseweb="select"] {{
            background-color: {colors['tertiary']} !important;
        }}
        div[data-baseweb="select"] > div {{
            background-color: {colors['tertiary']} !important;
            color: white !important;
            border: 2px solid white !important;
            border-radius: 8px !important;
        }}
        div[data-baseweb="select"] * {{
            background-color: {colors['tertiary']} !important;
            color: white !important;
        }}
        div[data-baseweb="select"] div {{
            background-color: {colors['tertiary']} !important;
        }}
        div[data-baseweb="select"] [data-highlighted="true"] {{
            background-color: #80FFDB !important;
            color: {colors['tertiary']} !important;
            border: none !important;
            outline: none !important;
            box-shadow: none !important;
        }}
        div[data-baseweb="select"] [aria-selected="true"] {{
            background-color: #80FFDB !important;
            color: {colors['tertiary']} !important;
            border: none !important;
            outline: none !important;
            box-shadow: none !important;
        }}
        div[data-baseweb="menu"],
        div[data-baseweb="popover"],
        div[data-baseweb="select-dropdown"],
        div[role="listbox"],
        div[data-baseweb="menu"] div,
        div[data-baseweb="popover"] div,
        div[data-baseweb="select-dropdown"] div {{
            max-height: 1000px !important;
            overflow: visible !important;
        }}
        div[data-baseweb="select"] {{
            max-height: 1000px !important;
            overflow: visible !important;
        }}
        ul[role="listbox"] {{
            max-height: 1000px !important;
            overflow: visible !important;
        }}
        div[data-baseweb="menu"] {{
            background-color: {colors['tertiary']} !important;
            max-height: none !important;
            overflow: visible !important;
        }}
        div[data-baseweb="menu"] * {{
            background-color: {colors['tertiary']} !important;
            color: white !important;
        }}
        div[data-baseweb="menu"] div:hover {{
            background-color: #80FFDB !important;
            color: {colors['tertiary']} !important;
        }}
        div[data-baseweb="popover"] {{
            max-height: none !important;
            overflow: visible !important;
        }}
        div[data-baseweb="popover"] * {{
            background-color: {colors['tertiary']} !important;
            color: white !important;
        }}
        div[data-baseweb="popover"] div:hover {{
            background-color: #80FFDB !important;
            color: {colors['tertiary']} !important;
        }}
        div[data-baseweb="select-dropdown"] {{
            max-height: none !important;
            overflow: visible !important;
        }}
        div[data-baseweb="select-dropdown"] * {{
            background-color: {colors['tertiary']} !important;
            color: white !important;
        }}
        div[data-baseweb="select-dropdown"] div:hover {{
            background-color: #80FFDB !important;
            color: {colors['tertiary']} !important;
        }}
        .stExpander {{
            background-color: {colors['tertiary']};
            border: none !important;
            border-radius: 8px;
            color: white;
        }}
        .stExpander:hover {{
            background-color: {colors['tertiary']};
        }}
        .streamlit-expanderHeader {{
            color: white !important;
            background-color: transparent !important;
        }}
        .streamlit-expanderContent {{
            color: white !important;
            background-color: {colors['quaternary']} !important;
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
        }}
        p {{
            color: white !important;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: white !important;
        }}
        code {{
            color: {colors['denary']} !important;
        }}
        .stMarkdown a {{
            color: {colors['denary']} !important;
            text-decoration: underline;
        }}
        .stMarkdown a:hover {{
            color: white !important;
        }}
        div[data-baseweb="popover"] {{
            background-color: {colors['tertiary']} !important;
        }}
        div[data-baseweb="popover"] * {{
            background-color: {colors['tertiary']} !important;
            color: white !important;
        }}
        div[data-baseweb="popover"] div:hover {{
            background-color: #80FFDB !important;
            color: {colors['tertiary']} !important;
        }}
        div[data-baseweb="menu"] {{
            background-color: {colors['tertiary']} !important;
        }}
        div[data-baseweb="menu"] * {{
            background-color: {colors['tertiary']} !important;
            color: white !important;
        }}
        div[data-baseweb="menu"] div:hover {{
            background-color: #80FFDB !important;
            color: {colors['tertiary']} !important;
        }}
        div[data-baseweb="select-dropdown"] {{
            background-color: {colors['tertiary']} !important;
        }}
        div[data-baseweb="select-dropdown"] * {{
            background-color: {colors['tertiary']} !important;
            color: white !important;
        }}
        div[data-baseweb="select-dropdown"] div:hover {{
            background-color: #80FFDB !important;
            color: {colors['tertiary']} !important;
        }}
        header {{
            background-color: #5E60CE !important;
            color: white !important;
        }}
        .stDeployButton {{
            background-color: #5E60CE !important;
            color: white !important;
        }}
        .stToolbar {{
            background-color: #5E60CE !important;
            color: white !important;
        }}
        </style>
        """, unsafe_allow_html=True)

    # Custom CSS for Marker Felt font
    st.markdown("""
    <style>
    /* Set Marker Felt as the default font for all elements */
    * {
        font-family: "Marker Felt", "Comic Sans MS", cursive !important;
    }

    /* Apply font to specific Streamlit elements */
    .stMarkdown, .stText, .stTitle, .stHeader, 
    .stSelectbox, .stMultiSelect, .stTextInput,
    button, .stButton, .streamlit-expanderHeader {
        font-family: "Marker Felt", "Comic Sans MS", cursive !important;
    }

    /* Ensure font applies to dropdown options */
    div[data-baseweb="select"] * {
        font-family: "Marker Felt", "Comic Sans MS", cursive !important;
    }

    /* Apply to expander content */
    .streamlit-expanderContent {
        font-family: "Marker Felt", "Comic Sans MS", cursive !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Main content
    st.title("Recipe Browser")
    st.write("Browse recipes and filter by allergies")

    # Sidebar for filters
    st.sidebar.markdown("<h1 class='allergy-title'>Allergy Filters</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<p class='allergy-subtitle'>Select allergens to exclude:</p>", unsafe_allow_html=True)
    selected_allergens = st.sidebar.multiselect("", allergens, key="allergen_filter", label_visibility="collapsed")

    # Meal type selection (capitalized)
    meal_type = st.selectbox(
        'Select meal type:',
        ['Breakfast', 'Lunch', 'Dinner']
    )

    # Filter and display recipes
    st.header(f'{meal_type} Recipes')
    
    # Convert meal_type to lowercase for dictionary lookup
    meal_type_lower = meal_type.lower()
    
    for recipe in recipes[meal_type_lower]:
        # Skip recipe if it contains any selected allergens
        if any(allergen.lower() in [a.lower() for a in recipe['allergens']] for allergen in selected_allergens):
            continue
            
        with st.expander(f"{recipe['name']}"):
            st.write('**Ingredients:**')
            for ingredient in recipe['ingredients']:
                st.write(f"- {ingredient}")
            
            st.write('**Instructions:**')
            st.write(recipe['instructions'])
            
            if recipe['allergens']:
                # Capitalize allergens in display
                display_allergens = [allergen.title() for allergen in recipe['allergens']]
                st.write('**Contains allergens:**', ', '.join(display_allergens))
            else:
                st.write('**Allergen-free!**')
            
            # Add source attribution
            st.write('**Source:**')
            st.markdown(f"[{recipe['source'].split('/')[2]}]({recipe['source']})")

if __name__ == '__main__':
    main()
