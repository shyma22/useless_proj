import psutil
import time
import random
from datetime import datetime

def get_cpu_message(cpu_usage):
    """Generate CPU message"""
    if cpu_usage < 3:
        messages = [
          "Your CPU is taking a well-deserved nap! 😴 Too bad it’s dreaming of doing nothing.",
          "CPU usage is extremely low. Your computer is basically staring at the ceiling.",
          "Your system is barely breaking a sweat! Maybe it’s training for the Olympics of idleness.",
          "CPU is chilling at minimal usage. Perfect time to… still not do anything important.",

            ]
    elif cpu_usage < 5:
        messages = [
          "CPU usage is nice and low. Perfect conditions for absolutely nothing to happen.",
"Light computational load detected. Your computer is basically on vacation.",
"Your CPU is working at a comfortable pace. It might start knitting soon.",

        ]
    elif cpu_usage < 30:
        messages = [
            "CPU usage is getting moderate.\nYour system is working but not stressed.",
            "Medium computational load detected.\nStill within comfortable limits.",
            "Your processor is warming up a bit.\nBut everything is running fine.",
        ]
    elif cpu_usage < 50:
        messages = [
            "CPU usage is climbing up!\nYour system is getting busy.",
            "Higher computational load detected.\nConsider closing unnecessary programs.",
            "Your processor is working hard.\nMonitor for performance impacts.",
        ]
    elif cpu_usage < 75:
        messages = [
            "High CPU usage detected! 🔥\nYour system is under heavy load.",
            "CPU is working overtime!\nConsider closing some applications.",
            "Heavy computational stress detected.\nPerformance may be affected.",
        ]
    else:
        messages = [
            "CRITICAL: Very high CPU usage! 🚨\nYour system may become unresponsive.",
            "DANGER: CPU is maxed out!\nImmediate action required.",
            "ALERT: Extreme computational load!\nSystem stability at risk.",
        ]
    return random.choice(messages)

def monitor_cpu(monitor_instance):
    """CPU monitoring loop"""
    print("CPU Monitor started...")
    try:
        while monitor_instance.cpu_monitoring:
            cpu_usage = psutil.cpu_percent(interval=1)
            current_time = datetime.now().strftime("%H:%M:%S")

            print(f"[{current_time}] CPU: {cpu_usage:.1f}% | Clicks: {monitor_instance.click_count} | Keys: {monitor_instance.key_count}")

            current_time_sec = time.time()
            if (current_time_sec - monitor_instance.last_popup_time >= monitor_instance.popup_cooldown and
                (cpu_usage < 5 or cpu_usage > 15 or random.random() < 0.2)):

                monitor_instance.last_popup_time = current_time_sec
                message = get_cpu_message(cpu_usage)

                if cpu_usage < 5:
                    title = "CPU Monitor - Low Usage"
                elif cpu_usage < 30:
                    title = "CPU Monitor - Normal"
                elif cpu_usage < 50:
                    title = "CPU Monitor - Moderate"
                else:
                    title = "CPU Monitor - High Usage"

                monitor_instance.show_popup(message, title, "cpu", {"cpu_usage": cpu_usage})

            time.sleep(monitor_instance.cpu_check_interval)

    except KeyboardInterrupt:
        print("\nCPU Monitor stopped.")
        monitor_instance.cpu_monitoring = False
