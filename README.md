# 🎙️ JARVIS — Voice Controlled Desktop Assistant (No AI)

Jarvis is a **voice-controlled personal desktop assistant for Windows**, built entirely in Python **without using any AI platforms**.  
It listens for a wake word ("Jarvis") and performs system tasks, web actions, and media controls through voice commands.

---

## 🚀 Features

After saying **“Jarvis”**, you can use commands like:

### 🌐 Web & Apps
- **Open Google**
- **Open YouTube**
- **Open LinkedIn**
- **Open Gmail**
- **Open Spotify**
- **Open Jarvis window (GUI panel)**

### 🎵 Music & Media
- **Play \<song name\>** → Searches YouTube  
- **Play on Spotify \<song name\>** → Searches Spotify  

### 💬 Messaging
- **Send WhatsApp \<message\>** → Opens WhatsApp with prefilled text  

### 🖥️ System Controls
- **Shutdown my computer**
- **Restart my computer**
- **Increase volume**
- **Decrease volume**
- **Take screenshot**
- **What is my battery?**

### 🧠 Info
- **What is the time?**
- **What is the date?**
- **Search Wikipedia \<topic\>**

---

## 🛠️ Installation

Run this command in PowerShell:

```bash
pip install SpeechRecognition pyttsx3 wikipedia pyaudio psutil pycaw pyautogui pillow comtypes
