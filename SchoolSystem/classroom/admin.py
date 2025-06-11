from django.contrib import admin
from .models import (
    Principal, Student, Teacher, Subject, Curriculum, Classroom,
    Assignment, AssignmentSubmission, Testpaper, TestpaperResult
)
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import localtime

# ======================
# Inline Admins
# ======================
class AssignmentSubmissionInline(admin.TabularInline):
    model = AssignmentSubmission
    extra = 0


class TestpaperResultInline(admin.TabularInline):
    model = TestpaperResult
    extra = 0


# ======================
# BaseProfile Admins
# ======================
@admin.register(Principal)
class PrincipalAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'get_created_at')  # Fix the error
    search_fields = ('user__username', 'full_name')
    list_filter = (('created_at', admin.DateFieldListFilter),)

    def get_created_at(self, obj):
        return localtime(obj.created_at).strftime("%Y-%m-%d %H:%M")
    get_created_at.admin_order_field = 'created_at'
    get_created_at.short_description = 'Created At'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'classroom', 'enrollment_date')
    search_fields = ('user__username', 'full_name')
    list_filter = ('classroom', 'enrollment_date')
    inlines = [AssignmentSubmissionInline, TestpaperResultInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'hire_date', 'subject_name')
    search_fields = ('user__username', 'full_name', 'subject__name')
    list_filter = ('hire_date', 'subject')
    filter_horizontal = ('classroom',)

    def subject_name(self, obj):
        return obj.subject.name
    subject_name.short_description = "Subject"


# ======================
# Core Model Admins
# ======================
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'credits')
    search_fields = ('name',)
    list_filter = ('credits',)


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')
    filter_horizontal = ('subjects',)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'curriculum')
    search_fields = ('name', 'curriculum__name')
    list_filter = ('curriculum',)


# ======================
# Assignment & Test Admins
# ======================
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'target', 'subject', 'curriculum', 'classroom', 'deadline')
    search_fields = ('title', 'description')
    list_filter = ('target', 'subject', 'curriculum', 'classroom', 'deadline')
    date_hierarchy = 'deadline'


@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'submission_date', 'remarks')
    search_fields = ('assignment__title', 'student__full_name')
    list_filter = ('submission_date',)
    date_hierarchy = 'submission_date'


@admin.register(Testpaper)
class TestpaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'category', 'target', 'subject', 'curriculum', 'classroom', 'duration')
    search_fields = ('title', 'description')
    list_filter = ('type', 'category', 'target', 'subject', 'curriculum', 'classroom')
    inlines = [TestpaperResultInline]


@admin.register(TestpaperResult)
class TestpaperResultAdmin(admin.ModelAdmin):
    list_display = ('testpaper', 'student', 'marks', 'percentage', 'failed')
    search_fields = ('testpaper__title', 'student__full_name')
    list_filter = ('testpaper__type', 'student__classroom')

    def percentage(self, obj):
        return f"{obj.percentage:.2f}%"
    percentage.short_description = "Percentage"

    def failed(self, obj):
        return obj.failed
    failed.boolean = True
    failed.short_description = "Failed"
