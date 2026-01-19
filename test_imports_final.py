print("Testing imports after fix...")
print("=" * 50)

imports_to_test = [
    ("modules.wifi_scanner", "WiFiScanner"),
    ("modules.breach_checker", "BreachChecker"),
    ("modules.password_generator", "PasswordGenerator"),
    ("modules.report_generator", "ReportGenerator"),
    ("modules.password_analyzer", "PasswordAnalyzer"),
]

for module_name, class_name in imports_to_test:
    try:
        exec(f"from {module_name} import {class_name}")
        print(f" {class_name} imported successfully")
    except ImportError as e:
        print(f" {class_name}: ImportError - {e}")
    except SyntaxError as e:
        print(f" {class_name}: SyntaxError - {e}")
    except Exception as e:
        print(f" {class_name}: {type(e).__name__} - {e}")

print("=" * 50)
