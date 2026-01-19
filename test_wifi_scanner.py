import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.wifi_scanner import WiFiScanner

scanner = WiFiScanner()
print("Testing WiFi Scanner...")
print("=" * 60)

networks = scanner.scan()
print(f"Number of networks: {len(networks)}")

if networks:
    print("\nFirst network keys and values:")
    print("-" * 40)
    for key, value in networks[0].items():
        print(f"{key}: {value}")
    
    print("\n" + "=" * 60)
    print("All networks:")
    print("-" * 40)
    for i, net in enumerate(networks, 1):
        print(f"\nNetwork {i}:")
        # Try to get values with fallback
        ssid = net.get('ssid') or net.get('SSID') or 'Unknown'
        security = net.get('security') or net.get('Security') or 'Unknown'
        signal = net.get('signal') or net.get('Signal') or 'Unknown'
        channel = net.get('channel') or net.get('Channel') or 'Unknown'
        
        print(f"  SSID: {ssid}")
        print(f"  Security: {security}")
        print(f"  Signal: {signal}")
        print(f"  Channel: {channel}")
