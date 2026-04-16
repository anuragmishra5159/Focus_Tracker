<div align="center">
  <h1>🎯 FocusTracker</h1>
  <p><strong>Stay Productive, Stay Focused</strong></p>
  <p><em>A productivity‑focused Chrome extension that tracks your browsing behavior, categorizes websites, and generates a personalized Focus Score to help you improve your daily efficiency.</em></p>
</div>

---

## 📖 Overview

Whether you're studying, working, or simply trying to reduce online distractions, **FocusTracker** provides real‑time insights into how you spend your time online. Operating as a Chrome extension with a powerful Python backend, it categorizes your browsing into *Productive*, *Distractive*, and *Neutral*, measuring your overall focus and visualizing your performance through clean analytics dashboards.

## ✨ Features

- 📊 **Track time spent** across multiple websites automatically.
- 🧠 **Categorize websites** into Productive, Distractive, and Neutral.
- ⏱️ **Real-time activity polling**: Rechecks browsing activity every 2 seconds.
- 🪟 **Accurate tracking**: Detects websites even when opened but not actively used.
- 🎯 **Focus Score calculation**: A simple, powerful metric of your daily productivity.
- 📈 **Visual analytics dashboard**: Beautiful charts built with Chart.js based on local cache data.
- ⚡ **High-performance backend**: Powered by FastAPI and Uvicorn.
- 🔄 **Real-time tracking and updates** to keep your data fresh.

## 🎯 Focus Score Logic

The Focus Score tells you how productive your browsing session has been:

\Focus Score = (Productivity Time / Total Time) * 100\

- **Productivity Time**: Time spent on productive websites (e.g., LinkedIn, educational platforms).
- **Total Time**: Total browsing time tracked.

*Example: 3 hours of Productive Time out of 5 hours Total Time = Focus Score of 60%.*

### Focus Score Categories

| Focus Score | Category | Meaning |
| :---: | :--- | :--- |
| **0 — 39** | 📉 Require Improvement | High distraction level |
| **40 — 69** | ⚖️ Average Focus Person | Moderate productivity |
| **70 — 100** | 🚀 High Focus Power | Highly productive |

## 🛠️ Tech Stack

**Backend**
- Python 3.8+
- FastAPI & Uvicorn
- SQLAlchemy
- Pydantic
- Python Multipart

**Frontend**
- HTML / CSS / Vanilla JavaScript
- Bootstrap
- Chart.js
- FontAwesome & Google Fonts

**Platform**
- Google Chrome Extension (Manifest V3)

## 📁 Project Structure

\\\	ext
FocusTracker/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── routes.py
│
├── extension/
│   ├── manifest.json
│   ├── background.js
│   ├── popup.html
│   ├── popup.js
│   └── styles.css
│
├── templates/
│   └── dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── charts/
│
└── README.md
\\\

## 💻 System Requirements

- **Python**: 3.14 (Recommended) or 3.8+
- **Browser**: Google Chrome (Latest Version) with Developer Mode Enabled
- **Hardware**: Minimum 512 MB RAM, At least 50 MB Disk Space
- **Network**: Localhost Network Configuration (No WiFi Required, operates offline)
- **Routing**: Routing Activation Enabled

## 🚀 Installation Guide

### 1. Clone the Repository
\\\ash
git clone https://github.com/your-username/FocusTracker.git
cd FocusTracker
\\\

### 2. Create & Activate Virtual Environment
\\\ash
# Create Virtual Environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
\\\

### 3. Install Dependencies & Run Backend
\\\ash
# Install dependencies
pip install fastapi uvicorn sqlalchemy pydantic python-multipart

# Run the Backend Server
uvicorn main:app --reload
\\\
*The server will start at: \http://127.0.0.1:8000\*

### 4. Load Chrome Extension
**1.** Open Google Chrome.
**2.** Go to \chrome://extensions/\.
**3.** Enable **Developer Mode** (top right corner).
**4.** Click **Load Unpacked**.
**5.** Select the \extension/\ folder (or the directory containing your \manifest.json\).

## 📊 Dashboard Features

- **Daily Focus Score**: At-a-glance metric of your day.
- **Productive vs Distractive Chart**: Clear visual breakdown of your time.
- **Website‑wise Breakdown**: Detailed stats per domain.
- **Time Tracking Visualization**: Historical performance viewing.

## 💡 Use Cases

- **Students** preparing for exams or lengthy study sessions.
- **Developers** tracking coding and reading time.
- **Remote workers** looking to improve focus and flow.
- **Anyone** trying to reduce social media distractions and doomscrolling.

## 🔮 Future Improvements

- [ ] AI‑based website classification
- [ ] Weekly & Monthly reports
- [ ] Customizable productivity goals
- [ ] Block distracting websites entirely during focus sessions
- [ ] Pomodoro Timer Integration

## 🤝 Contributing

Contributions are always welcome! 

1. Fork the repo
2. Create a feature branch (\git checkout -b feature/AmazingFeature\)
3. Commit your changes (\git commit -m 'Add some AmazingFeature'\)
4. Push to the branch (\git push origin feature/AmazingFeature\)
5. Open a Pull Request

## 💬 Support & Contact

If you found this project helpful, please consider giving it a **star** ⭐ on GitHub!

For suggestions, feedback, or issues, feel free to open an issue in the repository.

---
<div align="center">
  <p><em>FocusTracker helps you understand where your time goes, so you can take control of your productivity and stay focused every day.</em></p>
  <p>🚀 <strong>Stay Focused. Stay Productive.</strong> 🚀</p>
</div>


Day-2: initialise the files for the chrome extension 
In chrome-extension subfolder:
1. manifest.json
2. popup.js
3. background.js
4. popup.html

- Add icon files of all three sizes: 16px, 48px, 128px (icon16, icon48, icon128)
intilaize backend subfolder:
- __init_.py allows 
