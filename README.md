# Secure Ops Crypto Tool

A lightweight, open-source Command-Line Interface (CLI) application built in Python designed to provide secure file encryption, decryption, and compliance auditing for development environments.

## Features
- **Data Confidentiality:** Implements an open-source byte-level XOR cryptographic algorithm to sanitize and protect sensitive file contents.
- **Automated Lifecycle Management:** Automatically detects missing target files and initializes them safely.
- **Audit Logging:** Generates a real-time sequential audit trail (`audit_log.txt`) with absolute timestamps to track authorization and compliance events.

## Installation & Usage
1. Clone the repository or download `crypto_tool.py`.
2. Run the application using the native Python launcher:
   ```bash
   python crypto_tool.py
