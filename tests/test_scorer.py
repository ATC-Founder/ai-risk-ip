from models.scorer import score

def test_high_risk():
    row = {'event_count': 200, 'login_freq_drop': 10}
    assert score(row) == "High"

def test_medium_risk():
    row = {'event_count': 80, 'login_freq_drop': 20}
    assert score(row) == "Medium"

def test_low_risk():
    row = {'event_count': 30, 'login_freq_drop': 10}
    assert score(row) == "Low"

