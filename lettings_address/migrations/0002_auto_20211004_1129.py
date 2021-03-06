# Generated by Django 3.1.13 on 2021-10-04 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings_address', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
                INSERT INTO lettings_address_address (
                    id,
                    number,
                    street,
                    city,
                    state,
                    zip_code,
                    country_iso_code
                    
                )
                SELECT
                    id,
                    number,
                    street,
                    city,
                    state,
                    zip_code,
                    country_iso_code
                FROM
                    oc_lettings_site_address;
            """, reverse_sql="""
                INSERT INTO oc_lettings_site_address (
                    id,
                    number,
                    street,
                    city,
                    state,
                    zip_code,
                    country_iso_code
                )
                SELECT
                    id,
                    number,
                    street,
                    city,
                    state,
                    zip_code,
                    country_iso_code
                FROM
                    lettings_address_address;
            """),
        migrations.RunSQL("""
                    INSERT INTO lettings_address_letting (
                        id,
                        title,
                        address_id
                    )
                    SELECT
                        id,
                        title,
                        address_id
                    FROM
                        oc_lettings_site_letting;
                """, reverse_sql="""
                    INSERT INTO oc_lettings_site_letting (
                        id,
                        title,
                        address_id
                    )
                    SELECT
                        id,
                        title,
                        address_id
                    FROM
                        lettings_address_letting;
                """)
    ]
