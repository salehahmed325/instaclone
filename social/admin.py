from django.contrib import admin
from social.models import FollowUser, MyPost, MyProfile, PostComments, PostLike
from django.contrib.admin.options import ModelAdmin

# Register your models here.

class followUserAdmin(ModelAdmin):
    list_display = ["profile", "followed_by"]
    search_fields = ["profile", "followed_by"]
    list_filter = ["profile", "followed_by"]
admin.site.register(FollowUser, followUserAdmin)

class MyPostAdmin(ModelAdmin):
    list_display = ["subject", "cr_date", "uploaded_by"]
    search_fields = ["subject", "msg", "uploaded_by"]
    list_filter = ["cr_date", "uploaded_by"]
admin.site.register(MyPost, MyPostAdmin)

class MyProfileAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "phone_no", "status"]
    list_filter = ["status", "gender"]
admin.site.register(MyProfile, MyProfileAdmin)

class PostCommentAdmin(ModelAdmin):
    list_display = ["post", "msg"]
    search_fields = ["msg", "post", "commented_by"]
    list_filter = ["cr_date", "flag"]
admin.site.register(PostComments, PostCommentAdmin)

class PostLikeAdmin(ModelAdmin):
    list_display = ["post", "liked_by"]
    search_fields = ["post", "liked_by"]
    list_filter = ["cr_date"]
admin.site.register(PostLike, PostLikeAdmin)