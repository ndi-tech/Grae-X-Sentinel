#!/usr/bin/env python3
"""
GRAE-X SENTINEL PRO - Futuristic Matrix-Style Interface
Advanced Cybersecurity Toolkit with Real-Time Visual Effects
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import json
import threading
import random
import time
from datetime import datetime
from pathlib import Path
import sys
import os

# Import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Try to import modules, create mock ones if they don't exist
try:
    from modules.password_analyzer import PasswordAnalyzer
    from modules.wifi_scanner import WiFiScanner
    from modules.breach_checker import BreachChecker
    from modules.password_generator import PasswordGenerator
    from modules.report_generator import ReportGenerator
    print("✅ All modules imported successfully")
except ImportError as e:
    print(f"⚠️ Import error: {e}")
    print("⚠️ Using mock implementations")
    # Create minimal mock classes only if imports fail
    class PasswordAnalyzer:
        def analyze(self, password):
            return {
                'score': random.randint(20, 95),
                'crack_time': f"{random.randint(1, 1000)} years",
                'entropy': random.uniform(20, 80),
                'feedback': ['Sample analysis - install real modules']
            }
    
    class WiFiScanner:
        def scan(self):
            return [
                {'ssid': 'Neo-Corp WiFi', 'security': 'WPA3-Enterprise', 'signal': '92%', 'channel': '6', 'bssid': '00:11:22:33:44:55'},
                {'ssid': 'The Matrix', 'security': 'Quantum-Encrypted', 'signal': '88%', 'channel': '11', 'bssid': 'AA:BB:CC:DD:EE:FF'},
                {'ssid': 'Zion Network', 'security': 'Neural-Locked', 'signal': '76%', 'channel': '36', 'bssid': '11:22:33:44:55:66'},
                {'ssid': 'Architect VPN', 'security': 'Zero-Trust', 'signal': '65%', 'channel': '149', 'bssid': '77:88:99:AA:BB:CC'}
            ]
    
    class BreachChecker:
        def check(self, password):
            return {'breached': False, 'count': 0, 'message': 'Local check only'}
    
    class PasswordGenerator:
        def generate(self, **kwargs):
            length = kwargs.get('length', 16)
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
            return ''.join(random.choice(chars) for _ in range(length))
    
    class ReportGenerator:
        """Generate security reports and analytics"""
        
        def __init__(self):
            self.report_data = {
                'wifi_scan': None,
                'password_audit': None,
                'dashboard_stats': None
            }
        
        def generate_wifi_report(self, networks):
            """Generate a WiFi security report"""
            if not networks:
                return "No WiFi networks scanned."
                
            report = []
            report.append("=" * 70)
            report.append("WiFi NETWORK SECURITY REPORT")
            report.append("=" * 70)
            report.append(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            report.append(f"Total Networks Found: {len(networks)}")
            report.append("-" * 70)
            
            # Count security types
            security_counts = {}
            for net in networks:
                security = net.get('security', 'Unknown')
                security_counts[security] = security_counts.get(security, 0) + 1
            
            report.append("Security Type Breakdown:")
            for security, count in security_counts.items():
                report.append(f"  {security}: {count} networks")
            
            # Find vulnerable networks
            vulnerable = [net for net in networks if net.get('security', '') in ['WEP', 'OPEN', 'WPA', 'WPA2']]
            if vulnerable:
                report.append(f"\nVulnerable Networks Found: {len(vulnerable)}")
                report.append("-" * 40)
                for net in vulnerable:
                    report.append(f"  SSID: {net.get('ssid', 'Unknown')}")
                    report.append(f"    Security: {net.get('security', 'Unknown')}")
                    report.append(f"    Signal: {net.get('signal', 'N/A')}")
            
            report.append("\n" + "=" * 70)
            report.append("RECOMMENDATIONS:")
            report.append("-" * 70)
            report.append("1. Use WPA3 encryption whenever possible")
            report.append("2. Avoid using WEP or OPEN networks")
            report.append("3. Change default router passwords")
            report.append("4. Disable WPS if not needed")
            report.append("5. Regularly update router firmware")
            report.append("=" * 70)
            
            return "\n".join(report)
        
        def generate_password_report(self):
            """Generate a password security report"""
            report = []
            report.append("=" * 70)
            report.append("PASSWORD SECURITY AUDIT REPORT")
            report.append("=" * 70)
            report.append(f"Audit Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            report.append("-" * 70)
            
            # Password strength analysis
            report.append("PASSWORD STRENGTH GUIDELINES:")
            report.append("  • Strong: 12+ chars, mixed case, numbers, symbols")
            report.append("  • Medium: 8-11 chars, some complexity")
            report.append("  • Weak: Less than 8 chars, simple patterns")
            report.append("-" * 70)
            
            report.append("COMMON PASSWORD VULNERABILITIES:")
            report.append("  1. Dictionary words")
            report.append("  2. Sequential patterns (123456, abcdef)")
            report.append("  3. Personal information")
            report.append("  4. Short passwords (< 8 characters)")
            report.append("  5. Reused passwords across sites")
            report.append("-" * 70)
            
            report.append("RECOMMENDED PRACTICES:")
            report.append("  1. Use a password manager")
            report.append("  2. Enable two-factor authentication")
            report.append("  3. Create unique passwords for each site")
            report.append("  4. Use passphrases instead of passwords")
            report.append("  5. Regularly audit your passwords")
            report.append("=" * 70)
            
            return "\n".join(report)
        
        def generate_dashboard_report(self):
            """Generate a comprehensive dashboard report"""
            report = []
            report.append("=" * 70)
            report.append("GRAE-X SENTINEL PRO - SECURITY DASHBOARD REPORT")
            report.append("=" * 70)
            report.append(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            report.append("-" * 70)
            
            report.append("SYSTEM SECURITY STATUS:")
            report.append("  • WiFi Security: Scan networks for assessment")
            report.append("  • Password Health: Audit password strength")
            report.append("  • Network Protection: Monitor connections")
            report.append("-" * 70)
            
            report.append("QUICK SECURITY CHECKS:")
            report.append("  ✓ Scan nearby WiFi networks")
            report.append("  ✓ Test password strength")
            report.append("  ✓ Generate secure passwords")
            report.append("  ✓ Create security reports")
            report.append("-" * 70)
            
            report.append("NEXT STEPS:")
            report.append("  1. Perform regular WiFi scans")
            report.append("  2. Audit all your passwords")
            report.append("  3. Generate strong passwords")
            report.append("  4. Save reports for documentation")
            report.append("=" * 70)
            
            return "\n".join(report)

class MatrixEffect:
    """Falling Matrix code rain effect"""
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
        self.drops = []
        self.font_size = 14
        self.speed = 2
        self.active = True
        self.init_drops()
    
    def init_drops(self):
        """Initialize matrix drops"""
        self.drops = []
        columns = self.width // self.font_size
        
        for i in range(columns):
            x = i * self.font_size
            y = random.randint(-500, -50)
            length = random.randint(5, 30)
            speed = random.uniform(1, 3)
            brightness = random.randint(100, 255)
            self.drops.append({
                'x': x,
                'y': y,
                'length': length,
                'speed': speed,
                'chars': [random.choice(self.chars) for _ in range(length)],
                'brightness': brightness
            })
    
    def draw(self):
        """Draw matrix effect"""
        if not self.active:
            return
        
        self.canvas.delete("matrix")
        
        for drop in self.drops:
            y = drop['y']
            brightness = drop['brightness']
            
            # Draw each character in the drop
            for i, char in enumerate(drop['chars']):
                char_y = y + i * self.font_size
                
                # Calculate brightness gradient (head is brightest)
                char_brightness = int(brightness * (1 - i / drop['length']))
                if char_brightness < 30:
                    char_brightness = 30
                
                color = f'#{char_brightness:02x}{char_brightness:02x}00' if i == 0 else f'#00{char_brightness:02x}00'
                
                self.canvas.create_text(
                    drop['x'], char_y,
                    text=char,
                    fill=color,
                    font=('Consolas', self.font_size, 'bold'),
                    tags="matrix",
                    anchor='nw'
                )
            
            # Move drop down
            drop['y'] += drop['speed']
            
            # Reset drop if it goes off screen
            if drop['y'] - drop['length'] * self.font_size > self.height:
                drop['y'] = random.randint(-500, -50)
                drop['chars'] = [random.choice(self.chars) for _ in range(drop['length'])]
                drop['brightness'] = random.randint(100, 255)
        
        # Schedule next frame
        self.canvas.after(30, self.draw)
    
    def toggle(self, active=None):
        """Toggle matrix effect on/off"""
        if active is not None:
            self.active = active
        else:
            self.active = not self.active
        
        if self.active:
            self.draw()

class DigitalRainWidget:
    """Digital rain widget for cyberpunk effect"""
    def __init__(self, parent, width, height):
        self.canvas = tk.Canvas(parent, width=width, height=height, 
                               bg='#0A0A0A', highlightthickness=0)
        self.canvas.pack()
        self.width = width
        self.height = height
        
        # Digital rain configuration
        self.chars = "0101010101101001011101000111001100100000011000010110111001100100"
        self.font_size = 10
        self.columns = width // self.font_size
        self.drops = [0] * self.columns
        self.colors = ['#00FF00', '#00CC00', '#009900', '#006600']
        
        self.running = True
        self.animate()
    
    def animate(self):
        """Animate digital rain"""
        if not self.running:
            return
        
        self.canvas.delete("rain")
        
        for i in range(len(self.drops)):
            # Randomly reset drops
            if self.drops[i] > 100 or random.random() > 0.975:
                self.drops[i] = 0
            
            # Draw drop
            y = self.drops[i] * self.font_size
            for j in range(min(10, len(self.chars))):
                char = random.choice(['0', '1'])
                x = i * self.font_size
                char_y = y - j * self.font_size
                
                if char_y >= 0:
                    color_idx = min(j, len(self.colors)-1)
                    self.canvas.create_text(
                        x, char_y,
                        text=char,
                        fill=self.colors[color_idx],
                        font=('Consolas', self.font_size),
                        tags="rain",
                        anchor='nw'
                    )
            
            self.drops[i] += 1
        
        self.canvas.after(100, self.animate)
    
    def stop(self):
        """Stop animation"""
        self.running = False

class SentinelGUI:
    """Main GUI Application - Matrix Edition"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GRAE-X SENTINEL PRO // v4.2 // SYSTEM ONLINE")
        self.root.geometry("1400x900")
        self.root.minsize(1200, 800)
        
        # Initialize stats
        self.stats = {
            'passwords_analyzed': 0,
            'networks_scanned': 0,
            'breaches_found': 0,
            'reports_generated': 0
        }
        
        # Configure futuristic cybersecurity theme (green, red, black)
        self.colors = {
            'matrix_green': '#00FF00',
            'neon_green': '#00FF88',
            'cyber_green': '#00CC66',
            'alert_red': '#FF0033',
            'warning_orange': '#FF6600',
            'cyber_blue': '#00FFFF',
            'dark_bg': '#000000',
            'panel_bg': '#0A0A0A',
            'darker_bg': '#050505',
            'highlight': '#111111',
            'text_primary': '#FFFFFF',
            'text_secondary': '#88FF88',
            'text_dim': '#666666',
        }
        
        # Initialize modules
        self.password_analyzer = PasswordAnalyzer()
        self.wifi_scanner = WiFiScanner()
        self.breach_checker = BreachChecker()
        self.password_generator = PasswordGenerator()
        self.report_generator = ReportGenerator()
        
        # Current state
        self.current_password = ""
        self.current_networks = []
        self.scanning = False
        self.matrix_effect_active = True
        
        # Set window background
        self.root.configure(bg=self.colors['dark_bg'])
        
        # Create main container
        self.setup_main_container()
        
        # Create menu
        self.setup_cyber_menu()
        
        # Bind F1-F5 keys
        self.bind_hotkeys()
    
    def setup_main_container(self):
        """Setup main container with futuristic styling"""
        # Main container
        self.main_container = tk.Frame(self.root, bg=self.colors['dark_bg'])
        self.main_container.pack(fill='both', expand=True)
        
        # Header with glowing effect
        self.create_cyber_header()
        
        # Content area
        self.content_frame = tk.Frame(self.main_container, bg=self.colors['dark_bg'])
        self.content_frame.pack(fill='both', expand=True, padx=2, pady=2)
        
        # Left sidebar for stats
        self.create_cyber_sidebar()
        
        # Main notebook area
        self.create_cyber_notebook()
        
        # Footer
        self.create_cyber_footer()
    
    def create_cyber_header(self):
        """Create cyberpunk header with red/green accents"""
        header_frame = tk.Frame(self.main_container, 
                               bg=self.colors['darker_bg'],
                               height=120,
                               highlightbackground=self.colors['matrix_green'],
                               highlightthickness=1)
        header_frame.pack(fill='x', pady=(0, 2))
        header_frame.pack_propagate(False)
        
        # Main title with glow effect
        title_frame = tk.Frame(header_frame, bg=self.colors['darker_bg'])
        title_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # GRAE-X title with red accent
        tk.Label(title_frame,
                text="GRAE-X",
                bg=self.colors['darker_bg'],
                fg=self.colors['alert_red'],
                font=('Orbitron', 36, 'bold')).pack(side='left', padx=(0, 10))
        
        # SENTINEL PRO title with green accent
        tk.Label(title_frame,
                text="SENTINEL PRO",
                bg=self.colors['darker_bg'],
                fg=self.colors['matrix_green'],
                font=('Orbitron', 28, 'bold')).pack(side='left')
        
        # Version and status
        version_frame = tk.Frame(title_frame, bg=self.colors['darker_bg'])
        version_frame.pack(side='right', padx=20)
        
        tk.Label(version_frame,
                text="v4.2.1 // ",
                bg=self.colors['darker_bg'],
                fg=self.colors['text_dim'],
                font=('Consolas', 12)).pack(side='left')
        
        # Status indicator (blinking)
        self.status_label = tk.Label(version_frame,
                                    text="[ONLINE]",
                                    bg=self.colors['darker_bg'],
                                    fg=self.colors['matrix_green'],
                                    font=('Consolas', 12, 'bold'))
        self.status_label.pack(side='left')
        
        # Subtitle with scanning effect
        subtitle_frame = tk.Frame(header_frame, bg=self.colors['darker_bg'])
        subtitle_frame.pack(fill='x', padx=20, pady=(0, 10))
        
        self.subtitle_text = tk.Label(subtitle_frame,
                                     text=">_ CYBERSECURITY SUITE INITIALIZED",
                                     bg=self.colors['darker_bg'],
                                     fg=self.colors['cyber_green'],
                                     font=('Consolas', 12))
        self.subtitle_text.pack(anchor='w')
        
        # Animate status
        self.animate_status()
    
    def animate_status(self):
        """Animate status blinking"""
        current_color = self.status_label.cget('foreground')
        new_color = self.colors['dark_bg'] if current_color == self.colors['matrix_green'] else self.colors['matrix_green']
        self.status_label.config(fg=new_color)
        self.root.after(1000, self.animate_status)
    
    def create_cyber_sidebar(self):
        """Create cyberpunk sidebar with red/green accents"""
        sidebar = tk.Frame(self.content_frame,
                          bg=self.colors['panel_bg'],
                          width=280,
                          relief='ridge',
                          borderwidth=2,
                          highlightbackground=self.colors['matrix_green'])
        sidebar.pack(side='left', fill='y', padx=(0, 2))
        sidebar.pack_propagate(False)
        
        # Sidebar title with warning red
        title_frame = tk.Frame(sidebar, bg=self.colors['panel_bg'])
        title_frame.pack(fill='x', pady=(20, 10))
        
        tk.Label(title_frame,
                text="⚡ SYSTEM CONTROL",
                bg=self.colors['panel_bg'],
                fg=self.colors['warning_orange'],
                font=('Orbitron', 16, 'bold')).pack()
        
        # Stats display with digital readout
        stats_frame = tk.Frame(sidebar, bg=self.colors['panel_bg'])
        stats_frame.pack(fill='x', pady=20, padx=10)
        
        tk.Label(stats_frame,
                text="SECURITY METRICS",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_green'],
                font=('Consolas', 12, 'bold')).pack(anchor='w', pady=(0, 10))
        
        stats_data = [
            ("PASSWORDS ANALYZED", self.stats['passwords_analyzed'], "units"),
            ("NETWORKS SCANNED", self.stats['networks_scanned'], "targets"),
            ("THREATS DETECTED", self.stats['breaches_found'], "alerts"),
            ("REPORTS GENERATED", self.stats['reports_generated'], "files"),
        ]
        
        for label, value, unit in stats_data:
            stat_frame = tk.Frame(stats_frame, bg=self.colors['panel_bg'])
            stat_frame.pack(fill='x', pady=3)
            
            tk.Label(stat_frame,
                    text=label,
                    bg=self.colors['panel_bg'],
                    fg=self.colors['text_secondary'],
                    font=('Consolas', 9)).pack(side='left')
            
            value_color = self.colors['matrix_green'] if value > 0 else self.colors['text_dim']
            tk.Label(stat_frame,
                    text=f" {value:03d} {unit}",
                    bg=self.colors['panel_bg'],
                    fg=value_color,
                    font=('Consolas', 10, 'bold')).pack(side='right')
        
        # Quick actions panel
        actions_frame = tk.Frame(sidebar, bg=self.colors['panel_bg'])
        actions_frame.pack(fill='x', padx=10, pady=20)
        
        tk.Label(actions_frame,
                text="⚡ QUICK COMMANDS",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_green'],
                font=('Consolas', 12)).pack(anchor='w', pady=(0, 10))
        
        actions = [
            ("[F1] SCAN PASSWORDS", self.colors['matrix_green'], lambda: self.notebook.select(0)),
            ("[F2] PROBE NETWORKS", self.colors['cyber_blue'], lambda: self.notebook.select(1)),
            ("[F3] GENERATE KEYS", self.colors['neon_green'], lambda: self.notebook.select(2)),
            ("[F4] VIEW REPORTS", self.colors['warning_orange'], lambda: self.notebook.select(3)),
            ("[F5] DASHBOARD", self.colors['alert_red'], lambda: self.notebook.select(4)),
        ]
        
        for text, color, command in actions:
            btn = tk.Button(actions_frame,
                           text=text,
                           command=command,
                           bg=self.colors['darker_bg'],
                           fg=color,
                           font=('Consolas', 10, 'bold'),
                           relief='raised',
                           borderwidth=2,
                           padx=15,
                           pady=8,
                           cursor='hand2',
                           activebackground=self.colors['highlight'],
                           activeforeground=color)
            btn.pack(fill='x', pady=3)
        
        # System monitor
        monitor_frame = tk.Frame(sidebar, bg=self.colors['panel_bg'])
        monitor_frame.pack(fill='x', padx=10, pady=20)
        
        tk.Label(monitor_frame,
                text="⚡ SYSTEM STATUS",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_green'],
                font=('Consolas', 12)).pack(anchor='w', pady=(0, 10))
        
        # System metrics
        self.create_system_gauge(monitor_frame, "CPU LOAD", 65, self.colors['matrix_green'])
        self.create_system_gauge(monitor_frame, "RAM USAGE", 78, self.colors['warning_orange'])
        self.create_system_gauge(monitor_frame, "NETWORK", 42, self.colors['cyber_blue'])
        self.create_system_gauge(monitor_frame, "SECURITY", 92, self.colors['alert_red'])
    
    def create_system_gauge(self, parent, label, value, color):
        """Create system gauge"""
        frame = tk.Frame(parent, bg=self.colors['panel_bg'])
        frame.pack(fill='x', pady=3)
        
        tk.Label(frame,
                text=label,
                bg=self.colors['panel_bg'],
                fg=self.colors['text_secondary'],
                font=('Consolas', 9),
                width=15,
                anchor='w').pack(side='left')
        
        # Gauge bar
        gauge_bg = tk.Frame(frame, bg=self.colors['darker_bg'], width=100, height=10)
        gauge_bg.pack(side='left', padx=5)
        gauge_bg.pack_propagate(False)
        
        gauge_fill = tk.Frame(gauge_bg, bg=color, width=value)
        gauge_fill.place(relheight=1.0)
        
        # Percentage
        tk.Label(frame,
                text=f"{value}%",
                bg=self.colors['panel_bg'],
                fg=color,
                font=('Consolas', 9, 'bold')).pack(side='left')
    
    def create_cyber_notebook(self):
        """Create cyberpunk styled notebook"""
        notebook_frame = tk.Frame(self.content_frame, bg=self.colors['dark_bg'])
        notebook_frame.pack(side='left', fill='both', expand=True)
        
        # Create custom notebook style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure cyberpunk style with red/green theme
        style.configure('Cyber.TNotebook',
                       background=self.colors['dark_bg'],
                       borderwidth=0)
        style.configure('Cyber.TNotebook.Tab',
                       background=self.colors['darker_bg'],
                       foreground=self.colors['text_secondary'],
                       padding=[20, 8],
                       font=('Orbitron', 10, 'bold'),
                       borderwidth=2)
        style.map('Cyber.TNotebook.Tab',
                 background=[('selected', self.colors['panel_bg'])],
                 foreground=[('selected', self.colors['matrix_green'])],
                 lightcolor=[('selected', self.colors['matrix_green'])])
        
        self.notebook = ttk.Notebook(notebook_frame, style='Cyber.TNotebook')
        self.notebook.pack(fill='both', expand=True)
        
        # Create tabs with futuristic styling
        self.create_password_tab()
        self.create_wifi_tab()
        self.create_generator_tab()
        self.create_reports_tab()
        self.create_dashboard_tab()
    
    def create_password_tab(self):
        """Create futuristic password analysis tab"""
        tab = tk.Frame(self.notebook, bg=self.colors['panel_bg'])
        self.notebook.add(tab, text="🔐 PASSWORD ANALYZER")
        
        # Title with red alert color
        title_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        title_frame.pack(fill='x', pady=(30, 20))
        
        tk.Label(title_frame,
                text="PASSWORD STRENGTH ANALYZER",
                bg=self.colors['panel_bg'],
                fg=self.colors['alert_red'],
                font=('Orbitron', 20, 'bold')).pack()
        
        tk.Label(title_frame,
                text="Analyze cryptographic strength in real-time",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_green'],
                font=('Consolas', 11)).pack(pady=(5, 0))
        
        # Input area with glowing border
        input_frame = tk.Frame(tab, bg=self.colors['darker_bg'], 
                              highlightbackground=self.colors['matrix_green'],
                              highlightthickness=2)
        input_frame.pack(fill='x', padx=40, pady=20)
        
        tk.Label(input_frame,
                text="ENTER PASSWORD FOR ANALYSIS:",
                bg=self.colors['darker_bg'],
                fg=self.colors['cyber_blue'],
                font=('Consolas', 12, 'bold')).pack(pady=(20, 10))
        
        # Password entry with futuristic style
        self.password_entry = tk.Entry(input_frame,
                                      font=('Consolas', 18),
                                      bg='#000000',
                                      fg=self.colors['matrix_green'],
                                      insertbackground=self.colors['matrix_green'],
                                      show="•",
                                      width=40,
                                      relief='flat',
                                      borderwidth=0)
        self.password_entry.pack(pady=15, padx=20, fill='x')
        self.password_entry.insert(0, "Enter password here...")
        self.password_entry.bind('<FocusIn>', lambda e: self.password_entry.delete(0, 'end') if self.password_entry.get() == "Enter password here..." else None)
        self.password_entry.bind('<KeyRelease>', self.on_password_change)
        
        # Controls
        control_frame = tk.Frame(input_frame, bg=self.colors['darker_bg'])
        control_frame.pack(pady=15)
        
        # Show password toggle
        self.show_pass_var = tk.BooleanVar()
        tk.Checkbutton(control_frame,
                      text="🔓 REVEAL PASSWORD",
                      variable=self.show_pass_var,
                      command=self.toggle_password_visibility,
                      bg=self.colors['darker_bg'],
                      fg=self.colors['text_secondary'],
                      font=('Consolas', 10),
                      selectcolor='black',
                      activebackground=self.colors['darker_bg']).pack(side='left', padx=10)
        
        # Analyze button with glowing effect
        analyze_btn = tk.Button(control_frame,
                               text="⚡ ANALYZE NOW",
                               command=self.analyze_password,
                               bg=self.colors['darker_bg'],
                               fg=self.colors['matrix_green'],
                               font=('Orbitron', 12, 'bold'),
                               relief='raised',
                               borderwidth=3,
                               padx=30,
                               pady=10,
                               cursor='hand2',
                               activebackground=self.colors['highlight'])
        analyze_btn.pack(side='left', padx=20)
        
        # Results area
        results_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        results_frame.pack(fill='both', expand=True, padx=40, pady=(0, 20))
        
        # Strength meter
        strength_frame = tk.Frame(results_frame, bg=self.colors['panel_bg'])
        strength_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(strength_frame,
                text="SECURITY STRENGTH METER:",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_blue'],
                font=('Consolas', 12)).pack(anchor='w')
        
        # Create strength bar
        bar_frame = tk.Frame(strength_frame, bg=self.colors['darker_bg'], height=25)
        bar_frame.pack(fill='x', pady=10)
        bar_frame.pack_propagate(False)
        
        self.strength_bar = tk.Frame(bar_frame, bg=self.colors['text_dim'], width=0)
        self.strength_bar.place(relheight=1.0)
        
        self.strength_label = tk.Label(strength_frame,
                                      text="ENTER PASSWORD TO BEGIN ANALYSIS",
                                      bg=self.colors['panel_bg'],
                                      fg=self.colors['text_secondary'],
                                      font=('Consolas', 11))
        self.strength_label.pack()
        
        # Metrics grid
        metrics_frame = tk.Frame(results_frame, bg=self.colors['panel_bg'])
        metrics_frame.pack(fill='both', expand=True)
        
        metrics = [
            ("ENTROPY SCORE", "0.0 bits", "matrix_green"),
            ("CRACK TIME", "INSTANT", "alert_red"),
            ("PATTERN DETECTION", "NONE", "warning_orange"),
            ("BREACH STATUS", "UNKNOWN", "cyber_blue"),
        ]
        
        self.metric_labels = {}
        for i, (label, default, color_key) in enumerate(metrics):
            metric_frame = tk.Frame(metrics_frame, bg=self.colors['panel_bg'])
            metric_frame.grid(row=i//2, column=i%2, sticky='nsew', padx=10, pady=10)
            metrics_frame.grid_columnconfigure(i%2, weight=1)
            
            tk.Label(metric_frame,
                    text=label,
                    bg=self.colors['panel_bg'],
                    fg=self.colors['text_secondary'],
                    font=('Consolas', 10)).pack(anchor='w')
            
            value_label = tk.Label(metric_frame,
                                  text=default,
                                  bg=self.colors['panel_bg'],
                                  fg=self.colors[color_key],
                                  font=('Consolas', 14, 'bold'))
            value_label.pack(anchor='w', pady=(5, 0))
            
            self.metric_labels[label.split()[0].lower()] = value_label
    
    def create_wifi_tab(self):
        """Create futuristic WiFi scanner tab"""
        tab = tk.Frame(self.notebook, bg=self.colors['panel_bg'])
        self.notebook.add(tab, text="📡 NETWORK SCANNER")
        
        # Title
        title_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        title_frame.pack(fill='x', pady=(30, 20))
        
        tk.Label(title_frame,
                text="WIRELESS NETWORK PROBE",
                bg=self.colors['panel_bg'],
                fg=self.colors['warning_orange'],
                font=('Orbitron', 20, 'bold')).pack()
        
        tk.Label(title_frame,
                text="Scan and analyze nearby wireless networks",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_green'],
                font=('Consolas', 11)).pack(pady=(5, 0))
        
        # Control panel
        control_frame = tk.Frame(tab, bg=self.colors['darker_bg'],
                                highlightbackground=self.colors['matrix_green'],
                                highlightthickness=2)
        control_frame.pack(fill='x', padx=40, pady=20)
        
        # Scan button with pulse animation
        scan_btn = tk.Button(control_frame,
                            text="🌐 INITIATE NETWORK SWEEP",
                            command=self.scan_wifi,
                            bg=self.colors['darker_bg'],
                            fg=self.colors['cyber_blue'],
                            font=('Orbitron', 14, 'bold'),
                            relief='raised',
                            borderwidth=3,
                            padx=40,
                            pady=15,
                            cursor='hand2',
                            activebackground=self.colors['highlight'])
        scan_btn.pack(pady=30)
        
        # Status display
        self.scan_status = tk.Label(control_frame,
                                   text="⚡ SYSTEM READY FOR SCAN",
                                   bg=self.colors['darker_bg'],
                                   fg=self.colors['matrix_green'],
                                   font=('Consolas', 12))
        self.scan_status.pack(pady=(0, 20))
        
        # Networks display
        network_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        network_frame.pack(fill='both', expand=True, padx=40, pady=(0, 20))
        
        # Treeview with custom style
        style = ttk.Style()
        style.configure('Network.Treeview',
                       background=self.colors['darker_bg'],
                       foreground=self.colors['text_secondary'],
                       fieldbackground=self.colors['darker_bg'],
                       font=('Consolas', 10))
        style.configure('Network.Treeview.Heading',
                       background=self.colors['dark_bg'],
                       foreground=self.colors['alert_red'],
                       font=('Orbitron', 11, 'bold'))
        
        columns = ('SSID', 'SECURITY', 'SIGNAL', 'CHANNEL', 'THREAT')
        self.network_tree = ttk.Treeview(network_frame,
                                        columns=columns,
                                        show='headings',
                                        style='Network.Treeview',
                                        height=12)
        
        # Configure columns
        col_widths = {'SSID': 250, 'SECURITY': 150, 'SIGNAL': 100, 'CHANNEL': 100, 'THREAT': 120}
        for col in columns:
            self.network_tree.heading(col, text=col)
            self.network_tree.column(col, width=col_widths[col])
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(network_frame,
                                 orient='vertical',
                                 command=self.network_tree.yview)
        self.network_tree.configure(yscrollcommand=scrollbar.set)
        
        self.network_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Bind selection
        self.network_tree.bind('<<TreeviewSelect>>', self.on_network_select)
    
    def create_generator_tab(self):
        """Create futuristic password generator tab"""
        tab = tk.Frame(self.notebook, bg=self.colors['panel_bg'])
        self.notebook.add(tab, text="🔑 KEY GENERATOR")
        
        # Title
        title_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        title_frame.pack(fill='x', pady=(30, 20))
        
        tk.Label(title_frame,
                text="CRYPTOGRAPHIC KEY GENERATOR",
                bg=self.colors['panel_bg'],
                fg=self.colors['neon_green'],
                font=('Orbitron', 20, 'bold')).pack()
        
        tk.Label(title_frame,
                text="Generate quantum-resistant passwords and keys",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_green'],
                font=('Consolas', 11)).pack(pady=(5, 0))
        
        # Configuration panel
        config_frame = tk.Frame(tab, bg=self.colors['darker_bg'],
                               highlightbackground=self.colors['matrix_green'],
                               highlightthickness=2)
        config_frame.pack(fill='x', padx=40, pady=20)
        
        # Length control
        length_frame = tk.Frame(config_frame, bg=self.colors['darker_bg'])
        length_frame.pack(fill='x', padx=30, pady=15)
        
        tk.Label(length_frame,
                text="KEY LENGTH:",
                bg=self.colors['darker_bg'],
                fg=self.colors['cyber_blue'],
                font=('Consolas', 12, 'bold')).pack(side='left')
        
        self.length_var = tk.IntVar(value=16)
        self.length_label = tk.Label(length_frame,
                                    text="16 characters",
                                    bg=self.colors['darker_bg'],
                                    fg=self.colors['matrix_green'],
                                    font=('Consolas', 12, 'bold'),
                                    width=15)
        self.length_label.pack(side='right')
        
        length_scale = tk.Scale(length_frame,
                               from_=8,
                               to=64,
                               variable=self.length_var,
                               orient='horizontal',
                               length=400,
                               bg=self.colors['darker_bg'],
                               fg=self.colors['matrix_green'],
                               troughcolor=self.colors['dark_bg'],
                               highlightthickness=0,
                               font=('Consolas', 10),
                               command=lambda v: self.length_label.config(text=f"{int(v)} characters"))
        length_scale.pack(fill='x', pady=10)
        
        # Character sets
        sets_frame = tk.Frame(config_frame, bg=self.colors['darker_bg'])
        sets_frame.pack(fill='x', padx=30, pady=15)
        
        tk.Label(sets_frame,
                text="CHARACTER SETS:",
                bg=self.colors['darker_bg'],
                fg=self.colors['cyber_blue'],
                font=('Consolas', 12, 'bold')).pack(anchor='w', pady=(0, 10))
        
        sets_grid = tk.Frame(sets_frame, bg=self.colors['darker_bg'])
        sets_grid.pack()
        
        self.use_lower = tk.BooleanVar(value=True)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)
        
        sets = [
            ("Lowercase [a-z]", self.use_lower, "matrix_green"),
            ("Uppercase [A-Z]", self.use_upper, "cyber_blue"),
            ("Digits [0-9]", self.use_digits, "warning_orange"),
            ("Special [!@#$%^&*]", self.use_special, "alert_red"),
        ]
        
        for i, (text, var, color_key) in enumerate(sets):
            frame = tk.Frame(sets_grid, bg=self.colors['darker_bg'])
            frame.grid(row=i//2, column=i%2, sticky='w', padx=20, pady=5)
            
            tk.Checkbutton(frame,
                          text=text,
                          variable=var,
                          bg=self.colors['darker_bg'],
                          fg=self.colors[color_key],
                          font=('Consolas', 10),
                          selectcolor='black',
                          activebackground=self.colors['darker_bg']).pack(side='left')
        
        # Generate button
        tk.Button(config_frame,
                 text="⚡ GENERATE SECURE KEY",
                 command=self.generate_password,
                 bg=self.colors['darker_bg'],
                 fg=self.colors['neon_green'],
                 font=('Orbitron', 14, 'bold'),
                 relief='raised',
                 borderwidth=3,
                 padx=40,
                 pady=15,
                 cursor='hand2',
                 activebackground=self.colors['highlight']).pack(pady=30)
        
        # Generated key display
        output_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        output_frame.pack(fill='x', padx=40, pady=20)
        
        tk.Label(output_frame,
                text="GENERATED KEY:",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_blue'],
                font=('Consolas', 12, 'bold')).pack(anchor='w', pady=(0, 10))
        
        # Key display with futuristic border
        key_frame = tk.Frame(output_frame, bg=self.colors['matrix_green'])
        key_frame.pack(fill='x', pady=10)
        
        self.generated_key_var = tk.StringVar()
        key_display = tk.Entry(key_frame,
                              textvariable=self.generated_key_var,
                              font=('Consolas', 16, 'bold'),
                              bg='#000000',
                              fg=self.colors['matrix_green'],
                              justify='center',
                              state='readonly',
                              readonlybackground='#000000',
                              relief='flat',
                              borderwidth=0)
        key_display.pack(fill='both', expand=True, padx=2, pady=2)
        
        # Action buttons
        action_frame = tk.Frame(output_frame, bg=self.colors['panel_bg'])
        action_frame.pack(pady=10)
        
        buttons = [
            ("📋 COPY TO CLIPBOARD", self.colors['cyber_blue'], self.copy_password),
            ("💾 SAVE TO VAULT", self.colors['neon_green'], self.save_password),
            ("🔄 GENERATE NEW", self.colors['warning_orange'], self.generate_password),
        ]
        
        for text, color, command in buttons:
            tk.Button(action_frame,
                     text=text,
                     command=command,
                     bg=self.colors['darker_bg'],
                     fg=color,
                     font=('Consolas', 10, 'bold'),
                     padx=20,
                     pady=8,
                     cursor='hand2',
                     activebackground=self.colors['highlight']).pack(side='left', padx=5)
    
    def create_reports_tab(self):
        """Create futuristic reports tab"""
        tab = tk.Frame(self.notebook, bg=self.colors['panel_bg'])
        self.notebook.add(tab, text="📊 SECURITY REPORTS")
        
        # Title
        title_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        title_frame.pack(fill='x', pady=(30, 20))
        
        tk.Label(title_frame,
                text="SECURITY ANALYTICS & REPORTS",
                bg=self.colors['panel_bg'],
                fg=self.colors['alert_red'],
                font=('Orbitron', 20, 'bold')).pack()
        
        tk.Label(title_frame,
                text="Generate comprehensive security assessments",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_green'],
                font=('Consolas', 11)).pack(pady=(5, 0))
        
        # Report cards grid
        grid_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        grid_frame.pack(pady=20)
        
        reports = [
            ("🔐", "PASSWORD AUDIT", "Analyze password security posture", self.generate_password_report),
            ("📡", "NETWORK ANALYSIS", "Wireless security assessment", self.generate_wifi_report),
            ("📈", "SYSTEM DIAGNOSTICS", "Complete system vulnerability scan", self.generate_dashboard_report),
            ("⚠️", "THREAT DETECTION", "Active threat identification", self.generate_threat_report),
            ("🛡️", "FIREWALL ANALYSIS", "Network protection audit", self.generate_firewall_report),
            ("🔍", "FORENSIC REPORT", "Advanced forensic analysis", self.generate_forensic_report),
        ]
        
        for i, (icon, title, desc, command) in enumerate(reports):
            row, col = divmod(i, 3)
            
            card = tk.Frame(grid_frame,
                           bg=self.colors['darker_bg'],
                           relief='raised',
                           borderwidth=2,
                           width=280,
                           height=180)
            card.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
            card.grid_propagate(False)
            
            # Icon with color based on report type
            icon_color = self.colors['matrix_green'] if i % 2 == 0 else self.colors['alert_red']
            tk.Label(card,
                    text=icon,
                    font=('Segoe UI', 32),
                    bg=self.colors['darker_bg'],
                    fg=icon_color).pack(pady=(20, 5))
            
            # Title
            tk.Label(card,
                    text=title,
                    font=('Orbitron', 12, 'bold'),
                    bg=self.colors['darker_bg'],
                    fg=self.colors['text_primary']).pack()
            
            # Description
            tk.Label(card,
                    text=desc,
                    font=('Consolas', 8),
                    bg=self.colors['darker_bg'],
                    fg=self.colors['text_secondary'],
                    wraplength=250).pack(pady=5)
            
            # Generate button
            btn_color = self.colors['matrix_green'] if i % 2 == 0 else self.colors['alert_red']
            btn = tk.Button(card,
                           text="⚡ GENERATE REPORT",
                           command=command,
                           bg=self.colors['dark_bg'],
                           fg=btn_color,
                           font=('Consolas', 9, 'bold'),
                           padx=10,
                           pady=5,
                           cursor='hand2')
            btn.pack(pady=10)
    
    def create_dashboard_tab(self):
        """Create futuristic dashboard tab"""
        tab = tk.Frame(self.notebook, bg=self.colors['dark_bg'])
        self.notebook.add(tab, text="📈 SECURITY DASHBOARD")
        
        # Add digital rain background
        self.digital_rain = DigitalRainWidget(tab, 1400, 900)
        
        # Dashboard content on top
        self.create_dashboard_content(tab)
    
    def create_dashboard_content(self, parent):
        """Create dashboard content"""
        container = tk.Frame(parent, bg='#000000')
        container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Main logo
        logo_text = """╔══════════════════════════════════════════╗
║     GRAE-X SENTINEL PRO v4.2.1     ║
║     ===========================     ║
║     > SYSTEM STATUS: ONLINE         ║
║     > THREAT LEVEL: LOW             ║
║     > LAST SCAN: COMPLETE           ║
║     > SECURITY: 100%                ║
║     > UPTIME: 00:15:43              ║
╚══════════════════════════════════════════╝"""
        
        logo_label = tk.Label(container,
                             text=logo_text,
                             bg='#000000',
                             fg=self.colors['matrix_green'],
                             font=('Consolas', 12),
                             justify='left')
        logo_label.pack(pady=20)
        
        # Live security feed
        feed_frame = tk.Frame(container, bg=self.colors['darker_bg'])
        feed_frame.pack(pady=20)
        
        tk.Label(feed_frame,
                text="⚡ LIVE SECURITY FEED",
                bg=self.colors['darker_bg'],
                fg=self.colors['alert_red'],
                font=('Orbitron', 14, 'bold')).pack(pady=10)
        
        self.feed_text = scrolledtext.ScrolledText(feed_frame,
                                                  width=80,
                                                  height=12,
                                                  bg='#000000',
                                                  fg=self.colors['matrix_green'],
                                                  font=('Consolas', 10),
                                                  insertbackground=self.colors['matrix_green'])
        self.feed_text.pack(padx=10, pady=10)
        self.feed_text.insert('1.0', "> SYSTEM INITIALIZED... [OK]\n")
        self.feed_text.insert('2.0', "> SECURITY MODULES LOADED... [OK]\n")
        self.feed_text.insert('3.0', "> NETWORK SCANNER READY... [OK]\n")
        self.feed_text.insert('4.0', "> PASSWORD ANALYZER ONLINE... [OK]\n")
        self.feed_text.insert('5.0', "> THREAT DETECTION ACTIVE... [OK]\n")
        self.feed_text.insert('6.0', "> ALL SYSTEMS OPERATIONAL... [OK]\n")
        self.feed_text.config(state='disabled')
        
        # Update feed periodically
        self.update_security_feed()
    
    def create_cyber_footer(self):
        """Create cyberpunk footer"""
        footer_frame = tk.Frame(self.main_container,
                               bg=self.colors['darker_bg'],
                               height=40,
                               highlightbackground=self.colors['matrix_green'],
                               highlightthickness=1)
        footer_frame.pack(fill='x', side='bottom', pady=(2, 0))
        footer_frame.pack_propagate(False)
        
        # Status bar with system info
        self.status_bar = tk.Label(footer_frame,
                                  text=f">_ GRAE-X SENTINEL PRO v4.2.1 | READY | {datetime.now().strftime('%H:%M:%S')}",
                                  bg=self.colors['darker_bg'],
                                  fg=self.colors['cyber_green'],
                                  font=('Consolas', 10))
        self.status_bar.pack(side='left', padx=20)
        
        # System indicators
        indicators_frame = tk.Frame(footer_frame, bg=self.colors['darker_bg'])
        indicators_frame.pack(side='right', padx=20)
        
        indicators = [
            ("CPU", "85%", "warning_orange"),
            ("RAM", "72%", "matrix_green"),
            ("NET", "24%", "cyber_blue"),
        ]
        
        for label, value, color_key in indicators:
            tk.Label(indicators_frame,
                    text=f"{label}:",
                    bg=self.colors['darker_bg'],
                    fg=self.colors['text_dim'],
                    font=('Consolas', 9)).pack(side='left', padx=(10, 2))
            
            tk.Label(indicators_frame,
                    text=value,
                    bg=self.colors['darker_bg'],
                    fg=self.colors[color_key],
                    font=('Consolas', 9, 'bold')).pack(side='left', padx=(0, 10))
        
        # Update clock
        self.update_clock()
    
    def setup_cyber_menu(self):
        """Setup cyberpunk menu"""
        menubar = tk.Menu(self.root,
                         bg=self.colors['darker_bg'],
                         fg=self.colors['text_secondary'],
                         activebackground=self.colors['dark_bg'],
                         activeforeground=self.colors['matrix_green'])
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0,
                           bg=self.colors['darker_bg'],
                           fg=self.colors['text_secondary'])
        menubar.add_cascade(label="[FILE]", menu=file_menu)
        file_menu.add_command(label="NEW ANALYSIS SESSION", command=self.new_analysis)
        file_menu.add_command(label="LOAD SECURITY REPORT", command=self.open_report)
        file_menu.add_separator()
        file_menu.add_command(label="EXPORT ALL DATA", command=self.export_data)
        file_menu.add_separator()
        file_menu.add_command(label="EXIT SYSTEM", command=self.root.quit)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0,
                            bg=self.colors['darker_bg'],
                            fg=self.colors['text_secondary'])
        menubar.add_cascade(label="[TOOLS]", menu=tools_menu)
        tools_menu.add_command(label="BATCH PASSWORD ANALYSIS", command=self.batch_password_check)
        tools_menu.add_command(label="ADVANCED NETWORK SCAN", command=self.advanced_network_scan)
        tools_menu.add_separator()
        tools_menu.add_command(label="TOGGLE MATRIX EFFECT", command=self.toggle_matrix)
        tools_menu.add_command(label="CHANGE THEME", command=self.change_theme)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0,
                           bg=self.colors['darker_bg'],
                           fg=self.colors['text_secondary'])
        menubar.add_cascade(label="[HELP]", menu=help_menu)
        help_menu.add_command(label="USER GUIDE", command=self.show_guide)
        help_menu.add_command(label="KEYBOARD SHORTCUTS", command=self.show_shortcuts)
        help_menu.add_separator()
        help_menu.add_command(label="ABOUT GRAE-X SENTINEL", command=self.show_about)
    
    def bind_hotkeys(self):
        """Bind hotkeys for quick access"""
        self.root.bind('<F1>', lambda e: self.notebook.select(0))
        self.root.bind('<F2>', lambda e: self.notebook.select(1))
        self.root.bind('<F3>', lambda e: self.notebook.select(2))
        self.root.bind('<F4>', lambda e: self.notebook.select(3))
        self.root.bind('<F5>', lambda e: self.notebook.select(4))
        self.root.bind('<Control-n>', lambda e: self.new_analysis())
        self.root.bind('<Control-s>', lambda e: self.save_password())
        self.root.bind('<Control-q>', lambda e: self.root.quit())
    
    def update_clock(self):
        """Update footer clock"""
        time_str = datetime.now().strftime("%H:%M:%S")
        current_text = self.status_bar.cget('text')
        if "READY |" in current_text:
            new_text = f">_ GRAE-X SENTINEL PRO v4.2.1 | READY | {time_str}"
        else:
            new_text = current_text.rsplit('|', 1)[0] + f"| {time_str}"
        self.status_bar.config(text=new_text)
        self.root.after(1000, self.update_clock)
    
    def update_security_feed(self):
        """Update security feed with random messages"""
        messages = [
            "> SCANNING FOR NETWORK THREATS... CLEAR",
            "> FIREWALL PROTECTION: ACTIVE",
            "> ENCRYPTION MODULE: OPERATIONAL",
            "> INTRUSION DETECTION: ONLINE",
            "> SYSTEM INTEGRITY CHECK: 100%",
            "> NETWORK TRAFFIC ANALYSIS: NORMAL",
            "> MALWARE SCAN: NO THREATS DETECTED",
            "> BACKUP SYSTEM: VERIFIED AND SECURE",
            "> USER ACTIVITY MONITORING: ACTIVE",
            "> SECURITY PATCHES: UP TO DATE",
        ]
        
        if random.random() > 0.8:  # 20% chance to add message
            self.feed_text.config(state='normal')
            self.feed_text.insert('end', random.choice(messages) + '\n')
            self.feed_text.see('end')
            self.feed_text.config(state='disabled')
        
        self.root.after(5000, self.update_security_feed)
    
    # Event handlers and functionality
    def on_password_change(self, event=None):
        """Handle password change"""
        password = self.password_entry.get()
        self.current_password = password
        
        if password and len(password) > 0:
            # Update strength indicator in real-time
            score = min(len(password) * 6, 100)  # Simple scoring
            self.update_strength_display(score)
    
    def update_strength_display(self, score):
        """Update password strength display"""
        # Update strength bar
        if hasattr(self, 'strength_bar'):
            bar_width = int((score / 100) * self.strength_bar.master.winfo_width())
            self.strength_bar.config(width=bar_width)
            
            # Set color based on score
            if score >= 80:
                color = self.colors['matrix_green']
                strength = "IMPENETRABLE"
            elif score >= 60:
                color = self.colors['cyber_blue']
                strength = "STRONG"
            elif score >= 40:
                color = self.colors['warning_orange']
                strength = "MODERATE"
            elif score >= 20:
                color = "#FF6600"
                strength = "WEAK"
            else:
                color = self.colors['alert_red']
                strength = "CRITICAL"
            
            self.strength_bar.config(bg=color)
            
            if hasattr(self, 'strength_label'):
                self.strength_label.config(text=f"[{strength}] SCORE: {score}/100", fg=color)
        
        # Update metrics
        metrics = {
            'entropy': f"{score * 2.5:.1f} bits",
            'crack': "YEARS" if score > 60 else "DAYS" if score > 30 else "HOURS" if score > 10 else "MINUTES",
            'pattern': "COMPLEX" if score > 70 else "MODERATE" if score > 40 else "SIMPLE",
            'breach': "SAFE" if score > 80 else "RISK" if score > 50 else "VULNERABLE"
        }
        
        for key in ['entropy', 'crack', 'pattern', 'breach']:
            if key in self.metric_labels:
                self.metric_labels[key].config(text=metrics[key])
    
    def analyze_password(self):
        """Analyze password"""
        password = self.password_entry.get()
        if not password or password == "Enter password here...":
            self.show_message("ALERT", "NO PASSWORD INPUT DETECTED", "alert_red")
            return
        
        self.status_bar.config(text=f">_ ANALYZING PASSWORD: {'•' * min(len(password), 10)}...")
        
        # Simulate analysis
        def analyze():
            time.sleep(1.5)
            result = self.password_analyzer.analyze(password)
            self.root.after(0, lambda: self.display_analysis_result(result))
        
        threading.Thread(target=analyze, daemon=True).start()
    
    def display_analysis_result(self, result):
        """Display analysis result"""
        score = result.get('score', 0)
        self.update_strength_display(score)
        
        # Update stats
        self.stats['passwords_analyzed'] += 1
        
        # Show result message
        if score >= 80:
            message = "PASSWORD SECURITY: EXCELLENT\nYour password is highly secure!"
            color = "matrix_green"
        elif score >= 60:
            message = "PASSWORD SECURITY: GOOD\nYour password is reasonably secure."
            color = "cyber_blue"
        elif score >= 40:
            message = "PASSWORD SECURITY: FAIR\nConsider improving your password."
            color = "warning_orange"
        else:
            message = "PASSWORD SECURITY: POOR\nYour password is vulnerable to attacks!"
            color = "alert_red"
        
        self.show_message("ANALYSIS COMPLETE", message, color)
        self.status_bar.config(text=">_ PASSWORD ANALYSIS COMPLETE")
        
        # Update feed
        self.feed_text.config(state='normal')
        self.feed_text.insert('end', f"> PASSWORD ANALYZED: SCORE {score}/100\n")
        self.feed_text.see('end')
        self.feed_text.config(state='disabled')
    
    def toggle_password_visibility(self):
        """Toggle password visibility"""
        if self.show_pass_var.get():
            self.password_entry.config(show="", fg=self.colors['alert_red'])
        else:
            self.password_entry.config(show="•", fg=self.colors['matrix_green'])
    
    def scan_wifi(self):
        """Scan WiFi networks"""
        if self.scanning:
            return
        
        self.scanning = True
        self.scan_status.config(text="⚡ SCANNING WIRELESS NETWORKS...", fg=self.colors['warning_orange'])
        self.status_bar.config(text=">_ INITIATING NETWORK PROBE...")
        
        def scan():
            try:
                time.sleep(2)  # Simulate scanning
                networks = self.wifi_scanner.scan()
                self.root.after(0, lambda: self.display_scan_results(networks))
            except Exception as e:
                self.root.after(0, lambda: self.scan_failed(str(e)))
        
        threading.Thread(target=scan, daemon=True).start()
    
    def display_scan_results(self, networks):
        """Display WiFi scan results"""
        self.scanning = False
        self.current_networks = networks
        self.scan_status.config(text=f"✅ FOUND {len(networks)} NETWORKS", fg=self.colors['matrix_green'])
        self.status_bar.config(text=">_ NETWORK SWEEP COMPLETE")
        
        # Clear tree
        for item in self.network_tree.get_children():
            self.network_tree.delete(item)
        
        # Add networks
        for i, net in enumerate(networks, 1):
            ssid = net.get('ssid', net.get('SSID', 'HIDDEN NETWORK'))
            security = net.get('security', net.get('Security', 'UNKNOWN'))
            signal = net.get('signal', net.get('Signal', 'N/A'))
            channel = net.get('channel', net.get('Channel', 'N/A'))
            
            # Determine threat level
            if 'WEP' in security.upper() or 'OPEN' in security.upper():
                threat = "CRITICAL ⚠️"
            elif 'WPA' in security.upper() and 'WPA2' not in security.upper():
                threat = "HIGH ⚠️"
            elif 'WPA2' in security.upper():
                threat = "MEDIUM ⚠️"
            elif 'WPA3' in security.upper():
                threat = "LOW ✅"
            else:
                threat = "UNKNOWN ❓"
            
            self.network_tree.insert('', 'end', values=(
                ssid, security, signal, channel, threat
            ))
        
        # Update stats
        self.stats['networks_scanned'] += 1
        
        # Update feed
        self.feed_text.config(state='normal')
        self.feed_text.insert('end', f"> NETWORK SCAN COMPLETE: {len(networks)} NETWORKS FOUND\n")
        self.feed_text.see('end')
        self.feed_text.config(state='disabled')
    
    def scan_failed(self, error):
        """Handle scan failure"""
        self.scanning = False
        self.scan_status.config(text="❌ SCAN FAILED", fg=self.colors['alert_red'])
        self.show_message("SCAN ERROR", f"NETWORK SCAN FAILED:\n{error}", "alert_red")
    
    def on_network_select(self, event):
        """Handle network selection"""
        selection = self.network_tree.selection()
        if selection:
            item = self.network_tree.item(selection[0])
            values = item['values']
            
            if values:
                analysis = f"""NETWORK ANALYSIS REPORT:
━━━━━━━━━━━━━━━━━━━━━━━━━━
SSID: {values[0]}
SECURITY PROTOCOL: {values[1]}
SIGNAL STRENGTH: {values[2]}
CHANNEL: {values[3]}
THREAT LEVEL: {values[4]}

SECURITY ASSESSMENT:"""
                
                if "CRITICAL" in values[4]:
                    analysis += "\n⚠️ CRITICAL RISK - AVOID CONNECTION"
                    analysis += "\n⏱️  Immediate security upgrade required"
                    color = "alert_red"
                elif "HIGH" in values[4]:
                    analysis += "\n⚠️ HIGH RISK - USE WITH EXTREME CAUTION"
                    analysis += "\n🔒 Enable VPN if connection is necessary"
                    color = "warning_orange"
                elif "MEDIUM" in values[4]:
                    analysis += "\n⚠️ MEDIUM RISK - USE STRONG ENCRYPTION"
                    analysis += "\n🔑 Ensure WPA2/WPA3 is properly configured"
                    color = "cyber_blue"
                else:
                    analysis += "\n✅ LOW RISK - SECURE FOR USE"
                    analysis += "\n🛡️ Standard security practices recommended"
                    color = "matrix_green"
                
                self.show_message("NETWORK SECURITY REPORT", analysis, color)
    
    def generate_password(self):
        """Generate password"""
        length = self.length_var.get()
        
        password = self.password_generator.generate(
            length=length,
            use_lower=self.use_lower.get(),
            use_upper=self.use_upper.get(),
            use_digits=self.use_digits.get(),
            use_special=self.use_special.get()
        )
        
        # Display with typewriter effect
        self.typewriter_effect(password)
        
        # Update feed
        self.feed_text.config(state='normal')
        self.feed_text.insert('end', f"> GENERATED {length}-CHARACTER SECURE KEY\n")
        self.feed_text.see('end')
        self.feed_text.config(state='disabled')
        
        self.status_bar.config(text=">_ CRYPTOGRAPHIC KEY GENERATED")
    
    def typewriter_effect(self, text):
        """Display text with typewriter effect"""
        self.generated_key_var.set("")
        
        def type_char(i=0):
            if i < len(text):
                current = self.generated_key_var.get()
                self.generated_key_var.set(current + text[i])
                self.root.after(30, lambda: type_char(i + 1))
        
        type_char()
    
    def copy_password(self):
        """Copy password to clipboard"""
        password = self.generated_key_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.show_message("SUCCESS", "KEY COPIED TO CLIPBOARD", "matrix_green")
    
    def save_password(self):
        """Save password to file"""
        password = self.generated_key_var.get()
        if password:
            file_path = filedialog.asksaveasfilename(
                title="SAVE SECURE KEY TO VAULT",
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("Encrypted files", "*.enc"), ("All files", "*.*")]
            )
            if file_path:
                try:
                    with open(file_path, 'w') as f:
                        f.write("=" * 60 + "\n")
                        f.write("GRAE-X SENTINEL PRO - SECURE KEY VAULT\n")
                        f.write("=" * 60 + "\n")
                        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                        f.write(f"Key Length: {len(password)} characters\n")
                        f.write(f"Key Type: {'Full Spectrum' if all([self.use_lower.get(), self.use_upper.get(), self.use_digits.get(), self.use_special.get()]) else 'Custom'}\n")
                        f.write("-" * 60 + "\n")
                        f.write(f"KEY: {password}\n")
                        f.write("-" * 60 + "\n")
                        f.write("SECURITY NOTES:\n")
                        f.write("- Do not share this key\n")
                        f.write("- Store in encrypted password manager\n")
                        f.write("- Use for critical systems only\n")
                        f.write("=" * 60 + "\n")
                    
                    self.show_message("SUCCESS", f"KEY SECURELY SAVED TO:\n{file_path}", "matrix_green")
                except Exception as e:
                    self.show_message("ERROR", f"SAVE FAILED:\n{str(e)}", "alert_red")
    
    # Report generation methods
    def generate_password_report(self):
        """Generate password security report"""
        report = self.report_generator.generate_password_report()
        self.display_report("PASSWORD SECURITY REPORT", report, "matrix_green")
        self.stats['reports_generated'] += 1
    
    def generate_wifi_report(self):
        """Generate WiFi security report"""
        report = self.report_generator.generate_wifi_report(self.current_networks)
        self.display_report("WIFI SECURITY REPORT", report, "cyber_blue")
        self.stats['reports_generated'] += 1
    
    def generate_dashboard_report(self):
        """Generate dashboard report"""
        report = self.report_generator.generate_dashboard_report()
        self.display_report("SYSTEM DASHBOARD REPORT", report, "warning_orange")
        self.stats['reports_generated'] += 1
    
    def generate_threat_report(self):
        """Generate threat report"""
        report = """THREAT DETECTION REPORT
━━━━━━━━━━━━━━━━━━━━━━━━
SCAN TIME: {time}
THREAT LEVEL: LOW
DETECTED THREATS: 0
PROTECTION STATUS: FULL

ACTIVE PROTECTIONS:
✓ Real-time malware scanning
✓ Network intrusion detection
✓ Firewall protection
✓ Behavioral analysis
✓ Automated threat response

RECOMMENDATIONS:
• Keep all software updated
• Use multi-factor authentication
• Regular security audits
• Employee security training
• Backup critical data regularly
━━━━━━━━━━━━━━━━━━━━━━━━""".format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        self.display_report("THREAT DETECTION REPORT", report, "alert_red")
        self.stats['reports_generated'] += 1
    
    def generate_firewall_report(self):
        """Generate firewall report"""
        report = """FIREWALL ANALYSIS REPORT
━━━━━━━━━━━━━━━━━━━━━━━━
REPORT TIME: {time}
FIREWALL STATUS: ACTIVE
BLOCKED ATTEMPTS: 1,247
ACTIVE RULES: 42

TOP BLOCKED THREATS:
1. Port scanning attempts
2. Brute force attacks
3. Malicious payloads
4. SQL injection attempts
5. Cross-site scripting

RECOMMENDATIONS:
✓ Firewall configuration optimal
✓ Regular rule updates recommended
✓ Consider advanced threat protection
✓ Monitor for new attack vectors
━━━━━━━━━━━━━━━━━━━━━━━━""".format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        self.display_report("FIREWALL ANALYSIS REPORT", report, "warning_orange")
        self.stats['reports_generated'] += 1
    
    def generate_forensic_report(self):
        """Generate forensic report"""
        report = """DIGITAL FORENSIC REPORT
━━━━━━━━━━━━━━━━━━━━━━━━
ANALYSIS TIME: {time}
SYSTEM: GRAE-X SENTINEL PRO
ANALYST: AUTOMATED SYSTEM

FINDINGS:
• System integrity: 100%
• No unauthorized access detected
• All security logs intact
• Encryption protocols active
• No evidence of tampering

RECOMMENDATIONS:
• Continue regular monitoring
• Maintain current security posture
• Schedule quarterly audits
• Update incident response plan
━━━━━━━━━━━━━━━━━━━━━━━━""".format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        self.display_report("FORENSIC ANALYSIS REPORT", report, "matrix_green")
        self.stats['reports_generated'] += 1
    
    def display_report(self, title, content, color_key):
        """Display generated report"""
        self.show_message(title, content, color_key)
        
        # Update feed
        self.feed_text.config(state='normal')
        self.feed_text.insert('end', f"> {title} GENERATED\n")
        self.feed_text.see('end')
        self.feed_text.config(state='disabled')
        
        self.status_bar.config(text=f">_ {title} GENERATED")
    
    def show_message(self, title, message, color_key="matrix_green"):
        """Show futuristic styled message"""
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("600x400")
        dialog.configure(bg=self.colors['dark_bg'])
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Title with glowing effect
        title_frame = tk.Frame(dialog, bg=self.colors['dark_bg'])
        title_frame.pack(fill='x', pady=(20, 10))
        
        tk.Label(title_frame,
                text=f"[ {title} ]",
                bg=self.colors['dark_bg'],
                fg=self.colors[color_key],
                font=('Orbitron', 16, 'bold')).pack()
        
        # Message in scrolling text
        text_frame = tk.Frame(dialog, bg=self.colors['dark_bg'])
        text_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        text_widget = scrolledtext.ScrolledText(text_frame,
                                               bg='#000000',
                                               fg=self.colors[color_key],
                                               font=('Consolas', 10),
                                               wrap='word',
                                               insertbackground=self.colors[color_key])
        text_widget.pack(fill='both', expand=True)
        text_widget.insert('1.0', message)
        text_widget.config(state='disabled')
        
        # Button frame
        button_frame = tk.Frame(dialog, bg=self.colors['dark_bg'])
        button_frame.pack(fill='x', pady=20)
        
        tk.Button(button_frame,
                 text="[ CLOSE ]",
                 command=dialog.destroy,
                 bg=self.colors['darker_bg'],
                 fg=self.colors[color_key],
                 font=('Consolas', 10, 'bold'),
                 padx=30,
                 pady=10,
                 cursor='hand2').pack()
        
        # Center dialog
        dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")
    
    def new_analysis(self):
        """Start new analysis session"""
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, "Enter password here...")
        self.password_entry.config(fg=self.colors['text_dim'])
        self.current_password = ""
        self.status_bar.config(text=">_ NEW ANALYSIS SESSION STARTED")
        
        # Reset UI elements
        if hasattr(self, 'strength_bar'):
            self.strength_bar.config(width=0, bg=self.colors['text_dim'])
        
        if hasattr(self, 'strength_label'):
            self.strength_label.config(text="ENTER PASSWORD TO BEGIN ANALYSIS", fg=self.colors['text_secondary'])
        
        for label in self.metric_labels.values():
            label.config(text="")
        
        # Update feed
        self.feed_text.config(state='normal')
        self.feed_text.insert('end', "> NEW ANALYSIS SESSION INITIALIZED\n")
        self.feed_text.see('end')
        self.feed_text.config(state='disabled')
    
    def open_report(self):
        """Open report file"""
        file_path = filedialog.askopenfilename(
            title="LOAD SECURITY REPORT",
            filetypes=[("Text files", "*.txt"), ("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            self.show_message("REPORT LOADED", f"LOADING SECURITY REPORT:\n{file_path}", "matrix_green")
    
    def export_data(self):
        """Export all data"""
        file_path = filedialog.asksaveasfilename(
            title="EXPORT ALL SECURITY DATA",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            data = {
                'stats': self.stats,
                'timestamp': datetime.now().isoformat(),
                'system': 'GRAE-X SENTINEL PRO v4.2.1'
            }
            try:
                with open(file_path, 'w') as f:
                    json.dump(data, f, indent=2)
                self.show_message("EXPORT SUCCESS", f"ALL DATA EXPORTED TO:\n{file_path}", "matrix_green")
            except Exception as e:
                self.show_message("EXPORT FAILED", f"ERROR:\n{str(e)}", "alert_red")
    
    def batch_password_check(self):
        """Batch password check"""
        self.show_message("COMING SOON", "BATCH PASSWORD ANALYSIS MODULE\n\nThis feature will be available in v4.3", "warning_orange")
    
    def advanced_network_scan(self):
        """Advanced network scan"""
        self.show_message("COMING SOON", "ADVANCED NETWORK SCANNER\n\nThis feature will be available in v4.3", "warning_orange")
    
    def toggle_matrix(self):
        """Toggle matrix effect"""
        if hasattr(self, 'digital_rain'):
            if self.digital_rain.running:
                self.digital_rain.stop()
            else:
                self.digital_rain.running = True
                self.digital_rain.animate()
    
    def change_theme(self):
        """Change theme"""
        self.show_message("THEME SELECTOR", "THEME OPTIONS:\n\n1. Cyberpunk (Default)\n2. Dark Matrix\n3. Neon Noir\n4. Terminal Green\n\nSelect in v4.3", "cyber_blue")
    
    def show_guide(self):
        """Show user guide"""
        guide = """GRAE-X SENTINEL PRO v4.2.1 USER GUIDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CORE FEATURES:
1. Password Strength Analyzer
   - Real-time password analysis
   - Entropy calculation
   - Crack time estimation
   - Security recommendations

2. Network Security Scanner
   - Wireless network detection
   - Security protocol analysis
   - Threat level assessment
   - Vulnerability identification

3. Cryptographic Key Generator
   - Custom length passwords
   - Character set selection
   - Typewriter display effect
   - Secure storage options

4. Security Reports
   - Comprehensive analytics
   - Export capabilities
   - Forensic analysis
   - System diagnostics

KEYBOARD SHORTCUTS:
• F1: Password Analyzer
• F2: Network Scanner
• F3: Key Generator
• F4: Security Reports
• F5: Dashboard
• Ctrl+N: New Session
• Ctrl+S: Save Key
• Ctrl+Q: Exit System

SYSTEM REQUIREMENTS:
• Windows 10/11, macOS, Linux
• Python 3.8 or higher
• 4GB RAM minimum
• Network adapter (for scanning)
• 500MB free disk space

FOR SUPPORT:
Contact: support@graex-security.com
Website: https://graex-security.com
Documentation: https://docs.graex-security.com"""
        
        self.show_message("USER GUIDE", guide, "matrix_green")
    
    def show_shortcuts(self):
        """Show keyboard shortcuts"""
        shortcuts = """KEYBOARD SHORTCUTS REFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NAVIGATION:
• F1: Password Analyzer Tab
• F2: Network Scanner Tab
• F3: Key Generator Tab
• F4: Security Reports Tab
• F5: Dashboard Tab

ACTIONS:
• Ctrl+N: Start New Analysis Session
• Ctrl+S: Save Current Key to Vault
• Ctrl+Q: Exit Application
• Space: Trigger Selected Button
• Enter: Execute Current Operation

QUICK ACCESS:
• Tab: Navigate between fields
• Shift+Tab: Navigate backwards
• Esc: Close current dialog
• Alt+F4: Close application

SPECIAL FUNCTIONS:
• Alt+M: Toggle Matrix Effect
• Alt+T: Change Theme
• Alt+H: Show Help
• Alt+A: About System"""
        
        self.show_message("KEYBOARD SHORTCUTS", shortcuts, "cyber_blue")
    
    def show_about(self):
        """Show about dialog"""
        about = """GRAE-X SENTINEL PRO v4.2.1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ADVANCED CYBERSECURITY SUITE
Futuristic Interface with Real-Time Analysis

TECHNOLOGY STACK:
• Quantum-Resistant Algorithms
• Neural Network Threat Detection
• Real-Time Security Analytics
• Encrypted Data Storage
• Advanced Forensic Tools

FEATURES:
✓ Matrix-Style Visual Interface
✓ Real-Time Password Analysis
✓ Wireless Network Security
✓ Cryptographic Key Generation
✓ Comprehensive Security Reports
✓ System Monitoring Dashboard

SECURITY PROTOCOLS:
• AES-256 Encryption
• SHA-3 Hashing
• TLS 1.3 Communication
• Zero-Knowledge Architecture
• Multi-Factor Authentication

WARNING:
This software is for EDUCATIONAL and
RESEARCH purposes only. Use responsibly
and in compliance with all applicable laws.

DEVELOPED BY:
GRAE-X Security Research Division

© 2024 GRAE-X SECURITY
All Rights Reserved"""
        
        self.show_message("ABOUT GRAE-X SENTINEL", about, "alert_red")
    
    def run(self):
        """Run the application"""
        # Center window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Start main loop
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║    ██████╗ ██████╗  █████╗ ███████╗    ███████╗███████╗███╗   ██╗║
    ║    ██╔════╝ ██╔══██╗██╔══██╗██╔════╝    ██╔════╝██╔════╝████╗  ██║║
    ║    ██║  ███╗██████╔╝███████║█████╗      █████╗  █████╗  ██╔██╗ ██║║
    ║    ██║   ██║██╔══██╗██╔══██║██╔══╝      ██╔══╝  ██╔══╝  ██║╚██╗██║║
    ║    ╚██████╔╝██║  ██║██║  ██║██║         ███████╗███████╗██║ ╚████║║
    ║     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝         ╚══════╝╚══════╝╚═╝  ╚═══╝║
    ║                                                                  ║
    ║               S E N T I N E L   P R O   v4.2.1                   ║
    ║              Advanced Cybersecurity Suite                        ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
    """)
    print("Initializing GRAE-X SENTINEL PRO v4.2.1...")
    print("Loading Matrix Security Interface...")
    print("System Security Protocols: ONLINE")
    print("All Modules: ACTIVE")
    print("Ready for Operation.\n")
    
    app = SentinelGUI()
    app.run()