# โจทย์ Day 1 - Git Fundamentals 🎯

> ⚠️ **กฎ**: ห้าม Copy! ให้พิมพ์เองและเข้าใจก่อน

---

## Exercise 1: รู้จัก Git ก่อน (10 นาที)

### คำถาม: ตอบก่อนเริ่ม (ตอบในใจได้)
1. Git คืออะไร? (ตอบด้วยคำพูดตัวเอง 1 ประโยค)
- Git คือโปรแกรม ที่เชื่อมกับ Github ไว้อัพโหลด Code ขึ้นไป
2. GitHub ต่างจาก Git ยังไง?
- Gihub คือ เว็ป ส่วน Git คือโปรแกรมที่ลงในเครื่อง
3. ทำไมต้องใช้ Version Control?
- เพื่อไม่ให้สับสนไง

---

## Exercise 2: ตั้งค่า Git ครั้งแรก (5 นาที)

พิมพ์คำสั่งนี้ใน Terminal ด้วยตัวเอง:

```bash
# ดูการตั้งค่าปัจจุบัน
git config --list

# ถ้ายังไม่มี ให้ตั้งค่าชื่อและอีเมล
git config --global user.name "YOUR_NAME_HERE"
git config --global user.email "YOUR_EMAIL_HERE"
```

**✅ Checkpoint:** รัน `git config user.name` แล้วเห็นชื่อตัวเองไหม?
เห็นดิ

---

## Exercise 3: สร้าง Repository แรก (15 นาที)

**โจทย์:** สร้างโฟลเดอร์ `my-first-repo` และ init git

```bash
# สร้างโฟลเดอร์และเข้าไป
mkdir my-first-repo
cd my-first-repo

# เริ่มต้น Git Repository
git init

# ดูว่าเกิดอะไรขึ้น
ls -la
PS C:\Users\MewMew\Desktop\9_Month_ZerotoHero\my-first-repo> ls -la
Get-ChildItem : A parameter cannot be found that matches parameter name 'la'.
At line:1 char:4
+ ls -la
+    ~~~
    + CategoryInfo          : InvalidArgument: (:) [Get-ChildItem], ParameterBindingException
    + FullyQualifiedErrorId : NamedParameterNotFound,Microsoft.PowerShell.Commands.GetChildItemComman
```

**คำถาม:** เห็น folder `.git` ไหม? มันคืออะไร?  
**เขียนคำตอบตรงนี้:** เห็นละ มันเหมือนสมอง , Database ของ git , Object คือโกดัง git commit จะบีบไปเก็บในนั้น 2.refs/ ป้ายบอกทางว่าเราอยู่ไหน 3.HEAD ไฟล์หน้าเดียวบอกว่าอยู่ยืนไหน 4. config เก็บตั้งค่าว่าเช่นโปรเจคนี้จะอัพไป URL ไหน

---

## Exercise 4: Commit ครั้งแรก (20 นาที)

**โจทย์:** สร้างไฟล์และทำ Commit แรก

```bash
# สร้างไฟล์ (พิมพ์เองในไฟล์ ห้าม copy)
# ใน VS Code สร้างไฟล์ hello.txt แล้วพิมพ์:
# "สวัสดี! นี่คือไฟล์แรกของผม"

# ดูสถานะ
git status

# เพิ่มไฟล์เข้า staging
git add hello.txt

# ดูสถานะอีกครั้ง (สังเกตความต่าง!)
git status

# Commit!
git commit -m "feat: add hello.txt - first commit ever!"

# ดูประวัติ
git log --oneline
```

**คำถาม:** สีของ `hello.txt` ใน `git status` เปลี่ยนยังไงก่อนและหลัง `git add`?  
**เขียนคำตอบตรงนี้:** ก่อนสีแดง หลังสีเขียว

---

## Exercise 5: เปลี่ยนแปลงและ Commit อีกครั้ง (15 นาที)

**โจทย์:** แก้ไขไฟล์และ commit ใหม่

1. เปิด `hello.txt` แล้วเพิ่มข้อความ: "วันนี้ผมเรียน Git แล้ว!"
2. รัน `git diff` เพื่อดูความเปลี่ยนแปลง
3. Add และ Commit โดยใช้ข้อความ commit ของตัวเอง
4. รัน `git log --oneline` ดูประวัติ

**คำถาม:** `git diff` แสดงอะไร? บรรทัดที่มี `+` คืออะไร?  
**เขียนคำตอบตรงนี้:** Git diff แสดงความแตกต่างไฟล์เก่ากะใหม่ , + คือมีไรเพิ่ม 

---

## 🏆 Boss Exercise: README ของตัวเอง (30 นาที)

**โจทย์สุดท้าย:** สร้าง `my-profile.md` ในโฟลเดอร์นี้

ไฟล์ต้องมี:
- ชื่อของตัวเอง
- ทำไมถึงเรียน Programming
- เป้าหมาย 9 เดือน (ของตัวเอง ไม่ใช่ copy!)
- สิ่งที่เรียนวันนี้ (1-3 ข้อ)

แล้ว Commit ด้วย message ที่สื่อความหมาย

---

## 📊 สรุปคะแนน

| Exercise | คะแนน | เสร็จแล้ว? |
|---------|-------|-----------|
| Ex 1: ตอบคำถาม | 10 | [ ] |
| Ex 2: ตั้งค่า Git | 15 | [ ] |
| Ex 3: สร้าง Repo | 20 | [ ] |
| Ex 4: First Commit | 25 | [ ] |
| Ex 5: แก้ไขและ Commit | 15 | [ ] |
| Boss: README | 15 | [ ] |
| **รวม** | **100** | |

---

## 💡 Hints (เปิดเมื่อติดจริงๆ เท่านั้น!)

<details>
<summary>Hint Exercise 3 - .git คืออะไร?</summary>

`.git` คือโฟลเดอร์ที่ Git ใช้เก็บข้อมูลทุกอย่าง
เช่น ประวัติ commit, settings ฯลฯ
ถ้าลบโฟลเดอร์นี้ = repo หายทันที!

</details>

<details>
<summary>Hint Exercise 4 - สีใน git status</summary>

- **แดง** = ไฟล์ที่เปลี่ยนแต่ยังไม่ add (Untracked/Modified)
- **เขียว** = ไฟล์ที่ add แล้ว รอ commit (Staged)

</details>

<details>
<summary>Hint Exercise 5 - git diff</summary>

- `+` สีเขียว = บรรทัดที่เพิ่มเข้ามา
- `-` สีแดง = บรรทัดที่ลบออก

</details>
