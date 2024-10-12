# Generated by Django 3.0.7 on 2020-06-07 12:37
# pylint: disable=invalid-name,missing-module-docstring,missing-class-docstring
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("small_small_hr", "0007_auto_20190625_2111"),
    ]

    operations = [
        migrations.RenameField(
            model_name="leave", old_name="reason", new_name="review_reason",
        ),
        migrations.RenameField(
            model_name="leave", old_name="status", new_name="review_status",
        ),
        migrations.RenameField(
            model_name="overtime", old_name="reason", new_name="review_reason",
        ),
        migrations.RenameField(
            model_name="overtime", old_name="status", new_name="review_status",
        ),
        migrations.RemoveField(model_name="leave", name="comments",),
        migrations.RemoveField(model_name="overtime", name="comments",),
        migrations.AddField(
            model_name="leave",
            name="review_date",
            field=models.DateTimeField(
                blank=True, default=None, null=True, verbose_name="Review Date"
            ),
        ),
        migrations.AddField(
            model_name="overtime",
            name="review_date",
            field=models.DateTimeField(
                blank=True, default=None, null=True, verbose_name="Review Date"
            ),
        ),
        migrations.AlterField(
            model_name="annualleave",
            name="year",
            field=models.PositiveIntegerField(
                choices=[
                    (2017, 2017),
                    (2018, 2018),
                    (2019, 2019),
                    (2020, 2020),
                    (2021, 2021),
                    (2022, 2022),
                    (2023, 2023),
                    (2024, 2024),
                    (2025, 2025),
                    (2026, 2026),
                    (2027, 2027),
                    (2028, 2028),
                    (2029, 2029),
                ],
                db_index=True,
                default=2017,
                verbose_name="Year",
            ),
        ),
    ]
