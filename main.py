#!/usr/bin/env python3
"""
Simple Secure Messenger
Demo using Fernet (AES + HMAC)
"""

from cryptography.fernet import Fernet
import os
import sys

KEY_FILE = "key.key"

def load_or_generate_key():
    """Load key from file or generate new one."""
    if os.path.exists(KEY_FILE):
        return open(KEY_FILE, "rb").read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        print(f"New key generated and saved to {KEY_FILE}")
        print("Share this file securely with the other user!")
        return key

def main():
    cipher = Fernet(load_or_generate_key())
    
    print("\nSecure Messaging Simulator (Fernet/AES)")
    print("s = send (encrypt) | r = receive (decrypt) | q = quit\n")

    while True:
        choice = input(" > ").strip().lower()
        
        if choice == 'q':
            print("Goodbye!\n")
            break
        elif choice == 's':
            msg = input("  Message: ").strip()
            if msg:
                encrypted = cipher.encrypt(msg.encode()).decode()
                print(f"  Send: {encrypted}\n")
        elif choice == 'r':
            try:
                token = input("  Paste token: ").strip()
                decrypted = cipher.decrypt(token.encode()).decode()
                print(f"  Decrypted: {decrypted}\n")
            except Exception:
                print("  Invalid or tampered message!\n")
        else:
            print("  Invalid: use s, r, or q\n")

if __name__ == "__main__":
    main()
        print("Invalid choice. Try 's' or 'r'.")
