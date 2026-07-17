import sys
from crypto_utils import generate_key, encrypt_password, decrypt_password

# ไฟล์ที่เราจะเก็บรหัสผ่านที่ถูกเข้ารหัสแล้ว (แบบเบสิค)
DATABASE_FILE = "passwords_db.txt"

def save_password(site, password):
    """เข้ารหัสและบันทึกรหัสผ่านลงไฟล์ Text"""
    encrypted_pw = encrypt_password(password)
    
    # เปิดไฟล์โหมด 'a' (Append) เพื่อต่อท้ายข้อมูลเดิม
    with open(DATABASE_FILE, "a") as f:
        # บันทึกในรูปแบบ เว็บไซต์|รหัสผ่านที่เข้ารหัสแล้ว
        f.write(f"{site}|{encrypted_pw.decode()}\n")
    print(f"✅ บันทึกรหัสผ่านของ '{site}' เรียบร้อยแล้ว!")

def get_password(site):
    """ค้นหาและถอดรหัสรหัสผ่านจากไฟล์ Text"""
    try:
        with open(DATABASE_FILE, "r") as f:
            for line in f:
                # แยกข้อมูลด้วยตัว |
                parts = line.strip().split("|")
                if len(parts) == 2 and parts[0] == site:
                    # ถอดรหัส
                    encrypted_pw = parts[1].encode()
                    decrypted_pw = decrypt_password(encrypted_pw)
                    print(f"🔓 รหัสผ่านสำหรับ '{site}' คือ: {decrypted_pw}")
                    return
        
        print(f"❌ ไม่พบรหัสผ่านสำหรับเว็บไซต์ '{site}'")
    except FileNotFoundError:
        print("❌ ไม่พบฐานข้อมูลรหัสผ่าน (passwords_db.txt) คุณอาจจะยังไม่เคยบันทึกอะไรเลย")

def main():
    # ตรวจสอบก่อนว่าเรามีกุญแจเข้ารหัสหรือยัง ถ้ายังให้สร้างขึ้นมา
    generate_key()
    
    while True:
        print("\n--- 🔐 Password Manager ---")
        print("1. บันทึกรหัสผ่านใหม่ (Add)")
        print("2. ดูรหัสผ่าน (View)")
        print("3. ออกจากโปรแกรม (Exit)")
        
        choice = input("เลือกเมนู (1/2/3): ")
        
        if choice == "1":
            site = input("ชื่อเว็บไซต์/บริการ (เช่น facebook, gmail): ")
            password = input("รหัสผ่าน: ")
            save_password(site, password)
        
        elif choice == "2":
            site = input("ชื่อเว็บไซต์ที่ต้องการค้นหา: ")
            get_password(site)
            
        elif choice == "3":
            print("ลาก่อน! 👋")
            sys.exit(0)
            
        else:
            print("⚠️ กรุณาเลือก 1, 2, หรือ 3 เท่านั้น")

if __name__ == "__main__":
    main()
