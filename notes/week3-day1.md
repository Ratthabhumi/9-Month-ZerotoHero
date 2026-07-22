# Week 3 Day 1: DNS & Domain Resolution

## 📝 หัวข้อที่เรียน
- ลำดับการทำงานของ DNS (Root, TLD, Authoritative Nameserver)
- DNS Records พื้นฐาน (A, CNAME, TXT, MX)
- Hands-on: `dig` และ `nslookup`
- ทำความเข้าใจเรื่อง TTL (Time to Live)

---

## 🛠️ แบบฝึกหัด (Hands-on)
> (เดี๋ยวเราจะมาจดคำสั่งและผลลัพธ์การทดลองที่นี่)
PS C:\Users\MewMew\Desktop\9_Month_ZerotoHero> nslookup google.com
Server:  UnKnown
Address:  fe80::f82a:e2ff:feac:7e64

Non-authoritative answer:
Name:    google.com
Addresses:  2404:6800:4016:80e::200e
          142.250.204.206

PS C:\Users\MewMew\Desktop\9_Month_ZerotoHero> nslookup -type=mx google.com
Server:  UnKnown
Address:  fe80::f82a:e2ff:feac:7e64

Non-authoritative answer:
google.com      MX preference = 10, mail exchanger = smtp.google.com
PS C:\Users\MewMew\Desktop\9_Month_ZerotoHero>
---

## 📝 สะท้อนความคิด (Self-Reflection)
1. **อธิบายการทำงานของ DNS ด้วยคำพูดของตัวเอง:**
   > [พิมพ์คำตอบที่นี่]
   > DNS คือ ตัวชี้แทน IP Address เพื่อให้เราสามารถจำชื่อเว็บไซต์ได้ง่ายๆ โดยไม่ต้องนั่งจำ Ip ยาวๆ ด้วยตัวเอง

2. **A Record ต่างจาก CNAME Record อย่างไร?**
   > [พิมพ์คำตอบที่นี่]
   > A Record คือ ตัวชี้โดยตรงว่า Dns นี้ ไปที่ Ip อะไร
   > CNAME Record คือ ตัวชี้ไปที่นามแฝงของ Dns นี้ว่า ไปที่ Dns อะไร (ไม่ใช่ Ip โดยตรง)

3. **ทำไมเวลาเปลี่ยน IP ของเว็บไซต์ มันถึงไม่เปลี่ยนให้คนทั้งโลกเห็นทันที? (อธิบายโดยใช้คำว่า TTL)**
   > [พิมพ์คำตอบที่นี่]
   > เพราะมันมีการตั้ง TTL ไว้ มันไม่เปลี่ยนจนกว่าเวลา Time To Live จะหมด
   > TTL มันคือ ระยะเวลาที่จะเก็บข้อมูลไว้ 