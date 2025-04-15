# Encrypted File Transfer Utility

A Flask-based dashboard for managing IT assets, including authentication, device tracking, and lifecycle status (Available, Assigned, Retired). Uses SQLite for persistent storage and a responsive front-end UI.

## Features
- AES-256 file encryption and decryption
- Password-based key derivation
- Cross-platform compatible (Windows, macOS, Linux)
- Simple GUI interface for selecting files

## Requirements
- Python 3.x
- `pycryptodome`
- `tkinter` (comes pre-installed with Python)

## Setup
```bash
pip install -r requirements.txt
python encrypt_file.py
python decrypt_file.py
```
