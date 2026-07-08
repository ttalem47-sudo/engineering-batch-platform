from django.shortcuts import render
from .models import Material

def home(request):
    # جلب جميع المواد المقسمة حسب الترم الدراسي
    # يمكنك تعديل الأرقام لتناسب الفصول الدراسية الحالية للدفعة
    semester_1_materials = Material.objects.filter(semester=1)
    semester_2_materials = Material.objects.filter(semester=2)
    semester_3_materials = Material.objects.filter(semester=3) # مثل الرسم الهندسي التطبيقي
    semester_4_materials = Material.objects.filter(semester=4)

    context = {
        'semester_1': semester_1_materials,
        'semester_2': semester_2_materials,
        'semester_3': semester_3_materials,
        'semester_4': semester_4_materials,
    }
    
    # إرسال البيانات إلى ملف التصميم الرئيسي
    return render(request, 'index.html', context)
