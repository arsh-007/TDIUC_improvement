from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('satisfaction', 'date','details')
    list_filter = ('satisfaction', 'date')
    search_fields = ('image_id','question_id', 'details','initial_answer')

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
