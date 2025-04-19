def calculate_tiles(area, tile_area, tile_price):
    tiles_needed = area / tile_area
    tiles_needed = int(tiles_needed) + (tiles_needed % 1 > 0)  # Округляем в большую сторону
    total_cost = tiles_needed * tile_price
    return tiles_needed, total_cost