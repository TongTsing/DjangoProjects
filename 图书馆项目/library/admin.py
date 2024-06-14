from django.contrib import admin

import library.models

# Register your models here.
admin.site.register(library.models.Author)
admin.site.register(library.models.Publisher)
admin.site.register(library.models.Book)