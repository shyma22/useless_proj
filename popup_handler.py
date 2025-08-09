import tkinter as tk
import random
from datetime import datetime

CLICK_MILESTONES = [10, 20, 30, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]

class UnifiedXPPopup:
    def __init__(self, message, title="System Monitor", popup_type="cpu", extra_data=None):
        self.root = tk.Tk()
        self.message = message
        self.title = title
        self.popup_type = popup_type
        self.extra_data = extra_data or {}
        self.setup_window()
        self.create_widgets()
        self.position_randomly()

    def setup_window(self):
        self.root.title(self.title)
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        self.root.overrideredirect(True)
        self.root.configure(bg="#ece9d8")
        self.root.attributes("-topmost", True)

        if self.popup_type == "cpu" and self.extra_data.get('cpu_usage', 0) > 20:
            self.root.after(12000, self.auto_close)
        else:
            self.root.after(10000, self.auto_close)

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg="#ece9d8", relief="raised", bd=2)
        main_frame.pack(fill="both", expand=True)
        self.create_titlebar(main_frame)
        self.create_content(main_frame)
        self.create_buttons(main_frame)

    def create_titlebar(self, parent):
        titlebar = tk.Frame(parent, bg="#0054e3", height=22, relief="flat")
        titlebar.pack(fill="x")
        titlebar.pack_propagate(False)

        for i in range(15):
            color_r = int(0x00 + (0x43 - 0x00) * i / 14)
            color_g = int(0x54 + (0x97 - 0x54) * i / 14)
            color_b = int(0xe3 + (0xfd - 0xe3) * i / 14)
            color = f"#{color_r:02x}{color_g:02x}{color_b:02x}"
            gradient_frame = tk.Frame(titlebar, bg=color, height=22)
            gradient_frame.place(x=i * 25, y=0, width=26, height=22)

        title_content = tk.Frame(titlebar, bg="#0054e3")
        title_content.pack(side="left", fill="y", padx=6, pady=2)

        if self.popup_type == "cpu":
            icon_text = "⚡"
        elif self.popup_type == "click":
            icon_text = "👆"
        else:
            icon_text = "⌨️"

        title_icon = tk.Label(title_content, text=icon_text, bg="white", fg="#0054e3",
                              font=("Arial", 8, "bold"), width=2, height=1, relief="solid", bd=1)
        title_icon.pack(side="left", pady=2)

        title_label = tk.Label(title_content, text=self.title,
                               fg="white", bg="#0054e3", font=("Tahoma", 8, "bold"))
        title_label.pack(side="left", padx=4, pady=2)

        close_btn = tk.Button(titlebar, text="×", bg="#ff6666", fg="black",
                              font=("Arial", 8, "bold"), width=2, height=1,
                              relief="raised", bd=1, command=self.close_popup,
                              activebackground="#ff7777")
        close_btn.pack(side="right", padx=4, pady=2)

    def create_content(self, parent):
        content_frame = tk.Frame(parent, bg="#ece9d8", pady=16, padx=16)
        content_frame.pack(fill="both", expand=True)

        icon_frame = tk.Frame(content_frame, bg="#ece9d8")
        icon_frame.pack(side="left", padx=(0, 12), pady=2)

        icon_canvas = tk.Canvas(icon_frame, width=32, height=32, bg="#ece9d8",
                                highlightthickness=0, relief="raised", bd=1)
        icon_canvas.pack()

        if self.popup_type == "cpu":
            bg_color, icon_emoji = self.get_cpu_icon()
        elif self.popup_type == "click":
            bg_color, icon_emoji = self.get_click_icon()
        else:
            bg_color, icon_emoji = self.get_key_icon()

        icon_canvas.create_rectangle(0, 0, 32, 32, fill=bg_color, outline="#333")
        icon_canvas.create_text(16, 16, text=icon_emoji, font=("Arial", 12))

        text_frame = tk.Frame(content_frame, bg="#ece9d8")
        text_frame.pack(side="left", fill="both", expand=True, pady=2)

        if self.popup_type == "cpu":
            cpu_usage = self.extra_data.get('cpu_usage', 0)
            status_label = tk.Label(text_frame, text=f"CPU Usage: {cpu_usage:.1f}%",
                                    bg="#ece9d8", fg="black", font=("Tahoma", 9, "bold"))
        elif self.popup_type == "click":
            click_count = self.extra_data.get('click_count', 0)
            status_label = tk.Label(text_frame, text=f"Total Clicks: {click_count}",
                                    bg="#ece9d8", fg="black", font=("Tahoma", 9, "bold"))
        else:
            key_pressed = self.extra_data.get('key_pressed', 'Unknown')
            status_label = tk.Label(text_frame, text=f"Key Pressed: {key_pressed}",
                                    bg="#ece9d8", fg="black", font=("Tahoma", 9, "bold"))
        status_label.pack(anchor="w", pady=(0, 5))

        message_label = tk.Label(text_frame, text=self.message,
                                 bg="#ece9d8", fg="black", font=("Tahoma", 8),
                                 justify="left", wraplength=280)
        message_label.pack(anchor="w")

        if self.popup_type == "click" and self.extra_data.get('click_count', 0) in CLICK_MILESTONES:
            achievement_text = self.get_click_achievement()
            achievement_label = tk.Label(text_frame, text=achievement_text,
                                         bg="#ece9d8", fg="blue", font=("Tahoma", 7, "italic"))
            achievement_label.pack(anchor="w", pady=(3, 0))

        timestamp = datetime.now().strftime("%H:%M:%S")
        time_label = tk.Label(text_frame, text=f"Time: {timestamp}",
                              bg="#ece9d8", fg="gray", font=("Tahoma", 7))
        time_label.pack(anchor="w", pady=(5, 0))

    def get_cpu_icon(self):
        cpu_usage = self.extra_data.get('cpu_usage', 0)
        if cpu_usage < 5:
            return "#28a745", "😴"
        elif cpu_usage < 15:
            return "#ffc107", "😐"
        elif cpu_usage < 30:
            return "#fd7e14", "😰"
        else:
            return "#dc3545", "🔥"

    def get_click_icon(self):
        click_count = self.extra_data.get('click_count', 0)
        if click_count <= 10:
            return "#28a745", "🎉"
        elif click_count <= 30:
            return "#ffc107", "🏆"
        elif click_count <= 50:
            return "#fd7e14", "⭐"
        else:
            return "#dc3545", "💎"

    def get_key_icon(self):
        colors = ["#28a745", "#ffc107", "#fd7e14", "#dc3545", "#6f42c1", "#20c997"]
        icons = ["⌨️", "📝", "✨", "🎹", "💫", "🌟"]
        return random.choice(colors), random.choice(icons)

    def get_click_achievement(self):
        messages = {
            10: "First milestone unlocked! 🌟",
            20: "You're on fire! Keep clicking! 🔥",
            30: "Click master in the making! 💪",
            50: "Halfway to legendary status! ⚡",
            75: "Almost there, champion! 🎯",
            100: "LEGENDARY CLICKER ACHIEVED! 👑",
            150: "Beyond legendary! You're unstoppable! 🚀",
            200: "CLICK GOD STATUS UNLOCKED! 👑✨",
            250: "You're on fire! Keep clicking! 🔥",
            300: "Click master in the making! 💪",
            350: "Halfway to legendary status! ⚡",
            400: "Almost there, champion! 🎯",
            450: "LEGENDARY CLICKER ACHIEVED! 👑",
            500: "Beyond legendary! You're unstoppable! 🚀",
            550: "CLICK GOD STATUS UNLOCKED! 👑✨"
        }
        return messages.get(self.extra_data.get('click_count', 0), "Amazing clicking skills! 🎉")

    def create_buttons(self, parent):
        separator = tk.Frame(parent, bg="#d4d0c8", height=1)
        separator.pack(fill="x")

        button_frame = tk.Frame(parent, bg="#ece9d8", pady=8, padx=16)
        button_frame.pack(fill="x")

        if self.popup_type == "cpu":
            dismiss_btn = tk.Button(button_frame, text="Dismiss", font=("Tahoma", 8),
                                    width=10, relief="raised", bd=1, bg="#ece9d8",
                                    activebackground="#f5f2e8", command=self.close_popup)
            dismiss_btn.pack(side="right", padx=(8, 0))
            ok_btn = tk.Button(button_frame, text="OK", font=("Tahoma", 8, "bold"),
                               width=10, relief="raised", bd=1, bg="#ece9d8",
                               activebackground="#f5f2e8", command=self.close_popup)
        elif self.popup_type == "click":
            keep_btn = tk.Button(button_frame, text="Keep Clicking!", font=("Tahoma", 8),
                                 width=12, relief="raised", bd=1, bg="#ece9d8",
                                 activebackground="#f5f2e8", command=self.close_popup)
            keep_btn.pack(side="right", padx=(8, 0))
            ok_btn = tk.Button(button_frame, text="Awesome!", font=("Tahoma", 8, "bold"),
                               width=10, relief="raised", bd=1, bg="#ece9d8",
                               activebackground="#f5f2e8", command=self.close_popup)
        else:
            type_btn = tk.Button(button_frame, text="Keep Typing!", font=("Tahoma", 8),
                                 width=12, relief="raised", bd=1, bg="#ece9d8",
                                 activebackground="#f5f2e8", command=self.close_popup)
            type_btn.pack(side="right", padx=(8, 0))
            ok_btn = tk.Button(button_frame, text="Nice!", font=("Tahoma", 8, "bold"),
                               width=10, relief="raised", bd=1, bg="#ece9d8",
                               activebackground="#f5f2e8", command=self.close_popup)

        ok_btn.pack(side="right")
        ok_btn.focus_set()

        self.root.bind("<Return>", lambda e: self.close_popup())
        self.root.bind("<Escape>", lambda e: self.close_popup())

    # def position_randomly(self):
    #     self.root.update_idletasks()
    #     screen_width = self.root.winfo_screenwidth()
    #     screen_height = self.root.winfo_screenheight()
    #     max_x = screen_width - 380
    #     max_y = screen_height - 160
    #     margin = 100
    #     random_x = random.randint(margin, max_x - margin)
    #     random_y = random.randint(margin, max_y - margin)
    #     self.root.geometry(f"380x160+{random_x}+{random_y}")

    def position_randomly(self):
     self.root.update_idletasks()
     width = self.root.winfo_reqwidth()
     height = self.root.winfo_reqheight()
     screen_width = self.root.winfo_screenwidth()
     screen_height = self.root.winfo_screenheight()
     max_x = screen_width - width
     max_y = screen_height - height
     margin = 100
     random_x = random.randint(margin, max_x - margin)
     random_y = random.randint(margin, max_y - margin)
     self.root.geometry(f"{width}x{height}+{random_x}+{random_y}")




    def auto_close(self):
        try:
            if self.root.winfo_exists():
                self.root.destroy()
        except:
            pass

    def close_popup(self):
        try:
            self.root.destroy()
        except:
            pass

    def show(self):
        self.root.mainloop()
