# 07_Networking_HTTP_Cheatsheet.md (Week 3)

## 🌐 HTTP (Hypertext Transfer Protocol)
ภาษามาตรฐานที่ Web Browser และ Web Server ใช้พูดคุยแลกเปลี่ยนข้อมูลกัน

---

## 🛠️ HTTP Methods (กริยาที่ใช้สั่งงาน)
เปรียบเทียบกับการสั่งอาหารในร้าน:
- **GET (ขอดู):** เหมือนขอดูเมนู (ใช้เพื่อดึงข้อมูลมาดูเฉยๆ ห้ามมีการอัปเดตข้อมูลบนเซิร์ฟเวอร์)
- **POST (สร้างใหม่):** เหมือนสั่งอาหารจานใหม่ (ส่งข้อมูลไปให้เซิร์ฟเวอร์สร้างของใหม่ เช่น สร้างโพสต์, สมัครสมาชิก)
- **PUT (แทนที่/แก้ไข):** เหมือนขอแก้หรือแทนที่ออเดอร์เดิม (ส่งข้อมูลไปเขียนทับของเก่า เช่น อัปเดตโปรไฟล์)
- **DELETE (ลบทิ้ง):** เหมือนขอยกเลิกออเดอร์ (ลบข้อมูลออกจากเซิร์ฟเวอร์)

---

## 🚦 HTTP Status Codes (รหัสตอบกลับ)
รหัสตัวเลข 3 หลักที่ฝั่งเซิร์ฟเวอร์ตอบกลับมา เพื่อบอกสถานะของคำสั่ง:

- **2xx (Success - สำเร็จ):**
  - `200 OK`: สำเร็จ ได้รับข้อมูลเรียบร้อย
  - `201 Created`: สร้างข้อมูลใหม่ (จากคำสั่ง POST) สำเร็จ
- **3xx (Redirect - ย้ายที่):**
  - `301 Moved Permanently`: ย้ายหน้าเว็บนี้ไปที่ URL ใหม่อย่างถาวร
  - `302 Found`: ย้ายชั่วคราว
- **4xx (Client Error - ความผิดฝั่งผู้ใช้/คนสั่ง):**
  - `400 Bad Request`: ส่งข้อมูลมาผิดรูปแบบ
  - `401 Unauthorized`: ยังไม่ได้ล็อกอิน (ไม่มีสิทธิ์เข้า)
  - `403 Forbidden`: ล็อกอินแล้ว แต่สิทธิ์ไม่ถึง (ห้ามเข้า)
  - `404 Not Found`: หาไฟล์/หน้าเว็บไม่เจอ (ส่วนใหญ่เพราะพิมพ์ URL ผิด)
- **5xx (Server Error - ความผิดฝั่งเซิร์ฟเวอร์/ร้านอาหาร):**
  - `500 Internal Server Error`: โค้ดฝั่งเซิร์ฟเวอร์พัง หรือฐานข้อมูลล่ม
  - `502 Bad Gateway`: เซิร์ฟเวอร์ต้นทาง (Upstream) พังหรือไม่ตอบสนอง
  - `504 Gateway Timeout`: เซิร์ฟเวอร์ต้นทางทำงานช้าเกินไปจนหมดเวลารอ

---

## ✉️ HTTP Headers (ข้อมูลจ่าหน้าซอง)
Metadata ที่แนบไปกับการส่งข้อมูลทุกครั้ง

**Request Headers (เราส่งไปหา Server):**
- `Host`: ระบุชื่อโดเมนที่เราต้องการเข้าถึง (เช่น `www.google.com`)
- `User-Agent`: ระบุประเภทอุปกรณ์ เบราว์เซอร์ หรือ OS ที่เราใช้ (เช่น Safari บน iPhone) เพื่อให้เซิร์ฟเวอร์ปรับหน้าตาเว็บให้เหมาะสม (Responsive)

**Response Headers (Server ตอบกลับมาหาเรา):**
- `Content-Type`: ชนิดของข้อมูลที่ส่งกลับมา (เช่น `text/html`, `application/json`, `image/png`)
- `Server`: โปรแกรม Web Server ที่ให้บริการอยู่ (เช่น `nginx`, `apache`, `gws`)

---

## 💻 การใช้ `curl` ตรวจสอบ HTTP
ในฐานะ DevOps เรามักใช้ `curl` ยิงไปทดสอบเซิร์ฟเวอร์ผ่าน Terminal โดยไม่ต้องเปิดเบราว์เซอร์

**ดูเฉพาะ Headers (ไม่เอาหน้าเว็บ):**
```bash
curl -I https://www.google.com
# หรือ curl.exe -I บน Windows PowerShell
```

**ดึงข้อมูลหน้าเว็บปกติ:**
```bash
curl https://www.google.com
```

---

## 🛠️ ตัวอย่างการยิง API ด้วย `curl` (GET, POST, PUT, DELETE)
ใช้เว็บ `jsonplaceholder.typicode.com` สำหรับทดสอบยิง API ได้ฟรีโดยไม่โดนบล็อก

**1. GET (ขอดูข้อมูล):**
```bash
curl.exe -X GET https://jsonplaceholder.typicode.com/posts/1
```

**2. POST (ส่งข้อมูลไปสร้างใหม่):**
ใช้ Flag `-d` (data) เพื่อแนบข้อมูลไปกับ Request
```bash
curl.exe -X POST https://jsonplaceholder.typicode.com/posts -d "title=MyNewPost" -d "body=HelloDevOps"
```

**3. PUT (ส่งข้อมูลไปแก้ของเดิม):**
ระบุ ID ของสิ่งที่จะแก้ใน URL (เช่น `/posts/1`)
```bash
curl.exe -X PUT https://jsonplaceholder.typicode.com/posts/1 -d "title=UpdatedTitle"
```

**4. DELETE (สั่งลบทิ้ง):**
```bash
curl.exe -X DELETE https://jsonplaceholder.typicode.com/posts/1
```
