# ภารกิจฝึกซ้อม Linux Command Line 🐧

ในฐานะ Junior DevOps วันนี้คุณได้รับมอบหมายให้ตรวจสอบไฟล์ Log ของเซิร์ฟเวอร์
เราจะใช้คำสั่ง Linux ที่ได้เรียนรู้มาเพื่อแก้ปัญหาต่างๆ

**ข้อแนะนำ:** เนื่องจากคุณใช้ Windows (PowerShell) บางคำสั่งของ Linux อาจจะไม่ทำงานบน PowerShell ปกติ
วิธีที่ดีที่สุดคือการเปิด **Git Bash** (คลิกขวาที่โฟลเดอร์นี้ แล้วเลือก "Git Bash Here" หรือกดสลับ Terminal ใน VS Code ให้เป็น Git Bash)

---

## 🎯 Task 1: ตรวจสอบที่อยู่ปัจจุบัน (Where am I?)
ลองพิมพ์คำสั่งเพื่อดูว่าตอนนี้คุณอยู่โฟลเดอร์ไหน
```bash
pwd

MewMew@Mew MINGW64 ~/Desktop/9_Month_ZerotoHero (main)
$ cd Week02_Day03_Linux_Fundamentals

MewMew@Mew MINGW64 ~/Desktop/9_Month_ZerotoHero/Week02_Day03_Linux_Fundamentals (main)
$ pwd
/c/Users/MewMew/Desktop/9_Month_ZerotoHero/Week02_Day03_Linux_Fundamentals
```

## 🎯 Task 2: ส่องดูไฟล์ในโฟลเดอร์ (Look around)
พิมพ์คำสั่งเพื่อดูว่าในโฟลเดอร์ปัจจุบันนี้ มีไฟล์อะไรซ่อนอยู่บ้าง
```bash
ls -a

MewMew@Mew MINGW64 ~/Desktop/9_Month_ZerotoHero/Week02_Day03_Linux_Fundamentals (main)
$ ls -a
./  ../  exercise_guide.md  log_analyzer.sh*  sample_server.log
```

## 🎯 Task 3: ดูข้อมูลไฟล์แบบไวๆ (Peek into a file)
มีไฟล์ชื่อ `sample_server.log` อยู่ ลองพิมพ์คำสั่งเพื่อดูเนื้อหาทั้งหมดในไฟล์นี้
```bash
cat sample_server.log
MewMew@Mew MINGW64 ~/Desktop/9_Month_ZerotoHero/Week02_Day03_Linux_Fundamentals (main)
$ cat sample_server.log
[2026-07-15 08:00:01] INFO  Server started successfully.
[2026-07-15 08:05:12] INFO  User 'mew' logged in.
[2026-07-15 08:10:23] WARN  High memory usage detected (85%).
[2026-07-15 08:15:34] INFO  Database connection established.
[2026-07-15 08:20:45] ERROR Connection timeout to database 'production-db'.
[2026-07-15 08:22:12] ERROR Failed to write to disk. Disk full.
[2026-07-15 08:25:10] INFO  User 'mew' logged out.
```

## 🎯 Task 4: กรองเฉพาะ Error (The Magic of Pipe `|` and `grep`)
เซิร์ฟเวอร์พัง! รุ่นพี่บอกให้คุณกรองดูเฉพาะบรรทัดที่มีคำว่า `ERROR` จากไฟล์ `sample_server.log`
ให้ใช้คำสั่ง `cat` รวมร่างกับ `grep` (ใช้เครื่องหมาย `|` คั่นกลาง)
```bash
cat sample_server.log | grep "ERROR"
```
MewMew@Mew MINGW64 ~/Desktop/9_Month_ZerotoHero/Week02_Day03_Linux_Fundamentals (main)
$ cat sample_server.log | grep "ERROR"
[2026-07-15 08:20:45] ERROR Connection timeout to database 'production-db'.
[2026-07-15 08:22:12] ERROR Failed to write to disk. Disk full.


---
ทำภารกิจด้านบนเสร็จแล้ว ลองพิมพ์ตอบผมกลับมานะครับว่า "รันคำสั่ง Task 4 แล้วเจอ Error กี่บรรทัด และเป็น Error อะไรบ้าง?" 🚀

2 บรรทัด ERROR Connection 
1.timeout to database 'production-db'  (Time out ตอน connect Db)
2.Failed to write to disk. Disk full. (Disk เต็ม)
$ cat sample_server.log | grep "ERROR"
[2026-07-15 08:20:45] ERROR Connection timeout to database 'production-db'.
[2026-07-15 08:22:12] ERROR Failed to write to disk. Disk full.
