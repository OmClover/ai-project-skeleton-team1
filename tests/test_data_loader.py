import os
import pytest
from src.data_loader import load_csv

def test_load_csv_success():
    """Tests that load_csv correctly parses a standard CSV file."""
    test_filename = "test_mock_data.csv"
    
    # 1. Create a temporary mock CSV file
    with open(test_filename, mode='w', encoding='utf-8') as f:
        f.write("name,age,role\n")
        f.write("Alice,24,Engineer\n")
        f.write("Bob,30,Designer\n")
        
    try:
        # 2. Run your loader function
        result = load_csv(test_filename)
        
        # 3. Assertions to confirm success
        assert len(result) == 2
        assert result[0]["name"] == "Alice"
        assert result[0]["role"] == "Engineer"
        assert result[1]["age"] == "30"
        
    finally:
        # 4. Clean up the file after testing
        if os.path.exists(test_filename):
            os.remove(test_filename)

def test_load_csv_missing_file():
    """Tests that load_csv properly raises FileNotFoundError for missing paths."""
    with pytest.raises(FileNotFoundError):
        load_csv("non_existent_file.csv")