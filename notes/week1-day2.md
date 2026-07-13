# Week 1 Day 2 — Branching & Merge Conflicts

**Date:** 2026-07-11
**Theme:** Git Branching and Merge Conflicts Resolution

---

## ✅ What I Completed Today

1. **Git Branching:**
   - การแยก Branch ช่วยให้สามารถพัฒนา Feature ใหม่ๆ หรือแก้ Bug ได้โดยไม่กระทบกับโค้ดหลัก (`master`/`main`)
   - คำสั่ง: `git branch <name>`, `git checkout <name>` หรือ `git switch <name>`
2. **Merging:**
   - รวมโค้ดจาก Branch อื่นเข้าสู่ Branch ปัจจุบัน
   - คำสั่ง: `git merge <branch-name>`
3. **Merge Conflict Resolution:**
   - เกิดขึ้นเมื่อมีการแก้ไขไฟล์เดียวกัน บรรทัดเดียวกัน ใน 2 Branch
   - **วิธีแก้:**
     1. เปิดไฟล์ที่มีปัญหาใน VS Code (จะเห็นแถบ Current Change / Incoming Change)
     2. เลือกว่าจะเก็บโค้ดส่วนไหนไว้ (Accept Current / Accept Incoming / Accept Both)
     3. Save ไฟล์
     4. `git add <file>` และ `git commit` เพื่อเสร็จสิ้นการรวมโค้ด

## 💡 Key Takeaway
การแก้ Conflict ไม่ใช่เรื่องน่ากลัว แค่ต้องตั้งสติและอ่านโค้ดว่าเวอร์ชันไหนคือสิ่งที่เราต้องการจริงๆ สิ่งสำคัญคือก่อนทำฟีเจอร์ใหม่ ให้แตก Branch เสมอ อย่าเขียนโค้ดลง Branch หลักโดยตรง!
