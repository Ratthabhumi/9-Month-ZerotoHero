# Week 2 Day 2 — Python Advanced (Decorators & Generators)

**Date:** 2026-07-14
**Theme:** Python Advanced features for DevOps

---

## ✅ What I Learned Today

1. **Decorators คืออะไร?**
   > [พิมพ์คำตอบของคุณตรงนี้: มันเอาไว้ทำอะไร? มีประโยชน์ยังไงเวลาเรามีฟังก์ชันที่ต้องเช็คสิทธิ์การเข้าถึงหลายๆ ฟังก์ชัน?]
   > คือ ถ้าเราสร้าง Function แล้วจะเอาไปใช้ @require_admin มันจะเข้าไปแทรกแซงการทำงานของ Function นั้นๆ ทีนี้ไปแปะ @require_admin ก่อน Function อื่นก็จะเช็คสิทได้ว่าสิทที่เรากำหนดไว้มีสิทไหม จะมีwrapper function ที่คอยแทรกแซงการทำงาน

2. **Generators (yield) ต่างจากฟังก์ชันปกติ (return) ยังไง?**
   > [พิมพ์คำตอบของคุณตรงนี้: อธิบายเรื่องความแตกต่างของการใช้ Memory (RAM) ระหว่าง yield กับ return]
   > Return เนี่ยอ่านไฟล์ทั้งหมดเลย แล้ว รวมมาตอบทีเดียว
   > Yield เนี่ย อ่านแล้วทิ้ง ถ้าไม่เจอก็ Next() ต่อไปจนเจอก็จบเลย ประหยัด Ram กว่าเยอะเลย
   

3. **Error Handling & Context Managers คืออะไร?**
   > [พิมพ์คำตอบของคุณตรงนี้: try...except ช่วยแก้อะไร? และการใช้ 'with open(...)' ดีกว่าการเปิดไฟล์แบบธรรมดายังไง?]
   > Try เนี่ยให้ลอง Function ที่เขียนไว้ก่อน
   > Except เนี่ยสมมุติ Try แล้วไม่มีก็มาเข้า Except
   > with open('') เนี่ยมันช่วย ปิดให้ Auto เลย ไม่ต้องใส่ f.close() ซ้ำๆ
