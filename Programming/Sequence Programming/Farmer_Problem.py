def tomato_sales(acres):
    area_30 = acres * 0.30
    area_70 = acres * 0.70

    yield_30 = area_30 * 10 * 1000   # kg
    yield_70 = area_70 * 12 * 1000   # kg

    total_kg = yield_30 + yield_70
    return total_kg * 7


def crop_sales(acres, yield_per_acre, price_per_kg):
    total_kg = acres * yield_per_acre * 1000
    return total_kg * price_per_kg


def sugarcane_sales(acres):
    total_tonnes = acres * 45
    return total_tonnes * 4000


if __name__ == "__main__":
    acres_per_crop = 16

    tomato = tomato_sales(acres_per_crop)
    potato = crop_sales(acres_per_crop, 10, 20)
    cabbage = crop_sales(acres_per_crop, 14, 24)
    sunflower = crop_sales(acres_per_crop, 0.7, 200)
    sugarcane = sugarcane_sales(acres_per_crop)

    # a. Overall sales
    total_sales = tomato + potato + cabbage + sunflower + sugarcane

    # b. Chemical-free sales at 11 months (excluding sugarcane)
    chemical_free_sales = tomato + potato + cabbage + sunflower

    print("Overall Sales from 80 acres = Rs.", total_sales)
    print("Chemical-Free Sales after 11 months = Rs.", chemical_free_sales)
