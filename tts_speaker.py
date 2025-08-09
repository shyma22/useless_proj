import threading
import pyttsx3
import random

def speak_message(message, popup_type="cpu", extra_data=None):
    """Convert popup message to speech-friendly text and speak it"""
    def speak_async():
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 1.0)

            if popup_type == "cpu":
                cpu_usage = extra_data.get('cpu_usage', 0) if extra_data else 0
                if cpu_usage < 3:
                    speech_text = f" check out this super useless pop-up. CPU Usage:  {cpu_usage:.1f} percent."
                elif cpu_usage < 4:
                    speech_text = f"CPU is just chilling and sipping coffee... {cpu_usage:.1f} percent."
                elif cpu_usage < 30:
                    speech_text = f"CPU’s starting to sweat a little... {cpu_usage:.1f} percent."
                elif cpu_usage < 50:
                    speech_text = f"CPU usage is climbing to {cpu_usage:.1f} percent."
                elif cpu_usage < 75:
                    speech_text = f"High CPU usage detected at {cpu_usage:.1f} percent."
                else:
                    speech_text = f"Critical! Very high CPU usage at {cpu_usage:.1f} percent."

            elif popup_type == "click":
                click_count = extra_data.get('click_count', 0) if extra_data else 0
                if click_count == 10:
                    speech_text = f"Achievement unlocked: {click_count} clicks! Achievement description: totally meaningless."
                elif click_count == 20:
                    speech_text = f"You’ve clicked {click_count} times. The internet is proud of your dedication to uselessness."
                elif click_count == 30:
                    speech_text = f"Breaking news: {click_count} clicks! No prizes, no cookies, just this popup."
                elif click_count == 50:
                    speech_text = f"Amazing! {click_count} clicks! Keep going, and maybe you will find… still nothing."
                elif click_count == 75:
                    speech_text = f"Outstanding! {click_count} clicks accomplished!"
                elif click_count == 100:
                    speech_text = f"You’re now at {click_count} clicks! Your productivity called, it is worried"
                elif click_count >= 150:
                    speech_text = f"Milestone unlocked: {click_count} pointless clicks!"
                else:
                    speech_text = f"Congratulations! You have reached {click_count} clicks! Still wondering why you are doing this."

            elif popup_type == "key":
                key_pressed = extra_data.get('key_pressed', 'unknown key') if extra_data else 'unknown key'
                celebrations = [
                    f"Wow! You pressed {key_pressed}! …And nothing happened.",
                    f"Amazing! The {key_pressed} key was pressed! Totally unnecessary.",
                    f"Fantastic! You hit {key_pressed}! Your life is now 0% better.",
                    f"Great job pressing {key_pressed}! The universe remains unchanged.",
                    f"Excellent! {key_pressed} key activated! No purpose detected.",
                    f"Wonderful! You typed {key_pressed}! Absolutely no reason why.",
                    f"Superb! {key_pressed} was pressed! Still pointless.",
                    f"Brilliant! The {key_pressed} key! …Why though?",
                    f"Incredible! {key_pressed} key strike! Achievement unlocked: Nothing.",
                    f"Legendary! {key_pressed} was pressed! Your reward: this message.",

                ]
                speech_text = random.choice(celebrations)

            else:
                speech_text = message.replace('\n', '. ').replace('🎉', '').replace('🏆', '').replace('⭐', '').replace('💪', '').replace('⚡', '').replace('👑', '').replace('🚀', '').replace('✨', '').replace('🔥', '').replace('🎯', '').replace('💎', '').replace('🌟', '').replace('😴', '').replace('😐', '').replace('😰', '').replace('🚨', '')

            print(f"🔊 Speaking: {speech_text}")
            engine.say(speech_text)
            engine.runAndWait()
            engine.stop()

        except Exception as e:
            print(f"TTS Error: {e}")

    speech_thread = threading.Thread(target=speak_async, daemon=True)
    speech_thread.start()


