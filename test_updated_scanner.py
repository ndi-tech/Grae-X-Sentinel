import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.wifi_scanner import WiFiScanner

scanner = WiFiScanner()
print("Testing Updated WiFi Scanner...")
print("=" * 60)

networks = scanner.scan()
print(f"Number of networks found: {len(networks)}")

if networks:
    print("\nNetwork Details:")
    print("-" * 40)
    for i, net in enumerate(networks, 1):
        # Get values with fallback
        ssid = net.get('ssid') or net.get('SSID') or 'Unknown'
        security = net.get('security') or net.get('Security') or 'Unknown'
        signal = net.get('signal') or net.get('Signal') or 'Unknown'
        channel = net.get('channel') or net.get('Channel') or 'Unknown'
        bssid = net.get('bssid') or net.get('BSSID') or 'Unknown'
        
        print(f"\n{i}. {ssid}")
        print(f"   Security: {security}")
        print(f"   Signal: {signal}")
        print(f"   Channel: {channel}")
        print(f"   BSSID: {bssid}")
        
        # Show all keys for debugging
        if i == 1:
            print(f"\n   All keys in first network: {list(net.keys())}")
else:
    print("No networks found")

print("=" * 60)
