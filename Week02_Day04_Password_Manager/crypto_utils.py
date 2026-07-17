import os
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def generate_key():
    """สร้างกุญแจ (Key) สำหรับเข้ารหัสและถอดรหัส ถ้ายังไม่มีกุญแจ"""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        print("✅ สร้างกุญแจใหม่สำเร็จ (secret.key)")
    else:
        print("ℹ️ พบกุญแจในระบบแล้ว (secret.key)")

def load_key():
    """โหลดกุญแจจากไฟล์เพื่อเอาไปใช้งาน"""
    return open(KEY_FILE, "rb").read()

def encrypt_password(password):
    """เข้ารหัส (Encrypt) ข้อความธรรมดา ให้เป็นข้อความที่อ่านไม่ออก"""
    key = load_key()
    f = Fernet(key)
    # Fernet รับและคืนค่าเป็น bytes ดังนั้นต้องเข้ารหัสสตริง (encode) ก่อน
    encrypted_data = f.encrypt(password.encode())
    return encrypted_data

def decrypt_password(encrypted_password):
    """ถอดรหัส (Decrypt) ข้อความที่อ่านไม่ออก ให้กลับมาเป็นข้อความธรรมดา"""
    key = load_key()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_password)
    # ผลลัพธ์เป็น bytes จึงต้องถอดรหัสกลับเป็น string (decode)
    return decrypted_data.decode()

if __name__ == "__main__":
    # ทดสอบระบบถ้ารันไฟล์นี้โดยตรง
    print("--- ทดสอบระบบเข้ารหัส ---")
    generate_key()
    test_pass = "my_super_secret_password_123!"
    
    enc = encrypt_password(test_pass)
    print(f"\n🔒 ข้อความที่ถูกเข้ารหัสแล้ว: \n{enc}")
    
    dec = decrypt_password(enc)
    print(f"\n🔓 ข้อความที่ถูกถอดรหัส: \n{dec}")
    
    if test_pass == dec:
        print("\n✅ การเข้ารหัสและถอดรหัสทำงานถูกต้องสมบูรณ์!")
    else:
        print("\n❌ มีข้อผิดพลาดเกิดขึ้น")
