# AI System Optimizer

An AI-powered desktop application that monitors system performance, analyzes RAM and CPU usage in real time, detects heavy processes, and provides intelligent optimization insights for developers and power users.

---

## Features

### Real-Time System Monitoring

* Live CPU usage tracking
* Live RAM usage tracking
* Auto-refreshing dashboard
* Real-time process monitoring

### Interactive Dashboard

* Modern dark-themed UI
* Live performance graphs
* Process usage table
* Responsive desktop interface

### Process Analysis

* Detect top RAM-consuming applications
* Display active processes with:

  * Process Name
  * PID
  * RAM Usage %
* Sort processes dynamically

### Intelligent Alerts

* High RAM usage detection
* System health status monitoring
* Performance bottleneck identification

### Future Features

* AI-based optimization suggestions
* Memory leak detection
* One-click optimization
* Process priority management
* System cleanup tools
* Export performance reports
* EXE packaging

---

## Tech Stack

### Language

* Python

### GUI Framework

* PyQt6

### System Monitoring

* psutil

### Graphing

* matplotlib

### Version Control

* Git & GitHub

---

## Project Structure

```bash
ai-system-optimizer/
│
├── ai/
│   └── recommendation_engine.py
│
├── database/
│
├── gui/
│   └── dashboard.py
│
├── monitor/
│   ├── cpu_monitor.py
│   ├── process_scanner.py
│   └── ram_monitor.py
│
├── optimizer/
│   └── cleaner.py
│
├── assets/
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/visshalb2007/ai-system-optimizer.git
```

### Move Into Project Folder

```bash
cd ai-system-optimizer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
.\venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running The Application

### Run GUI Dashboard

```bash
python gui/dashboard.py
```

### Run RAM Monitor

```bash
python monitor/ram_monitor.py
```

### Run CPU Monitor

```bash
python monitor/cpu_monitor.py
```

### Run Process Scanner

```bash
python monitor/process_scanner.py
```

---

## Screenshots

### Dashboard

(Add screenshots here later)

---

## Current Progress

* [x] RAM Monitoring
* [x] CPU Monitoring
* [x] Process Scanner
* [x] Live Dashboard
* [x] Dark Theme UI
* [x] Live Performance Graphs
* [x] Process Table

---

## Upcoming Improvements

* [ ] AI Recommendation Engine
* [ ] Memory Leak Detection
* [ ] Temperature Monitoring
* [ ] System Optimization Engine
* [ ] Startup App Analyzer
* [ ] One-Click Cleanup
* [ ] Export Reports
* [ ] EXE Installer

---

## Why This Project?

Modern developer workflows consume massive system resources due to:

* Browsers
* IDEs
* Docker containers
* AI tools
* Background applications

This project aims to provide:

* Better visibility into system performance
* Intelligent recommendations
* Real-time optimization assistance
* A modern lightweight monitoring experience

---

## Author

### Visshal Balaji

* GitHub: https://github.com/visshalb2007
* LeetCode: https://leetcode.com/VISSHALB2007

---

## License

This project is licensed under the MIT License.
