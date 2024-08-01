def calculate_policy_price(original_policy_price, age, height, weight, does_smoke, does_drink, has_diabetes, had_any_surgery):
    """
    Calculate a new policy price based on various factors.

    Parameters:
    - original_policy_price (float): The base price of the policy.
    - age (int): Age of the policyholder.
    - height (float): Height of the policyholder in centimeters.
    - weight (float): Weight of the policyholder in kilograms.
    - does_smoke (bool): Whether the policyholder smokes.
    - does_drink (bool): Whether the policyholder consumes alcohol.
    - has_diabetes (bool): Whether the policyholder has diabetes.
    - had_any_surgery (bool): Whether the policyholder has had any surgery.

    Returns:
    - float: The new policy price.
    """

    age_factor = 0.05
    height_factor = 0.01
    weight_factor = 0.02
    smoke_factor = 0.1
    drink_factor = 0.05
    diabetes_factor = 0.15
    surgery_factor = 0.1

    age_adjustment = (age - 30) * age_factor if age > 30 else 0
    height_adjustment = (height - 170) * height_factor if height < 170 else 0
    weight_adjustment = (weight - 70) * weight_factor if weight > 70 else 0
    smoke_adjustment = smoke_factor if does_smoke else 0
    drink_adjustment = drink_factor if does_drink else 0
    diabetes_adjustment = diabetes_factor if has_diabetes else 0
    surgery_adjustment = surgery_factor if had_any_surgery else 0

    total_adjustment = age_adjustment + height_adjustment + weight_adjustment + smoke_adjustment + drink_adjustment + diabetes_adjustment + surgery_adjustment

    new_policy_price = original_policy_price * (1 + total_adjustment)

    return new_policy_price
