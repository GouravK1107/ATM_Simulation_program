# 🏧 Adex Bank — ATM Simulator

A simple yet functional console-based ATM simulation built in pure Python. Mimics real-world ATM operations — cash withdrawal, balance enquiry, PIN management, OTP-based reset, and receipt generation — all through a clean text-based interface.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-Console%2FCLI-333333?style=for-the-badge)

---

## 📖 About

This project simulates core ATM workflows end-to-end in a single Python script — built as a fundamentals project to practice conditionals, loops, functions, time delays, and dictionary-based data handling, structured the way a real ATM would behave. I built it on my own after learning python.

---

## 🚀 Features

- 💵 Cash withdrawal
- 💰 Balance enquiry
- 📱 Phone number update
- 🔢 PIN generation
- 🔐 PIN verification on every session
- 🔑 OTP-based authentication for PIN reset
- 🚫 Card blocking after multiple failed PIN attempts
- 🧾 Receipt generation with full transaction details
- 🖥️ Clean, console-based UI simulating a real ATM workflow

---

## 🛠️ Tech Stack

- Python (standard library only — no external dependencies)

---

## 📂 Project Structure

```
ATM_Simulation_program/
│
├── atm.py       # Complete ATM simulation logic
└── README.md
```

---

## ⚙️ Installation & Usage

**1️⃣ Clone the repository**
```
git clone https://github.com/GouravK1107/ATM_Simulation_program.git
cd ATM_Simulation_program
```

**2️⃣ Run it — no dependencies needed**
```
python atm.py
```

Follow the on-screen console prompts to withdraw cash, check balance, update your phone number, reset your PIN via OTP, or generate a transaction receipt.

---

## 🧠 What This Project Demonstrates

- Conditionals, loops, and function design in Python
- Dictionary-based data modeling (accounts, PINs, balances)
- Basic security logic — PIN verification, OTP flow, failed-attempt lockout
- Simulated time delays for a realistic ATM feel
- Structuring a multi-feature CLI application cleanly in a single script

---

## 🙏 A Note on How This Was Built

This was a learning project — most of the logic (menu flow, withdrawal, balance checks, PIN/OTP handling, account structure) was written independently. A couple of specific pieces got AI assistance along the way: the `zfill()` padding method (wasn't familiar with it beforehand) and the `slip_fun()` receipt-formatting helper, plus some general testing support. Being upfront about that here since it's a more honest picture of the build process than pretending otherwise.

---

## 🔥 Future Improvements

- 💾 Persist account data to a file/database instead of in-memory
- 👥 Multi-user account support
- 🖥️ Simple GUI version (Tkinter)
- 📊 Transaction history log
- 🌐 Convert into a Flask/Django web-based ATM simulator

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Fork → create a branch → commit → push → open a pull request.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Gourav R**
Backend Developer | Applied AI Developer

GitHub: https://github.com/GouravK1107
Portfolio: https://gouravk1107.github.io/my-portfolio/

---

Made with ❤️ and a healthy respect for `.zfill()`.
