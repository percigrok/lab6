def calculate_laminate(area, plank_area, plank_price):
    planks_needed = area / plank_area
    planks_needed = int(planks_needed) + (planks_needed % 1 > 0)  # Округляем в большую сторону
    total_cost = planks_needed * plank_price
    return planks_needed, total_cost