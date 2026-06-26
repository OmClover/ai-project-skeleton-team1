# src/preprocess.py
def clean_data(records):
    """Removes empty rows and strips whitespace from all string fields."""
    cleaned = []
    for row in records:
        if not row or all(value.strip() == "" for value in row.values()):
            continue
        cleaned_row = {k: v.strip() if isinstance(v, str) else v for k, v in row.items()}
        cleaned.append(cleaned_row)
    return cleaned
