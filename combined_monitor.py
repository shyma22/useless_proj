import threading
import time
from pynput import mouse, keyboard

from popup_handler import UnifiedXPPopup
from tts_speaker import speak_message
from cpu_monitor import monitor_cpu
from click_and_key_monitor import on_click, on_key_press

class CombinedMonitor:
    def __init__(self):
        # CPU monitoring
        self.cpu_monitoring = False
        self.cpu_check_interval = 10
        self.last_popup_time = 0
        self.popup_cooldown = 3

        # Click tracking
        self.click_count = 0

        # Key tracking
        self.key_count = 0

    def show_popup(self, message, title, popup_type, extra_data=None):
        """Show unified popup with voice narration"""
        # Speak the message first (non-blocking)
        speak_message(message, popup_type, extra_data)

        def create_popup():
            try:
                popup = UnifiedXPPopup(message, title, popup_type, extra_data)
                popup.show()
            except Exception as e:
                print(f"Error creating popup: {e}")

        popup_thread = threading.Thread(target=create_popup, daemon=True)
        popup_thread.start()

    def start_monitoring(self):
        """Start CPU, click, and key monitoring"""
        print("=" * 70)
        print("🖥️  COMBINED CPU, CLICK & KEY MONITOR WITH VOICE")
        print("=" * 70)
        print(f"🔧 CPU check interval: {self.cpu_check_interval} seconds")
        print("🎹 Key press celebration: EVERY key!")
        print("🔊 Voice narration enabled for all popups!")
        print("Starting all monitors... Press Ctrl+C to stop.")
        print("-" * 70)

        # Start CPU monitoring
        self.cpu_monitoring = True
        cpu_thread = threading.Thread(target=monitor_cpu, args=(self,), daemon=True)
        cpu_thread.start()

        # Start click monitoring
        mouse_listener = mouse.Listener(on_click=lambda x, y, b, p: on_click(self, x, y, b, p))
        mouse_listener.start()

        # Start key monitoring
        key_listener = keyboard.Listener(on_press=lambda k: on_key_press(self, k))
        key_listener.start()

        try:
            while self.cpu_monitoring:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Shutting down all monitors...")
            self.cpu_monitoring = False
            mouse_listener.stop()
            key_listener.stop()
            print(f"📊 Final stats: CPU Monitor stopped | Total clicks: {self.click_count} | Total keys: {self.key_count}")
            print("🎉 Thanks for using the monitor! Goodbye!")
