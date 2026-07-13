import dataclasses
class Server:
    # 1. Constructor (ตอนสร้างวัตถุ จะให้กำหนดค่าเริ่มต้นอะไรบ้าง)
    def __init__(self, name, ip, status="stopped"):
        self.name = name
        self.ip = ip
        self.status = status

    # 2. Method (ความสามารถของ Server นี้)
    def start(self):
        if self.status == "running":
            print(f"[{self.name}] is already running at {self.ip}.")
        else:
            print(f"[{self.name}] Starting server at {self.ip}...")
            self.status = "running"
    def stop(self):
        if self.status == "stopped":
            print(f"[{self.name}] is already stopped.")
        else:
            print(f"[{self.name}] Stopping server at {self.ip}...")
            self.status = "stopped"

# สร้างคลาส DatabaseServer ที่สืบทอดความสามารถมาจาก Server
class DatabaseServer(Server):
    def __init__(self, name, ip, cores, status="stopped"):
        # 1. ให้คลาสแม่ (Server) ช่วยตั้งค่า name, ip, status ให้
        super().__init__(name, ip, status)
        # 2. ตั้งค่าเฉพาะตัวของคลาสลูก
        self.cores = cores

    # ฟังก์ชันเฉพาะตัวที่มีแค่ใน DatabaseServer
    def backup(self):
        print(f"[{self.name}] Backing up database using {self.cores} cores...")

# สร้างคลาส WebServer
class WebServer(Server):
    # ถ้าไม่ได้ตั้งค่าอะไรพิเศษ ไม่ต้องเขียน __init__ ก็ได้ มันจะใช้ของแม่โดยอัตโนมัติ

    # เขียนทับ (Override) ฟังก์ชัน stop()
    def stop(self):
        print(f"[{self.name}] Clearing cache before stopping...")
        # เรียกฟังก์ชัน stop() ของคลาสแม่มาทำงานต่อ (เพื่อเปลี่ยน status เป็น stopped)
        super().stop()


# --- ทดสอบคลาสลูก ---
db1 = DatabaseServer("MySQL-Prod", "10.0.0.5", cores=8, status="running")

# ลองเรียกใช้ความสามารถของคลาสแม่
db1.stop()

# ลองเรียกใช้ความสามารถของตัวเอง
db1.backup()

# --- ทดสอบ Polymorphism ---
web1 = WebServer("Nginx-Proxy", "10.0.0.9", status="running")

# ลองสั่งปิด WebServer ดู
web1.stop()



