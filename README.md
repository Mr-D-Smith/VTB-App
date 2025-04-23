# 🔐 Intentionally Vulnerable Flask Login App

This is a Flask-based web application created intentionally vulnerable for the purpose of testing brute-force password attack tools and learning about web security.

## 💡 Project Goals

- Provide a safe and controlled environment to practice brute-force techniques.
- Simulate real-world login systems with increasing levels of protection.
- Learn about bruteforcing tools and techniques.

## 🏗️ Features

The app is divided into **security levels** that increase in complexity:

| Level | Description |
|-------|-------------|
| 1     | No protection: basic login form with no rate limiting, no CSRF, and fixed user credentials. |
| 2     | Basic redirection, slient failure. |
| 3     | CSRF protection: implements token-based protection and more advanced session handling. *(Current Level)* |
| 🚧    | More levels coming soon — such as CAPTCHA, account lockout, etc... |

## 🧪 Use Cases

- Practice brute-forcing with tools like your custom Python brute-force script.
- Test session reuse, threading, rate-limiting behavior, and CSRF handling.
- Use it as a teaching tool for web app security or ethical hacking courses.

## ⚠️ Disclaimer

> This project is for **educational purposes only**. Do **not** use these techniques against real systems without proper authorization.

## 🛠️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Mr-D-Smith/VTB-App
cd VTB-App
```
### 2. Start your lab

```bash
chmod +x start.sh
./start.sh
```
<br>

This will start the lab.
**Remeber** You need to submit the flag for previous level first , for lab to proceed further. <br>

**You will will promted to enter the flag on console once you have terminated the current flask session.** <br>

If you want to use just one particular level without submitting the flag just do:
```bash
python create_db.py
python lvl{n}.py
```

### 3. Resetting progress
If you ever want to reset your progress just do:
```bash
chmod +x reset.sh
./reset.sh
```
