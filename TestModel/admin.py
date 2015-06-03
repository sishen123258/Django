from django.contrib import admin
from TestModel.models import Test, Contact, Tag

# Register your models here.
# admin.site.register(Test)

# list tup()
# admin.site.register([Test, Contact, Tag])

#Foreign Key

# class ContactAdmin(admin.ModelAdmin):
# fields = ('name', 'email')
# class ContactAdmin(admin.ModelAdmin):
#
#
#     fieldsets = (
#         ['Main', {
#             'fields': ('name', 'email'),
#         }],
#         ['Advance', {
#             'classes': ('collapse',),  # CSS
#             'fields': ('age',),
#         }]
#     )
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test, Tag])

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
            }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
            }]

    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])


