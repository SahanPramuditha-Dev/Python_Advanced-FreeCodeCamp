from unittest.mock import patch

inputs = ["name", "age"]

with patch("builtins.input", side_effect=inputs):
    print(input("Key 1: "))  # name
    print(input("Key 2: "))  # age