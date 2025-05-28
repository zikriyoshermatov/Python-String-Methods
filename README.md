### ✅ Task01

**Matn faqat harflardan iboratligini tekshiring**

| Input                  | Output  |
| ---------------------- | ------- |
| `"Salom"`    | `True`  |
| `"Salom123"` | `False` |

---

### ✅ Task02

**Matn faqat raqamlardan iboratligini tekshiring**

| Input               | Output  |
| ------------------- | ------- |
| `"2025"`  | `True`  |
| `"20y25"` | `False` |

---

### ✅ Task03

**Matnda faqat harf yoki raqamdan iboratligini tekshiring**

| Input                  | Output  |
| ---------------------- | ------- |
| `"Python3"`  | `True`  |
| `"Python 3"` | `False` |

---

### ✅ Task04

**Matn faqat kichik harflardan iboratligini tekshiring**

| Input                | Output  |
| -------------------- | ------- |
| `"python"` | `True`  |
| `"Python"` | `False` |

---

### ✅ Task05

**Matn faqat katta harflardan iboratligini tekshiring**

| Input               | Output  |
| ------------------- | ------- |
| `"HELLO"` | `True`  |
| `"Hello"` | `False` |

---

### ✅ Task06

**Matn faqat bo‘sh joylardan iboratligini tekshiring**

| Input               | Output  |
| ------------------- | ------- |
| `"   "`   | `True`  |
| `"  a  "` | `False` |

---

### ✅ Task07

**Matn ma’lum so‘z bilan tugashini tekshiring**

| Input                               | Output  |
| ----------------------------------- | ------- |
| `"Hello world"`, `"Hello"` | `False`  |
| `"Hi there"`, `"there"`    | `True` |

---

### ✅ Task08

**Matn ma’lum so‘z bilan boshlanishini tekshiring**

| Input                               | Output  |
| ----------------------------------- | ------- |
| `"Hello world"`, `"Hello"` | `True`  |
| `"Hi there"`, `"Hello"`    | `False` |

---

### ✅ Task09

**Matndagi barcha harflarni katta harfga o‘tkazing**

| Input              | Output   |
| ------------------ | -------- |
| `"python"` | `PYTHON` |

---

### ✅ Task10

**Matndagi barcha harflarni kichik harfga o‘tkazing**

| Input              | Output   |
| ------------------ | -------- |
| `"PYTHON"` | `python` |

---

### ✅ Task11

**Matnning faqat birinchi harfini katta qilish**

| Input                            | Output            |
| -------------------------------- | ----------------- |
| `"python darslari"` | `Python darslari` |

---

### ✅ Task12

**Matndagi har bir so‘zning bosh harfini katta qilish**

| Input                                  | Output                       |
| -------------------------------------- | ---------------------------- |
| `"python dasturlash asoslari"` | `Python Dasturlash Asoslari` |

---

### ✅ Task13

**Ikkita matn kiritiladi birinchisi ikkinchisida bor yoki yo'qligini aniqlash**

| Input                             | Output                         |
| --------------------------------- | ------------------------------ |
| `"salom"`, `"salom dunyo"` | `True` |
| `"SALOM"`, `"salom dunyo"` | `True` |
| `"hello"`, `"salom dunyo"` | `False` |

---

### ✅ Task14

**Ikkita matn o'qilganda bir qil yoki yo'qligini tekshiring**

| Input                           | Output         |
| ------------------------------- | -------------- |
| `"salom"`, `"salom"` | `True` |
| `"SALOM"`, `"salom"` | `True` |
| `"hello"`, `"salom"` | `False` |

---

### ✅ Task15

**Matndan boshidagi va oxiridagi bo‘sh joylarni olib tashlang**

| Input                       | Output        |
| --------------------------- | ------------- |
| `"  Hello world  "` | `Hello world` |

---

### ✅ Task16

**Matn ichidagi so‘zlarni almashtiring**

