def score(row):
    if row['event_count'] > 150 or row['login_freq_drop'] > 50:
        return "High"
    elif row['event_count'] > 75 or row['login_freq_drop'] > 30:
        return "Medium"
    else:
        return "Low"

