# 🔐 Cryptography & Python Project Structure Cheatsheet (Week 2 Day 4)

## 1. การจัดโครงสร้างโปรเจค (Project Structuring)
การเขียนโค้ดที่ดี ไม่ควรยัดทุกอย่างไว้ในไฟล์เดียว ควรแยกเป็น **โมดูล (Module)** ตามหน้าที่การทำงาน (Separation of Concerns)

**ตัวอย่างโครงสร้าง:**
```text
MyProject/
 ├── main.py           # ตัวรันโปรแกรมหลัก / ส่วนติดต่อผู้ใช้ (UI/CLI)
 ├── crypto_utils.py   # ไฟล์รวมฟังก์ชันเฉพาะทาง (เช่น การเข้ารหัส)
 ├── database.py       # ไฟล์สำหรับติดต่อฐานข้อมูล
 └── requirements.txt  # ไฟล์เก็บรายชื่อไลบรารีภายนอกที่ต้องใช้
```

**การเรียกใช้งานข้ามไฟล์ (Importing):**
```python
# ในไฟล์ main.py
from crypto_utils import encrypt_password, decrypt_password
```

## 2. การใช้งานไลบรารี `cryptography`
เราใช้โมดูล `Fernet` สำหรับการเข้ารหัสแบบ **Symmetric Encryption** (ใช้กุญแจดอกเดียวกันทั้งล็อคและปลดล็อค)

### ติดตั้งไลบรารี
```bash
pip install cryptography
```

### การสร้างและโหลดกุญแจ (Key Management)
กุญแจ (Key) คือหัวใจสำคัญที่สุด ถ้ากุญแจหาย จะไม่มีใครถอดรหัสได้อีกเลย ถ้ากุญแจหลุด แฮกเกอร์ถอดรหัสได้หมด
```python
from cryptography.fernet import Fernet

# 1. สร้างกุญแจใหม่ (ทำแค่ครั้งแรกครั้งเดียว)
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# 2. โหลดกุญแจมาใช้งาน
key = open("secret.key", "rb").read()
f = Fernet(key)
```

### การเข้ารหัส (Encryption)
แปลงข้อความธรรมดา (Plain Text) เป็นข้อความอ่านไม่ออก (Ciphertext)
```python
plain_text = "my_password123"
# ต้องแปลง string เป็น bytes ก่อนด้วย .encode()
encrypted_data = f.encrypt(plain_text.encode()) 
```

### การถอดรหัส (Decryption)
แปลงข้อความอ่านไม่ออก (Ciphertext) กลับเป็นข้อความธรรมดา (Plain Text)
```python
# ผลลัพธ์จะเป็น bytes
decrypted_data = f.decrypt(encrypted_data)
# แปลง bytes กลับเป็น string ด้วย .decode()
plain_text = decrypted_data.decode()
```
