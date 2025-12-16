# Total land and segments
total_land = 80
segments = 5
land_per_segment = total_land / segments  # 16 acres each

# ---------------- TOMATOES ----------------
tomato_land = land_per_segment
tomato_yield_30 = 0.30 * tomato_land * 10      # tonnes
tomato_yield_70 = 0.70 * tomato_land * 12      # tonnes
total_tomato_yield = tomato_yield_30 + tomato_yield_70  # tonnes
tomato_sales = total_tomato_yield * 1000 * 7   # Rs (kg × price)

# ---------------- POTATOES ----------------
potato_yield = land_per_segment * 10           # tonnes
potato_sales = potato_yield * 1000 * 20        # Rs

# ---------------- CABBAGE ----------------
cabbage_yield = land_per_segment * 14           # tonnes
cabbage_sales = cabbage_yield * 1000 * 24       # Rs

# ---------------- SUNFLOWER ----------------
sunflower_yield = land_per_segment * 0.7        # tonnes
sunflower_sales = sunflower_yield * 1000 * 200  # Rs

# ---------------- SUGARCANE ----------------
sugarcane_yield = land_per_segment * 45         # tonnes
sugarcane_sales = sugarcane_yield * 4000        # Rs (per tonne)

# (a) Overall sales
overall_sales = (tomato_sales + potato_sales +
                 cabbage_sales + sunflower_sales +
                 sugarcane_sales)

# (b) Chemical-free sales after 11 months
# Vegetables + Sunflower only
chemical_free_sales = (tomato_sales + potato_sales +
                        cabbage_sales + sunflower_sales)

# Display results
print("Overall Sales from 80 acres: Rs.", overall_sales)
print("Chemical-free farming sales after 11 months: Rs.", chemical_free_sales)
