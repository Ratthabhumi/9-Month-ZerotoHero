# Week 3 Day 2: HTTP Status Codes & Web Protocol Basics

## 📝 หัวข้อที่เรียน
- HTTP Methods (GET, POST, PUT, DELETE)
- HTTP Status Codes เบื้องต้น (200, 301, 404, 500)
- HTTP Headers ที่สำคัญ (Host, User-Agent, Content-Type)
- Hands-on: การใช้คำสั่ง `curl` เรียกดู Response Headers

---

## 🛠️ แบบฝึกหัด (Hands-on)
> (เดี๋ยวเราจะมาจดคำสั่ง curl และผลลัพธ์การทดลองที่นี่)
PS C:\Users\MewMew\Desktop\9_Month_ZerotoHero> curl.exe -I https://www.google.com
HTTP/1.1 200 OK
Content-Type: text/html; charset=ISO-8859-1
Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-OswgOcJeE81G29d7Pf5iOQ' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
Accept-CH: Sec-CH-Prefers-Color-Scheme
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Date: Tue, 21 Jul 2026 16:14:51 GMT
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Expires: Tue, 21 Jul 2026 16:14:51 GMT
Cache-Control: private
Set-Cookie: __Secure-STRP=ANmZwa2j-B5lGAyQm9fNf2Eqev9AKpWZqlVEKET4z2wqsssunL9zdo82MZdJSshho7tVwD6uZNJTMda2g7bKrM3ND31VIqlISPn8; expires=Tue, 21-Jul-2026 16:19:51 GMT; path=/; domain=.google.com; Secure; SameSite=strict
Set-Cookie: AEC=AdJVEauSjhH1mhUcjjcrihl8ActJniwH3p6yZmNeJJwvc8hJCpuw_wVkvr0; expires=Sun, 17-Jan-2027 16:14:51 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax
Set-Cookie: NID=533=BZP5gFQOsLyRKLCy7Qs4cZH-PBppzMZhGg6WZRVSybaONxepsKWnryPC9AnYTw9kmK1_Hs3kuF8lj0y7AAmlvCY4NgG4rwPzZHdEuT3VBlYgPzVQlc4JAA0uIlnXJ4wkhAAinN1F1MC5fg-idpjbSCbytEbPGE5vdZdlMy-pl_agqVw6yJ1Z1lJt4NUfGZoSBw_8fs9v8DoU93-KP6I; expires=Wed, 20-Jan-2027 16:14:51 GMT; path=/; domain=.google.com; HttpOnly
Transfer-Encoding: chunked
Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

---

## 📝 สะท้อนความคิด (Self-Reflection)
1. **ลองเปรียบเทียบ HTTP Methods ทั้ง 4 ตัว (GET, POST, PUT, DELETE) กับการกระทำในชีวิตประจำวัน:**
   > [พิมพ์คำตอบที่นี่]
   > Get คือ เหมือนขอเมนูว่ามีอะไรบ้าง
   > Post คือ เหมือนสั่งอาหาร สั่งทีละอย่าง สั่งอย่างอื่นเพิ่มต้องสั่งใหม่
   > Put คือ เหมือนสั่งอาหารเพิ่ม หรือแก้ไขออเดอร์เดิมได้
   > Delete คือ เหมือนเอาอาหารออกหรือยกเลิกออเดอร์อาหาร

2. **ถ้ายิงคำสั่งไปแล้วได้ Status Code นำหน้าด้วยเลข 4 (เช่น 404) กับเลข 5 (เช่น 500) ความผิดพลาดนี้ต่างกันอย่างไร ใครเป็นคนผิด?**
   > [พิมพ์คำตอบที่นี่]
   > 404 Client Error: ฝั่งผู้ใช้ส่งคำขอผิด เช่น พิมพ์ URL มั่ว หรือหาหน้าเว็บไม่เจอ (ฝั่งคนสั่งผิด)
   > 500 Server Error: ฝั่งเซิร์ฟเวอร์เจอปัญหาภายใน เช่น โค้ดผิด หรือฐานข้อมูลล่ม (ฝั่งร้านเจ๊งเอง)

3. **HTTP Header 'User-Agent' มีประโยชน์อย่างไร ทำไมเซิร์ฟเวอร์ถึงอยากรู้ว่าเราใช้อะไรเข้าเว็บ?**
   > [พิมพ์คำตอบที่นี่]
   > User-Agent บอกว่าเราใช้เครื่องอะไร เบราว์เซอร์อะไร เช่น Brave ใน Computer Server ก็ส่งเว็ปแบบ PC, ใช้ iPhone Safari เซิร์ฟเวอร์จะได้ส่งหน้าเว็บแบบ Mobile กลับมาให้
