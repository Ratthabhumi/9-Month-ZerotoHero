# 🐍 Python Cheatsheet (Week 2)

## Day 1: Object-Oriented Programming (OOP)

### 1. Class & Object
- **Class (แบบแปลน):** ต้นแบบสำหรับสร้างวัตถุ กำหนดว่าต้องมีข้อมูลอะไรและทำอะไรได้บ้าง
- **Object (วัตถุ):** สิ่งที่ถูกสร้างขึ้นมาจาก Class แต่ละ Object จะมีข้อมูล (State) เป็นของตัวเองแยกจากกัน

```python
class Server:
    # Constructor: กำหนดค่าเริ่มต้นเมื่อสร้าง Object
    def __init__(self, name, ip, status="stopped"):
        self.name = name
        self.ip = ip
        self.status = status

    # Method: ความสามารถ
    def start(self):
        self.status = "running"
        print(f"[{self.name}] Started.")

# การสร้าง Object
web = Server("Web1", "10.0.0.1")
db = Server("DB1", "10.0.0.2")
```

### 2. Inheritance (การสืบทอด)
- ช่วยลดการเขียนโค้ดซ้ำซ้อน
- คลาสลูก (Child) จะได้รับคุณสมบัติและความสามารถทั้งหมดจากคลาสแม่ (Parent)
- สามารถเพิ่มคุณสมบัติหรือความสามารถเฉพาะตัวให้คลาสลูกได้

```python
# DatabaseServer สืบทอดมาจาก Server
class DatabaseServer(Server):
    def __init__(self, name, ip, cores):
        # เรียก Constructor ของคลาสแม่
        super().__init__(name, ip)
        self.cores = cores # เพิ่มคุณสมบัติใหม่

    def backup(self):
        print("Backing up...")
```

### 3. Polymorphism (การเขียนทับ/Override)
- คลาสลูกสามารถ **ดัดแปลง (Override)** ฟังก์ชันที่มีอยู่แล้วในคลาสแม่ ให้ทำงานแตกต่างออกไป
- ใช้ `super()` หากต้องการเรียกใช้การทำงานดั้งเดิมของคลาสแม่ร่วมด้วย

```python
class WebServer(Server):
    # Override ฟังก์ชัน start() ของคลาสแม่
    def start(self):
        print("Clearing cache...")
        super().start() # เรียกฟังก์ชัน start() ของแม่ให้ทำงานต่อ
```

---

## Day 2: Advanced Python Features

### 4. Decorators (ตัวตกแต่งฟังก์ชัน)
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

### 5. Generators & Yield (เครื่องผลิตข้อมูลประหยัดแรม)
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

### 6. Error Handling (try...except)
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

### 7. Context Managers (with statement)
ใช้จัดการ Resource อัตโนมัติ เช่น การเปิด-ปิดไฟล์ ป้องกันปัญหาลืมปิดไฟล์ (Memory leak)

```python
# ไม่ต้องใช้ f.close() อีกต่อไป เพราะ 'with' จะจัดการปิดให้ทันทีที่ทำงานเสร็จ หรือแม้กระทั่งตอนเกิด Error
with open("server_config.txt", "r") as f:
    content = f.read()
    print(content)
```
