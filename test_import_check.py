import sys
print("Testing WiFiScanner import...")

# Simulate what the GUI does
try:
    from modules.wifi_scanner import WiFiScanner
    scanner = WiFiScanner()
    networks = scanner.scan()
    print(f" Using REAL WiFiScanner from modules")
    print(f"   Networks found: {len(networks)}")
    print(f"   First network: {networks[0] if networks else 'None'}")
except ImportError as e:
    print(f" Real import failed: {e}")
    print("   Using mock/fake WiFiScanner")
