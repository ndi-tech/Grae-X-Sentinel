print("=== Testing Module Imports ===")
print()

# Test WiFiScanner
try:
    from modules.wifi_scanner import WiFiScanner
    scanner = WiFiScanner()
    print(f" WiFiScanner: Success")
    print(f"   Sample scan: {scanner.scan()[:1]}")  # Show first network
except Exception as e:
    print(f" WiFiScanner: {type(e).__name__}: {e}")

print()

# Test BreachChecker
try:
    from modules.breach_checker import BreachChecker
    checker = BreachChecker()
    print(f" BreachChecker: Success")
except Exception as e:
    print(f" BreachChecker: {type(e).__name__}: {e}")

print()

# Test PasswordGenerator
try:
    from modules.password_generator import PasswordGenerator
    generator = PasswordGenerator()
    password = generator.generate()
    print(f" PasswordGenerator: Success")
    print(f"   Generated: {password}")
except Exception as e:
    print(f" PasswordGenerator: {type(e).__name__}: {e}")

print()

# Test ReportGenerator
try:
    from modules.report_generator import ReportGenerator
    reporter = ReportGenerator()
    print(f" ReportGenerator: Success")
except Exception as e:
    print(f" ReportGenerator: {type(e).__name__}: {e}")

print()
print("=" * 40)
