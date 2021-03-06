# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-29 06:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0069_auto_20200528_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='rd_bai_0_id',
            new_name='erp_bai_0_id',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_bai_1_name',
            new_name='erp_bai_1_name',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_bai_2_organisation',
            new_name='erp_bai_2_organisation',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_bai_3_providers',
            new_name='erp_bai_3_providers',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_bai_4_webpage',
            new_name='erp_bai_4_webpage',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_cli_1_scientific_domain',
            new_name='erp_cli_1_scientific_domain',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_cli_2_scientific_subdomain',
            new_name='erp_cli_2_scientific_subdomain',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_cli_3_category',
            new_name='erp_cli_3_category',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_cli_4_subcategory',
            new_name='erp_cli_4_subcategory',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_cli_5_tags',
            new_name='erp_cli_5_tags',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_gla_1_geographical_availability',
            new_name='erp_gla_1_geographical_availability',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_gla_2_language',
            new_name='erp_gla_2_language',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mgi_1_helpdesk_webpage',
            new_name='erp_mgi_1_helpdesk_webpage',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mgi_2_helpdesk_email',
            new_name='erp_mgi_2_helpdesk_email',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mgi_3_user_manual',
            new_name='erp_mgi_3_user_manual',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mgi_4_terms_of_use',
            new_name='erp_mgi_4_terms_of_use',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mgi_5_privacy_policy',
            new_name='erp_mgi_5_privacy_policy',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mgi_6_sla_specification',
            new_name='erp_mgi_6_sla_specification',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mgi_7_training_information',
            new_name='erp_mgi_7_training_information',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mgi_8_status_monitoring',
            new_name='erp_mgi_8_status_monitoring',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mgi_9_maintenance',
            new_name='erp_mgi_9_maintenance',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mri_1_description',
            new_name='erp_mri_1_description',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mri_2_tagline',
            new_name='erp_mri_2_tagline',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mri_3_logo',
            new_name='erp_mri_3_logo',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mri_4_mulitimedia',
            new_name='erp_mri_4_mulitimedia',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mri_5_target_users',
            new_name='erp_mri_5_target_users',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mri_6_target_customer_tags',
            new_name='erp_mri_6_target_customer_tags',
        ),
        migrations.RenameField(
            model_name='resource',
            old_name='rd_mri_7_use_cases',
            new_name='erp_mri_7_use_cases',
        ),
    ]
