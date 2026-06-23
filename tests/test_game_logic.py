from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_win_on_first_attempt_scores_90():
    # attempt_number is 1 on a first-attempt win: 100 - 10*1 = 90.
    # The original off-by-one (+1) wrongly produced 80.
    assert update_score(0, "Win", 1) == 90

def test_win_score_floors_at_10():
    # A very late win never drops below the 10-point floor.
    assert update_score(0, "Win", 20) == 10

def test_wrong_guess_subtracts_5():
    assert update_score(50, "Too High", 3) == 45
    assert update_score(50, "Too Low", 3) == 45
