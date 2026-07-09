# Day 01 - Git Setup & Fundamentals 🌱

**Date:** 2026-07-09  
**Time Spent:** ~2 hours  
**Status:** ✅ Completed

---

## 📖 สิ่งที่เรียนรู้วันนี้

### 1. Git คืออะไร?
Git คือ Version Control System ที่ช่วยให้เราติดตาม
การเปลี่ยนแปลงของโค้ดได้ เหมือนกับ "checkpoint" ในเกม

### 2. คำสั่ง Git พื้นฐาน

```bash
# ตรวจสอบเวอร์ชัน Git
git --version

# ตั้งค่าชื่อและอีเมล (ทำครั้งแรกครั้งเดียว)
git config --global user.name "ชื่อของเรา"
git config --global user.email "อีเมลของเรา"

# สร้าง Repository ใหม่
git init

# ดูสถานะของไฟล์
git status

# เพิ่มไฟล์เข้า Staging Area
git add ชื่อไฟล์
git add .   # เพิ่มทุกไฟล์

# บันทึก Commit
git commit -m "ข้อความ commit"

# ดูประวัติ Commit
git log
git log --oneline  # แบบสั้น
```

### 3. Git Workflow

```
Working Directory → Staging Area → Repository
    (แก้ไขไฟล์)    (git add)     (git commit)
```

---

## 🎯 โจทย์วันนี้ (แก้ด้วยตัวเอง!)

ดู `exercises/` folder สำหรับโจทย์ฝึกหัด

---

## 💭 สิ่งที่ยังสงสัย / ต้องเรียนเพิ่ม

- [ ] Staging Area ทำงานยังไงกันแน่?
- [ ] ทำไมต้อง `git add` ก่อน `git commit`?

---

## 📝 Note ส่วนตัว

> *เขียน Note ของตัวเองที่นี่ หลังจากทำโจทย์เสร็จแล้ว*
