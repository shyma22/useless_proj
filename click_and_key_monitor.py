from pynput import mouse, keyboard
import random

CLICK_MILESTONES = [10, 20, 30, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]

def get_key_message(key_name):
    """Generate celebration message for key press"""
    celebrations = [
        f"🎉 WOW! You pressed the '{key_name}' key!\nAnd absolutely nothing happened!",
        f"✨ FANTASTIC! The '{key_name}' key was activated!\nThis changes… nothing.",
        f"🌟 INCREDIBLE! You hit '{key_name}'!\nScience still can’t explain why.",
        f"🎯 AWESOME! '{key_name}' key pressed!\nThe universe remains unimpressed.",
        f"🚀 BRILLIANT! The '{key_name}' key!\nNo reason, just vibes.",
        f"💫 AMAZING! You typed '{key_name}'!\nTotally useless, yet satisfying.",
        f"🎊 SUPERB! '{key_name}' was pressed!\nThis popup is your only reward.",
        f"⭐ EXCELLENT! The magical '{key_name}' key!\nNothing magical actually happened."

    ]
    return random.choice(celebrations)

def get_click_message(clicks):
    """Generate click milestone message"""
    messages = {
       10: "🎉 10 clicks!\nCongratulations on achieving… nothing.",
       20: "🏆 20 clicks!\nYour mouse is already questioning your life choices.",
       30: "⭐ 30 clicks!\nThat’s 30 more than you ever needed.",
       50: "💪 50 clicks!\nYour finger must be so proud… and confused.",
       75: "⚡ 75 clicks!\nElite level of wasting time unlocked.",
       100: "👑 100 clicks!\nOfficially a Click Legend… in your own mind.",
       150: "🚀 150 clicks!\nYou’ve transcended into the realm of pointless glory.",
       200: "✨ 200 clicks!\nYou are now the Supreme Ruler of Absolutely Nothing.",
       250: "🎯 250 clicks!\nYou’re clicking beyond reason and logic.",
       300: "💎 300 clicks!\nMaster of clicks, servant to no purpose.",
       350: "🌟 350 clicks!\nUnstoppable… but still achieving nothing.",
       400: "⚡ 400 clicks!\nCongratulations, Click Deity of Meaninglessness.",
       450: "🚀 450 clicks!\nBeyond human clicking! Still no prize.",
       500: "👑 500 clicks!\nYou rule over the Empty Kingdom of Clicks.",
       550: "💫 550 clicks!\nYou have transcended clicking… into pure absurdity."

    }
    return messages.get(clicks, f"🎯 {clicks} clicks reached!\nKeep up the amazing clicking!")

def on_key_press(monitor_instance, key):
    """Handle keyboard key press events"""
    try:
        monitor_instance.key_count += 1

        if hasattr(key, 'char') and key.char:
            key_name = key.char.upper() if key.char.isalpha() else key.char
        else:
            key_name = str(key).replace('Key.', '').upper()

        print(f"Key #{monitor_instance.key_count}: {key_name}")
        message = get_key_message(key_name)

        monitor_instance.show_popup(message, "🎉 Key Celebration!", "key",
                                    {"key_pressed": key_name, "key_count": monitor_instance.key_count})
    except Exception as e:
        print(f"Error handling key press: {e}")

def on_click(monitor_instance, x, y, button, pressed):
    """Handle mouse click events"""
    if pressed:
        monitor_instance.click_count += 1
        print(f"Click #{monitor_instance.click_count} at ({x}, {y})")

        if monitor_instance.click_count in CLICK_MILESTONES:
            message = get_click_message(monitor_instance.click_count)
            print(f"🎉 MILESTONE REACHED: {monitor_instance.click_count} clicks!")
            monitor_instance.show_popup(message, "🖱️ Click Milestone!", "click",
                                        {"click_count": monitor_instance.click_count})
