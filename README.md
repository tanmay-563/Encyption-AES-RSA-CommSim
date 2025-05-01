# 🔐 AES-RSA-CommSim

**A Secure Communication Simulator using AES Encryption and RSA Key Exchange**

> Simulate a real-time encrypted chat between two users with AES for fast symmetric encryption and RSA for secure key exchange. Ideal for students, enthusiasts, and anyone interested in understanding how hybrid encryption works in real-world messaging apps.

---

## 🚀 Features

- 🔑 **AES-128 Encryption** for secure message confidentiality  
- 🧾 **HMAC** for message integrity verification  
- 🔐 **RSA Encryption** for secure AES key sharing  
- 👥 **Two-user chat simulation** with encrypted + decrypted views  
- 🖥️ **Simple GUI (Tkinter)** for interactive chatting  
- 💬 **Switch between User A and User B** to view encrypted and decrypted messages

---

## 🛠️ How It Works

This project simulates secure chat using a **hybrid cryptography model**:

### 🧠 Step-by-step:
1. **RSA Key Generation**:  
   On app start, RSA public-private keys are generated.

2. **AES Key Creation**:  
   A random 128-bit AES key is generated for symmetric encryption.

3. **Key Exchange via RSA**:  
   AES key is encrypted with the RSA public key and then decrypted using the private key — mimicking a secure exchange.

4. **Message Encryption**:  
   Messages are encrypted with AES and verified using HMAC to ensure they haven’t been tampered with.

5. **User View Switching**:  
   The user can switch between A and B, seeing encrypted messages and decrypting them on demand.

---

## 📸 Preview

> Chat window with encrypted and decrypted views:

![screenshot](assets/demo-screenshot.png) <!-- optional, add your screenshot -->

---

## 💾 Installation

### 🔧 Prerequisites:
- Python 3.7+
- Required libraries:
  ```bash
  pip install pycryptodome
