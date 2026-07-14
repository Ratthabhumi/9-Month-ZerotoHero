import time

# ตัวแปรจำลองสถานะของ User ปัจจุบัน
current_user = "admin"  # ลองเปลี่ยนเป็น "admin" ดูทีหลัง
# 1. สร้าง Decorator ชื่อ require_admin
def require_admin(func):
    # ฟังก์ชันห่อหุ้ม (Wrapper) ที่จะเข้าไปแทรกแซงการทำงาน
    def wrapper(*args, **kwargs):
        if current_user != "admin":
            print(f"❌ Access Denied! 'guest' cannot run {func.__name__}()")
            return  # เด้งออกเลย ไม่ให้รันต่อ
        
        # ถ้าเป็น admin ให้รันฟังก์ชันเดิมต่อได้
        return func(*args, **kwargs)
    return wrapper

@require_admin
def restart_server(ip):
    print(f"Connecting to {ip}...")
    time.sleep(1)
    print(f"Server {ip} has been restarted successfully!")

@require_admin
def delete_database(db_name):
    print(f"Connecting to database {db_name}...")
    time.sleep(1)
    print(f"Database {db_name} has been deleted permanently!")


# --- ทดสอบการทำงาน ---
print("--- Action 1 ---")
restart_server("192.168.1.10")

print("\n--- Action 2 ---")
delete_database("production-db")
