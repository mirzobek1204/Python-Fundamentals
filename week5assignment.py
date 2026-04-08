print("RETAIL SALES PERFORMANCE SYSTEM")

def calculate_revenue_generated(product_category, units_sold, price_tier):
    if product_category == "electronics"and price_tier == "low":
        
            price_per_unit = 45
    elif price_tier == "medium":
            price_per_unit = 75
    elif price_tier == "high":
            price_per_unit = 120

    elif product_category == "clothing":
        if price_tier == "low":
            price_per_unit = 25
        elif price_tier == "medium":
            price_per_unit = 40
        elif price_tier == "high":
            price_per_unit = 65

    elif product_category == "accessories":
        if price_tier == "low":
            price_per_unit = 15
        elif price_tier == "medium":
            price_per_unit = 25
        elif price_tier == "high":
            price_per_unit = 35

    total_revenue = units_sold * price_per_unit
    return total_revenue

# Calculate expected sales: 1000 + (experience_years * 100)
# Calculate sales capacity: expected_sales - baseline_sales
# Calculate performance percentage: (actual_sales - baseline_sales) / sales_capacity * 100
# Return the performance percentage

def calculate_performance_ratio(experience_years, baseline_sales, actual_sales):
    expected_sales = 1000 + (experience_years * 100)
    sales_capacity = expected_sales - baseline_sales
    performance_percent = (actual_sales - baseline_sales) / sales_capacity * 100
    return round(performance_percent, 1)
# Below 50%: “Developing Level”
# 50-60%: “Competent Level”
# 60-70%: “Proficient Level”
# 70-85%: “Advanced Level”
# Above 85%: “Expert Level”

def determine_achievement_level(performance_percent):
    if performance_percent < 50:
        return "Developing Level"
    elif performance_percent < 60:
        return "Competent Level"
    elif performance_percent < 70:
        return "Proficient Level"
    elif performance_percent < 85:
        return "Advanced Level"
    else:
        return "Expert Level"


def calculate_commission_earned(revenue, units, level):
    base_commission = revenue * 0.05 + (units * 2)

    if level == "Developing Level":
        multiplier = 0.5
    elif level == "Competent Level":
        multiplier = 1.0
    elif level == "Proficient Level":
        multiplier = 1.2
    elif level == "Advanced Level":
        multiplier = 1.5
    elif level == "Expert Level":
        multiplier = 1.8

    final_commission = base_commission * multiplier
    return round(final_commission, 1)


def needs_training_support(consecutive_months, total_units, avg_performance):
    if consecutive_months >= 6 and avg_performance < 50:
        return True
    elif total_units < 100 and avg_performance < 60:
        return True
    elif consecutive_months >= 4 and avg_performance < 40:
        return True
    else:
        return False


def generate_sales_report(employee, product_category, units, price_tier, experience_years, baseline_sales, actual_sales, consecutive_months):
   
    revenue = calculate_revenue_generated(product_category, units, price_tier)
    performance = calculate_performance_ratio(experience_years, baseline_sales, actual_sales)
    achievement = determine_achievement_level(performance)
    commission = calculate_commission_earned(revenue, units, achievement)
    training_needed = needs_training_support(consecutive_months, units, performance)

    print("=" * 45)
    print(f"Sales Report for:{employee}")
    print("-" * 45)
    print(f"Product Category: {product_category}")
    print(f"Units Sold:{units}")
    print(f"Price Tier:{price_tier}")
    print(f"Revenue Generated:${revenue}")
    print("Performance Analysis:")
    print(f"  Experience:{experience_years} years")
    print(f"  Baseline Sales:{baseline_sales}")
    print(f"  Actual Sales:{actual_sales}")
    print(f"  Performance:{performance}%")
    print(f"  Achievement Level:{achievement}")
    print(f"Commission Earned:${commission}")
    print(f"Consecutive Months:{consecutive_months}")
    print(f"Training Support Needed: {'Yes' if training_needed else 'No'}")
    print()



generate_sales_report("Blake", "electronics", 45, "high", 3, 800, 1150, 3)
generate_sales_report("Dana", "clothing", 60, "medium", 5, 900, 1300, 5)
generate_sales_report("Finley", "accessories", 30, "low", 8, 850, 950, 7)

print("=" * 40)


