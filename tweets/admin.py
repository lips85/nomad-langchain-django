from django.contrib import admin
from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):

    title = "Elon Musk Filter"

    parameter_name = "ElonMusk"

    def lookups(self, request, model_admin):
        return [
            ("elon musk", "Contain Elon"),
            ("exclude elon", "exclude Elon"),
        ]

    def queryset(self, request, tweets):
        word = self.value()
        check_word = "elon musk"
        if word == check_word:
            return tweets.filter(payload__contains=check_word)
        elif word == "exclude elon":
            return tweets.exclude(payload__contains=check_word)
        else:
            tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "payload",
        "user",
        "like_count",
    )
    search_fields = [
        "user__username__in",
        "payload",
    ]
    list_filter = (
        "created_at",
        WordFilter,
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tweet",
    )

    search_fields = [
        "user__username__in",
    ]

    list_filter = ("created_at",)


# Mission:
# Tweet 그리고 Like models의 어드민을 개선하세요.

# Like Admin: (개선필요사항)
# Search by username of user foreign key.
# Filter by created_at

# Tweet Admin: (개선필요사항)
# Search by payload
# Search by username of user foreign key.
# Filter by created_at
# Make a CUSTOM filter for Tweets that contain and don't contain the words Elon Musk
