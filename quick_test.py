print("Testing basic imports...")
print("=" * 50)

tests = [
    ("WiFiScanner", "wifi_scanner"),
    ("BreachChecker", "breach_checker"),
    ("PasswordGenerator", "password_generator"),
    ("ReportGenerator", "report_generator"),
]

for class_name, module_name in tests:
    try:
        exec(f"from modules.{module_name} import {class_name}")
        print(f" {class_name} imported successfully")
    except Exception as e:
        print(f" {class_name} failed: {e}")

print("=" * 50)
