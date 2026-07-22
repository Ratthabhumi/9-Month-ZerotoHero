import argparse
from crypto_utils import generate_key, encrypt_password, decrypt_password

# ไฟล์ที่เราจะเก็บรหัสผ่านที่ถูกเข้ารหัสแล้ว (แบบเบสิค)
DATABASE_FILE = "passwords_db.txt"

def save_password(site, password):
    """เข้ารหัสและบันทึกรหัสผ่านลงไฟล์ Text"""
    encrypted_pw = encrypt_password(password)
    with open(DATABASE_FILE, "a") as f:
        f.write(f"{site}|{encrypted_pw.decode()}\n")
    print(f"✅ บันทึกรหัสผ่านของ '{site}' เรียบร้อยแล้ว!")

def get_password(site):
    """ค้นหาและถอดรหัสรหัสผ่านจากไฟล์ Text"""
    try:
        with open(DATABASE_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2 and parts[0] == site:
                    encrypted_pw = parts[1].encode()
                    decrypted_pw = decrypt_password(encrypted_pw)
                    print(f"🔓 รหัสผ่านสำหรับ '{site}' คือ: {decrypted_pw}")
                    return
        print(f"❌ ไม่พบรหัสผ่านสำหรับเว็บไซต์ '{site}'")
    except FileNotFoundError:
        print("❌ ไม่พบฐานข้อมูลรหัสผ่าน (passwords_db.txt) คุณอาจจะยังไม่เคยบันทึกอะไรเลย")

def delete_password(site):
    try:
        with open(DATABASE_FILE, "r") as f:
            lines = f.readlines()
        with open(DATABASE_FILE, "w") as f:
            for line in lines:
                parts = line.strip().split("|")
                if len(parts) == 2 and parts[0] != site:
                    f.write(line)
            print(f"✅ ลบรหัสผ่านของ '{site}' เรียบร้อยแล้ว!")
    except FileNotFoundError:
        print("❌ ไม่พบฐานข้อมูลรหัสผ่าน")   

def list_sites():
    sites = []
    try:
        with open(DATABASE_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    sites.append(parts[0])
        if sites:
            print("รายชื่อเว็บไซต์ทั้งหมด:")
            for site in sites:
                print(f"- {site}")
        else:
            print("ยังไม่มีข้อมูลรหัสผ่านในระบบ")
    except FileNotFoundError:
        print("❌ ไม่พบฐานข้อมูลรหัสผ่าน")  

def main():
    # ตรวจสอบก่อนว่าเรามีกุญแจเข้ารหัสหรือยัง ถ้ายังให้สร้างขึ้นมา
    generate_key()
    
    # สร้างตัวจัดการ Argument แบบมืออาชีพ
    parser = argparse.ArgumentParser(
        description="🔐 Password Manager CLI Tool",
        epilog="ตัวอย่างการใช้งาน: python main.py add facebook 123456"
    )
    
    # กำหนด Subcommands (เช่น add, get)
    subparsers = parser.add_subparsers(dest="command", help="คำสั่งที่ต้องการทำ")
    
    # คำสั่ง 'add'
    parser_add = subparsers.add_parser("add", help="เพิ่มรหัสผ่านใหม่")
    parser_add.add_argument("site", help="ชื่อเว็บไซต์หรือบริการ")
    parser_add.add_argument("password", help="รหัสผ่านที่ต้องการบันทึก")
    
    # คำสั่ง 'get'
    parser_get = subparsers.add_parser("get", help="ดูรหัสผ่าน")
    parser_get.add_argument("site", help="ชื่อเว็บไซต์หรือบริการที่ต้องการค้นหา")

     # คำสั่ง 'list'
    parser_list = subparsers.add_parser("list", help="ดูรายชื่อเว็บไซต์ทั้งหมด")

    # คำสั่ง 'delete' (ใหม่)
    parser_delete = subparsers.add_parser("delete", help="ลบรหัสผ่าน")
    parser_delete.add_argument("site", help="ชื่อเว็บไซต์ที่ต้องการลบ")
    
    # อ่านค่าคำสั่งที่ผู้ใช้พิมพ์มา
    args = parser.parse_args()
    
    # ประมวลผลตามคำสั่ง
    if args.command == "add":
        save_password(args.site, args.password)
    elif args.command == "get":
        get_password(args.site)
    elif args.command == "delete":
        delete_password(args.site)
    elif args.command == "list":
        list_sites()
    else:
        # ถ้าไม่พิมพ์คำสั่งย่อย ให้แสดง Help Menu
        parser.print_help()

if __name__ == "__main__":
    main()
