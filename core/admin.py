from django.contrib import admin
from core.models import Contactus, Level, UserProfile, QuizTakers, Answer, Response, LevelPublish, Notification, Goodie, Customize
import nested_admin


class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created',)
    readonly_fields = ('name', 'email', 'subject', 'comments', 'department', 'year', 'created',)
    search_fields = ['name', 'email']


# class LevelAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', )
#     readonly_fields = ('created',)


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 1
    max_num = 1


class ResponseInline(admin.TabularInline):
    model = Response


class LevelPublishInline(admin.TabularInline):
    model = LevelPublish


class QuizTakersAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)
    inlines = [ResponseInline, ]


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [LevelPublishInline, ]


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('level', 'quiztaker',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('level', 'text',)


class LevelPublishAdmin(admin.ModelAdmin):
    list_display = ('userprofile', 'level', 'publish')
    ordering = ['userprofile', ]


class GoodieAdmin(admin.ModelAdmin):
    list_display = ('title', )


class CustomizeAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(Level)
admin.site.register(Notification)
admin.site.register(LevelPublish, LevelPublishAdmin)
admin.site.register(QuizTakers, QuizTakersAdmin)
admin.site.register(Response, ResponseAdmin)

admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Contactus, ContactusAdmin)
admin.site.register(Goodie, GoodieAdmin)
admin.site.register(Customize, CustomizeAdmin)
