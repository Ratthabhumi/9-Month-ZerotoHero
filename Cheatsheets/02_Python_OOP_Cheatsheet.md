# 🐍 Python OOP Cheatsheet (Week 2 Day 1)

## 1. Class & Object
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

## 2. Inheritance (การสืบทอด)
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

## 3. Polymorphism (การเขียนทับ/Override)
- คลาสลูกสามารถ **ดัดแปลง (Override)** ฟังก์ชันที่มีอยู่แล้วในคลาสแม่ ให้ทำงานแตกต่างออกไป
- ใช้ `super()` หากต้องการเรียกใช้การทำงานดั้งเดิมของคลาสแม่ร่วมด้วย

```python
class WebServer(Server):
    # Override ฟังก์ชัน start() ของคลาสแม่
    def start(self):
        print("Clearing cache...")
        super().start() # เรียกฟังก์ชัน start() ของแม่ให้ทำงานต่อ
```
