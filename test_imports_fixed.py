import sys
import os

print("Python Test Script")
print("=" * 50)

# Test WiFiScanner
try:
    from modules.wifi_scanner import WiFiScanner
    scanner = WiFiScanner()
    print(f" WiFiScanner: Success - {scanner}")
    networks = scanner.scan()
    print(f"   Found {len(networks)} networks")
except Exception as e:
    print(f" WiFiScanner: {e}")

# Test BreachChecker
try:
    from modules.breach_checker import BreachChecker
    checker = BreachChecker()
    print(f" BreachChecker: Success - {checker}")
except Exception as e:
    print(f" BreachChecker: {e}")

# Test PasswordGenerator
try:
    from modules.password_generator import PasswordGenerator
    generator = PasswordGenerator()
    print(f" PasswordGenerator: Success - {generator}")
    password = generator.generate()
    print(f"   Generated password: {password}")
except Exception as e:
    print(f" PasswordGenerator: {e}")

# Test ReportGenerator
try:
    from modules.report_generator import ReportGenerator
    reporter = ReportGenerator()
    print(f" ReportGenerator: Success - {reporter}")
except Exception as e:
    print(f" ReportGenerator: {e}")

print("=" * 50)
print("Test complete!")