| Input                                    | Output       |
| ---------------------------------------- | ------------ |
| `"Salom dunyo"`, `"dunyo"`, `"olam"` | `Salom olam` |

---

### ✅ Task17

**Matnni berilgan uzunlikka yetkazib, chapdan to‘ldiring (`rjust`)**

| Input                | Output  |
| -------------------- | ------- |
| `"42".rjust(5, "0")` | `00042` |

---

### ✅ Task18

**Matnni berilgan uzunlikka yetkazib, o‘ngdan to‘ldiring (`ljust`)**

| Input                | Output  |
| -------------------- | ------- |
| `"42".ljust(5, "0")` | `42000` |

---

### ✅ Task19

**Matnni kichik harflarga o‘tkazing va faqat raqamlardan iborat emasligini tekshiring**

| Input                          | Output  |
| ------------------------------ | ------- |
| `"HELLO123"` | `False` |
| `"HELLO"`    | `True`  |

---

### ✅ Task20

**Matnning faqat birinchi harfini katta qilib, bosh harf bilan boshlanganini tekshiring**

| Input                                      | Output  |
| ------------------------------------------ | ------- |
| `"python darslari"` | `False` |
| `"Python darslari"` | `True`  |

---

### ✅ Task21

**Matnni kichik harfga o‘tkazing va ‘python’ so‘zi borligini tekshiring**

| Input                                                      | Output  |
| ---------------------------------------------------------- | ------- |
| `"Men PYTHONni yoqtiraman"` | `True`  |
| `"Java afzal"`              | `False` |

---

### ✅ Task22

**Bo‘sh joylarni olib tashlab, satr bo‘sh emasligini tekshiring**

| Input                        | Output  |
| ---------------------------- | ------- |
| `"     "`  | `False` |
| `"Hello "` | `False` |

---

### ✅ Task23

**Matnni `upper` qilgach, faqat katta harflardan iboratligini tekshiring**

| Input                       | Output |
| --------------------------- | ------ |
| `"hello"` | `True` |
| `"Hello"` | `True` |

---

### ✅ Task24 – Email tekshiruv (Django user auth dan ilhomlangan)

**Foydalanuvchining email manzili `@` bilan boshlanmasligi va `.com` bilan tugashini tekshiring**

| Input                | Output  |
| -------------------- | ------- |
| `"user@example.com"` | `True`  |
| `"@example.com"`     | `False` |
| `"user@example.net"` | `False` |

---

### ✅ Task25 – Tozalangan foydalanuvchi ismi (Telegram botlardan ilhom)

**Foydalanuvchi yuborgan ismni bo‘sh joylardan tozalang va bosh harf bilan boshlansin**

| Input         | Output   |
| ------------- | -------- |
| `"   ali"`    | `Ali`    |
| `"  diyora "` | `Diyora` |

---

### ✅ Task26 – GitHub username validatsiyasi

**GitHub usernames faqat `a-z`, `A-Z`, `0-9`, `-` dan iborat bo‘lishi kerak, `isalpha()` bilan tekshirishdan oldin `replace("-", "")` bilan `-` belgilarini olib tashlang.**

| Input         | Output  |
| ------------- | ------- |
| `"ali-coder"` | `True`  |
| `"diyor_123"` | `False` |

---

### ✅ Task27 – Document type aniqlash (Linux file command ilhomida)

**Fayl nomi `.pdf`, `.docx`, yoki `.txt` bilan tugashini tekshiring**

| Input          | Output  |
| -------------- | ------- |
| `"report.pdf"` | `True`  |
| `"photo.jpeg"` | `False` |

---

### ✅ Task28 – Comment string tozalash (Blog saytlardagi filter logikasi)

**Izoh matnidan “yomon” so‘zlarni olib tashlang, so‘ngra `islower()` bilan tekshiring**

| Input                                      | Output |
| ------------------------------------------ | ------ |
| `"this is bad".replace("bad", "")`         | `True` |
| `"This is BAD".lower().replace("bad", "")` | `True` |
