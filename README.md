# 🔐 JWT Attack Lab

A hands-on lab demonstrating real-world JWT vulnerabilities, exploitation techniques, and misconfigurations commonly found in modern applications.

---

## 🚨 Vulnerabilities Covered

* alg:none signature bypass
* Weak secret brute-force attack
* Privilege escalation via token forging
* Expired token bypass (no exp validation)

---

## ⚔️ Exploits Included

* Forge admin tokens
* Crack weak JWT secrets using wordlists
* Craft unsigned tokens (alg:none attack)

---

## 🧪 Usage

### Start the vulnerable server:

```bash
python app.py
```

### Get a token:

```
http://127.0.0.1:5000/login?user=test
```

### Run exploits:

```bash
python exploits/forge_token.py
python exploits/alg_none.py
python exploits/brute_force.py
```

---

## 🎯 Purpose

This project is built for:

* Security researchers
* Bug bounty hunters
* Developers learning secure authentication

---

## ⚠️ Disclaimer

This lab is for educational purposes only. Do not use these techniques on systems you do not own or have permission to test.

---

## 👨‍💻 Author

Usman Soni
