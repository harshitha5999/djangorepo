from django.contrib import admin

from catalog.models import Book,Author,Genre,Student

# Register your models here.

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('id','name')
    fields = [('name','purchase_date')]
    # note : RelatedOnlyListFilter=>applicable when some fields are related to other tables
    list_filter = ('name','purchase_date',('book_author',admin.RelatedOnlyFieldListFilter))
    list_filter = ('name','purchase_date','book_author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('author_name','date_of_birth')
    list_filter = ('author_name','date_of_birth')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('student_name','date_of_purchase')
    list_filter = ('student_name','date_of_purchase')