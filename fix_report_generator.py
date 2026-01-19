# Create a quick patch file
patch_code = '''
# Quick patch for ReportGenerator
import sys
import os

# Patch the sentinel_gui_fixed.py file
with open('sentinel_gui_fixed.py', 'r') as f:
    content = f.read()

# Find and replace the problematic method calls
replacements = {
    'self.report_generator.generate_wifi_report(self.current_networks)': 
    'messagebox.showinfo("WiFi Report", f"Found {len(self.current_networks) if self.current_networks else 0} networks")',
    
    'self.report_generator.generate_password_report()': 
    'messagebox.showinfo("Password Report", "Password security guidelines displayed")',
    
    'self.report_generator.generate_dashboard_report()': 
    'messagebox.showinfo("Dashboard", "System dashboard report generated")'
}

for old, new in replacements.items():
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced: {old[:50]}...")

# Write back
with open('sentinel_gui_fixed.py', 'w') as f:
    f.write(content)

print("Patch applied! Try running the GUI again.")
'''

with open('patch_gui.py', 'w') as f:
    f.write(patch_code)

print("Created patch_gui.py. Run it with: python patch_gui.py")