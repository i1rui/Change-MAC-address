
# Change MAC Address

A simple Python script to change the MAC address of a network interface on Linux systems.

> ⚠️ **Disclaimer**: This tool is for educational and authorized testing purposes only. Changing your MAC address without permission may violate network or legal policies.

## 📌 Author
- **By N3cr0Sh3ll**
- Telegram: [@i1rui](https://t.me/i1rui)

---

## 🛠 Requirements

- Python 3.x
- Root privileges
- `ifconfig` command (Install via `sudo apt install net-tools`)

---

## 📥 Installation & Usage

### 1. Clone the repository:

```bash
git clone https://github.com/i1rui/Change-MAC-address.git
```

### 2. Navigate into the project directory:

```bash
cd Change-MAC-address
```

### 3. Run the script:

```bash
sudo python3 mac_changer.py -i <interface> -m <new_mac>
```

### ✅ Example:

```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

---

## 📄 Script Options

| Option | Description |
|--------|-------------|
| `-i`   | Network interface name (e.g., `eth0`, `wlan0`) |
| `-m`   | New MAC address to assign (e.g., `00:11:22:33:44:55`) |

---

## 🧪 Sample Output

```
[+] By N3cr0Sh3ll|Telegram:i1rui):
[+] Changing MAC Address for eth0 to 00:11:22:33:44:55
[+] MAC address has changed successfully to 00:11:22:33:44:55
[+] By N3cr0Sh3ll|Telegram:i1rui):
```

---

## ⚠️ Notes

- Run the script as root using `sudo`.
- Interface name and MAC format must be valid.
- Script uses `ifconfig`, ensure it’s installed.

---

## 📬 Contact

For help or feedback:

**Telegram:** [@i1rui](https://t.me/i1rui)
