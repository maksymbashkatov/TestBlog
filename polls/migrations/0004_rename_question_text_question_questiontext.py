# Generated by Django 4.0.1 on 2022-01-29 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_дата публиации_question_publicationdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='QuestionText',
        ),
    ]
