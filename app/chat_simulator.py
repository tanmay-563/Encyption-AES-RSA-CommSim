import tkinter as tk
from tkinter import scrolledtext
from aes_simulation import encrypt_with_hmac, decrypt_with_hmac
from rsa_key_exchange import generate_rsa_keys, encrypt_aes_key, decrypt_aes_key
from Crypto.Random import get_random_bytes
import base64

# Generate RSA keys and AES key
public_key, private_key = generate_rsa_keys()
aes_key = get_random_bytes(16)  # AES key (simulated)

# Encrypt AES key using RSA public key (for key exchange)
encrypted_aes_key = encrypt_aes_key(aes_key, public_key)

# Simulate RSA key exchange (User B decrypts AES key)
decrypted_aes_key = decrypt_aes_key(encrypted_aes_key, private_key)

# GUI setup
window = tk.Tk()
window.title("AES Secure Chat")
window.config(bg="#34495E")  # Dark background color for the window

# Configure chat log area
chat_log = scrolledtext.ScrolledText(window, width=60, height=20, state='disabled', bg="#2C3E50", fg="white", font=("Helvetica", 12))
chat_log.pack(pady=10)

# Configure user input field
user_input = tk.Entry(window, width=50, font=("Helvetica", 12), bd=2, relief="solid", fg="black", bg="#ECF0F1")
user_input.pack(side=tk.LEFT, padx=10)

# Sender dropdown menu
sender_var = tk.StringVar(value="A")
sender_menu = tk.OptionMenu(window, sender_var, "A", "B")
sender_menu.config(bg="#2980B9", fg="white", font=("Helvetica", 12))
sender_menu.pack(side=tk.LEFT, padx=10)

# Store messages
messages = []

def send_message():
    sender = sender_var.get()
    receiver = "B" if sender == "A" else "A"
    message = user_input.get().strip()

    if not message:
        return

    # Encrypt with AES and add HMAC for integrity
    encrypted_message, hmac_value = encrypt_with_hmac(message, decrypted_aes_key, decrypted_aes_key)

    # Store the message (encrypted) and its sender/receiver
    messages.append((sender, receiver, encrypted_message, hmac_value))

    # Display encrypted message in chat log
    chat_log.configure(state='normal')
    chat_log.insert(tk.END, f"{sender} ➤ {receiver} (Encrypted): {encrypted_message}\n", "encrypted")
    chat_log.insert(tk.END, f"HMAC: {hmac_value}\n", "hmac")
    chat_log.configure(state='disabled')

    # Clear the input field
    user_input.delete(0, tk.END)

def decrypt_message():
    # Get the current active user
    sender = sender_var.get()
    receiver = "B" if sender == "A" else "A"

    # Loop through all messages and decrypt the ones for the current user
    chat_log.configure(state='normal')

    for msg_sender, msg_receiver, encrypted_message, hmac_value in messages:
        if msg_receiver == sender:
            # Decrypt the message using the same AES key
            decrypted_message, _ = decrypt_with_hmac(encrypted_message, decrypted_aes_key, decrypted_aes_key)

            # Display the decrypted message for the active user
            chat_log.insert(tk.END, f"{msg_sender} ➤ {msg_receiver} (Decrypted): {decrypted_message}\n\n", "decrypted")
    
    chat_log.configure(state='disabled')

# Button to send the message
send_button = tk.Button(window, text="Send", command=send_message, bg="#27AE60", fg="white", font=("Helvetica", 12), relief="solid", bd=2)
send_button.pack(side=tk.LEFT, padx=10)

# Button for user to decrypt message
decrypt_button = tk.Button(window, text="Decrypt Messages", command=decrypt_message, bg="#E74C3C", fg="white", font=("Helvetica", 12), relief="solid", bd=2)
decrypt_button.pack(side=tk.LEFT, padx=10)

# Show the shared AES key (base64-encoded for display)
# If you'd like to keep the AES key hidden, comment out the next line:
tk.Label(window, text=f"Shared AES Key (base64): {base64.b64encode(aes_key).decode()}", font=("Courier", 8), bg="#34495E", fg="white").pack(pady=5)

# Add tag configurations for colored text
chat_log.tag_configure("encrypted", foreground="cyan")  # Encrypted messages in cyan
chat_log.tag_configure("decrypted", foreground="lime")   # Decrypted messages in lime
chat_log.tag_configure("hmac", foreground="yellow")      # HMAC in yellow

window.mainloop()
