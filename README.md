
<h1 align="center">⚔️ DIRHUNTER v1.0.1</h1>

<p align="center">
  <b>A blazing-fast, elegant directory brute-force tool built for ethical hackers, penetration testers, and cybersecurity researchers.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square&logo=python">
  <img src="https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-green.svg?style=flat-square">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg?style=flat-square">
  <img src="https://img.shields.io/github/stars/yourusername/dirhunter?style=flat-square">
</p>

---

## 🧠 What is DIRHUNTER?

`DIRHUNTER` is a terminal-based tool for scanning hidden directories and files on a web server using a wordlist. It’s fast, visually slick, and customizable — perfect for **bug bounty hunters**, **pentesters**, or anyone looking to improve their reconnaissance.

Built with ⚡ `httpx`, 💄 `rich`, and 🎯 `click` — for modern CLI interaction and high-speed HTTP requests.

---

## ✨ Features

- ⚡ **High performance:** Powered by `httpx` with customizable timeouts.
- 🖼️ **Beautiful terminal UI:** Spinner, progress bar, color-coded responses.
- 📂 **Extension support:** Scan for `.php`, `.html`, `.bak`, and more.
- 🔐 **Status code filtering:** See only what matters (200, 403, redirects).
- 💾 **Output saving:** Save successful results to a file automatically.
- 🧪 **Custom headers (coming soon):** Easily spoof User-Agent/Cookies.

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.8+
- `httpx`
- `rich`
- `click`

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install httpx rich click
```

### 📦 Clone the Repo

```bash
git clone https://github.com/m0n3ef/dirhunter.git
cd dirhunter
```

---

## 🛠️ Usage

```bash
python dirhunter.py -t https://example.com/
```

### 🧾 CLI Options

| Option      | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| `-t`        | 🔥 **Target URL** — must end with a `/` (required)                          |
| `-ext`      | Add file extension (e.g., `.php`, `.html`, `.bak`, etc.)                    |
| `-o`        | Save hits to `output.txt` (set to `True`)                                   |
| `-tm`       | Set HTTP timeout (in seconds). Default is `10`                              |
| `-c`        | Show status codes (200, 403, etc.)                                          |
| `-w`        | Use a custom wordlist (wordlist.txt)                                        |
| `-sub`      | sub-domain scanning and hunting                                             |

### 🔍 Example

```bash
python dirhunter.py -t https://target.com/ -ext .php -c -o True -tm 5
```

This command will:

- Look for `.php` files in `dlistlowercasesmall.txt`
- Show you results with status codes
- Save successful results to a file
- Timeout each request after 5 seconds

---

## 📁 Wordlist

The tool uses the file `dlistlowercasesmall.txt` in the same directory as your script.  
You can replace it with a bigger or custom wordlist to enhance discovery:

```bash
wordlist.txt → dlistlowercasesmall.txt
```

---

## 📌 Sample Output

```bash
[+] Found: https://target.com/admin/ | Code: 200
[!] Forbidden: https://target.com/private/ | Code: 403
[!] Redirected: https://target.com/login/ | Code: 301
[x] Error: https://target.com/.env — timeout
```

Color-coded for clarity. Live updated while scanning!

---

## 📤 Output

If `-o True` is passed, all valid URLs will be saved to `output.txt`:

```
https://target.com/admin/
https://target.com/dashboard.php
https://target.com/config/
```

Perfect for post-processing, automation, or reporting.

---

## 🧩 Planned Features

- [ ] Proxy support (HTTP/SOCKS)
- [ ] Custom headers (User-Agent, Cookies)
- [ ] Recursive scanning (e.g. follow `/admin/` for deeper paths)
- [ ] Threads/Async speed boost
- [ ] Interactive mode

---

## 🧑‍💻 Author

Created with 💀 and 💻 by [@m0n3ef](https://github.com/m0n3ef)

If you find this useful, give it a ⭐ on GitHub and spread the word!

---

## 🤝 Contributing

Contributions are more than welcome!

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request 🧠

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## ☕ Support This Project

- Leave a ⭐ on GitHub
- Share it on Twitter, LinkedIn, or with your hacker friends
- Submit issues and pull requests
- Suggest ideas and features

---

## 🧬 Disclaimer

This tool is for **educational and authorized security testing purposes only**.  
Unauthorized use of this tool against targets without explicit permission is **illegal and unethical**.

---
