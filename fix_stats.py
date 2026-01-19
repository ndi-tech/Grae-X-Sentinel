import sys
import os

# Fix the sentinel_gui.py file
file_path = "sentinel_gui.py"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the __init__ method and add stats initialization
import re

# Look for the __init__ method and add stats after colors
init_pattern = r'def __init__\(self\):(.*?)self\.root = tk\.Tk\(\)'
match = re.search(init_pattern, content, re.DOTALL)

if match:
    init_content = match.group(1)
    
    # Check if stats is initialized
    if 'self.stats =' not in init_content:
        # Add stats initialization after colors
        colors_section = "self.colors = {"
        if colors_section in content:
            # Find where to insert stats after colors
            colors_end = content.find(colors_section) + len(colors_section)
            # Find the end of the colors dictionary
            brace_count = 0
            in_string = False
            escape_next = False
            for i in range(colors_end, len(content)):
                char = content[i]
                
                if escape_next:
                    escape_next = False
                    continue
                    
                if char == '\\':
                    escape_next = True
                    continue
                    
                if char == '"' or char == "'":
                    in_string = not in_string
                    continue
                    
                if not in_string:
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            # Found the end of colors dict
                            insert_pos = i + 1
                            # Add stats after colors
                            new_content = content[:insert_pos] + '\n\n        # Initialize stats\n        self.stats = {\n            \'passwords_analyzed\': 0,\n            \'networks_scanned\': 0,\n            \'breaches_found\': 0,\n            \'reports_generated\': 0\n        }\n        ' + content[insert_pos:]
                            
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            
                            print(" Fixed sentinel_gui.py - Added stats initialization")
                            break
else:
    print("Could not find __init__ method to fix")
