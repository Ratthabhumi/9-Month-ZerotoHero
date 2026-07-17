# 05_Argparse_CLI_Cheatsheet.md (Week 2 Day 5)

## 📌 ทำไมต้องใช้ `argparse`?
ตอนเราเขียนโค้ดเบื้องต้น เรามักจะใช้ `input()` เพื่อถามผู้ใช้ทีละข้อ:
```python
name = input("Enter name: ")
age = input("Enter age: ")
```
**ข้อเสีย:** ถ้าเราอยากรันสคริปต์แบบอัตโนมัติ (Automated) เราจะไม่สามารถมานั่งพิมพ์ตอบทีละบรรทัดได้

**ทางแก้:** เราใช้ `argparse` เพื่อรับค่าทั้งหมดพร้อมกับการรันคำสั่งในบรรทัดเดียวจบ เหมือนเวลาเราใช้คำสั่ง Linux หรือ Git (เช่น `git add .` หรือ `python script.py --name John --age 20`)

---

## 🛠️ โครงสร้างพื้นฐานของ `argparse`

```python
import argparse

# 1. สร้างตัวแปลคำสั่ง (Parser)
parser = argparse.ArgumentParser(description="คำอธิบายโปรแกรมของคุณ")

# 2. เพิ่มคำสั่งย่อย (Subcommands) เช่น add, get, delete
subparsers = parser.add_subparsers(dest="command", help="เลือกคำสั่งที่ต้องการ")

# ----------------------------------------------------
# 3. สร้างคำสั่งย่อย 'add' (เปรียบเหมือนเมนู Add)
# ----------------------------------------------------
parser_add = subparsers.add_parser("add", help="เพิ่มข้อมูลใหม่")
parser_add.add_argument("site", help="ชื่อเว็บไซต์")     # รับค่าที่ 1
parser_add.add_argument("password", help="รหัสผ่าน")    # รับค่าที่ 2

# ----------------------------------------------------
# 4. ให้ระบบอ่านค่าที่ผู้ใช้พิมพ์เข้ามาใน Terminal
# ----------------------------------------------------
args = parser.parse_args()

# 5. นำค่าไปใช้งาน
if args.command == "add":
    print(f"คุณต้องการเพิ่มรหัสผ่านของเว็บ {args.site} คือ {args.password}")
```

## 💻 วิธีการรันโปรแกรมผ่าน Terminal

สมมติว่าเซฟโค้ดด้านบนไว้ในไฟล์ชื่อ `main.py`
เวลาเรารัน เราต้องส่งค่าเข้าไปพร้อมกับการเรียกไฟล์เลย:

**ถ้าไม่ใส่อะไรเลย (หรือใส่ -h) มันจะขึ้นคู่มือให้อัตโนมัติ:**
```bash
python main.py -h
```

**ถ้าต้องการรันคำสั่ง add พร้อมส่งค่า 2 ค่า:**
```bash
python main.py add facebook 123456
```
- ระบบจะมองว่า `add` คือค่าของ `args.command`
- ระบบจะมองว่า `facebook` คือค่าของ `args.site`
- ระบบจะมองว่า `123456` คือค่าของ `args.password`
