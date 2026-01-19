from modules.password_generator import PasswordGenerator

pg = PasswordGenerator()

# Test with parameters the GUI will use
print("Testing PasswordGenerator with GUI parameters...")
print("=" * 50)

# Test 1: All options enabled
try:
    pw1 = pg.generate(length=12, use_lower=True, use_upper=True, 
                      use_digits=True, use_special=True)
    print(f" Test 1 (all options): {pw1}")
except Exception as e:
    print(f" Test 1 failed: {e}")

# Test 2: Only lowercase and digits
try:
    pw2 = pg.generate(length=10, use_lower=True, use_upper=False,
                      use_digits=True, use_special=False)
    print(f" Test 2 (lower+digits): {pw2}")
except Exception as e:
    print(f" Test 2 failed: {e}")

# Test 3: Memorable password
try:
    pw3 = pg.generate_memorable(word_count=3)
    print(f" Test 3 (memorable): {pw3}")
except Exception as e:
    print(f" Test 3 failed: {e}")

print("=" * 50)
print("All tests completed!")
