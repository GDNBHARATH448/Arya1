<h1 align="center">
DeadlineTech Music
</h1>

<p align="center">
    <img src="https://files.catbox.moe/lxn8yz.jpg" width="400">
</p>

<p align="center">
    <a href="https://github.com/deadlineTech/Music/stargazers">
        <img src="https://img.shields.io/github/stars/deadlineTech/Music?color=ffd700&style=for-the-badge&logo=github" />
    </a>
    <a href="https://github.com/deadlineTech/Music/network/members">
        <img src="https://img.shields.io/github/forks/deadlineTech/Music?color=blue&style=for-the-badge&logo=github" />
    </a>
    <a href="https://github.com/deadlineTech/Music/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/deadlineTech/Music?color=purple&style=for-the-badge&logo=open-source-initiative" />
    </a>
    <a href="https://www.python.org">
        <img src="https://img.shields.io/badge/Made%20With-Python-306998?style=for-the-badge&logo=python&logoColor=yellow" />
    </a>
</p>

---

## 🎧 Advanced Telegram Group Music Bot

> A modern Telegram bot for high-quality group music streaming using PyTgCalls and DeadlineTech’s powerful Music API key.

---

## ✨ Features

- 🎵 Stream music in group voice/video chats
- 🚀 Lightning-fast, stable, and scalable performance
- 🖼️ Dynamic thumbnails with song metadata
- 🎛️ Admin dashboard and playback controls
- 🧠 Intelligent queue management system
- ⚙️ Simple deployment on Heroku or VPS
- 🔑 Powered by [Deadline API Key](https://deadlinetech.site) for smooth music delivery

---

## 🔑 What is the API Key?

> A **Music API Key** by DeadlineTech gives you powerful music fetching, blazing-fast downloads, rich metadata, and seamless YouTube support.  
> Just buy it once and enjoy the best streaming experience on your Telegram groups!

- 🔗 [Buy API Key](https://deadlinetech.site)
- 💬 [Ask on Telegram](https://t.me/DeadlineTechOwner)

---

## 📜 Commands Introduction

### 🎵 Music Playback
- `/play <song name or YouTube URL>` – Play audio.
- `/vplay <video name or URL>` – Play video.
- `/pause` – Pause current song.
- `/resume` – Resume paused song.
- `/skip` – Skip current song.
- `/end` – End music and clear queue.

### 🧰 Utilities
- `/start` – Start bot.
- `/help` – Help menu.
- `/ping` – Check ping.
- `/stats` – Bot stats.

### 🎛️ Admin Controls
- `/auth` – Authorize user.
- `/unauth` – Remove auth.
- `/authusers` – List authorized users.

### 📋 Queue System
- `/queue` – Show queue.
- `/shuffle` – Shuffle queue.
- `/loop` – Toggle loop.

---

## 🚀 Deployment Options

<details>
<summary><b>🔹 Deploy to Heroku</b></summary>

[![Deploy](https://img.shields.io/badge/Deploy%20to-Heroku-4700f5?style=for-the-badge&logo=heroku)](https://dashboard.heroku.com/new?template=https://github.com/deadlineTech/Music)

</details>

<details>
<summary><b>🔸 Deploy on VPS / Localhost</b></summary>

**1. Install Dependencies**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip ffmpeg -y
sudo pip3 install -U pip
```

**2. Install NodeJS**
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && source ~/.bashrc && nvm install v18
```

**3. Clone Project**
```bash
git clone https://github.com/deadlineTech/music
cd music
pip3 install -U -r requirements.txt
```

**4. Setup .env**
```bash
cp sample.env .env
vi .env
```

- Press `I` to edit, `Ctrl + C`, then `:wq` to save.

**5. Run Bot**
```bash
sudo apt install tmux && tmux
bash start
```
Detach with: `Ctrl + B`, then `D`

</details>

---

## 🔧 Environment Variables

```env
API_ID=123456
API_HASH=abcdef1234567890abcdef1234567890
BOT_TOKEN=YOUR_BOT_TOKEN
OWNER_ID=123456789
MONGO_DB_URI=mongodb+srv://username:password@cluster.mongodb.net/dbname
API_KEY=YOUR_API_KEY  # Get from @DeadlineApiBot
STRING_SESSION=YOUR_STRING_SESSION
```

---

## 👥 Support & Community

- 🔔 [Channel](https://t.me/DeadlineTechTeam)
- 💬 [Support Group](https://t.me/DeadlineTechSupport)
- 🧑‍💻 [Developer Contact](https://t.me/DeadlineTechOwner)

---

## 🧠 Credits

- ⚙️ Base: [Anon Music](https://github.com/AnonymousX1025/AnonXMusic)
- 💻 Contributors: `@DeadlineTechOwner`, open source devs

---

## 📄 License

> Licensed under the MIT License.

---

## 🔗 Quick Links

- 💰 [Buy API Key](https://deadlinetech.site)
- 👨‍💻 [Developer](https://t.me/DeadlineTechOwner)
- 🛠️ [Support](https://t.me/DeadlineTechSupport)

---

<p align="center">
  <b>Made with ❤️ by <a href="https://t.me/DeadlineTechTeam">DeadlineTech</a></b>
</p>
