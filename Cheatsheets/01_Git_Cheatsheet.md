# Git Cheat Sheet - สำหรับ Beginners 📋

## 🔧 ตั้งค่าครั้งแรก
```bash
git config --global user.name "ชื่อเรา"
git config --global user.email "อีเมลเรา"
git config --list                    # ดูการตั้งค่าทั้งหมด
```

## 📁 เริ่มต้น Repository
```bash
git init                             # สร้าง repo ใหม่
git clone <URL>                      # clone repo จาก GitHub
```

## 📊 ดูสถานะ
```bash
git status                           # ดูสถานะไฟล์
git log                              # ดูประวัติ commit ทั้งหมด
git log --oneline                    # ดูแบบสั้น
git diff                             # ดูความเปลี่ยนแปลง
```

## ➕ เพิ่มไฟล์
```bash
git add ชื่อไฟล์                     # เพิ่มไฟล์เดียว
git add .                            # เพิ่มทุกไฟล์
git add *.js                         # เพิ่มไฟล์ .js ทั้งหมด
```

## 💾 Commit
```bash
git commit -m "ข้อความ"              # commit พร้อม message
git commit -am "ข้อความ"             # add + commit ในคำสั่งเดียว
```

## 🌐 GitHub (Remote)
```bash
git remote add origin <URL>          # เชื่อมต่อ GitHub
git push origin main                 # อัพโหลดขึ้น GitHub
git pull origin main                 # ดาวน์โหลดจาก GitHub
```

## 📝 Good Commit Message Format
```
feat: เพิ่มฟีเจอร์ใหม่
fix: แก้ไข bug
docs: อัพเดท documentation
style: แก้ format โค้ด
refactor: ปรับปรุงโค้ด
```

## ⚡ Workflow พื้นฐาน
```
1. แก้ไขไฟล์
2. git status    (ดูว่าเปลี่ยนอะไรบ้าง)
3. git add .     (เพิ่มไฟล์)
4. git commit    (บันทึก)
5. git push      (อัพ GitHub)
```

## 🌿 Branching & Merging (การแยกและรวมกิ่ง)
```bash
git branch                           # ดูรายชื่อกิ่งที่มีอยู่ (* คือกิ่งปัจจุบัน)
git checkout -b <ชื่อกิ่ง>            # สร้างกิ่งใหม่และสลับไปที่กิ่งนั้นทันที
git checkout <ชื่อกิ่ง>              # สลับไปใช้กิ่งที่มีอยู่แล้ว
git merge <ชื่อกิ่ง>                 # รวมโค้ดจากกิ่งอื่นเข้ามายังกิ่งปัจจุบัน
```

## 🛡️ File Recovery (การกู้คืนไฟล์)
```bash
git restore <ชื่อไฟล์>                # กู้คืนไฟล์เดียวที่เพิ่งลบหรือแก้ไข (ก่อน git add)
git restore .                        # กู้คืนไฟล์ทั้งหมดในโฟลเดอร์ปัจจุบันกลับมาสภาพเดิม
```

## 💥 Conflict Resolution (การแก้โค้ดชนกัน)
เมื่อรัน `git merge` แล้วเจอทางตันเพราะโค้ดทับบรรทัดกัน:
1. เปิดไฟล์ที่มีสัญลักษณ์ `<<<<<<< HEAD`, `=======`, `>>>>>>>`
2. เลือกว่าจะใช้โค้ดส่วนไหน หรือจะเขียนใหม่รวมกัน
3. ลบสัญลักษณ์ยึกยือออกให้หมดแล้วกด **Save**
4. รันกระบวนการเซฟปกติเพื่อปิดงาน:
   ```bash
   git add <ชื่อไฟล์>
   git commit -m "merge: resolve merge conflict"
   ```
   
