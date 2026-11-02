import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


# REWARD POINTS - BRANCH TESTS

def test_invalid_card_tier():
    with pytest.raises(ValueError):
        reward_points("silver", 1000, "grocery", False)

def test_invalid_amount():
    with pytest.raises(ValueError):
        reward_points("gold", -100, "grocery", False)

def test_fuel():
    assert reward_points("gold", 1000, "fuel", False) == 0

def test_grocery():
    assert reward_points("gold", 1000, "grocery", False) == 20

def test_dining():
    assert reward_points("gold", 1000, "dining", False) == 40

def test_travel():
    assert reward_points("gold", 1000, "travel", False) == 40

def test_weekend_gold():
    assert reward_points("gold", 1000, "grocery", True) == 70

def test_weekend_classic():
    assert reward_points("classic", 1000, "grocery", True) == 10


# LATE PAYMENT FEE - BRANCH TESTS

def test_no_days_late():
    assert late_payment_fee(5000, 0) == 0

def test_no_outstanding():
    assert late_payment_fee(0, 10) == 0

def test_fee_boundary_1000():
    assert late_payment_fee(1000, 10) == 100

def test_fee_boundary_1001():
    assert late_payment_fee(1001, 10) == 500

def test_fee_boundary_10000():
    assert late_payment_fee(10000, 10) == 500

def test_fee_above_10000():
    assert late_payment_fee(10001, 10) == 1000

def test_exactly_30_days():
    assert late_payment_fee(5000, 30) == 500

def test_above_30_days():
    assert late_payment_fee(5000, 31) == 1250


# CARD STATUS - BRANCH TESTS

def test_frozen():
    assert card_status(95, 3, True) == "frozen"

def test_blocked():
    assert card_status(50, 3, False) == "blocked"

def test_over_limit():
    assert card_status(91, 0, False) == "over limit risk"

def test_exactly_90_percent():
    assert card_status(90, 0, False) == "watch"

def test_exactly_30_percent():
    assert card_status(30, 0, False) == "good"

def test_below_30_percent():
    assert card_status(20, 0, False) == "good"

def test_missed_payment_watch():
    assert card_status(20, 1, False) == "watch"

def test_good_status():
    assert card_status(10, 0, False) == "good"