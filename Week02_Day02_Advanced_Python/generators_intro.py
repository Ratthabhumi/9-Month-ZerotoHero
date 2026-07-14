import time
import sys

# สมมติว่านี่คือฟังก์ชันดึงข้อมูล Log ทีเดียว 10 ล้านบรรทัด (ใช้ Memory มหาศาล)
def get_all_logs_normal():
    print("Loading ALL logs into memory...")
    # สร้าง List เก็บตัวเลข 1 ถึง 5 ล้าน
    logs = [f"Log line {i}" for i in range(1, 5000001)] 
    return logs

# สมมติว่านี่คือ Generator (ทะยอยส่งข้อมูลมาทีละบรรทัด ไม่เปลือง Memory)
def get_logs_generator():
    print("Yielding logs one by one...")
    for i in range(1, 5000001):
        yield f"Log line {i}"

# --- ทดสอบการกิน Memory ---
print("--- 1. Normal Function (List) ---")
normal_logs = get_all_logs_normal()
print(f"Memory used by Normal List: {sys.getsizeof(normal_logs) / 1024 / 1024:.2f} MB")

print("\n--- 2. Generator ---")
gen_logs = get_logs_generator()
print(f"Memory used by Generator: {sys.getsizeof(gen_logs) / 1024 / 1024:.6f} MB")

# ลองดึงข้อมูลจาก Generator ทีละบรรทัด
print("\nFetching first 3 lines from Generator:")
print(next(gen_logs))
print(next(gen_logs))
print(next(gen_logs))
