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
    """Display beautiful ASCII banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    ██████╗ ██████╗  █████╗ ███████╗   ███████╗███████╗      ║
    ║   ██╔════╝ ██╔══██╗██╔══██╗██╔════╝   ██╔════╝╚══███╔╝      ║
    ║   ██║  ███╗██████╔╝███████║█████╗     █████╗    ███╔╝       ║
    ║   ██║   ██║██╔══██╗██╔══██║██╔══╝     ██╔══╝   ███╔╝        ║
    ║   ╚██████╔╝██║  ██║██║  ██║██║        ███████╗███████╗      ║
    ║    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚══════╝╚══════╝      ║
    ║                                                              ║
    ║             S E N T I N E L   P R O   v4.0                   ║
    ║      Complete Cybersecurity Suite - GUI & CLI                ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print("\033[96m" + banner + "\033[0m")
    print("\033[92m" + "="*70 + "\033[0m")
    print("\033[93m Advanced Password & WiFi Security Tool with Beautiful GUI \033[0m")
    print("\033[92m" + "="*70 + "\033[0m\n")

def main():
    """Main launcher function"""
    parser = argparse.ArgumentParser(
        description="Grae-X Sentinel Pro - Complete Cybersecurity Suite",
        epilog="Examples:\n  grae_x_sentinel.py gui    (Launch GUI)\n  grae_x_sentinel.py cli    (Launch CLI)\n  grae_x_sentinel.py check \"mypassword\""
    )
    
    parser.add_argument(
        'mode',
        nargs='?',
        default='gui',
        choices=['gui', 'cli', 'check', 'scan', 'generate', 'report'],
        help='Mode: gui (graphical), cli (command line), check (password), scan (wifi), generate (password), report (security)'
    )
    
    parser.add_argument(
        'args',
        nargs='*',
        help='Additional arguments for the mode'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Display banner
    display_banner()
    
    # Launch appropriate mode
    if args.mode == 'gui':
        try:
            from sentinel_gui import SentinelGUI
            app = SentinelGUI()
            app.run()
        except ImportError as e:
            print(f"\n❌ Error: {e}")
            print("Make sure all modules are installed: pip install -r requirements.txt")
    
    elif args.mode == 'cli':
        try:
            from sentinel_cli import SentinelCLI
            cli = SentinelCLI()
            cli.run()
        except ImportError as e:
            print(f"\n❌ Error: {e}")
            print("Make sure all modules are installed: pip install -r requirements.txt")
    
    elif args.mode == 'check' and args.args:
        from modules.password_analyzer import PasswordAnalyzer
        analyzer = PasswordAnalyzer()
        result = analyzer.analyze(args.args[0])
        print(f"\nPassword: {'*' * len(args.args[0])}")
        print(f"Strength: {result['strength']} ({result['score']}/100)")
        print(f"Length: {result['length']} characters")
    
    elif args.mode == 'scan':
        from modules.wifi_scanner import WiFiScanner
        scanner = WiFiScanner()
        networks = scanner.scan()
        print(f"\nFound {len(networks)} networks")
    
    elif args.mode == 'generate':
        from modules.password_generator import PasswordGenerator
        gen = PasswordGenerator()
        password = gen.generate()
        print(f"\nGenerated: {password}")
    
    elif args.mode == 'report':
        from modules.report_generator import ReportGenerator
        report = ReportGenerator()
        report.generate_quick_report()
        print("\n✅ Report generated in reports/ folder")
    
    else:
        # Show help if no valid mode
        print("\nAvailable Modes:")
        print("  gui       - Launch beautiful graphical interface")
        print("  cli       - Launch command line interface")
        print("  check     - Quick password check: grae_x_sentinel.py check 'password'")
        print("  scan      - Quick WiFi scan")
        print("  generate  - Generate strong password")
        print("  report    - Generate security report")
        print("\nExamples:")
        print("  python grae_x_sentinel.py gui")
        print("  python grae_x_sentinel.py cli")
        print("  python grae_x_sentinel.py check 'MyPass123'")
        print("  python grae_x_sentinel.py scan")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")