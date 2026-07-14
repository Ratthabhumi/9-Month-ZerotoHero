# 🚀 Python Advanced Cheatsheet (Week 2 Day 2)

## 1. Decorators (ตัวตกแต่งฟังก์ชัน)
ใช้สำหรับ "แทรกแซง" หรือเพิ่มความสามารถให้ฟังก์ชันอื่น โดยไม่ต้องเข้าไปแก้โค้ดข้างในฟังก์ชันนั้น (มีประโยชน์มากเวลาต้องเขียนระบบเช็คสิทธิ์, จับเวลา, หรือเก็บบันทึก Log)

```python
# 1. สร้างตัว Wrapper
def require_admin(func):
    def wrapper(*args, **kwargs):
        if user != "admin":
            print("Access Denied!")
            return
        return func(*args, **kwargs) # ให้รันฟังก์ชันเดิมต่อ
    return wrapper

# 2. เอาไปแปะใช้งานด้วยสัญลักษณ์ @
@require_admin
def delete_database():
    print("Database deleted!")
```

## 2. Generators & Yield (เครื่องผลิตข้อมูลประหยัดแรม)
ใช้แทน `return` เมื่อต้องจัดการกับข้อมูลมหาศาล (เช่น ไฟล์ Log ระดับ GB)
- **`return`**: สร้างข้อมูลทั้งหมดพร้อมกัน กิน RAM มหาศาล
- **`yield`**: สร้างและส่งข้อมูลออกมาทีละ 1 ชิ้น ประหยัด RAM ขั้นสุด

```python
def read_huge_logs():
    for i in range(1, 1000000):
        yield f"Log Line {i}"

# นำมาใช้ร่วมกับ for loop
for line in read_huge_logs():
    if "Error" in line:
        print("Found error!")
        break # หยุดทำงานทันที ไม่ต้องโหลดบรรทัดที่เหลือ
```

## 3. Error Handling (try...except)
ใส่เกราะป้องกันให้สคริปต์ เพื่อไม่ให้โปรแกรมพัง (Crash) เมื่อเกิดข้อผิดพลาด

```python
try:
    # โค้ดที่เสี่ยงจะเกิด Error
    result = 10 / 0
except ZeroDivisionError:
    # ดักจับ Error ที่เฉพาะเจาะจง
    print("ห้ามหารด้วยศูนย์!")
except Exception as e:
    # ดักจับ Error อื่นๆ ทั้งหมด
    print(f"เกิดข้อผิดพลาด: {e}")
finally:
    # (มีหรือไม่มีก็ได้) ทำงานเสมอไม่ว่าจะ Error หรือไม่ก็ตาม
    print("ทำงานเสร็จสิ้น")
```

## 4. Context Managers (with statement)
ใช้จัดการ Resource อัตโนมัติ เช่น การเปิด-ปิดไฟล์ ป้องกันปัญหาลืมปิดไฟล์ (Memory leak)

```python
# ไม่ต้องใช้ f.close() อีกต่อไป เพราะ 'with' จะจัดการปิดให้ทันทีที่ทำงานเสร็จ หรือแม้กระทั่งตอนเกิด Error
with open("server_config.txt", "r") as f:
    content = f.read()
    print(content)
```
