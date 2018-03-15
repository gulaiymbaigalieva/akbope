from django.contrib import admin

# Register your models here.
class Location(meta.Model):

    class Admin:
        list_display = ("city", "state", "country")

class Job(meta.Model):

    class Admin:
     list_display = ("job_title", "location", "pub_date")
     ordering = ["-pub_date"]
     search_fields = ("job_title", "job_description")
     list_filter = ("location",)