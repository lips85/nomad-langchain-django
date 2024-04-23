from django.contrib import admin
from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):

    title = "Elon Musk Filter"

    parameter_name = "ElonMusk"

    def lookups(self, request, model_admin):
        return [
            ("", "All"),
            ("yes", "Contain Elon"),
            ("no", "exclude Elon"),
        ]

    def queryset(self, request, tweets):
        check_word = "Elon Musk"
        if self.value() == "yes":
            return tweets.filter(payload__contains=check_word)
        elif self.value() == "no":
            return tweets.exclude(payload__contains=check_word)
        else:
            return tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "payload",
        "user",
        "like_count",
    )
    search_fields = [
        "user__username",
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
        "user__username",
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
