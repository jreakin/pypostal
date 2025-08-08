#!/usr/bin/env python3
"""
Test script for pypostal functionality
"""

def test_expand_address():
    """Test address expansion functionality"""
    from postal.expand import expand_address
    
    # Test French address
    result = expand_address('Quatre vingt douze Ave des Champs-Élysées')
    assert len(result) > 0, "Should return at least one expansion"
    assert '92 avenue des champs-elysees' in result, "Should normalize French address"
    print("✓ Address expansion test passed")

def test_parse_address():
    """Test address parsing functionality"""
    from postal.parser import parse_address
    
    # Test complex address
    result = parse_address('The Book Club 100-106 Leonard St, Shoreditch, London, Greater London, EC2A 4RH, United Kingdom')
    assert len(result) > 0, "Should return parsed components"
    
    # Check that we get expected labels
    labels = [label for _, label in result]
    assert 'house_number' in labels, "Should identify house number"
    assert 'road' in labels, "Should identify road"
    assert 'city' in labels, "Should identify city"
    assert 'postcode' in labels, "Should identify postcode"
    print("✓ Address parsing test passed")

def test_normalize_string():
    """Test string normalization functionality"""
    from postal.normalize import normalize_string
    
    # Test normalization
    result = normalize_string('123 Fourth Ave')
    assert result == '123 fourth ave', f"Expected '123 fourth ave', got '{result}'"
    print("✓ String normalization test passed")

def test_tokenize():
    """Test tokenization functionality"""
    from postal.tokenize import tokenize
    
    # Test tokenization
    result = tokenize('123 Main Street')
    assert len(result) > 0, "Should return tokens"
    print("✓ Tokenization test passed")

if __name__ == "__main__":
    print("Running pypostal tests...\n")
    
    try:
        test_expand_address()
        test_parse_address()
        test_normalize_string()
        test_tokenize()
        print("\n🎉 All tests passed!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        exit(1)
