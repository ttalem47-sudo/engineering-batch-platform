from django.db import models

class Material(models.Model):
    SEMESTER_CHOICES = [
        (1, 'الترم الأول'),
        (2, 'الترم الثاني'),
        (3, 'الترم الثالث'),
        (4, 'الترم الرابع'),
    ]

    title = models.CharField(max_length=250, verbose_name="اسم الملف / المحاضرة")
    subject = models.CharField(max_length=150, verbose_name="اسم المادة (مثل: رسم هندسي)")
    semester = models.IntegerField(choices=SEMESTER_CHOICES, verbose_name="الترم الدراسي")
    pdf_url = models.URLField(verbose_name="رابط ملف الـ PDF (جوجل درايف أو ميديافاير)")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الرفع")

    class Meta:
        verbose_name = "مادة دراسية"
        verbose_name_plural = "المواد الدراسية"
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.subject} - {self.title}"
