#!/usr/bin/env python3
"""
GRAE-X SENTINEL PRO - Main Launcher
Launch GUI or CLI based on arguments
"""

import sys
import os
import argparse
from pathlib import Path

def display_banner():
    """Display ASCII banner"""
    banner = """
    
                                                                  
                     
                 
                         
                          
                         
                           
                                                                  
                 S E N T I N E L   P R O   v4.0                   
          Complete Cybersecurity Suite - GUI & CLI                
                                                                  
    
    """
    print("\033[96m" + banner + "\033[0m")
    print("\033[92m" + "="*70 + "\033[0m")
    print("\033[93m Advanced Password & WiFi Security Tool with Beautiful GUI \033[0m")
    print("\033[92m" + "="*70 + "\033[0m\n")

def main():
    """Main launcher function"""
    parser = argparse.ArgumentParser(
        description="Grae-X Sentinel Pro - Complete Cybersecurity Suite",
        epilog="Examples:\n  grae_x_sentinel.py gui    (Launch GUI)\n  grae_x_sentinel.py cli    (Launch CLI)"
    )

    parser.add_argument(
        'mode',
        nargs='?',
        default='gui',
        choices=['gui', 'cli'],
        help='Mode: gui (graphical), cli (command line)'
    )

    args = parser.parse_args()
    
    display_banner()
    
    if args.mode == 'gui':
        print("Launching Grae-X Sentinel Pro GUI...")
        print("-" * 70)
        
        # Try to import and run the fixed GUI
        try:
            # Add current directory to path
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            
            # Import the fixed GUI module
            from sentinel_gui_fixed import SentinelGUI
            
            # Run the application
            app = SentinelGUI()
            app.run()
            
        except ImportError as e:
            print(f" Error importing GUI module: {e}")
            print("Make sure sentinel_gui_fixed.py exists in the same directory.")
        except Exception as e:
            print(f" Error launching GUI: {e}")
            import traceback
            traceback.print_exc()
    
    elif args.mode == 'cli':
        print("CLI mode selected")
        print("Note: CLI interface is under development.")
        print("For now, use the GUI with: python grae_x_sentinel.py gui")
        
        # Simple CLI interface
        print("\nAvailable commands:")
        print("  scan    - Scan WiFi networks")
        print("  check   - Check password strength")
        print("  generate - Generate password")
        print("  exit    - Exit program")
        
        while True:
            try:
                command = input("\n> ").strip().lower()
                
                if command == 'scan':
                    print("Scanning WiFi networks...")
                    # Add WiFi scanning logic here
                    print("WiFi scan completed (CLI mode)")
                
                elif command == 'check':
                    password = input("Enter password to check: ")
                    print(f"Checking password: {password}")
                    # Add password checking logic here
                    print("Password check completed (CLI mode)")
                
                elif command == 'generate':
                    print("Generating password...")
                    # Add password generation logic here
                    print("Password: RandomPass123! (CLI mode)")
                
                elif command == 'exit':
                    print("Exiting Grae-X Sentinel Pro...")
                    break
                
                else:
                    print(f"Unknown command: {command}")
            
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
