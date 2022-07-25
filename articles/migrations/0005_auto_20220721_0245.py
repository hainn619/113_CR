# Generated by Django 4.0.6 on 2022-07-21 02:45

from django.db import migrations

def populate_article_status(apps, schemaeditor):
    status ={
        "Pending review":"pending",
        "Published":"Published",
        "Revision Request": "Revision Request",
        "Denied" : "Denied",
        "Draft" : "Draft",
    }
    Status = apps.get_model("articles","Status")
    for name, desc in status.items():
        status_obj=Status(name=name, description=desc)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_status_article_status'),
    ]

    operations = [
        migrations.RunPython(populate_article_status),
    ]