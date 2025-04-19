import requests
import warnings
import time
import os
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore
from pystyle import Center, Colors, Colorate

warnings.filterwarnings("ignore", category=DeprecationWarning)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    os.system("title Twitch Viewer Bot - Menu Version by PrimeEcto")
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter(""" 
 /$$$$$$$  /$$$$$$$  /$$$$$$ /$$      /$$ /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$ 
| $$__  $$| $$__  $$|_  $$_/| $$$    /$$$| $$_____/| $$_____/ /$$__  $$|__  $$__//$$__  $$ 
| $$  \ $$| $$  \ $$  | $$  | $$$$  /$$$$| $$      | $$      | $$  \__/   | $$  | $$  \ $$ 
| $$$$$$$/| $$$$$$$/  | $$  | $$ $$/$$ $$| $$$$$   | $$$$$   | $$         | $$  | $$  | $$ 
| $$____/ | $$__  $$  | $$  | $$  $$$| $$| $$__/   | $$__/   | $$         | $$  | $$  | $$ 
| $$      | $$  \ $$  | $$  | $$\  $ | $$| $$      | $$      | $$    $$   | $$  | $$  | $$ 
| $$      | $$  | $$ /$$$$$$| $$ \/  | $$| $$$$$$$$| $$$$$$$$|  $$$$$$/   | $$  |  $$$$$$/ 
|__/      |__/  |__/|______/|__/     |__/|________/|________/ \______/    |__/   \______/ 

PrimeEcto Viewer Bot — Interactive, No CLI Needed!
""")))

def check_for_updates():
    return True

def print_announcement():
    return "Welcome to the Twitch Viewer Bot by PrimeEcto! Updates coming soon."

def simulate_viewer_activity(driver, viewer_index):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(3, 5))
        if random.choice([True, False]):
            driver.execute_script("document.querySelector('video')?.pause();")
        else:
            driver.execute_script("document.querySelector('video')?.play();")
        time.sleep(random.uniform(5, 15))
    except Exception as e:
        print(f"Error simulating activity for viewer {viewer_index}: {e}")

def main():
    if not check_for_updates():
        return

    announcement = print_announcement()
    banner()
    print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
    print(Colors.yellow, Center.XCenter(f"{announcement}"))
    print()

    proxy_servers = {
        1: "https://www.croxyproxy.com",           # Recommended
        2: "https://www.croxyproxy.rocks",
        3: "https://www.croxy.network",
        4: "https://www.croxy.org",
        5: "https://www.croxyproxy.net",
        6: "https://www.blockaway.net",            # Previously #1
        7: "https://www.youtubeunblocked.live",
    }

    print(Colors.green, Center.XCenter("Proxy Server 1 (CroxyProxy.com) is Recommended"))
    print()
    for i in range(1, 8):
        print(Colorate.Vertical(Colors.green_to_blue, f"Proxy Server {i}: {proxy_servers[i]}"))

    proxy_choice = int(input("\nEnter Proxy Server Number: "))
    proxy_url = proxy_servers.get(proxy_choice, proxy_servers[1])

    twitch_username = input("Enter your Twitch channel name (e.g. PrimeEcto): ")
    viewer_count = int(input("How many viewers to simulate? (open windows): "))

    headless_mode = input("Run in headless mode (no windows visible)? (y/n): ").strip().lower()
    headless = headless_mode == "y"

    print("\nChoose launch mode:")
    print("1. Stealth Mode (realistic & slower)")
    print("2. Rapid Mode (opens all viewers quickly) (Might cause dipping)")
    mode_choice = input("Enter mode number (1 or 2): ").strip()
    rapid_mode = mode_choice == "2"

    clear()
    banner()
    print(Colors.green, Center.XCenter("Sending viewers... Please wait."))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')

    if os.path.exists('adblock.crx'):
        chrome_options.add_extension('adblock.crx')

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")

    if headless:
        chrome_options.add_argument('--headless')

    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"Error launching Chrome: {e}")
        return

    try:
        for i in range(viewer_count):
            if i == 0:
                driver.get(proxy_url)
            else:
                driver.execute_script(f"window.open('{proxy_url}')")
                driver.switch_to.window(driver.window_handles[-1])

            if not rapid_mode:
                time.sleep(random.uniform(1.5, 3.5))

            try:
                text_box = driver.find_element(By.ID, 'url')
                text_box.send_keys(f'https://www.twitch.tv/{twitch_username}')
                text_box.send_keys(Keys.RETURN)
            except Exception as e:
                print(f"Error loading Twitch in tab {i + 1}: {e}")
                continue

            if not rapid_mode:
                simulate_viewer_activity(driver, i)

        input("\nAll viewers sent. Press ENTER to close all views and exit.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
