# 🔐 WPA2 Password Crack-Time Simulator

A simple Python-based tool that demonstrates how long it might take for an attacker to brute-force a given password.  
It uses realistic GPU hash rates and calculates the total combinations based on password length and character set.

---

## 🚀 Features
- Estimates **crack time** for both:
  - 🖥️ Standard GPU (~150K guesses/sec)
  - ⚡ High-End GPU (~1.1M guesses/sec)
- Analyzes password **character diversity** (lowercase, uppercase, digits, special characters)
- Displays total possible combinations and estimated crack time in **human-readable format**
- Educates users about **password strength and entropy**

---

## 📸 Demo

| Example | Password | Length | Character Set | Crack Time (High-End GPU) |
|----------|-----------|---------|----------------|-----------------------------|
| `password` | 8 | 26 (a-z) | 2.2 days |
| `pass123` | 7 | 36 (a-z, 0-9) | 19.8 hours |
| `password!123` | 12 | 68 (a-z, A-Z, 0-9, symbols) | 281.8 million years |
| `password_not_found` | 18 | 58 | 1.5 billion years |

---

## 🧠 How It Works

1. **Input a password**
2. The tool determines the size of the **character set** based on which characters are used (letters, digits, symbols)
3. It calculates:
