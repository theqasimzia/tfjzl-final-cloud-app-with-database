from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Register ChoiceInline class
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

# Register QuestionInline class
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Register models with admin site
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)

# Register Question and Choice with ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
