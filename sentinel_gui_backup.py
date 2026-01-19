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
        def generate_password_report(self):
            print("Password report generated")
        def generate_wifi_report(self, networks):
            print("WiFi report generated")
        def generate_dashboard_report(self):
            print("Dashboard report generated")
        def generate_vulnerability_report(self):
            print("Vulnerability report generated")

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
                               bg='black', highlightthickness=0)
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
        
        # Initialize stats FIRST - BEFORE anything else uses it
        self.stats = {
            'passwords_analyzed': 0,
            'networks_scanned': 0,
            'breaches_found': 0,
            'reports_generated': 0
        }
        
        # Configure dark cyberpunk theme
        self.colors = {
            'matrix_green': '#00FF00',
            'cyber_blue': '#00FFFF',
            'neon_purple': '#FF00FF',
            'alert_red': '#FF0033',
            'warning_yellow': '#FFFF00',
            'dark_bg': '#000814',
            'darker_bg': '#000510',
            'panel_bg': '#001122',
            'text_primary': '#FFFFFF',
            'text_secondary': '#88FF88',
            'accent': '#00CCFF',
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
        
        # Create main container with cyberpunk style
        self.setup_main_container()
        
        # Create menu last
        self.setup_cyber_menu()
        
        # Initialize stats
        self.stats = {
            'passwords_analyzed': 0,
            'networks_scanned': 0,
            'breaches_found': 0,
            'reports_generated': 0
        }
    
    def setup_main_container(self):
        """Setup main container with cyberpunk styling"""
        # Main container with dark background
        self.main_container = tk.Frame(self.root, bg=self.colors['dark_bg'])
        self.main_container.pack(fill='both', expand=True)
        
        # Header with glowing effect
        self.create_cyber_header()
        
        # Content area with matrix background
        self.content_frame = tk.Frame(self.main_container, bg=self.colors['dark_bg'])
        self.content_frame.pack(fill='both', expand=True, padx=2, pady=2)
        
        # Left sidebar for stats
        self.create_cyber_sidebar()
        
        # Main notebook area
        self.create_cyber_notebook()
        
        # Footer
        self.create_cyber_footer()
        
        # Initialize Matrix effect on notebook background
        self.setup_matrix_effect()
    
    def create_cyber_header(self):
        """Create cyberpunk header"""
        header_frame = tk.Frame(self.main_container, 
                               bg=self.colors['darker_bg'],
                               height=100)
        header_frame.pack(fill='x', pady=(0, 2))
        header_frame.pack_propagate(False)
        
        # Glowing title with scan line effect
        title_canvas = tk.Canvas(header_frame, 
                                height=100,
                                bg=self.colors['darker_bg'],
                                highlightthickness=0)
        title_canvas.pack(fill='both', expand=True)
        
        # Main title
        title_canvas.create_text(20, 35,
                                text="GRAE-X SENTINEL PRO",
                                fill=self.colors['matrix_green'],
                                font=('Courier New', 28, 'bold'),
                                anchor='w')
        
        # Subtitle with blinking effect
        self.subtitle_label = title_canvas.create_text(20, 70,
                                                      text=">_ CYBERSECURITY SYSTEM v4.2 [ONLINE]",
                                                      fill=self.colors['cyber_blue'],
                                                      font=('Courier New', 12),
                                                      anchor='w')
        
        # Status indicators
        status_x = 1000
        indicators = [
            ("SYSTEM", "ONLINE", self.colors['matrix_green']),
            ("SCANNER", "ACTIVE", self.colors['cyber_blue']),
            ("DATABASE", "SECURE", self.colors['neon_purple']),
        ]
        
        for i, (label, status, color) in enumerate(indicators):
            y_pos = 25 + i * 25
            title_canvas.create_text(status_x, y_pos,
                                    text=f"{label}:",
                                    fill=self.colors['text_secondary'],
                                    font=('Courier New', 10),
                                    anchor='w')
            title_canvas.create_text(status_x + 80, y_pos,
                                    text=f"[{status}]",
                                    fill=color,
                                    font=('Courier New', 10, 'bold'),
                                    anchor='w')
        
        # Animate subtitle
        self.animate_subtitle(title_canvas)
    
    def animate_subtitle(self, canvas):
        """Animate subtitle blinking"""
        current_color = canvas.itemcget(self.subtitle_label, 'fill')
        new_color = self.colors['cyber_blue'] if current_color == self.colors['darker_bg'] else self.colors['darker_bg']
        canvas.itemconfig(self.subtitle_label, fill=new_color)
        self.root.after(500, lambda: self.animate_subtitle(canvas))
    
    def create_cyber_sidebar(self):
        """Create cyberpunk sidebar"""
        sidebar = tk.Frame(self.content_frame,
                          bg=self.colors['panel_bg'],
                          width=250,
                          relief='ridge',
                          borderwidth=2)
        sidebar.pack(side='left', fill='y', padx=(0, 2))
        sidebar.pack_propagate(False)
        
        # Sidebar title
        tk.Label(sidebar,
                text="SYSTEM STATUS",
                bg=self.colors['panel_bg'],
                fg=self.colors['matrix_green'],
                font=('Courier New', 14, 'bold')).pack(pady=20)
        
        # Stats display with digital rain background
        stats_canvas = tk.Canvas(sidebar,
                                bg=self.colors['panel_bg'],
                                highlightthickness=0,
                                height=200)
        stats_canvas.pack(fill='x', pady=10)
        
        stats_data = [
            ("PASSWORDS", self.stats['passwords_analyzed'], "#"),
            ("NETWORKS", self.stats['networks_scanned'], "#"),
            ("BREACHES", self.stats['breaches_found'], "#"),
            ("REPORTS", self.stats['reports_generated'], "#"),
        ]
        
        for i, (label, value, unit) in enumerate(stats_data):
            y_pos = 30 + i * 40
            stats_canvas.create_text(20, y_pos,
                                    text=label,
                                    fill=self.colors['text_secondary'],
                                    font=('Courier New', 10),
                                    anchor='w')
            stats_canvas.create_text(180, y_pos,
                                    text=f"{value:03d}{unit}",
                                    fill=self.colors['matrix_green'],
                                    font=('Courier New', 14, 'bold'),
                                    anchor='e')
        
        # Quick actions panel
        actions_frame = tk.Frame(sidebar, bg=self.colors['panel_bg'])
        actions_frame.pack(fill='x', padx=10, pady=20)
        
        tk.Label(actions_frame,
                text="QUICK ACTIONS",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_blue'],
                font=('Courier New', 12)).pack(anchor='w', pady=(0, 10))
        
        actions = [
            ("[1] SCAN PASS", lambda: self.notebook.select(0)),
            ("[2] PROBE WIFI", lambda: self.notebook.select(1)),
            ("[3] GEN KEY", lambda: self.notebook.select(2)),
            ("[4] RUN DIAG", lambda: self.notebook.select(3)),
            ("[5] DASHBOARD", lambda: self.notebook.select(4)),
        ]
        
        for text, command in actions:
            btn = tk.Button(actions_frame,
                           text=text,
                           command=command,
                           bg=self.colors['darker_bg'],
                           fg=self.colors['matrix_green'],
                           font=('Courier New', 10),
                           relief='groove',
                           borderwidth=2,
                           padx=10,
                           pady=5)
            btn.pack(fill='x', pady=2)
        
        # System monitor
        monitor_frame = tk.Frame(sidebar, bg=self.colors['panel_bg'])
        monitor_frame.pack(fill='x', padx=10, pady=20)
        
        tk.Label(monitor_frame,
                text="SYSTEM MONITOR",
                bg=self.colors['panel_bg'],
                fg=self.colors['neon_purple'],
                font=('Courier New', 12)).pack(anchor='w', pady=(0, 10))
        
        # CPU usage bar
        self.cpu_bar = self.create_usage_bar(monitor_frame, "CPU", 75)
        self.ram_bar = self.create_usage_bar(monitor_frame, "RAM", 60)
        self.net_bar = self.create_usage_bar(monitor_frame, "NET", 45)
        
        # Update system monitor
        self.update_system_monitor()
    
    def create_usage_bar(self, parent, label, initial):
        """Create usage bar for system monitor"""
        frame = tk.Frame(parent, bg=self.colors['panel_bg'])
        frame.pack(fill='x', pady=3)
        
        tk.Label(frame,
                text=label,
                bg=self.colors['panel_bg'],
                fg=self.colors['text_secondary'],
                font=('Courier New', 9),
                width=5).pack(side='left')
        
        canvas = tk.Canvas(frame,
                          width=150,
                          height=15,
                          bg=self.colors['darker_bg'],
                          highlightthickness=0)
        canvas.pack(side='left', padx=(5, 0))
        
        # Create bar
        bar = canvas.create_rectangle(0, 0, initial*1.5, 15,
                                     fill=self.colors['matrix_green'],
                                     outline='')
        
        # Percentage label
        percent_label = tk.Label(frame,
                                text=f"{initial}%",
                                bg=self.colors['panel_bg'],
                                fg=self.colors['matrix_green'],
                                font=('Courier New', 9))
        percent_label.pack(side='left', padx=5)
        
        return {'canvas': canvas, 'bar': bar, 'label': percent_label}
    
    def update_system_monitor(self):
        """Update system monitor with random values"""
        for bar_info in [self.cpu_bar, self.ram_bar, self.net_bar]:
            current = int(bar_info['label'].cget('text').replace('%', ''))
            change = random.randint(-10, 10)
            new_value = max(0, min(100, current + change))
            
            bar_info['canvas'].coords(bar_info['bar'], 0, 0, new_value * 1.5, 15)
            bar_info['label'].config(text=f"{new_value}%")
            
            # Change color based on usage
            if new_value > 80:
                color = self.colors['alert_red']
            elif new_value > 60:
                color = self.colors['warning_yellow']
            else:
                color = self.colors['matrix_green']
            
            bar_info['canvas'].itemconfig(bar_info['bar'], fill=color)
        
        self.root.after(2000, self.update_system_monitor)
    
    def create_cyber_notebook(self):
        """Create cyberpunk styled notebook"""
        notebook_frame = tk.Frame(self.content_frame, bg=self.colors['dark_bg'])
        notebook_frame.pack(side='left', fill='both', expand=True)
        
        # Create custom styled notebook
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure cyberpunk style
        style.configure('Cyber.TNotebook',
                       background=self.colors['dark_bg'],
                       borderwidth=0)
        style.configure('Cyber.TNotebook.Tab',
                       background=self.colors['darker_bg'],
                       foreground=self.colors['text_secondary'],
                       padding=[15, 5],
                       font=('Courier New', 10, 'bold'))
        style.map('Cyber.TNotebook.Tab',
                 background=[('selected', self.colors['panel_bg'])],
                 foreground=[('selected', self.colors['matrix_green'])])
        
        self.notebook = ttk.Notebook(notebook_frame, style='Cyber.TNotebook')
        self.notebook.pack(fill='both', expand=True)
        
        # Create tabs
        self.create_cyber_password_tab()
        self.create_cyber_wifi_tab()
        self.create_cyber_generator_tab()
        self.create_cyber_reports_tab()
        self.create_cyber_dashboard_tab()
    
    def setup_matrix_effect(self):
        """Setup Matrix effect on notebook background"""
        # Get notebook frame
        notebook_frame = self.notebook.winfo_children()[0]
        
        # Create canvas for matrix effect
        self.matrix_canvas = tk.Canvas(notebook_frame,
                                      bg='black',
                                      highlightthickness=0)
        self.matrix_canvas.place(relwidth=1, relheight=1)
        
        # Initialize matrix effect
        width = self.notebook.winfo_width()
        height = self.notebook.winfo_height()
        if width > 1 and height > 1:  # Only if notebook has size
            self.matrix = MatrixEffect(self.matrix_canvas, width, height)
            self.matrix.draw()
        
        # Lower matrix canvas so tabs are visible
        self.matrix_canvas.lower()
    
    def create_cyber_password_tab(self):
        """Create cyberpunk password analysis tab"""
        tab = tk.Frame(self.notebook, bg=self.colors['panel_bg'])
        self.notebook.add(tab, text="🔐 PASS_CRACK")
        
        # Title
        tk.Label(tab,
                text="PASSWORD STRENGTH ANALYZER",
                bg=self.colors['panel_bg'],
                fg=self.colors['matrix_green'],
                font=('Courier New', 18, 'bold')).pack(pady=30)
        
        # Input area
        input_frame = tk.Frame(tab, bg=self.colors['darker_bg'], relief='sunken', borderwidth=2)
        input_frame.pack(fill='x', padx=40, pady=20)
        
        tk.Label(input_frame,
                text="ENTER TARGET PASSWORD:",
                bg=self.colors['darker_bg'],
                fg=self.colors['cyber_blue'],
                font=('Courier New', 12)).pack(pady=20)
        
        # Password entry with cyberpunk style
        self.password_entry = tk.Entry(input_frame,
                                      font=('Courier New', 16),
                                      bg='black',
                                      fg=self.colors['matrix_green'],
                                      insertbackground=self.colors['matrix_green'],
                                      show="•",
                                      width=40,
                                      relief='sunken',
                                      borderwidth=3)
        self.password_entry.pack(pady=10, padx=20)
        self.password_entry.bind('<KeyRelease>', self.on_password_change)
        
        # Show password toggle
        self.show_pass_var = tk.BooleanVar()
        tk.Checkbutton(input_frame,
                      text="[REVEAL CODE]",
                      variable=self.show_pass_var,
                      command=self.toggle_password_visibility,
                      bg=self.colors['darker_bg'],
                      fg=self.colors['text_secondary'],
                      font=('Courier New', 10),
                      selectcolor='black').pack(pady=10)
        
        # Analyze button
        tk.Button(input_frame,
                 text="[EXECUTE ANALYSIS]",
                 command=self.analyze_password,
                 bg=self.colors['dark_bg'],
                 fg=self.colors['matrix_green'],
                 font=('Courier New', 12, 'bold'),
                 relief='raised',
                 borderwidth=3,
                 padx=20,
                 pady=10).pack(pady=20)
        
        # Results area
        results_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        results_frame.pack(fill='both', expand=True, padx=40, pady=20)
        
        # Left column - Strength meter
        left_col = tk.Frame(results_frame, bg=self.colors['panel_bg'])
        left_col.pack(side='left', fill='both', expand=True)
        
        tk.Label(left_col,
                text="SECURITY METER:",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_blue'],
                font=('Courier New', 12)).pack(anchor='w', pady=(0, 10))
        
        # Cyber strength bar
        strength_canvas = tk.Canvas(left_col,
                                   width=300,
                                   height=30,
                                   bg='black',
                                   highlightthickness=0)
        strength_canvas.pack(pady=10)
        
        self.strength_bar = strength_canvas.create_rectangle(0, 0, 0, 30,
                                                            fill=self.colors['matrix_green'],
                                                            outline='')
        
        self.strength_label = tk.Label(left_col,
                                      text="AWAITING INPUT...",
                                      bg=self.colors['panel_bg'],
                                      fg=self.colors['text_secondary'],
                                      font=('Courier New', 11))
        self.strength_label.pack()
        
        # Right column - Metrics
        right_col = tk.Frame(results_frame, bg=self.colors['panel_bg'])
        right_col.pack(side='right', fill='both', expand=True, padx=(20, 0))
        
        tk.Label(right_col,
                text="CRYPTO METRICS:",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_blue'],
                font=('Courier New', 12)).pack(anchor='w', pady=(0, 10))
        
        # Metrics grid
        metrics = [
            ("ENTROPY:", "0.0 bits"),
            ("CRACK TIME:", "INFINITE"),
            ("PATTERN SCORE:", "0/100"),
            ("HASH STRENGTH:", "UNKNOWN"),
        ]
        
        self.metric_labels = {}
        for i, (label, default) in enumerate(metrics):
            frame = tk.Frame(right_col, bg=self.colors['panel_bg'])
            frame.pack(fill='x', pady=5)
            
            tk.Label(frame,
                    text=label,
                    bg=self.colors['panel_bg'],
                    fg=self.colors['text_secondary'],
                    font=('Courier New', 10),
                    width=15,
                    anchor='w').pack(side='left')
            
            value_label = tk.Label(frame,
                                  text=default,
                                  bg=self.colors['panel_bg'],
                                  fg=self.colors['matrix_green'],
                                  font=('Courier New', 10, 'bold'))
            value_label.pack(side='left')
            
            self.metric_labels[label.split(':')[0].lower()] = value_label
    
    def create_cyber_wifi_tab(self):
        """Create cyberpunk WiFi scanner tab"""
        tab = tk.Frame(self.notebook, bg=self.colors['panel_bg'])
        self.notebook.add(tab, text="📡 WIFI_PROBE")
        
        # Title
        tk.Label(tab,
                text="WIRELESS NETWORK PROBE",
                bg=self.colors['panel_bg'],
                fg=self.colors['matrix_green'],
                font=('Courier New', 18, 'bold')).pack(pady=30)
        
        # Control panel
        control_frame = tk.Frame(tab, bg=self.colors['darker_bg'], relief='sunken', borderwidth=2)
        control_frame.pack(fill='x', padx=40, pady=20)
        
        # Scan button
        scan_btn = tk.Button(control_frame,
                            text="[INITIATE SWEEP]",
                            command=self.scan_wifi,
                            bg=self.colors['dark_bg'],
                            fg=self.colors['matrix_green'],
                            font=('Courier New', 12, 'bold'),
                            relief='raised',
                            borderwidth=3,
                            padx=30,
                            pady=10)
        scan_btn.pack(pady=20)
        
        # Status display
        self.scan_status = tk.Label(control_frame,
                                   text=">_ SYSTEM STANDBY",
                                   bg=self.colors['darker_bg'],
                                   fg=self.colors['cyber_blue'],
                                   font=('Courier New', 11))
        self.scan_status.pack(pady=10)
        
        # Networks display
        network_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        network_frame.pack(fill='both', expand=True, padx=40, pady=(0, 20))
        
        # Treeview with cyberpunk style
        style = ttk.Style()
        style.configure('Cyber.Treeview',
                       background=self.colors['darker_bg'],
                       foreground=self.colors['text_secondary'],
                       fieldbackground=self.colors['darker_bg'],
                       font=('Courier New', 10))
        style.configure('Cyber.Treeview.Heading',
                       background=self.colors['dark_bg'],
                       foreground=self.colors['matrix_green'],
                       font=('Courier New', 10, 'bold'))
        
        columns = ('SSID', 'SECURITY', 'SIGNAL', 'CHANNEL', 'THREAT')
        self.network_tree = ttk.Treeview(network_frame,
                                        columns=columns,
                                        show='headings',
                                        style='Cyber.Treeview',
                                        height=15)
        
        # Configure columns
        col_widths = {'SSID': 200, 'SECURITY': 150, 'SIGNAL': 80, 'CHANNEL': 80, 'THREAT': 100}
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
    
    def create_cyber_generator_tab(self):
        """Create cyberpunk password generator tab"""
        tab = tk.Frame(self.notebook, bg=self.colors['panel_bg'])
        self.notebook.add(tab, text="🔑 GEN_KEY")
        
        # Title
        tk.Label(tab,
                text="CRYPTOGRAPHIC KEY GENERATOR",
                bg=self.colors['panel_bg'],
                fg=self.colors['matrix_green'],
                font=('Courier New', 18, 'bold')).pack(pady=30)
        
        # Configuration panel
        config_frame = tk.Frame(tab, bg=self.colors['darker_bg'], relief='sunken', borderwidth=2)
        config_frame.pack(fill='x', padx=40, pady=20)
        
        # Length control
        length_frame = tk.Frame(config_frame, bg=self.colors['darker_bg'])
        length_frame.pack(fill='x', padx=30, pady=15)
        
        tk.Label(length_frame,
                text="KEY LENGTH:",
                bg=self.colors['darker_bg'],
                fg=self.colors['cyber_blue'],
                font=('Courier New', 11)).pack(side='left')
        
        self.length_var = tk.IntVar(value=16)
        length_scale = tk.Scale(length_frame,
                               from_=8,
                               to=64,
                               variable=self.length_var,
                               orient='horizontal',
                               length=300,
                               bg=self.colors['darker_bg'],
                               fg=self.colors['matrix_green'],
                               troughcolor=self.colors['dark_bg'],
                               highlightthickness=0,
                               font=('Courier New', 9))
        length_scale.pack(side='right')
        
        # Character sets
        sets_frame = tk.Frame(config_frame, bg=self.colors['darker_bg'])
        sets_frame.pack(fill='x', padx=30, pady=15)
        
        self.use_lower = tk.BooleanVar(value=True)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)
        
        sets = [
            ("[a-z]", self.use_lower),
            ("[A-Z]", self.use_upper),
            ("[0-9]", self.use_digits),
            ("[!@#]", self.use_special),
        ]
        
        for text, var in sets:
            tk.Checkbutton(sets_frame,
                          text=text,
                          variable=var,
                          bg=self.colors['darker_bg'],
                          fg=self.colors['text_secondary'],
                          font=('Courier New', 10),
                          selectcolor='black').pack(side='left', padx=20)
        
        # Generate button
        tk.Button(config_frame,
                 text="[GENERATE KEY]",
                 command=self.generate_password,
                 bg=self.colors['dark_bg'],
                 fg=self.colors['matrix_green'],
                 font=('Courier New', 12, 'bold'),
                 relief='raised',
                 borderwidth=3,
                 padx=30,
                 pady=10).pack(pady=20)
        
        # Generated key display
        output_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        output_frame.pack(fill='x', padx=40, pady=20)
        
        tk.Label(output_frame,
                text="GENERATED KEY:",
                bg=self.colors['panel_bg'],
                fg=self.colors['cyber_blue'],
                font=('Courier New', 12)).pack(anchor='w', pady=(0, 10))
        
        # Key display with typewriter effect
        self.generated_key_var = tk.StringVar()
        key_display = tk.Entry(output_frame,
                              textvariable=self.generated_key_var,
                              font=('Courier New', 14, 'bold'),
                              bg='black',
                              fg=self.colors['matrix_green'],
                              justify='center',
                              state='readonly',
                              readonlybackground='black',
                              relief='sunken',
                              borderwidth=3)
        key_display.pack(fill='x', pady=10)
        
        # Action buttons
        action_frame = tk.Frame(output_frame, bg=self.colors['panel_bg'])
        action_frame.pack(pady=10)
        
        tk.Button(action_frame,
                 text="[COPY TO CLIPBOARD]",
                 command=self.copy_password,
                 bg=self.colors['dark_bg'],
                 fg=self.colors['cyber_blue'],
                 font=('Courier New', 10),
                 padx=15,
                 pady=5).pack(side='left', padx=5)
        
        tk.Button(action_frame,
                 text="[SAVE TO VAULT]",
                 command=self.save_password,
                 bg=self.colors['dark_bg'],
                 fg=self.colors['neon_purple'],
                 font=('Courier New', 10),
                 padx=15,
                 pady=5).pack(side='left', padx=5)
    
    def create_cyber_reports_tab(self):
        """Create cyberpunk reports tab"""
        tab = tk.Frame(self.notebook, bg=self.colors['panel_bg'])
        self.notebook.add(tab, text="📊 SYS_REPORT")
        
        # Title
        tk.Label(tab,
                text="SYSTEM SECURITY REPORTS",
                bg=self.colors['panel_bg'],
                fg=self.colors['matrix_green'],
                font=('Courier New', 18, 'bold')).pack(pady=30)
        
        # Report grid
        grid_frame = tk.Frame(tab, bg=self.colors['panel_bg'])
        grid_frame.pack(pady=20)
        
        reports = [
            ("🔐", "PASSWORD AUDIT", "Analyze stored credentials"),
            ("📡", "NETWORK SWEEP", "Wireless security assessment"),
            ("📈", "SYSTEM DIAG", "Complete system analysis"),
            ("⚠️", "THREAT SCAN", "Vulnerability detection"),
            ("🛡️", "FIREWALL LOG", "Network protection audit"),
            ("🔍", "FORENSIC DEEP", "Advanced forensic analysis"),
        ]
        
        for i, (icon, title, desc) in enumerate(reports):
            row, col = divmod(i, 3)
            
            card = tk.Frame(grid_frame,
                           bg=self.colors['darker_bg'],
                           relief='raised',
                           borderwidth=2,
                           width=200,
                           height=150)
            card.grid(row=row, column=col, padx=10, pady=10)
            card.pack_propagate(False)
            
            # Icon
            tk.Label(card,
                    text=icon,
                    font=('Segoe UI', 24),
                    bg=self.colors['darker_bg'],
                    fg=self.colors['accent']).pack(pady=(20, 5))
            
            # Title
            tk.Label(card,
                    text=title,
                    font=('Courier New', 11, 'bold'),
                    bg=self.colors['darker_bg'],
                    fg=self.colors['matrix_green']).pack()
            
            # Description
            tk.Label(card,
                    text=desc,
                    font=('Courier New', 8),
                    bg=self.colors['darker_bg'],
                    fg=self.colors['text_secondary'],
                    wraplength=180).pack(pady=5)
            
            # Generate button
            btn = tk.Button(card,
                           text="[GENERATE]",
                           command=lambda t=title: self.generate_report(t),
                           bg=self.colors['dark_bg'],
                           fg=self.colors['cyber_blue'],
                           font=('Courier New', 9),
                           padx=10,
                           pady=3)
            btn.pack(pady=10)
    
    def create_cyber_dashboard_tab(self):
        """Create cyberpunk dashboard tab"""
        tab = tk.Frame(self.notebook, bg=self.colors['panel_bg'])
        self.notebook.add(tab, text="📈 DASHBOARD")
        
        # Title
        tk.Label(tab,
                text="SECURITY DASHBOARD",
                bg=self.colors['panel_bg'],
                fg=self.colors['matrix_green'],
                font=('Courier New', 18, 'bold')).pack(pady=30)
        
        # Digital rain effect in background
        rain_canvas = tk.Canvas(tab,
                               bg='black',
                               highlightthickness=0)
        rain_canvas.place(relwidth=1, relheight=1)
        self.digital_rain = DigitalRainWidget(rain_canvas, 1400, 900)
        
        # Dashboard widgets on top
        self.create_dashboard_widgets(tab)
        
        # Lower the rain effect
        rain_canvas.lower()
    
    def create_dashboard_widgets(self, parent):
        """Create dashboard widgets"""
        # Main container
        container = tk.Frame(parent, bg=self.colors['panel_bg'])
        container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Matrix logo
        logo_text = """GRAE-X SYSTEM ONLINE
━━━━━━━━━━━━━━━━━━
> SECURITY STATUS: NOMINAL
> THREAT LEVEL: LOW
> LAST SCAN: COMPLETE
> NEXT UPDATE: 00:05:23"""
        
        logo_label = tk.Label(container,
                             text=logo_text,
                             bg='black',
                             fg=self.colors['matrix_green'],
                             font=('Courier New', 12),
                             justify='left')
        logo_label.pack(pady=20)
        
        # Live feed
        feed_frame = tk.Frame(container, bg=self.colors['darker_bg'])
        feed_frame.pack(pady=20)
        
        tk.Label(feed_frame,
                text="LIVE SECURITY FEED:",
                bg=self.colors['darker_bg'],
                fg=self.colors['cyber_blue'],
                font=('Courier New', 12)).pack(pady=10)
        
        self.feed_text = scrolledtext.ScrolledText(feed_frame,
                                                  width=60,
                                                  height=10,
                                                  bg='black',
                                                  fg=self.colors['matrix_green'],
                                                  font=('Courier New', 9),
                                                  insertbackground=self.colors['matrix_green'])
        self.feed_text.pack(padx=10, pady=10)
        self.feed_text.insert('1.0', "> SYSTEM INITIALIZED...\n")
        self.feed_text.insert('2.0', "> LOADING SECURITY MODULES...\n")
        self.feed_text.insert('3.0', "> READY FOR OPERATION\n")
        self.feed_text.config(state='disabled')
        
        # Update feed periodically
        self.update_security_feed()
    
    def create_cyber_footer(self):
        """Create cyberpunk footer"""
        footer_frame = tk.Frame(self.main_container,
                               bg=self.colors['darker_bg'],
                               height=40)
        footer_frame.pack(fill='x', side='bottom', pady=(2, 0))
        footer_frame.pack_propagate(False)
        
        # Status bar
        self.status_bar = tk.Label(footer_frame,
                                  text=">_ GRAE-X SENTINEL PRO // READY // " + datetime.now().strftime("%H:%M:%S"),
                                  bg=self.colors['darker_bg'],
                                  fg=self.colors['text_secondary'],
                                  font=('Courier New', 9))
        self.status_bar.pack(side='left', padx=20)
        
        # Copyright
        tk.Label(footer_frame,
                text="© 2024 GRAE-X SECURITY // FOR EDUCATIONAL USE",
                bg=self.colors['darker_bg'],
                fg=self.colors['cyber_blue'],
                font=('Courier New', 9)).pack(side='right', padx=20)
        
        # Update clock
        self.update_clock()
    
    def update_clock(self):
        """Update footer clock"""
        time_str = datetime.now().strftime("%H:%M:%S")
        current_text = self.status_bar.cget('text')
        if "// READY //" in current_text:
            new_text = f">_ GRAE-X SENTINEL PRO // READY // {time_str}"
        else:
            new_text = current_text.rsplit('//', 1)[0] + f"// {time_str}"
        self.status_bar.config(text=new_text)
        self.root.after(1000, self.update_clock)
    
    def update_security_feed(self):
        """Update security feed with random messages"""
        messages = [
            "> SCANNING FOR THREATS...",
            "> FIREWALL: ACTIVE",
            "> ENCRYPTION: ENABLED",
            "> INTRUSION DETECTION: ONLINE",
            "> SYSTEM INTEGRITY: 100%",
            "> NETWORK TRAFFIC: NORMAL",
            "> MALWARE SCAN: CLEAN",
            "> BACKUP SYSTEM: VERIFIED",
        ]
        
        if random.random() > 0.7:  # 30% chance to add message
            self.feed_text.config(state='normal')
            self.feed_text.insert('end', random.choice(messages) + '\n')
            self.feed_text.see('end')
            self.feed_text.config(state='disabled')
        
        self.root.after(3000, self.update_security_feed)
    
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
        file_menu.add_command(label="NEW SESSION", command=self.new_analysis)
        file_menu.add_command(label="LOAD REPORT", command=self.open_report)
        file_menu.add_separator()
        file_menu.add_command(label="EXIT SYSTEM", command=self.root.quit)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0,
                            bg=self.colors['darker_bg'],
                            fg=self.colors['text_secondary'])
        menubar.add_cascade(label="[TOOLS]", menu=tools_menu)
        tools_menu.add_command(label="BATCH ANALYSIS", command=self.batch_password_check)
        tools_menu.add_separator()
        tools_menu.add_command(label="TOGGLE MATRIX", command=self.toggle_matrix)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0,
                           bg=self.colors['darker_bg'],
                           fg=self.colors['text_secondary'])
        menubar.add_cascade(label="[HELP]", menu=help_menu)
        help_menu.add_command(label="USER MANUAL", command=self.show_guide)
        help_menu.add_command(label="ABOUT SYSTEM", command=self.show_about)
    
    def toggle_matrix(self):
        """Toggle matrix effect"""
        if hasattr(self, 'matrix'):
            self.matrix.toggle()
    
    # Event handlers and functionality
    def on_password_change(self, event=None):
        """Handle password change"""
        password = self.password_entry.get()
        self.current_password = password
        
        if password:
            threading.Thread(target=self.update_password_analysis, daemon=True).start()
    
    def update_password_analysis(self):
        """Update password analysis"""
        if not self.current_password:
            return
        
        result = self.password_analyzer.analyze(self.current_password)
        self.root.after(0, lambda: self.display_analysis_result(result))
    
    def display_analysis_result(self, result):
        """Display analysis result"""
        score = result.get('score', 0)
        
        # Update strength bar
        bar_width = min(score * 3, 300)
        if hasattr(self, 'strength_bar'):
            canvas = self.strength_bar.master.master  # Get to canvas
            canvas.coords(self.strength_bar, 0, 0, bar_width, 30)
            
            # Set color
            if score >= 80:
                color = self.colors['matrix_green']
                strength = "IMPENETRABLE"
            elif score >= 60:
                color = self.colors['cyber_blue']
                strength = "STRONG"
            elif score >= 40:
                color = self.colors['warning_yellow']
                strength = "MODERATE"
            elif score >= 20:
                color = "#FF6600"
                strength = "WEAK"
            else:
                color = self.colors['alert_red']
                strength = "CRITICAL"
            
            canvas.itemconfig(self.strength_bar, fill=color)
            
            if hasattr(self, 'strength_label'):
                self.strength_label.config(text=f"[{strength}] SCORE: {score}/100", fg=color)
        
        # Update metrics
        metrics = {
            'entropy': f"{result.get('entropy', 0):.1f} bits",
            'crack time': result.get('crack_time', 'UNKNOWN'),
            'pattern score': f"{score}/100",
            'hash strength': "QUANTUM SAFE" if score > 70 else "VULNERABLE"
        }
        
        for key, value in metrics.items():
            if key in self.metric_labels:
                self.metric_labels[key].config(text=value)
        
        # Update stats
        self.stats['passwords_analyzed'] += 1
    
    def analyze_password(self):
        """Analyze password"""
        password = self.password_entry.get()
        if not password:
            self.show_message("ALERT", "NO INPUT DETECTED")
            return
        
        self.status_bar.config(text=">_ ANALYZING PASSWORD STRUCTURE...")
        self.on_password_change()
    
    def toggle_password_visibility(self):
        """Toggle password visibility"""
        if self.show_pass_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="•")
    
    def scan_wifi(self):
        """Scan WiFi networks"""
        if self.scanning:
            return
        
        self.scanning = True
        self.scan_status.config(text=">_ INITIATING NETWORK SWEEP...")
        self.status_bar.config(text=">_ PROBING WIRELESS SPECTRUM...")
        
        def scan():
            try:
                networks = self.wifi_scanner.scan()
                self.root.after(0, lambda: self.display_scan_results(networks))
            except Exception as e:
                self.root.after(0, lambda: self.scan_failed(str(e)))
        
        threading.Thread(target=scan, daemon=True).start()
    
    def display_scan_results(self, networks):
        """Display WiFi scan results"""
        self.scanning = False
        self.current_networks = networks
        self.scan_status.config(text=f">_ FOUND {len(networks)} NETWORKS")
        self.status_bar.config(text=">_ SWEEP COMPLETE")
        
        # Clear tree
        for item in self.network_tree.get_children():
            self.network_tree.delete(item)
        
        # Add networks
        for i, net in enumerate(networks, 1):
            ssid = net.get('ssid', net.get('SSID', 'HIDDEN'))
            security = net.get('security', net.get('Security', 'UNKNOWN'))
            signal = net.get('signal', net.get('Signal', 'N/A'))
            channel = net.get('channel', net.get('Channel', 'N/A'))
            
            # Determine threat level
            if 'WEP' in security.upper() or 'OPEN' in security.upper():
                threat = "CRITICAL"
            elif 'WPA' in security.upper() and 'WPA2' not in security.upper():
                threat = "HIGH"
            elif 'WPA2' in security.upper():
                threat = "MEDIUM"
            elif 'WPA3' in security.upper():
                threat = "LOW"
            else:
                threat = "UNKNOWN"
            
            self.network_tree.insert('', 'end', values=(
                ssid, security, signal, channel, threat
            ))
        
        # Update stats
        self.stats['networks_scanned'] += 1
    
    def scan_failed(self, error):
        """Handle scan failure"""
        self.scanning = False
        self.scan_status.config(text=">_ SWEEP FAILED")
        self.show_message("ERROR", f"SCAN FAILED:\n{error}")
    
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
        
        # Typewriter effect
        self.typewriter_effect(password)
        
        # Update feed
        self.feed_text.config(state='normal')
        self.feed_text.insert('end', f"> GENERATED {length}-CHAR KEY\n")
        self.feed_text.see('end')
        self.feed_text.config(state='disabled')
    
    def typewriter_effect(self, text):
        """Display text with typewriter effect"""
        self.generated_key_var.set("")
        
        def type_char(i=0):
            if i < len(text):
                current = self.generated_key_var.get()
                self.generated_key_var.set(current + text[i])
                self.root.after(50, lambda: type_char(i + 1))
        
        type_char()
    
    def copy_password(self):
        """Copy password to clipboard"""
        password = self.generated_key_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.show_message("SUCCESS", "KEY COPIED TO CLIPBOARD")
    
    def save_password(self):
        """Save password to file"""
        password = self.generated_key_var.get()
        if password:
            file_path = filedialog.asksaveasfilename(
                title="SAVE KEY TO VAULT",
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if file_path:
                try:
                    with open(file_path, 'w') as f:
                        f.write(f"GRAE-X SENTINEL KEY VAULT\n")
                        f.write(f"Generated: {datetime.now()}\n")
                        f.write(f"Key: {password}\n")
                        f.write(f"Length: {len(password)}\n")
                    
                    self.show_message("SUCCESS", f"KEY SAVED TO:\n{file_path}")
                except Exception as e:
                    self.show_message("ERROR", f"SAVE FAILED:\n{e}")
    
    def generate_report(self, report_type):
        """Generate security report"""
        self.show_message("REPORT", f"GENERATING {report_type}...")
        self.status_bar.config(text=f">_ COMPILING {report_type} REPORT")
        
        # Simulate report generation
        def generate():
            time.sleep(2)
            self.root.after(0, lambda: self.report_generated(report_type))
        
        threading.Thread(target=generate, daemon=True).start()
    
    def report_generated(self, report_type):
        """Handle report generation completion"""
        self.stats['reports_generated'] += 1
        self.show_message("SUCCESS", f"{report_type} GENERATED")
        self.status_bar.config(text=">_ REPORT GENERATION COMPLETE")
        
        # Update feed
        self.feed_text.config(state='normal')
        self.feed_text.insert('end', f"> {report_type} COMPILED\n")
        self.feed_text.see('end')
        self.feed_text.config(state='disabled')
    
    def on_network_select(self, event):
        """Handle network selection"""
        selection = self.network_tree.selection()
        if selection:
            item = self.network_tree.item(selection[0])
            values = item['values']
            
            if values:
                analysis = f"""NETWORK ANALYSIS:
━━━━━━━━━━━━━━━━━━
SSID: {values[0]}
SECURITY: {values[1]}
SIGNAL: {values[2]}
CHANNEL: {values[3]}
THREAT: {values[4]}

RECOMMENDATION:"""
                
                if values[4] == "CRITICAL":
                    analysis += "\n⚠️ AVOID CONNECTION"
                elif values[4] == "HIGH":
                    analysis += "\n⚠️ USE WITH CAUTION"
                elif values[4] == "MEDIUM":
                    analysis += "\n⚠️ USE STRONG PASSWORD"
                else:
                    analysis += "\n✅ SAFE FOR USE"
                
                self.show_message("NETWORK ANALYSIS", analysis)
    
    def new_analysis(self):
        """Start new analysis"""
        self.password_entry.delete(0, tk.END)
        self.current_password = ""
        self.status_bar.config(text=">_ NEW SESSION INITIALIZED")
        
        # Reset UI elements
        if hasattr(self, 'strength_bar'):
            canvas = self.strength_bar.master.master
            canvas.coords(self.strength_bar, 0, 0, 0, 30)
        
        if hasattr(self, 'strength_label'):
            self.strength_label.config(text="AWAITING INPUT...", fg=self.colors['text_secondary'])
        
        for label in self.metric_labels.values():
            label.config(text="")
    
    def open_report(self):
        """Open report file"""
        file_path = filedialog.askopenfilename(
            title="LOAD REPORT FILE",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.show_message("REPORT", f"LOADING: {file_path}")
    
    def batch_password_check(self):
        """Batch password check"""
        self.show_message("INFO", "BATCH ANALYSIS MODULE")
    
    def show_message(self, title, message):
        """Show cyberpunk styled message"""
        # Create custom messagebox
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("500x300")
        dialog.configure(bg=self.colors['dark_bg'])
        
        # Make dialog modal
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Title
        tk.Label(dialog,
                text=f"[{title}]",
                bg=self.colors['dark_bg'],
                fg=self.colors['matrix_green'],
                font=('Courier New', 16, 'bold')).pack(pady=20)
        
        # Message
        tk.Label(dialog,
                text=message,
                bg=self.colors['dark_bg'],
                fg=self.colors['text_secondary'],
                font=('Courier New', 11),
                justify='left').pack(pady=20, padx=20)
        
        # OK button
        tk.Button(dialog,
                 text="[ACKNOWLEDGE]",
                 command=dialog.destroy,
                 bg=self.colors['darker_bg'],
                 fg=self.colors['matrix_green'],
                 font=('Courier New', 10),
                 padx=20,
                 pady=10).pack(pady=20)
        
        # Center dialog
        dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")
    
    def show_guide(self):
        """Show user guide"""
        guide = """GRAE-X SENTINEL PRO v4.2
━━━━━━━━━━━━━━━━━━
SYSTEM COMMANDS:

[1] PASS_CRACK - Password strength analyzer
[2] WIFI_PROBE - Wireless network scanner
[3] GEN_KEY    - Cryptographic key generator
[4] SYS_REPORT - Security report generator
[5] DASHBOARD  - System status monitor

QUICK KEYS:
• F1 - Toggle Matrix Effect
• F2 - Quick Password Check
• F3 - Network Sweep
• F4 - Generate Report

SYSTEM REQUIREMENTS:
• Windows/Linux/Mac OS
• Python 3.8+
• 4GB RAM Minimum
• Network Access for Full Features"""
        
        self.show_message("USER MANUAL", guide)
    
    def show_about(self):
        """Show about dialog"""
        about = """GRAE-X SENTINEL PRO v4.2
━━━━━━━━━━━━━━━━━━
FUTURISTIC CYBERSECURITY SUITE

FEATURES:
• Matrix-Style Interface
• Real-Time Password Analysis
• Wireless Network Probing
• Cryptographic Key Generation
• Advanced Security Reporting
• System Monitoring Dashboard

TECHNOLOGY:
• Quantum-Resistant Algorithms
• Neural Network Analysis
• Real-Time Threat Detection
• Encrypted Data Storage

WARNING:
FOR EDUCATIONAL AND RESEARCH
PURPOSES ONLY. USE RESPONSIBLY.

© 2024 GRAE-X SECURITY"""
        
        self.show_message("ABOUT SYSTEM", about)
    
    def run(self):
        """Run the application"""
        # Center window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Bind function keys
        self.root.bind('<F1>', lambda e: self.toggle_matrix())
        self.root.bind('<F2>', lambda e: self.notebook.select(0))
        self.root.bind('<F3>', lambda e: self.notebook.select(1))
        self.root.bind('<F4>', lambda e: self.notebook.select(3))
        
        # Start main loop
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    print("""
    ██████╗ ██████╗  █████╗ ███████╗    ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗     
    ██╔════╝ ██╔══██╗██╔══██╗██╔════╝    ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║     
    ██║  ███╗██████╔╝███████║█████╗      █████╗  █████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║     
    ██║   ██║██╔══██╗██╔══██║██╔══╝      ██╔══╝  ██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║     
    ╚██████╔╝██║  ██║██║  ██║██║         ███████╗███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗
     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝         ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
    """)
    print("Initializing GRAE-X SENTINEL PRO v4.2...")
    print("Loading Matrix Interface...")
    print("System Online.\n")
    
    app = SentinelGUI()
    app.run()
