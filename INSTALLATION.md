# تعليمات التثبيت والتشغيل

## المتطلبات
- Python 3.9+
- Node.js 14+ (اختياري)
- npm (اختياري)

## الخطوات

### 1. استنساخ المستودع
```bash
git clone https://github.com/THWte/saudi-law-3d-courtroom.git
cd saudi-law-3d-courtroom
```

### 2. إنشاء بيئة افتراضية
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. تثبيت المتطلبات
```bash
pip install -r backend/requirements.txt
```

### 4. إعداد متغيرات البيئة
```bash
cp .env.example .env
# ثم عدّل .env بمفتاحك API
```

### 5. تشغيل التطبيق
```bash
python backend/app.py
```

سيكون التطبيق متاحاً في: `http://localhost:5000`

## الاستخدام

### الوصول إلى الواجهة
1. افتح المتصفح
2. اذهب إلى `http://localhost:5000`
3. اختر وضع الذكاء المطلوب
4. أدخل بيانات القضية
5. انقر على "تحليل القضية"

### الأوضاع الثلاثة
- **ذكاء كامل**: النظام يقرر بالكامل
- **مساعدة ذكية**: النظام يقترح والمستخدم يختار
- **المستخدم فقط**: عرض المعلومات فقط

## API Documentation

### تحليل القضية
```bash
POST /api/analyze-case
Content-Type: application/json

{
  "case": {
    "description": "نص القضية",
    "plaintiff": "اسم المدعي",
    "defendant": "اسم المدعى عليه",
    "caseType": "مدنية"
  },
  "mode": "AI_ASSISTED"
}
```

### رفع الملفات
```bash
POST /api/upload-files
Content-Type: multipart/form-data

files: [file1, file2, ...]
```

### تعيين الوضع
```bash
POST /api/set-mode
Content-Type: application/json

{
  "mode": "FULL_AI" | "AI_ASSISTED" | "USER_ONLY"
}
```

## استكشاف الأخطاء

### الخطأ: "ANTHROPIC_API_KEY not found"
- تأكد من وجود .env مع المفتاح الصحيح

### الخطأ: "Connection refused"
- تأكد من تشغيل الخادم
- افحص المنفذ (Port)

### الخطأ: "Module not found"
- أعد تثبيت المتطلبات:
  ```bash
  pip install -r backend/requirements.txt --force-reinstall
  ```

## الدعم والمساعدة
للمساعدة والدعم، يرجى فتح issue في المستودع.
