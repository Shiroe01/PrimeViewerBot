# 📺 Twitch Viewer Bot by PrimeEcto

An advanced, user-friendly Twitch Viewer Bot designed to simulate active viewers using real browser sessions — no command-line knowledge required.

This bot supports multiple viewing modes, proxy options, and automation tools, making it ideal for testing Twitch stream behavior, overlays, and interactions at scale.

---

## 🔧 Features

- ✅ **No Proxy Setup Needed**  
  Pre-integrated with multiple public proxy services — no configuration or sourcing required.

- 🚀 **Dual Launch Modes**  
  - **Stealth Mode**: Opens viewers gradually to mimic real user behavior.  
  - **Rapid Mode**: Launches all viewers instantly for speed and load testing.

- 🎮 **Realistic Viewer Simulation**  
  Simulates activity such as scrolling, pausing, and playing video streams to mimic live audience behavior.

- 🧠 **Intelligent Window Handling**  
  Supports multiple concurrent viewer sessions in separate browser tabs or windows.

- 🧼 **Clean UI**  
  Interactive interface with no command-line clutter — just launch, enter inputs, and go.

- 📦 **Auto Extension Support**  
  Optional `adblock.crx` support for cleaner Twitch sessions.

- 🔔 **Auto Version Checker**  
  Detects and announces new GitHub releases automatically — stay updated with zero effort.

- 🛠 **Headless Mode**  
  Run sessions invisibly in the background — perfect for multitasking or server setups.

---

## 📝 Notes

- This tool is for **educational and testing purposes only**.  
- It does **not guarantee engagement** or violate Twitch’s TOS if used responsibly.  
- No Twitch login or API access required.  
- Pickup-only bot — does not run in the cloud or external environments.

---

## 📥 Installation Instructions

1. Download the latest `.zip` file from the [Releases](../../releases) section  
2. Extract the contents using **7-Zip**, **WinRAR**, or your preferred archive tool  
3. Open the extracted folder (likely named `PrimeEctoBot2.0`)  
4. **Double-click** `install.bat`  
   - This will automatically install all required Python dependencies  
5. Once installation is complete, **double-click** `run.bat` to launch the bot

---

## ▶️ How to Use

After launching `run.bat`, follow the prompts:

1. **Select a Proxy Server**  
   - Recommended: **CroxyProxy.com**

2. **Enter your Twitch channel name**  
   - Example: `PrimeEcto`

3. **Enter how many viewers to simulate**  
   - This determines how many browser tabs or windows will open

4. **Choose whether to run in Headless Mode**  
   - `Y` = run in the background without showing browser windows  
   - `N` = open visible browser windows

5. **Choose a Launch Mode**  
   - **Stealth Mode**: Slower, more realistic loading pattern  
   - **Rapid Mode**: Faster, all viewers launched immediately

The bot will then launch the viewers and simulate active viewership on your Twitch stream.

---
