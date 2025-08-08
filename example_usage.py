#!/usr/bin/env python3
"""
Pypostal Usage Examples

This demonstrates the main functionality of pypostal for address
parsing and normalization.
"""

from postal.expand import expand_address
from postal.parser import parse_address
from postal.normalize import normalize_string
from postal.tokenize import tokenize

def main():
    print("🏠 Pypostal Usage Examples")
    print("=" * 50)
    
    # Example 1: Address Expansion
    print("\n1. Address Expansion")
    print("-" * 20)
    addresses_to_expand = [
        "123 Main St",
        "Quatre vingt douze Ave des Champs-Élysées",
        "1600 Pennsylvania Ave NW"
    ]
    
    for addr in addresses_to_expand:
        print(f"Original: {addr}")
        expanded = expand_address(addr)
        for exp in expanded[:3]:  # Show first 3 expansions
            print(f"  → {exp}")
        print()
    
    # Example 2: Address Parsing
    print("2. Address Parsing")
    print("-" * 18)
    addresses_to_parse = [
        "123 Main Street, Anytown, CA 12345",
        "The White House, 1600 Pennsylvania Ave NW, Washington, DC 20500",
        "221B Baker Street, London, UK"
    ]
    
    for addr in addresses_to_parse:
        print(f"Address: {addr}")
        parsed = parse_address(addr)
        for component, label in parsed:
            print(f"  {label}: {component}")
        print()
    
    # Example 3: String Normalization
    print("3. String Normalization")
    print("-" * 22)
    strings_to_normalize = [
        "123 Fourth Avenue",
        "St. John's Street",
        "N.Y.C."
    ]
    
    for s in strings_to_normalize:
        normalized = normalize_string(s)
        print(f"{s} → {normalized}")
    
    # Example 4: Tokenization
    print("\n4. Tokenization")
    print("-" * 15)
    strings_to_tokenize = [
        "123 Main Street Apt 4B",
        "P.O. Box 1234"
    ]
    
    for s in strings_to_tokenize:
        tokens = tokenize(s)
        print(f"'{s}' → {tokens}")

if __name__ == "__main__":
    main()
