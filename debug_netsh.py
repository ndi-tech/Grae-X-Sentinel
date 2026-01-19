import subprocess
import platform

print("Testing netsh command parsing...")
print("=" * 60)

# Run netsh command
result = subprocess.run(
    ["netsh", "wlan", "show", "networks", "mode=bssid"],
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="ignore"
)

print(f"Return code: {result.returncode}")
print(f"Output length: {len(result.stdout)} chars")
print("\nFirst 500 characters of output:")
print("-" * 40)
print(result.stdout[:500])
print("-" * 40)

# Also test simple command
print("\n\nTesting simple netsh command...")
print("=" * 60)
result2 = subprocess.run(
    ["netsh", "wlan", "show", "networks"],
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="ignore"
)

print(f"Return code: {result2.returncode}")
print(f"Output length: {len(result2.stdout)} chars")
print("\nFirst 500 characters of output:")
print("-" * 40)
print(result2.stdout[:500])
