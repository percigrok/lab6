def calculate_wallpapers(area, roll_coverage, roll_price):
    rolls_needed = area / roll_coverage
    rolls_needed = int(rolls_needed) + (rolls_needed % 1 > 0)  # Округляем в большую сторону
    total_cost = rolls_needed * roll_price
    return rolls_needed, total_cost