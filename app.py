import streamlit as st
import pandas as pd

# Sample recipe data from NYT Cooking, Bon Appétit, and Tasty
recipes = {
    'breakfast': [
        {
            'name': 'Buttery Breakfast Casserole',
            'ingredients': [
                '6 large croissants, split lengthwise',
                '2 tablespoons olive oil',
                '4 scallions, thinly sliced',
                '1 pound sweet Italian sausage, casings removed',
                '2 tablespoons fresh sage, chopped',
                '8 large eggs',
                '2 cups whole milk',
                '1 cup heavy cream',
                '8 ounces gruyère cheese, grated',
                '1 teaspoon kosher salt',
                '1/2 teaspoon black pepper'
            ],
            'allergens': ['dairy', 'eggs', 'gluten'],
            'instructions': 'Layer split croissants in buttered baking dish. Cook sausage with scallions and sage. Mix eggs, milk, cream, and seasonings. Pour over croissants, top with cheese. Bake until golden.',
            'source': 'https://cooking.nytimes.com/recipes/1017894-buttery-breakfast-casserole',
            'servings': 'Serves 6-8'
        },
        {
            'name': 'Açaí Bowl',
            'ingredients': [
                '2 frozen açaí packets',
                '1 large frozen banana',
                '1 cup mixed frozen berries',
                '1/2 cup almond milk',
                '2 tablespoons honey',
                'Toppings:',
                '1/2 cup granola',
                '1 sliced banana',
                '1/4 cup fresh berries',
                '1 tablespoon chia seeds'
            ],
            'allergens': ['tree nuts'],
            'instructions': 'Blend açaí, banana, berries, and almond milk. Top with granola and honey.',
            'source': 'https://cooking.nytimes.com/68861692-nyt-cooking/112038332-best-breakfast-recipes',
            'servings': 'Serves 1'
        },
        {
            'name': 'Matcha Chia Pudding',
            'ingredients': [
                '1/4 cup chia seeds',
                '1 cup coconut milk',
                '1 tablespoon matcha powder',
                '2 tablespoons maple syrup',
                '1/2 teaspoon vanilla extract',
                'Toppings:',
                '1/4 cup fresh berries',
                '2 tablespoons coconut flakes',
                '1 tablespoon honey'
            ],
            'allergens': [],
            'instructions': 'Mix chia seeds with coconut milk and matcha. Let sit overnight. Top with berries and coconut.',
            'source': 'https://justinesnacks.com/matcha-chia-pudding',
            'servings': 'Serves 2'
        },
        {
            'name': 'Loaded Carrot Muffins',
            'ingredients': [
                '2 cups all-purpose flour',
                '2 teaspoons baking soda',
                '1 teaspoon ground cinnamon',
                '1/2 teaspoon ground ginger',
                '1/2 teaspoon salt',
                '2 cups finely grated carrots (about 4 medium)',
                '1 cup chopped walnuts',
                '1/2 cup shredded coconut',
                '1/2 cup raisins',
                '3 large eggs',
                '2/3 cup vegetable oil',
                '1 cup brown sugar, packed',
                '1/2 cup plain yogurt',
                '2 teaspoons vanilla extract'
            ],
            'allergens': ['eggs', 'tree nuts', 'gluten', 'dairy'],
            'instructions': 'Mix dry ingredients. Combine wet ingredients separately. Fold in carrots and mix-ins. Bake at 375°F for 20-25 minutes.',
            'source': 'https://www.kingarthurbaking.com/recipes/morning-glory-muffins',
            'servings': 'Makes 12 muffins'
        },
        {
            'name': 'Creme Brulee French Toast',
            'ingredients': [
                'Caramel Base:',
                '1/2 cup unsalted butter',
                '1 cup packed brown sugar',
                '2 tablespoons corn syrup',
                'French Toast:',
                '1 loaf brioche bread (about 1 pound), cut into 1-inch slices',
                '5 large eggs',
                '1 1/2 cups half-and-half',
                '1 teaspoon vanilla extract',
                '1/4 teaspoon salt',
                '2 tablespoons granulated sugar (for topping)',
                'Fresh berries and maple syrup for serving'
            ],
            'allergens': ['eggs', 'dairy', 'gluten'],
            'instructions': 'Make caramel base and pour in baking dish. Layer bread. Whisk eggs with half-and-half, vanilla, and salt. Pour over bread. Refrigerate overnight. Sprinkle with sugar and bake at 350°F for 35-40 minutes until golden and crispy.',
            'source': 'https://www.foodnetwork.com/recipes/creme-brulee-french-toast-recipe2-1950186',
            'servings': 'Serves 6-8'
        },
        {
            'name': 'Whipped Ricotta Berry Bagel',
            'ingredients': [
                '2 fresh bagels, sliced and toasted',
                'Whipped Ricotta:',
                '1 cup whole milk ricotta cheese',
                '2 tablespoons honey',
                '1/4 teaspoon vanilla extract',
                'Pinch of sea salt',
                'Toppings:',
                '1 cup mixed fresh berries (strawberries, blueberries, raspberries)',
                '2 tablespoons honey for drizzling',
                '2 tablespoons chopped pistachios',
                'Fresh mint leaves for garnish'
            ],
            'allergens': ['dairy', 'gluten', 'tree nuts'],
            'instructions': 'Whip ricotta with honey, vanilla, and salt until smooth. Spread on toasted bagels. Top with berries, drizzle with honey, and sprinkle with pistachios.',
            'source': 'https://www.carolinagelen.com/whipped-ricotta-breakfast',
            'servings': 'Serves 2'
        },
        {
            'name': 'Vegan Carrot Muffins',
            'ingredients': [
                '2 cups all-purpose flour',
                '2 teaspoons baking powder',
                '1 teaspoon baking soda',
                '2 teaspoons ground cinnamon',
                '1/2 teaspoon ground ginger',
                '1/4 teaspoon ground nutmeg',
                '1/2 teaspoon salt',
                '2 cups grated carrots (about 3-4 medium)',
                '1/2 cup unsweetened applesauce',
                '1/2 cup plant-based milk',
                '1/3 cup melted coconut oil',
                '2/3 cup maple syrup',
                '1 teaspoon vanilla extract',
                '1/2 cup chopped walnuts (optional)',
                '1/3 cup raisins (optional)'
            ],
            'allergens': ['gluten', 'tree nuts'],
            'instructions': 'Mix dry ingredients. Combine wet ingredients separately. Fold in carrots and optional mix-ins. Bake at 350°F for 20-22 minutes.',
            'source': 'https://justinesnacks.com/vegan-carrot-muffins',
            'servings': 'Makes 12 muffins'
        },
        {
            'name': 'Salted Date & Brown Butter Carrot Bread',
            'ingredients': [
                '2 cups all-purpose flour',
                '1 teaspoon baking soda',
                '1 teaspoon baking powder',
                '1 teaspoon ground cinnamon',
                '1/2 teaspoon ground ginger',
                '1/2 teaspoon salt',
                '1/2 cup (1 stick) unsalted butter, browned and cooled',
                '2 large eggs',
                '3/4 cup brown sugar',
                '1/4 cup granulated sugar',
                '1 teaspoon vanilla extract',
                '2 cups grated carrots (about 3 medium)',
                '1 cup chopped Medjool dates',
                'Topping:',
                '2 tablespoons turbinado sugar',
                '1/2 teaspoon flaky sea salt'
            ],
            'allergens': ['eggs', 'dairy', 'gluten'],
            'instructions': 'Brown butter and cool. Mix dry ingredients. Whisk wet ingredients with brown butter. Combine and fold in carrots and dates. Top with sugar and salt. Bake at 350°F for 55-60 minutes.',
            'source': 'https://justinesnacks.com/salted-date-brown-butter-carrot-bread',
            'servings': 'Makes one 9x5-inch loaf'
        },
        {
            'name': 'Bananas Foster Overnight Oats',
            'ingredients': [
                'Overnight Oats Base:',
                '1 cup old-fashioned rolled oats',
                '1 cup almond milk (or milk of choice)',
                '1/4 cup Greek yogurt',
                '1 tablespoon chia seeds',
                '1 tablespoon maple syrup',
                '1/2 teaspoon vanilla extract',
                'Bananas Foster Topping:',
                '2 ripe bananas, sliced',
                '2 tablespoons butter',
                '1/4 cup brown sugar',
                '1/4 teaspoon ground cinnamon',
                'Pinch of sea salt',
                '2 tablespoons chopped pecans (optional)'
            ],
            'allergens': ['dairy', 'tree nuts'],
            'instructions': 'Mix oats, milk, yogurt, chia seeds, maple syrup, and vanilla. Refrigerate overnight. Before serving, caramelize bananas with butter, brown sugar, and cinnamon. Top oats with warm banana mixture.',
            'source': 'https://www.foodnetwork.com/recipes/bananas-foster-overnight-oats',
            'servings': 'Serves 2'
        },
        {
            'name': 'Light and Fluffy Buttermilk Pancakes',
            'ingredients': [
                'Dry Mix:',
                '2 cups (10 ounces) all-purpose flour',
                '1 teaspoon baking powder',
                '1/2 teaspoon baking soda',
                '1 teaspoon kosher salt',
                '1 tablespoon sugar',
                'Wet Ingredients:',
                '2 large eggs, separated',
                '1 1/2 cups (12 ounces) buttermilk',
                '1 cup (8 ounces) sour cream',
                '4 tablespoons unsalted butter, melted',
                'For Serving:',
                'Additional butter for griddle and serving',
                'Warm maple syrup'
            ],
            'allergens': ['dairy', 'eggs', 'gluten'],
            'instructions': 'Whisk dry ingredients. Separately, whip egg whites to stiff peaks. Mix yolks, buttermilk, and sour cream, then drizzle in melted butter. Fold in whites, then combine with dry mix until just mixed. Cook on griddle at medium heat, about 2 minutes per side.',
            'source': 'https://www.seriouseats.com/light-and-fluffy-pancakes-recipe',
            'servings': 'Makes 16 pancakes (serves 4-6)'
        },
        {
            'name': 'Overnight French Toast Casserole',
            'ingredients': [
                'French Toast Base:',
                '1 large loaf brioche bread (about 1 pound), cut into 1-inch cubes',
                '8 large eggs',
                '2 cups whole milk',
                '1 cup heavy cream',
                '1/2 cup brown sugar',
                '2 teaspoons vanilla extract',
                '1 tablespoon ground cinnamon',
                '1/4 teaspoon ground nutmeg',
                '1/4 teaspoon salt',
                'Streusel Topping:',
                '1/2 cup all-purpose flour',
                '1/2 cup brown sugar',
                '1 teaspoon ground cinnamon',
                '1/4 teaspoon salt',
                '1/2 cup (1 stick) cold butter, cubed',
                'For Serving:',
                'Warm maple syrup',
                'Fresh berries (optional)',
                'Whipped cream (optional)'
            ],
            'allergens': ['dairy', 'eggs', 'gluten'],
            'instructions': 'Layer bread in 9x13 baking dish. Whisk eggs, milk, cream, sugar, vanilla, and spices. Pour over bread. Cover and refrigerate overnight. Before baking, make streusel by cutting butter into dry ingredients. Sprinkle over casserole. Bake at 350°F for 45-50 minutes until golden.',
            'source': 'https://www.foodnetwork.com/recipes/overnight-french-toast-casserole',
            'servings': 'Serves 8-10'
        },
        {
            'name': 'Sheet Pan Breakfast Hash',
            'ingredients': [
                '2 pounds Yukon Gold potatoes, cut into 1/2-inch cubes',
                '1 large red bell pepper, diced',
                '1 large yellow onion, diced',
                '2 cups cremini mushrooms, quartered',
                '3 tablespoons olive oil',
                '2 teaspoons smoked paprika',
                '1 teaspoon garlic powder',
                '1 teaspoon dried thyme',
                '1 teaspoon kosher salt',
                '1/2 teaspoon black pepper',
                '6 large eggs',
                'For Serving:',
                '1/4 cup fresh parsley, chopped',
                '1/2 avocado, sliced (optional)',
                'Hot sauce to taste'
            ],
            'allergens': ['eggs'],
            'instructions': 'Toss vegetables with oil and seasonings. Spread on sheet pan and roast at 425°F for 25-30 minutes, stirring halfway. Create wells in vegetables, crack eggs into wells. Bake 5-7 minutes more until eggs are set. Garnish with parsley.',
            'source': 'https://www.seriouseats.com/sheet-pan-breakfast-hash',
            'servings': 'Serves 4-6'
        },
        {
            'name': 'Classic Egg Salad Sandwich',
            'ingredients': [
                'Egg Salad:',
                '8 large eggs, hard-boiled and peeled',
                '1/3 cup mayonnaise',
                '1 tablespoon Dijon mustard',
                '1/4 cup celery, finely diced',
                '2 tablespoons red onion, finely minced',
                '1 tablespoon fresh dill, chopped',
                '1/2 teaspoon kosher salt',
                '1/4 teaspoon black pepper',
                '1/8 teaspoon paprika',
                'For Assembly:',
                '8 slices good quality sandwich bread',
                '2 cups fresh lettuce leaves',
                '1 ripe tomato, sliced (optional)',
                'Additional salt and pepper to taste'
            ],
            'allergens': ['eggs', 'gluten'],
            'instructions': 'Chop eggs and mix with mayonnaise, mustard, celery, onion, and seasonings. Chill for at least 30 minutes. Serve on bread with lettuce and optional tomato.',
            'source': 'https://www.seriouseats.com/classic-egg-salad-recipe',
            'servings': 'Makes 4 sandwiches'
        },
        {
            'name': 'Tahini Banana Bread',
            'ingredients': [
                'Wet Ingredients:',
                '3 very ripe bananas, mashed (about 1 1/2 cups)',
                '1/2 cup well-stirred tahini',
                '1/3 cup neutral oil (like vegetable or canola)',
                '2 large eggs',
                '2/3 cup brown sugar',
                '1/4 cup honey',
                '1 teaspoon vanilla extract',
                'Dry Ingredients:',
                '2 cups all-purpose flour',
                '1 teaspoon baking soda',
                '1 teaspoon ground cinnamon',
                '1/2 teaspoon kosher salt',
                'Topping:',
                '2 tablespoons sesame seeds',
                '1 tablespoon turbinado sugar'
            ],
            'allergens': ['eggs', 'gluten', 'sesame'],
            'instructions': 'Whisk wet ingredients until smooth. Combine dry ingredients separately. Mix together until just combined. Pour into greased 9x5 loaf pan. Top with sesame seeds and sugar. Bake at 350°F for 55-60 minutes.',
            'source': 'https://www.carolinagelen.com/tahini-banana-bread',
            'servings': 'Makes one 9x5-inch loaf'
        },
        {
            'name': 'Crispy Potato Latkes',
            'ingredients': [
                '2 pounds russet potatoes, peeled',
                '1 medium onion, peeled',
                '2 large eggs',
                '1/2 cup matzo meal or all-purpose flour',
                '2 teaspoons kosher salt',
                '1/4 teaspoon black pepper',
                '1/4 teaspoon baking powder',
                'Vegetable oil for frying (about 2 cups)',
                'For Serving:',
                'Applesauce',
                'Sour cream',
                'Fresh chives, chopped (optional)'
            ],
            'allergens': ['eggs', 'gluten'],
            'instructions': 'Grate potatoes and onion, drain well. Mix with eggs, matzo meal, salt, pepper, and baking powder. Heat oil to 350°F. Drop batter by 1/4 cups, fry 3-4 minutes per side until golden brown. Serve with applesauce and sour cream.',
            'source': 'https://www.seriouseats.com/classic-potato-latkes-recipe',
            'servings': 'Makes about 24 latkes (serves 6-8)'
        },
    ],
    'lunch': [
        {
            'name': 'Grain Bowl With Sardines',
            'ingredients': ['quinoa', 'sardines', 'cucumber', 'tomatoes', 'olive oil', 'lemon', 'herbs'],
            'allergens': ['fish'],
            'instructions': 'Cook quinoa, arrange with sardines and vegetables. Dress with olive oil, lemon, and herbs.',
            'source': 'https://cooking.nytimes.com/topics/dinner-recipes'
        },
        {
            'name': 'Healthy Mediterranean Salad',
            'ingredients': [
                'Salad Base:',
                '2 cups mixed salad greens',
                '1 English cucumber, diced',
                '2 cups cherry tomatoes, halved',
                '1 red bell pepper, diced',
                '1/2 red onion, thinly sliced',
                '1 cup Kalamata olives, pitted',
                '8 oz feta cheese, cubed',
                '1 (15 oz) can chickpeas, drained and rinsed',
                'Dressing:',
                '1/3 cup extra virgin olive oil',
                '2 tablespoons red wine vinegar',
                '1 tablespoon fresh lemon juice',
                '2 cloves garlic, minced',
                '1 teaspoon dried oregano',
                '1/2 teaspoon Dijon mustard',
                'Salt and black pepper to taste',
                'For Serving:',
                '1/4 cup fresh parsley, chopped',
                'Pita bread (optional)'
            ],
            'allergens': ['dairy'],
            'instructions': 'Combine all salad ingredients in a large bowl. Whisk dressing ingredients until well combined. Toss salad with dressing just before serving. Garnish with fresh parsley. Serve with pita bread if desired.',
            'source': 'https://www.seriouseats.com/mediterranean-salad',
            'servings': 'Serves 4-6'
        },
        {
            'name': 'Apple Som Tam',
            'ingredients': [
                'Salad Base:',
                '2 Granny Smith apples, julienned',
                '2 medium carrots, julienned',
                '1 cup green beans, thinly sliced',
                '1 cup cherry tomatoes, halved',
                '1/4 cup roasted peanuts, crushed',
                'Fresh Thai chilies, to taste (optional)',
                'Dressing:',
                '3 tablespoons fresh lime juice',
                '2 tablespoons fish sauce',
                '1 tablespoon palm sugar or brown sugar',
                '2 cloves garlic, minced',
                'For Serving:',
                '1/4 cup fresh cilantro, chopped',
                '2 tablespoons roasted peanuts, crushed',
                'Sticky rice (optional)'
            ],
            'allergens': ['fish', 'peanuts'],
            'instructions': 'Combine julienned apples, carrots, green beans, and tomatoes in a large bowl. Mix dressing ingredients until sugar dissolves. Toss salad with dressing and crushed peanuts. Garnish with cilantro and additional peanuts. Serve immediately with sticky rice if desired.',
            'source': 'https://www.seriouseats.com/apple-som-tam',
            'servings': 'Serves 4'
        },
        {
            'name': 'Broccoli Date Salad',
            'ingredients': [
                'Salad Base:',
                '2 large heads broccoli, cut into small florets',
                '1 cup Medjool dates, pitted and chopped',
                '1/2 red onion, thinly sliced',
                '1/2 cup almonds, toasted and chopped',
                '4 oz aged cheddar cheese, crumbled',
                'Dressing:',
                '1/3 cup extra virgin olive oil',
                '3 tablespoons apple cider vinegar',
                '1 tablespoon Dijon mustard',
                '1 tablespoon honey',
                '1 clove garlic, minced',
                '1/2 teaspoon kosher salt',
                '1/4 teaspoon black pepper',
                'For Serving:',
                'Additional toasted almonds',
                'Fresh cracked black pepper'
            ],
            'allergens': ['dairy', 'tree nuts'],
            'instructions': 'Steam broccoli until bright green and crisp-tender, about 3-4 minutes. Shock in ice water, drain well. Combine with dates, onion, almonds, and cheese. Whisk dressing ingredients until emulsified. Toss salad with dressing just before serving. Top with additional almonds and pepper.',
            'source': 'https://www.seriouseats.com/broccoli-date-salad',
            'servings': 'Serves 6'
        },
        {
            'name': 'Butternut Squash Al Pastor Tacos',
            'ingredients': [
                'Squash Marinade:',
                '1 medium butternut squash (about 2.5 lbs), peeled and diced',
                '3 dried guajillo chilies, stemmed and seeded',
                '2 dried ancho chilies, stemmed and seeded',
                '3 cloves garlic, peeled',
                '1 small white onion, chopped',
                '1/4 cup achiote paste',
                '1/4 cup pineapple juice',
                '2 tablespoons apple cider vinegar',
                '1 tablespoon dried oregano',
                '2 teaspoons ground cumin',
                '1 teaspoon ground cinnamon',
                '2 tablespoons olive oil',
                'Salt to taste',
                'For Assembly:',
                '12 corn tortillas, warmed',
                '1 cup fresh pineapple, diced',
                '1 small white onion, finely diced',
                '1/2 cup fresh cilantro, chopped',
                '2 limes, cut into wedges',
                'Hot sauce to taste'
            ],
            'allergens': [],
            'instructions': 'Toast chilies, soak in hot water. Blend with garlic, onion, achiote, juice, vinegar, and spices until smooth. Toss squash with marinade, roast at 425°F for 25-30 minutes until tender and caramelized. Serve in warm tortillas topped with pineapple, onion, and cilantro.',
            'source': 'https://www.seriouseats.com/butternut-squash-al-pastor-tacos',
            'servings': 'Makes 12 tacos (serves 4-6)'
        },
        {
            'name': 'Meal Prep Salmon Bowl',
            'ingredients': [
                'Salmon:',
                '4 (6 oz) salmon fillets',
                '2 tablespoons olive oil',
                '2 tablespoons soy sauce',
                '1 tablespoon honey',
                '1 tablespoon ginger, grated',
                '2 cloves garlic, minced',
                'Bowl Base:',
                '2 cups brown rice',
                '4 cups water',
                '1/4 teaspoon salt',
                'Vegetables:',
                '4 cups broccoli florets',
                '2 medium carrots, julienned',
                '2 cups edamame, shelled',
                '1 avocado, sliced',
                'Sauce:',
                '1/4 cup rice vinegar',
                '3 tablespoons sesame oil',
                '2 tablespoons soy sauce',
                '1 tablespoon honey',
                '1 tablespoon ginger, grated',
                'For Serving:',
                'Sesame seeds',
                'Nori strips',
                'Pickled ginger (optional)'
            ],
            'allergens': ['fish', 'soy'],
            'instructions': 'Cook rice with water and salt. Marinate salmon in oil, soy, honey, ginger, and garlic for 30 minutes. Roast at 400°F for 12-15 minutes. Steam broccoli, prepare other vegetables. Whisk sauce ingredients. Assemble bowls with rice, salmon, vegetables, and sauce. Top with sesame seeds and nori.',
            'source': 'https://www.seriouseats.com/meal-prep-salmon-bowl',
            'servings': 'Makes 4 bowls'
        },
        {
            'name': 'Kabocha Squash Bowl with Golden Raisin & Olive Dressing',
            'ingredients': [
                'Squash Base:',
                '1 medium kabocha squash (about 3 pounds), seeded and cut into wedges',
                '3 tablespoons olive oil',
                'Sauce:',
                '2 tablespoons maple syrup',
                '1 tablespoon soy sauce',
                '1 tablespoon grated fresh ginger',
                'Grain Base:',
                '1 cup farro',
                '3 cups water',
                '1/2 teaspoon salt',
                'Dressing:',
                '1/2 cup golden raisins',
                '1/3 cup green olives, pitted and chopped',
                '1/4 cup extra virgin olive oil',
                '3 tablespoons sherry vinegar',
                '2 tablespoons capers, drained',
                '2 tablespoons fresh parsley, chopped',
                '1 small shallot, minced',
                '1 clove garlic, minced',
                'Red pepper flakes to taste',
                'For Serving:',
                '1/2 cup toasted pistachios, chopped',
                '1/4 cup fresh mint leaves',
                'Greek yogurt (optional)'
            ],
            'allergens': ['tree nuts', 'dairy'],
            'instructions': 'Toss squash with oil and salt. Roast at 425°F for 25-30 minutes until tender. Cook farro in water with salt until tender, about 30 minutes. Combine dressing ingredients. Arrange squash over farro, drizzle with dressing. Top with pistachios and mint.',
            'source': 'https://www.seriouseats.com/kabocha-squash-bowl-recipe',
            'servings': 'Serves 4'
        },
        {
            'name': 'Lemon Honey Snap Pea Toast',
            'ingredients': [
                'Dressing:',
                '2 tablespoons fresh lemon juice',
                '2 cloves garlic, minced',
                '2 tablespoons honey',
                '1 tablespoon white wine vinegar',
                '3 tablespoons extra virgin olive oil',
                'Salad:',
                '1/2 pound sugar snap peas, thinly sliced on the bias',
                '1/4 cup fresh basil leaves, torn',
                '1/4 cup fresh mint leaves, torn',
                'For Serving:',
                '4 thick slices sourdough bread',
                '1/2 cup pecorino romano, shaved',
                'Salt and black pepper to taste'
            ],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Whisk together dressing ingredients. Slice snap peas and toss with herbs and dressing. Toast sourdough until golden brown. Top each toast with dressed snap pea salad and shaved pecorino. Season with salt and pepper.',
            'source': 'https://justinesnacks.com/lemon-honey-snap-pea-toast/',
            'servings': 'Serves 4'
        },
        {
            'name': 'Crab Salad Sandwiches with Honey Dijon',
            'ingredients': [
                'Crab Salad:',
                '1 pound jumbo lump crab meat, picked over',
                '1/3 cup kewpie mayonnaise',
                '1 teaspoon hot sauce',
                '1 lemon, zested and juiced',
                'Slaw:',
                '2 cups red cabbage, finely shredded',
                '1/4 cup fresh dill, chopped',
                '3 scallions, thinly sliced',
                'Honey Dijon Dressing:',
                '2 tablespoons honey',
                '2 tablespoons dijon mustard',
                '1 tablespoon white wine vinegar',
                'For Serving:',
                '4 brioche buns',
                '2 tablespoons butter, softened',
                'Salt and pepper to taste'
            ],
            'allergens': ['shellfish', 'dairy', 'eggs', 'gluten'],
            'instructions': 'Gently mix crab with mayo, hot sauce, lemon zest and juice. Toss cabbage with dill and scallions. Whisk honey dijon dressing ingredients. Butter and toast brioche buns. Layer crab salad and slaw on buns, drizzle with honey dijon.',
            'source': 'https://justinesnacks.com/crab-salad-sandwiches-with-honey-dijon-dressing/',
            'servings': 'Serves 4'
        },
        {
            'name': 'Muffuletta Sandwich',
            'ingredients': [
                'Meats:',
                '1/4 pound soppressata, thinly sliced',
                '1/4 pound capicola, thinly sliced',
                '1/4 pound mortadella, thinly sliced',
                'Cheese:',
                '1/4 pound provolone, thinly sliced',
                'Olive Salad:',
                '1 cup mixed olives, chopped',
                '2 tablespoons capers, drained',
                '1/2 cup roasted red peppers, chopped',
                '1/2 cup giardiniera, chopped',
                '2 cloves garlic, minced',
                '1/4 cup olive oil',
                'For Serving:',
                '1 large round Italian bread loaf (about 10 inches)',
                'Salt and pepper to taste'
            ],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Mix olive salad ingredients and let marinate for at least 1 hour. Cut bread horizontally, hollow out some of the inside. Layer bottom half with meats and cheese. Top with olive salad. Close sandwich and wrap tightly in plastic wrap. Press under weight for at least 30 minutes before serving.',
            'source': 'https://www.seriouseats.com/sandwich-recipes',
            'servings': 'Serves 4-6'
        },
        {
            'name': 'Chicken Niçoise Salad',
            'ingredients': [
                'Chicken:',
                '2 chicken breasts (about 1 pound)',
                '2 tablespoons olive oil',
                'Herbs de Provence',
                'Vegetables:',
                '1/2 pound green beans, trimmed',
                '1/2 pound baby potatoes, halved',
                '4 large eggs',
                '1/2 cup Niçoise olives',
                '1 pint cherry tomatoes, halved',
                '1 head Boston lettuce',
                'Vinaigrette:',
                '1/4 cup red wine vinegar',
                '1 tablespoon Dijon mustard',
                '1/2 cup extra virgin olive oil',
                '1 shallot, minced',
                'Salt and pepper to taste'
            ],
            'allergens': ['eggs'],
            'instructions': 'Season chicken with herbs and grill 6-7 minutes per side. Boil potatoes until tender (12-15 minutes), adding green beans in last 4 minutes. Cook eggs 7 minutes for jammy centers. Whisk vinaigrette ingredients. Arrange lettuce, sliced chicken, vegetables, eggs, and olives on platter. Drizzle with vinaigrette.',
            'source': 'https://www.seriouseats.com/grilled-chicken-nicoise-salad-recipe',
            'servings': 'Serves 4'
        },
        {
            'name': 'Mediterranean Quinoa Bowl',
            'ingredients': [
                'Quinoa Base:',
                '1 cup quinoa, rinsed',
                '2 cups water',
                '1/4 teaspoon salt',
                'Vegetables & Toppings:',
                '2 cups cherry tomatoes, halved',
                '1 English cucumber, diced',
                '1 red bell pepper, diced',
                '1/2 red onion, thinly sliced',
                '1 cup kalamata olives, pitted',
                '6 oz feta cheese, crumbled',
                '1/2 cup fresh parsley, chopped',
                '1/4 cup fresh mint leaves, torn',
                'Dressing:',
                '1/3 cup extra virgin olive oil',
                '2 tablespoons fresh lemon juice',
                '1 tablespoon red wine vinegar',
                '2 cloves garlic, minced',
                '1 teaspoon dried oregano',
                '1/2 teaspoon Dijon mustard',
                'Salt and black pepper to taste'
            ],
            'allergens': ['dairy'],
            'instructions': 'Cook quinoa with water and salt until fluffy. Cool slightly. Combine vegetables in a large bowl. Whisk dressing ingredients. Toss quinoa with vegetables and dressing. Top with feta, herbs, and season to taste.',
            'source': 'https://www.seriouseats.com/mediterranean-quinoa-bowl',
            'servings': 'Serves 4-6'
        },
        {
            'name': 'Grilled Chicken Pesto Wrap',
            'ingredients': [
                'Chicken:',
                '2 boneless, skinless chicken breasts (about 1 pound)',
                '2 tablespoons olive oil',
                '1 teaspoon Italian seasoning',
                '1/2 teaspoon garlic powder',
                'Salt and black pepper to taste',
                'Pesto:',
                '2 cups fresh basil leaves, packed',
                '1/2 cup freshly grated Parmesan cheese',
                '1/3 cup pine nuts, toasted',
                '3 cloves garlic, minced',
                '1/2 cup extra virgin olive oil',
                'Salt and black pepper to taste',
                'Assembly:',
                '4 large flour tortillas (10-inch)',
                '2 cups fresh baby spinach',
                '1 cup cherry tomatoes, halved',
                '1/2 red onion, thinly sliced',
                '4 oz fresh mozzarella, sliced'
            ],
            'allergens': ['dairy', 'gluten', 'tree nuts'],
            'instructions': 'Season and grill chicken until cooked through, slice thin. Blend pesto ingredients until smooth. Warm tortillas, spread with pesto, layer with chicken, spinach, tomatoes, onion, and mozzarella. Roll tightly and grill briefly to seal.',
            'source': 'https://www.foodnetwork.com/recipes/grilled-chicken-pesto-wrap',
            'servings': 'Makes 4 wraps'
        },
        {
            'name': 'Charred Corn and Feta Salad',
            'ingredients': [
                'Salad Base:',
                '6 ears fresh corn, husked',
                '2 tablespoons olive oil (for grilling)',
                '2 cups cherry tomatoes, halved',
                '1 large cucumber, diced',
                '1/2 red onion, finely diced',
                '1 jalapeño pepper, seeded and minced',
                '1 cup fresh cilantro, chopped',
                '8 oz feta cheese, crumbled',
                '1 avocado, diced',
                'Dressing:',
                '1/4 cup lime juice (about 2-3 limes)',
                '1/4 cup extra virgin olive oil',
                '2 cloves garlic, minced',
                '1 teaspoon ground cumin',
                '1 teaspoon honey',
                '1/2 teaspoon chili powder',
                'Salt and black pepper to taste'
            ],
            'allergens': ['dairy'],
            'instructions': 'Brush corn with oil and grill until charred, about 10-12 minutes. Cut kernels off cob. Combine with other vegetables and herbs. Whisk dressing ingredients. Toss together, fold in feta and avocado gently. Season to taste.',
            'source': 'https://www.seriouseats.com/charred-corn-feta-salad',
            'servings': 'Serves 6-8'
        },
        {
            'name': 'Crispy Chickpea Gyros',
            'ingredients': [
                'Crispy Chickpeas:',
                '2 (15 oz) cans chickpeas, drained and dried well',
                '2 tablespoons olive oil',
                '1 teaspoon ground cumin',
                '1 teaspoon smoked paprika',
                '1 teaspoon garlic powder',
                '1/2 teaspoon dried oregano',
                '1/2 teaspoon salt',
                '1/4 teaspoon black pepper',
                'Tzatziki Sauce:',
                '1 cup Greek yogurt',
                '1/2 English cucumber, grated and squeezed dry',
                '2 cloves garlic, minced',
                '1 tablespoon fresh dill, chopped',
                '1 tablespoon fresh lemon juice',
                'Salt and pepper to taste',
                'Assembly:',
                '4 pita breads, warmed',
                '2 cups shredded lettuce',
                '1 cup cherry tomatoes, halved',
                '1/2 red onion, thinly sliced',
                '1/4 cup fresh parsley, chopped'
            ],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Roast chickpeas with oil and seasonings at 400°F for 25-30 minutes until crispy. Make tzatziki by combining all sauce ingredients. Warm pitas, fill with crispy chickpeas, vegetables, and tzatziki sauce.',
            'source': 'https://www.seriouseats.com/crispy-chickpea-gyros',
            'servings': 'Makes 4 gyros'
        },
        {
            'name': 'Quinoa Sardine Bowl',
            'ingredients': [
                'Quinoa Base:',
                '1 cup quinoa, rinsed',
                '2 cups water',
                '1/4 teaspoon salt',
                'Protein & Vegetables:',
                '2 cans (4.375 oz each) olive oil-packed sardines',
                '1 English cucumber, diced',
                '2 cups cherry tomatoes, halved',
                '1/2 red onion, thinly sliced',
                '1/2 cup Kalamata olives, pitted and halved',
                'Dressing:',
                '1/4 cup extra virgin olive oil',
                '2 tablespoons fresh lemon juice',
                '2 tablespoons fresh parsley, chopped',
                '2 tablespoons fresh dill, chopped',
                '1 clove garlic, minced',
                'Salt and black pepper to taste',
                'For Serving:',
                'Additional fresh herbs',
                'Lemon wedges'
            ],
            'allergens': ['fish'],
            'instructions': 'Cook quinoa with water and salt until fluffy, about 15-20 minutes. Let cool slightly. Combine vegetables in a bowl. Whisk dressing ingredients. Toss quinoa with vegetables and dressing. Top with sardines and fresh herbs. Serve with lemon wedges.',
            'source': 'https://cooking.nytimes.com/topics/dinner-recipes',
            'servings': 'Serves 4'
        },
    ],
    'dinner': [
        {
            'name': 'Tofu Larb',
            'ingredients': [
                'Base:',
                '14 oz firm tofu, crumbled',
                '2 tablespoons vegetable oil',
                '3 shallots, thinly sliced',
                'Sauce:',
                '3 tablespoons lime juice',
                '2 tablespoons fish sauce',
                '1 Thai chili, minced (adjust to taste)',
                'For Serving:',
                '1/2 cup fresh mint leaves',
                '1/2 cup fresh cilantro leaves',
                '2 tablespoons toasted rice powder',
                'Butter lettuce leaves or steamed rice'
            ],
            'allergens': ['soy', 'fish'],
            'instructions': 'Heat oil in a large skillet over medium-high heat. Cook crumbled tofu until golden, about 8-10 minutes. Mix sauce ingredients in a bowl. Combine with cooked tofu, herbs, and rice powder. Serve with lettuce cups or over rice.',
            'source': 'https://cooking.nytimes.com/topics/dinner-recipes',
            'servings': 'Serves 4'
        },
        {
            'name': 'Easy Weeknight Pasta',
            'ingredients': [
                'Base:',
                '1 pound spaghetti or linguine',
                '1/3 cup extra virgin olive oil',
                '6 cloves garlic, thinly sliced',
                '1/2 teaspoon red pepper flakes',
                'For Serving:',
                '1 cup freshly grated Parmesan cheese',
                '1/2 cup fresh parsley, chopped',
                'Salt and black pepper to taste'
            ],
            'allergens': ['gluten', 'dairy'],
            'instructions': 'Cook pasta in salted water according to package directions. Meanwhile, heat oil over medium heat, add garlic and pepper flakes, cook until garlic is golden (2-3 minutes). Toss cooked pasta with oil mixture, cheese, and parsley. Season with salt and pepper.',
            'source': 'https://cooking.nytimes.com/68861692-nyt-cooking/1604305-easy-weeknight-dinners',
            'servings': 'Serves 4-6'
        },
        {
            'name': 'Roasted Kabocha Squash',
            'ingredients': [
                'Squash:',
                '1 medium kabocha squash (about 3 pounds), seeded and cut into 1-inch wedges',
                '2 tablespoons olive oil',
                'Sauce:',
                '2 tablespoons maple syrup',
                '1 tablespoon soy sauce',
                '1 tablespoon grated fresh ginger',
                'For Serving:',
                '2 tablespoons sesame seeds, toasted',
                '3 scallions, thinly sliced',
                'Salt to taste'
            ],
            'allergens': ['soy'],
            'instructions': 'Preheat oven to 425°F. Toss squash with oil and salt. Roast for 25-30 minutes until tender. Mix maple syrup, soy sauce, and ginger. Drizzle over roasted squash. Top with sesame seeds and scallions.',
            'source': 'https://www.bonappetit.com/recipes/slideshow/fast-easy-weeknight-dinner-recipes-ideas',
            'servings': 'Serves 4'
        },
        {
            'name': 'Spicy Salmon Rice Bowl',
            'ingredients': [
                'Rice Base:',
                '2 cups sushi rice',
                '2 1/2 cups water',
                'Salmon:',
                '1 pound salmon fillet',
                '2 tablespoons gochugaru (Korean red pepper flakes)',
                '2 tablespoons sesame oil',
                'For Serving:',
                '2 sheets nori, cut into strips',
                '1 English cucumber, thinly sliced',
                '1 ripe avocado, sliced',
                'Sesame seeds for garnish'
            ],
            'allergens': ['fish'],
            'instructions': 'Cook rice according to package directions. Season salmon with salt and gochugaru. Heat sesame oil in a pan over medium-high heat. Cook salmon 4-5 minutes per side. Serve over rice with cucumber, avocado, nori, and sesame seeds.',
            'source': 'https://www.bonappetit.com/gallery/22-weeknight-dinners-ba-editors-make-again-and-again',
            'servings': 'Serves 4'
        },
        {
            'name': 'Sheet-Pan Gnocchi',
            'ingredients': [
                'Base:',
                '1 pound shelf-stable potato gnocchi',
                '2 pints cherry tomatoes',
                '4 cloves garlic, thinly sliced',
                '1/4 cup olive oil',
                'For Serving:',
                '1/2 cup fresh basil leaves, torn',
                '1/2 cup freshly grated parmesan cheese',
                'Salt and black pepper to taste'
            ],
            'allergens': ['gluten', 'dairy'],
            'instructions': 'Preheat oven to 425°F. On a large sheet pan, toss gnocchi, tomatoes, and garlic with oil, salt, and pepper. Roast 20-25 minutes, stirring halfway through, until gnocchi is crispy and tomatoes burst. Top with basil and cheese.',
            'source': 'https://tasty.co/article/jesseszewczyk/back-to-school-dinner-recipes',
            'servings': 'Serves 4'
        },
        {
            'name': 'Healthy Chicken Fajitas',
            'ingredients': [
                'Chicken:',
                '1 1/2 pounds chicken breast, sliced',
                '2 tablespoons fajita seasoning',
                'Vegetables:',
                '3 bell peppers, sliced',
                '2 large onions, sliced',
                '2 tablespoons olive oil',
                'For Serving:',
                '8-10 flour tortillas, warmed',
                '2 avocados, sliced',
                '2 limes, cut into wedges',
                'Sour cream (optional)'
            ],
            'allergens': ['gluten'],
            'instructions': 'Season chicken with fajita seasoning. Heat oil in a large skillet over high heat. Cook chicken 5-6 minutes until done, remove. Cook peppers and onions in same pan 6-8 minutes. Return chicken to pan, toss together. Serve in warm tortillas with avocado and lime.',
            'source': 'https://tasty.co/article/michelleno/easy-healthy-dinner-recipes',
            'servings': 'Serves 4-5'
        },
        {
            'name': 'Edamame Shiitake Dumplings',
            'ingredients': [
                'Filling:',
                '8 oz shiitake mushrooms, finely chopped',
                '2 cups shelled edamame, cooked and mashed',
                '4 scallions, finely chopped',
                '2 tablespoons chili crisp',
                'Wrapper:',
                '1 package round rice paper wrappers',
                '1/4 cup all-purpose flour (for dusting)',
                'Sides:',
                '4 baby bok choy, halved',
                '2 tablespoons avocado oil',
                '2 tablespoons black vinegar for serving'
            ],
            'allergens': ['gluten', 'soy'],
            'instructions': 'Mix filling ingredients. Wet rice paper, fill and fold dumplings. Heat oil in a non-stick pan, place dumplings and create crispy skirt with flour-water slurry. Cook bok choy separately. Serve with black vinegar.',
            'source': 'https://justinesnacks.com/edamame-shitake-dumplings/',
            'servings': 'Makes 20-24 dumplings'
        },
        {
            'name': 'Twice-Baked Japanese Sweet Potatoes',
            'ingredients': [
                'Base:',
                '4 medium Japanese sweet potatoes',
                '2 tablespoons olive oil',
                'Filling:',
                '2 tablespoons white miso paste',
                '1/2 cup skyr or Greek yogurt',
                '2 tablespoons maple syrup',
                'Salt to taste'
            ],
            'allergens': ['dairy', 'soy'],
            'instructions': 'Preheat oven to 400°F. Rub potatoes with oil, bake 45-60 minutes until tender. Cut in half, scoop out interior leaving a thin shell. Mix potato with miso, yogurt, and maple syrup. Restuff shells and bake 15-20 minutes until tops are caramelized.',
            'source': 'https://justinesnacks.com/twice-baked-japanese-sweet-potatoes/',
            'servings': 'Serves 4'
        },
        {
            'name': 'Kale Tahini Pasta',
            'ingredients': [
                'Sauce:',
                '2 bunches kale, stems removed',
                '1/2 cup tahini',
                '1 teaspoon dried oregano',
                '1 teaspoon ground coriander',
                '1 teaspoon ground cumin',
                '1 lemon, juiced',
                'Base:',
                '1 pound pasta of choice',
                '1/4 cup olive oil',
                'For Serving:',
                '1 teaspoon red pepper flakes',
                '2 tablespoons sesame seeds, toasted'
            ],
            'allergens': ['gluten', 'sesame'],
            'instructions': 'Blanch kale in salted water for 3 minutes, shock in ice water. Blend with tahini and seasonings until smooth. Cook pasta, reserve 1 cup pasta water. Toss pasta with sauce, adding pasta water as needed. Top with pepper flakes and sesame seeds.',
            'source': 'https://justinesnacks.com/kale-tahini-pasta/',
            'servings': 'Serves 4-6'
        },
        {
            'name': 'Arugula Orzo with Feta & Mint',
            'ingredients': [
                'Sauce:',
                '4 cups packed arugula',
                '1 cup fresh parsley',
                '3 cloves garlic',
                '1 lemon, zested and juiced',
                '1/2 cup olive oil',
                'Base:',
                '1 pound orzo pasta',
                '2 cups English peas, fresh or frozen',
                'For Serving:',
                '1 cup crumbled feta cheese',
                '1/4 cup fresh mint leaves',
                'Salt and black pepper to taste'
            ],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Cook orzo according to package directions, adding peas in last 2 minutes. Meanwhile, blend arugula, parsley, garlic, lemon, and oil until smooth. Toss hot orzo and peas with sauce. Top with feta and mint.',
            'source': 'https://justinesnacks.com/arugula-orzo-with-feta-lemon-mint/',
            'servings': 'Serves 6'
        },
        {
            'name': 'Pasta al Limone',
            'ingredients': [
                'Base:',
                '1 pound spaghetti',
                '1/2 cup (1 stick) unsalted butter',
                '2 lemons, zested and juiced',
                '4 cloves garlic, minced',
                'For Serving:',
                '1 cup freshly grated Parmigiano-Reggiano',
                'Freshly ground black pepper',
                'Salt to taste'
            ],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Cook pasta in well-salted water. Reserve 1 cup pasta water. In a large skillet, melt butter with lemon zest and garlic over medium heat. Add pasta, cheese, and 1/2 cup pasta water, tossing until creamy. Add lemon juice to taste, using more pasta water if needed.',
            'source': 'https://www.seriouseats.com/pasta-al-limone',
            'servings': 'Serves 4'
        },
        {
            'name': 'Slow-Cooked Bolognese Sauce',
            'ingredients': [
                'Meat Base:',
                '1 pound ground beef (80/20)',
                '4 oz pancetta, finely diced',
                'Vegetables:',
                '1 large onion, finely diced',
                '2 carrots, finely diced',
                '2 celery stalks, finely diced',
                '4 cloves garlic, minced',
                'Sauce:',
                '1 (28 oz) can whole peeled tomatoes',
                '1 cup whole milk',
                '1 cup dry white wine',
                '2 bay leaves',
                'Salt and pepper to taste'
            ],
            'allergens': ['dairy'],
            'instructions': 'Brown meat in a large pot over medium-high heat. Add vegetables, cook until softened (8-10 minutes). Add wine, reduce by half. Add milk, simmer 5 minutes. Add tomatoes and bay leaves. Reduce heat to low and simmer 4-6 hours, stirring occasionally. Season to taste.',
            'source': 'https://www.seriouseats.com/the-best-slow-cooked-bolognese-sauce-recipe',
            'servings': 'Serves 6-8'
        },
        {
            'name': 'One-Pot Lemon Garlic Shrimp Pasta',
            'ingredients': [
                '1 pound linguine pasta',
                '1 pound large shrimp, peeled and deveined',
                '6 cloves garlic, minced',
                '2 lemons (1 zested and juiced, 1 sliced for serving)',
                '1/2 cup dry white wine',
                '4 tablespoons unsalted butter',
                '1/4 cup extra virgin olive oil',
                '1/2 teaspoon red pepper flakes',
                '1/2 cup freshly grated Parmesan cheese',
                '1/4 cup fresh parsley, chopped',
                '4 cups chicken or vegetable broth',
                'Salt and black pepper to taste'
            ],
            'allergens': ['shellfish', 'dairy', 'gluten'],
            'instructions': 'In a large pot, combine pasta, shrimp, garlic, lemon, wine, butter, oil, and red pepper flakes. Add broth and bring to boil. Cook 8-10 minutes until pasta is al dente and shrimp is pink. Stir in Parmesan and parsley. Season to taste.',
            'source': 'https://www.seriouseats.com/one-pot-lemon-garlic-shrimp-pasta',
            'servings': 'Serves 4-6'
        },
        {
            'name': 'Herb-Crusted Rack of Lamb',
            'ingredients': [
                'Lamb:',
                '2 racks of lamb (8 ribs each), frenched',
                '2 tablespoons olive oil',
                '2 teaspoons kosher salt',
                '1 teaspoon black pepper',
                'Herb Crust:',
                '1 cup fresh breadcrumbs',
                '4 cloves garlic, minced',
                '1/4 cup fresh rosemary, finely chopped',
                '1/4 cup fresh thyme leaves',
                '2 tablespoons fresh parsley, chopped',
                '2 tablespoons Dijon mustard',
                '2 tablespoons olive oil',
                'Sauce:',
                '1 cup red wine',
                '2 cups beef stock',
                '2 tablespoons butter',
                'Salt and pepper to taste'
            ],
            'allergens': ['gluten', 'dairy'],
            'instructions': 'Season lamb with salt and pepper. Sear in hot pan until browned. Mix herb crust ingredients. Brush lamb with mustard, press on herb mixture. Roast at 375°F for 25-30 minutes for medium-rare. Rest 10 minutes. Meanwhile, make red wine sauce by reducing wine and stock, finish with butter.',
            'source': 'https://www.seriouseats.com/herb-crusted-rack-of-lamb-recipe',
            'servings': 'Serves 4-6'
        },
        {
            'name': 'Caramelized Onion and Mushroom Pasta',
            'ingredients': [
                'Pasta:',
                '1 pound fettuccine or pappardelle pasta',
                'Sauce:',
                '3 large yellow onions, thinly sliced',
                '1 pound mixed mushrooms (cremini, shiitake, oyster), sliced',
                '4 tablespoons butter',
                '2 tablespoons olive oil',
                '4 cloves garlic, minced',
                '2 tablespoons fresh thyme leaves',
                '1/2 cup dry white wine',
                '1 cup vegetable or chicken broth',
                '1/2 cup heavy cream',
                '1 cup freshly grated Parmesan cheese',
                '2 tablespoons fresh parsley, chopped',
                'Salt and black pepper to taste',
                'For Serving:',
                'Additional Parmesan cheese',
                'Fresh thyme sprigs',
                'Red pepper flakes (optional)'
            ],
            'allergens': ['dairy', 'gluten'],
            'instructions': 'Caramelize onions in butter and oil over medium-low heat, 30-40 minutes. Add mushrooms, increase heat and cook until golden. Add garlic and thyme. Deglaze with wine, add broth and cream. Cook pasta, toss with sauce. Finish with Parmesan and parsley.',
            'source': 'https://www.seriouseats.com/caramelized-onion-mushroom-pasta',
            'servings': 'Serves 4-6'
        },
        {
            'name': 'Harissa Roasted Chicken',
            'ingredients': [
                'Chicken:',
                '1 whole chicken (4-5 pounds)',
                '2 tablespoons olive oil',
                '3 tablespoons harissa paste',
                '2 tablespoons honey',
                '4 cloves garlic, minced',
                '1 lemon, zested and halved',
                '2 teaspoons kosher salt',
                '1 teaspoon ground cumin',
                '1 teaspoon ground coriander',
                'Vegetables:',
                '1 pound baby potatoes, halved',
                '2 large carrots, cut into 2-inch pieces',
                '1 large red onion, cut into wedges',
                '2 tablespoons olive oil',
                '1 teaspoon kosher salt',
                'For Serving:',
                '1/4 cup fresh cilantro, chopped',
                '1/4 cup fresh mint, chopped',
                'Greek yogurt (optional)',
                'Additional harissa for serving'
            ],
            'allergens': ['dairy'],
            'instructions': 'Mix harissa, honey, garlic, lemon zest, and spices. Rub all over chicken, including under skin. Toss vegetables with oil and salt. Arrange in roasting pan, place chicken on top. Roast at 425°F for 1 hour or until chicken registers 165°F. Rest 10 minutes before carving.',
            'source': 'https://www.seriouseats.com/harissa-roasted-chicken-recipe',
            'servings': 'Serves 4-6'
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
            max-height: 1000px !important;
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
        div[data-baseweb="popover"],
        div[data-baseweb="menu"],
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
