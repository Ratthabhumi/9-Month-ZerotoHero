# 🔐 Secure Password Manager CLI

นี่คือโปรเจค Password Manager ที่ทำงานผ่าน Command Line Interface (CLI) พัฒนาด้วย Python
จุดเด่นคือใช้การเข้ารหัสระดับสูงผ่านไลบรารี `cryptography` (Fernet Symmetric Encryption)

## 📦 การติดตั้ง (Installation)

1. ต้องมี Python 3 ติดตั้งอยู่ในเครื่อง
2. ติดตั้งไลบรารีที่จำเป็นโดยใช้คำสั่ง:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 วิธีการใช้งาน (Usage)

โปรแกรมนี้ออกแบบมาให้ใช้งานเหมือนคำสั่งใน Linux/Git โดยรับพารามิเตอร์แบบบรรทัดเดียวจบ

**1. ดูคู่มือคำสั่ง (Help)**
```bash
python main.py -h
```

**2. เพิ่มรหัสผ่านใหม่ (Add)**
```bash
python main.py add <ชื่อเว็บ> <รหัสผ่าน>
# ตัวอย่าง: python main.py add facebook mysecurepass123
```

**3. ดูรหัสผ่าน (Get)**
```bash
python main.py get <ชื่อเว็บ>
# ตัวอย่าง: python main.py get facebook
```

## ⚠️ ข้อควรระวัง (Security Warning)
- โปรแกรมจะสร้างไฟล์ `secret.key` อัตโนมัติในการรันครั้งแรก
- **ห้าม** ทำไฟล์ `secret.key` หายเด็ดขาด มิฉะนั้นคุณจะไม่สามารถถอดรหัสผ่านที่บันทึกไว้ได้อีกเลย
- **ห้าม** แชร์ไฟล์ `secret.key` ให้ผู้อื่น เพราะมันคือกุญแจมาสเตอร์ที่ไขฐานข้อมูลของคุณได้
