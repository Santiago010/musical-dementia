from django.apps import AppConfig


class SearchTagsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search_tags'
    verbose_name = "application responsible for searching profiles and publications by tags"
