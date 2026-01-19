#!/usr/bin/env python3
"""
GRAE-X SENTINEL PRO - Command Line Interface
Full-featured CLI version
"""

import sys
import os
import argparse
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List
import getpass

# Import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modules.password_analyzer import PasswordAnalyzer
from modules.wifi_scanner import WiFiScanner
from modules.breach_checker import BreachChecker
from modules.password_generator import PasswordGenerator
from modules.report_generator import ReportGenerator

class SentinelCLI:
    """Command Line Interface for Grae-X Sentinel Pro"""
    
    def __init__(self):
        self.password_analyzer = PasswordAnalyzer()
        self.wifi_scanner = WiFiScanner()
        self.breach_checker = BreachChecker()
        self.password_generator = PasswordGenerator()
        self.report_generator = ReportGenerator()
        
        # Colors for CLI
        self.colors = {
            'reset': '\033[0m',
            'bold': '\033[1m',
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
        }
    
    def print_banner(self):
        """Print CLI banner"""
        banner = f"""
{self.colors['cyan']}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     ██████╗ ██████╗  █████╗ ███████╗   ███████╗███████╗     ║
║    ██╔════╝ ██╔══██╗██╔══██╗██╔════╝   ██╔════╝╚══███╔╝     ║
║    ██║  ███╗██████╔╝███████║█████╗     █████╗    ███╔╝      ║
║    ██║   ██║██╔══██╗██╔══██║██╔══╝     ██╔══╝   ███╔╝       ║
║    ╚██████╔╝██║  ██║██║  ██║██║        ███████╗███████╗     ║
║     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚══════╝╚══════╝     ║
║                                                              ║
║              S E N T I N E L   P R O   v4.0                  ║
║           Command Line Interface - Cybersecurity Suite       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{self.colors['reset']}
"""
        print(banner)
    
    def print_menu(self):
        """Print main menu"""
        menu = f"""
{self.colors['bold']}{self.colors['blue']}MAIN MENU{self.colors['reset']}

{self.colors['green']}1.{self.colors['reset']} Password Analysis
{self.colors['green']}2.{self.colors['reset']} WiFi Security Scan
{self.colors['green']}3.{self.colors['reset']} Password Generator
{self.colors['green']}4.{self.colors['reset']} Security Reports
{self.colors['green']}5.{self.colors['reset']} Batch Operations
{self.colors['green']}6.{self.colors['reset']} Quick Check
{self.colors['green']}0.{self.colors['reset']} Exit

{self.colors['yellow']}Enter choice:{self.colors['reset']} """
        return menu
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title):
        """Print section header"""
        width = 60
        print(f"\n{self.colors['bold']}{self.colors['blue']}{'=' * width}")
        print(f"{title.center(width)}")
        print(f"{'=' * width}{self.colors['reset']}\n")
    
    def print_result(self, label, value, color='white'):
        """Print a result line"""
        print(f"{self.colors['cyan']}{label:<20}{self.colors['reset']}: {self.colors[color]}{value}{self.colors['reset']}")
    
    def print_success(self, message):
        """Print success message"""
        print(f"{self.colors['green']}✅ {message}{self.colors['reset']}")
    
    def print_warning(self, message):
        """Print warning message"""
        print(f"{self.colors['yellow']}⚠️  {message}{self.colors['reset']}")
    
    def print_error(self, message):
        """Print error message"""
        print(f"{self.colors['red']}❌ {message}{self.colors['reset']}")
    
    def password_analysis(self):
        """Password analysis mode"""
        self.print_header("PASSWORD STRENGTH ANALYSIS")
        
        while True:
            print(f"\n{self.colors['yellow']}Enter password (or 'back' to return):{self.colors['reset']}")
            password = getpass.getpass("Password: ")
            
            if password.lower() == 'back':
                break
            
            if not password:
                self.print_warning("Password cannot be empty")
                continue
            
            # Analyze password
            print(f"\n{self.colors['cyan']}Analyzing password...{self.colors['reset']}")
            result = self.password_analyzer.analyze(password)
            
            # Display results
            self.print_header("ANALYSIS RESULTS")
            
            # Strength with color
            strength = result['strength']
            score = result['score']
            
            if score >= 80:
                strength_color = 'green'
                strength_icon = '✅'
            elif score >= 60:
                strength_color = 'yellow'
                strength_icon = '⚠️'
            elif score >= 40:
                strength_color = 'yellow'
                strength_icon = '⚠️'
            else:
                strength_color = 'red'
                strength_icon = '❌'
            
            print(f"{strength_icon} {self.colors[strength_color]}{strength} ({score}/100){self.colors['reset']}\n")
            
            # Metrics
            self.print_result("Length", f"{result['length']} characters")
            self.print_result("Entropy", f"{result['entropy']:.1f} bits")
            self.print_result("Crack Time", result['crack_time'])
            
            # Requirements
            print(f"\n{self.colors['cyan']}Requirements:{self.colors['reset']}")
            reqs = result['requirements']
            for req, met in reqs.items():
                icon = '✅' if met else '❌'
                color = 'green' if met else 'red'
                req_name = req.replace('_', ' ').title()
                print(f"  {icon} {self.colors[color]}{req_name}{self.colors['reset']}")
            
            # Breach check option
            print(f"\n{self.colors['yellow']}Check for breaches? (y/n):{self.colors['reset']}", end=' ')
            if input().lower() == 'y':
                breach_result = self.breach_checker.check(password)
                if breach_result['breached']:
                    self.print_error(f"PASSWORD BREACHED! Found in {breach_result['count']:,} data breaches!")
                    print(f"{self.colors['red']}CHANGE THIS PASSWORD IMMEDIATELY!{self.colors['reset']}")
                else:
                    self.print_success("No breaches found")
            
            print(f"\n{self.colors['cyan']}{'─' * 60}{self.colors['reset']}")
    
    def wifi_scan(self):
        """WiFi security scan"""
        self.print_header("WiFi SECURITY SCAN")
        
        print(f"{self.colors['yellow']}Note: Run as Administrator/root for best results{self.colors['reset']}")
        print(f"{self.colors['cyan']}Scanning for WiFi networks...{self.colors['reset']}\n")
        
        try:
            networks = self.wifi_scanner.scan()
            
            if not networks:
                self.print_error("No networks found or insufficient permissions")
                return
            
            self.print_success(f"Found {len(networks)} network(s)\n")
            
            # Display networks
            print(f"{self.colors['cyan']}{'#':<3} {'SSID':<25} {'Security':<15} {'Signal':<10} {'Risk':<10}{self.colors['reset']}")
            print(f"{self.colors['cyan']}{'─' * 60}{self.colors['reset']}")
            
            for i, net in enumerate(networks, 1):
                ssid = net.get('ssid', 'Hidden')[:24]
                security = net.get('security', 'Unknown')[:14]
                signal = net.get('signal', 'N/A')[:9]
                
                # Determine risk
                if 'WEP' in security:
                    risk = 'CRITICAL'
                    risk_color = 'red'
                elif 'OPEN' in security:
                    risk = 'HIGH'
                    risk_color = 'red'
                elif 'WPA' in security and 'WPA2' not in security:
                    risk = 'MEDIUM'
                    risk_color = 'yellow'
                else:
                    risk = 'LOW'
                    risk_color = 'green'
                
                print(f"{i:<3} {ssid:<25} {security:<15} {signal:<10} {self.colors[risk_color]}{risk:<10}{self.colors['reset']}")
            
            # Option to analyze specific network
            print(f"\n{self.colors['yellow']}Enter number to analyze (or Enter to skip):{self.colors['reset']}", end=' ')
            try:
                choice = input().strip()
                if choice and choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(networks):
                        self.analyze_network(networks[idx])
            except:
                pass
            
            # Generate report
            print(f"\n{self.colors['yellow']}Generate report? (y/n):{self.colors['reset']}", end=' ')
            if input().lower() == 'y':
                self.report_generator.generate_wifi_report(networks)
                self.print_success("WiFi report generated in reports/ folder")
        
        except Exception as e:
            self.print_error(f"Scan failed: {str(e)}")
    
    def analyze_network(self, network):
        """Analyze a specific network"""
        self.print_header(f"NETWORK ANALYSIS: {network.get('ssid', 'Unknown')}")
        
        security = network.get('security', 'Unknown')
        signal = network.get('signal', 'N/A')
        
        print(f"{self.colors['cyan']}Security:{self.colors['reset']} {security}")
        print(f"{self.colors['cyan']}Signal:{self.colors['reset']} {signal}")
        
        # Security assessment
        if 'WEP' in security:
            self.print_error("WEP ENCRYPTION - EASILY CRACKABLE")
            print(f"{self.colors['red']}Upgrade to WPA2/WPA3 immediately!{self.colors['reset']}")
        elif 'OPEN' in security or 'NONE' in security:
            self.print_error("OPEN NETWORK - NO ENCRYPTION")
            print(f"{self.colors['red']}Enable WPA2/WPA3 encryption!{self.colors['reset']}")
        elif 'WPA' in security and 'WPA2' not in security:
            self.print_warning("Original WPA - Vulnerable to attacks")
            print(f"{self.colors['yellow']}Upgrade to WPA2 or WPA3{self.colors['reset']}")
        elif 'WPA2' in security or 'WPA3' in security:
            self.print_success("Good encryption (WPA2/WPA3)")
        
        print()
    
    def password_generation(self):
        """Password generator"""
        self.print_header("PASSWORD GENERATOR")
        
        print(f"{self.colors['yellow']}Configure password settings:{self.colors['reset']}")
        
        # Get length
        length = input(f"{self.colors['cyan']}Length (12-32, default 16):{self.colors['reset']} ").strip()
        length = int(length) if length.isdigit() else 16
        length = max(12, min(32, length))
        
        # Get character types
        print(f"\n{self.colors['cyan']}Include character types:{self.colors['reset']}")
        use_lower = input("Lowercase (a-z)? (y/n, default y): ").strip().lower() != 'n'
        use_upper = input("Uppercase (A-Z)? (y/n, default y): ").strip().lower() != 'n'
        use_digits = input("Digits (0-9)? (y/n, default y): ").strip().lower() != 'n'
        use_special = input("Special characters (!@#$)? (y/n, default y): ").strip().lower() != 'n'
        
        print(f"\n{self.colors['cyan']}Generating password...{self.colors['reset']}")
        
        password = self.password_generator.generate(
            length=length,
            use_lower=use_lower,
            use_upper=use_upper,
            use_digits=use_digits,
            use_special=use_special
        )
        
        print(f"\n{self.colors['green']}Generated Password:{self.colors['reset']}")
        print(f"{self.colors['bold']}{password}{self.colors['reset']}")
        print(f"{self.colors['cyan']}Length:{self.colors['reset']} {len(password)} characters")
        
        # Auto-analyze
        print(f"\n{self.colors['cyan']}Analyzing generated password...{self.colors['reset']}")
        result = self.password_analyzer.analyze(password)
        print(f"{self.colors['green']}Strength: {result['strength']} ({result['score']}/100){self.colors['reset']}")
        
        # Save option
        print(f"\n{self.colors['yellow']}Save to file? (y/n):{self.colors['reset']}", end=' ')
        if input().lower() == 'y':
            filename = f"generated_password_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                f.write(f"Generated: {datetime.now()}\n")
                f.write(f"Password: {password}\n")
                f.write(f"Length: {len(password)}\n")
                f.write(f"Strength: {result['strength']} ({result['score']}/100)\n")
            self.print_success(f"Password saved to {filename}")
    
    def security_reports(self):
        """Security reports"""
        self.print_header("SECURITY REPORTS")
        
        print(f"{self.colors['cyan']}Select report type:{self.colors['reset']}\n")
        
        reports = [
            ("1", "Password Audit", "Analyze password database"),
            ("2", "WiFi Security", "WiFi network analysis"),
            ("3", "Security Dashboard", "Complete security overview"),
            ("4", "Vulnerability Scan", "System vulnerability check"),
            ("5", "Quick Security", "Quick security assessment"),
        ]
        
        for num, title, desc in reports:
            print(f"{self.colors['green']}{num}.{self.colors['reset']} {title}")
            print(f"   {self.colors['cyan']}{desc}{self.colors['reset']}")
        
        print(f"\n{self.colors['yellow']}Enter choice:{self.colors['reset']}", end=' ')
        choice = input().strip()
        
        if choice == '1':
            self.report_generator.generate_password_report()
            self.print_success("Password audit report generated")
        elif choice == '2':
            self.report_generator.generate_wifi_report([])
            self.print_success("WiFi security report generated")
        elif choice == '3':
            self.report_generator.generate_dashboard_report()
            self.print_success("Security dashboard report generated")
        elif choice == '4':
            self.report_generator.generate_vulnerability_report()
            self.print_success("Vulnerability scan report generated")
        elif choice == '5':
            self.report_generator.generate_quick_report()
            self.print_success("Quick security report generated")
        else:
            self.print_error("Invalid choice")
    
    def batch_operations(self):
        """Batch operations"""
        self.print_header("BATCH OPERATIONS")
        
        print(f"{self.colors['cyan']}Select batch operation:{self.colors['reset']}\n")
        
        operations = [
            ("1", "Batch Password Check", "Check multiple passwords from file"),
            ("2", "Password List Generator", "Generate multiple passwords"),
            ("3", "WiFi Audit", "Comprehensive WiFi security audit"),
        ]
        
        for num, title, desc in operations:
            print(f"{self.colors['green']}{num}.{self.colors['reset']} {title}")
            print(f"   {self.colors['cyan']}{desc}{self.colors['reset']}")
        
        print(f"\n{self.colors['yellow']}Enter choice:{self.colors['reset']}", end=' ')
        choice = input().strip()
        
        if choice == '1':
            self.batch_password_check()
        elif choice == '2':
            self.batch_password_generate()
        elif choice == '3':
            self.batch_wifi_audit()
        else:
            self.print_error("Invalid choice")
    
    def batch_password_check(self):
        """Batch password check"""
        self.print_header("BATCH PASSWORD CHECK")
        
        print(f"{self.colors['cyan']}Enter path to password file (one per line):{self.colors['reset']}")
        filepath = input("File: ").strip()
        
        if not os.path.exists(filepath):
            self.print_error("File not found")
            return
        
        try:
            with open(filepath, 'r') as f:
                passwords = [line.strip() for line in f if line.strip()]
            
            print(f"\n{self.colors['cyan']}Checking {len(passwords)} passwords...{self.colors['reset']}")
            
            results = []
            weak_passwords = []
            
            for i, password in enumerate(passwords[:1000], 1):  # Limit to 1000
                result = self.password_analyzer.analyze(password)
                results.append((password, result))
                
                if result['score'] < 40:
                    weak_passwords.append((password, result['score']))
                
                if i % 100 == 0:
                    print(f"  Checked {i} passwords...")
            
            # Generate report
            report_file = f"batch_check_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(report_file, 'w') as f:
                f.write("BATCH PASSWORD CHECK REPORT\n")
                f.write("="*50 + "\n\n")
                f.write(f"Date: {datetime.now()}\n")
                f.write(f"Passwords checked: {len(results)}\n")
                f.write(f"Weak passwords found: {len(weak_passwords)}\n\n")
                
                if weak_passwords:
                    f.write("WEAK PASSWORDS FOUND:\n")
                    f.write("-"*30 + "\n")
                    for pwd, score in weak_passwords[:50]:  # Show first 50
                        f.write(f"{pwd[:10]}... - Score: {score}/100\n")
                
                f.write("\nRECOMMENDATIONS:\n")
                f.write("-"*30 + "\n")
                f.write("1. Change all weak passwords immediately\n")
                f.write("2. Use 12+ character passwords\n")
                f.write("3. Enable two-factor authentication\n")
                f.write("4. Use a password manager\n")
            
            self.print_success(f"Batch check complete!")
            print(f"{self.colors['cyan']}Results:{self.colors['reset']}")
            print(f"  Total passwords: {len(results)}")
            print(f"  Weak passwords: {len(weak_passwords)}")
            print(f"  Report file: {report_file}")
            
            if weak_passwords:
                self.print_error(f"{len(weak_passwords)} WEAK PASSWORDS FOUND!")
                print(f"{self.colors['red']}Change these passwords immediately!{self.colors['reset']}")
        
        except Exception as e:
            self.print_error(f"Error: {str(e)}")
    
    def batch_password_generate(self):
        """Generate multiple passwords"""
        self.print_header("BATCH PASSWORD GENERATOR")
        
        try:
            count = input(f"{self.colors['cyan']}Number of passwords to generate (1-100):{self.colors['reset']} ").strip()
            count = int(count) if count.isdigit() else 10
            count = max(1, min(100, count))
            
            length = input(f"{self.colors['cyan']}Password length (12-32, default 16):{self.colors['reset']} ").strip()
            length = int(length) if length.isdigit() else 16
            length = max(12, min(32, length))
            
            print(f"\n{self.colors['cyan']}Generating {count} passwords...{self.colors['reset']}")
            
            passwords = []
            for i in range(count):
                password = self.password_generator.generate(length=length)
                passwords.append(password)
                print(f"  {i+1:3}. {password}")
            
            # Save to file
            filename = f"password_list_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                f.write(f"Generated: {datetime.now()}\n")
                f.write(f"Count: {count}\n")
                f.write(f"Length: {length}\n\n")
                for i, pwd in enumerate(passwords, 1):
                    f.write(f"{i:3}. {pwd}\n")
            
            self.print_success(f"Passwords saved to {filename}")
        
        except Exception as e:
            self.print_error(f"Error: {str(e)}")
    
    def batch_wifi_audit(self):
        """Batch WiFi audit"""
        self.print_header("BATCH WiFi AUDIT")
        
        print(f"{self.colors['yellow']}This will perform comprehensive WiFi security audit{self.colors['reset']}")
        print(f"{self.colors['cyan']}Scanning networks...{self.colors['reset']}")
        
        try:
            networks = self.wifi_scanner.scan()
            
            if not networks:
                self.print_error("No networks found")
                return
            
            # Analyze each network
            insecure_networks = []
            for net in networks:
                if 'WEP' in net.get('security', '') or 'OPEN' in net.get('security', ''):
                    insecure_networks.append(net)
            
            # Generate report
            report_file = f"wifi_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(report_file, 'w') as f:
                f.write("WiFi SECURITY AUDIT REPORT\n")
                f.write("="*50 + "\n\n")
                f.write(f"Date: {datetime.now()}\n")
                f.write(f"Networks found: {len(networks)}\n")
                f.write(f"Insecure networks: {len(insecure_networks)}\n\n")
                
                f.write("NETWORK DETAILS:\n")
                f.write("-"*30 + "\n")
                for net in networks:
                    ssid = net.get('ssid', 'Hidden')
                    security = net.get('security', 'Unknown')
                    signal = net.get('signal', 'N/A')
                    
                    if 'WEP' in security:
                        risk = "CRITICAL"
                    elif 'OPEN' in security:
                        risk = "HIGH"
                    elif 'WPA' in security and 'WPA2' not in security:
                        risk = "MEDIUM"
                    else:
                        risk = "LOW"
                    
                    f.write(f"SSID: {ssid}\n")
                    f.write(f"  Security: {security} ({risk} risk)\n")
                    f.write(f"  Signal: {signal}\n\n")
                
                f.write("RECOMMENDATIONS:\n")
                f.write("-"*30 + "\n")
                f.write("1. Use WPA2 or WPA3 encryption\n")
                f.write("2. Change default router passwords\n")
                f.write("3. Disable WPS (WiFi Protected Setup)\n")
                f.write("4. Hide SSID if not needed\n")
                f.write("5. Enable MAC address filtering\n")
                f.write("6. Keep router firmware updated\n")
            
            self.print_success(f"WiFi audit complete!")
            print(f"{self.colors['cyan']}Results:{self.colors['reset']}")
            print(f"  Networks scanned: {len(networks)}")
            print(f"  Insecure networks: {len(insecure_networks)}")
            print(f"  Report file: {report_file}")
            
            if insecure_networks:
                self.print_warning(f"{len(insecure_networks)} INSECURE NETWORKS FOUND!")
        
        except Exception as e:
            self.print_error(f"Error: {str(e)}")
    
    def quick_check(self):
        """Quick security check"""
        self.print_header("QUICK SECURITY CHECK")
        
        print(f"{self.colors['cyan']}Performing quick security assessment...{self.colors['reset']}\n")
        
        # Check 1: Common weak passwords
        print(f"{self.colors['yellow']}1. Testing common weak passwords...{self.colors['reset']}")
        common_passwords = ['password', '123456', 'admin', 'welcome', 'qwerty']
        weak_found = 0
        
        for pwd in common_passwords:
            result = self.password_analyzer.analyze(pwd)
            if result['score'] < 20:
                weak_found += 1
        
        if weak_found > 0:
            self.print_error(f"Found {weak_found} extremely weak common passwords")
        else:
            self.print_success("No extremely weak common passwords")
        
        # Check 2: WiFi security basics
        print(f"\n{self.colors['yellow']}2. WiFi Security Basics:{self.colors['reset']}")
        print(f"   {self.colors['green']}✅ Use WPA2/WPA3 encryption{self.colors['reset']}")
        print(f"   {self.colors['green']}✅ 12+ character passwords{self.colors['reset']}")
        print(f"   {self.colors['green']}✅ Change default router settings{self.colors['reset']}")
        
        # Check 3: General recommendations
        print(f"\n{self.colors['yellow']}3. Security Recommendations:{self.colors['reset']}")
        print(f"   {self.colors['cyan']}• Enable two-factor authentication{self.colors['reset']}")
        print(f"   {self.colors['cyan']}• Use password manager{self.colors['reset']}")
        print(f"   {self.colors['cyan']}• Regular software updates{self.colors['reset']}")
        print(f"   {self.colors['cyan']}• Backup important data{self.colors['reset']}")
        
        # Generate quick report
        self.report_generator.generate_quick_report()
        print(f"\n{self.colors['green']}✅ Quick security report generated in reports/ folder{self.colors['reset']}")
    
    def run(self):
        """Run CLI interface"""
        self.clear_screen()
        self.print_banner()
        
        while True:
            try:
                print(self.print_menu(), end='')
                choice = input().strip()
                
                if choice == '0':
                    print(f"\n{self.colors['green']}Thank you for using Grae-X Sentinel Pro! 👋{self.colors['reset']}")
                    break
                
                elif choice == '1':
                    self.password_analysis()
                
                elif choice == '2':
                    self.wifi_scan()
                
                elif choice == '3':
                    self.password_generation()
                
                elif choice == '4':
                    self.security_reports()
                
                elif choice == '5':
                    self.batch_operations()
                
                elif choice == '6':
                    self.quick_check()
                
                else:
                    self.print_error("Invalid choice. Please try again.")
                
                # Pause before showing menu again
                if choice != '0':
                    print(f"\n{self.colors['cyan']}Press Enter to continue...{self.colors['reset']}", end='')
                    input()
                    self.clear_screen()
                    self.print_banner()
            
            except KeyboardInterrupt:
                print(f"\n\n{self.colors['yellow']}Interrupted. Returning to menu...{self.colors['reset']}")
            except Exception as e:
                self.print_error(f"Error: {str(e)}")
                print(f"{self.colors['cyan']}Press Enter to continue...{self.colors['reset']}", end='')
                input()

# Command line entry point
if __name__ == "__main__":
    cli = SentinelCLI()
    cli.run()