# สมมติว่าเป็นสคริปต์อ่านไฟล์ตั้งค่าของระบบ (Config)

def read_config(filename):
    print(f"กำลังพยายามเปิดไฟล์ {filename}...")
    
    # 1. ใช้ try เพื่อบอกให้ Python ลองรันโค้ดชุดนี้ดูก่อน
    try:
        # 2. ใช้ with (Context Manager) มันจะคอยจัดการปิดไฟล์ (f.close) ให้อัตโนมัติเสมอ!
        with open(filename, "r") as f:
            content = f.read()
            print("อ่านไฟล์สำเร็จ:", content)
            
    # 3. ใช้ except เพื่อดักจับ Error สีแดงๆ เมื่อกี้ ไม่ให้โปรแกรมพัง
    except FileNotFoundError:
        print(f"⚠️ การแจ้งเตือน: ไม่พบไฟล์ {filename} โปรแกรมจะข้ามขั้นตอนนี้ไปทำงานอื่นต่อ")


# --- ทดสอบการทำงาน ---
print("--- Test 1 ---")
read_config("server_config.txt")  # ไฟล์นี้ไม่มีอยู่จริง
