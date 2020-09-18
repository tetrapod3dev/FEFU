# Generated by Django 2.1.15 on 2020-09-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BadgeInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('badge_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'badge_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampaignBadge',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'campaign_badge',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampaignInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=45)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('photo', models.CharField(blank=True, max_length=45, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'campaign_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampaignProofMessage',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'campaign_proof_message',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CampaignTag',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'campaign_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyCampaignInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, max_length=45, null=True)),
                ('campaign_link', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'company_campaign_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DailyQuestInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'daily_quest_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainCategoryInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('main_category_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'main_category_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OfficialPersonalCampaignInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('mission', models.CharField(blank=True, max_length=100, null=True)),
                ('auth_process', models.CharField(blank=True, max_length=100, null=True)),
                ('auth_start_time', models.CharField(blank=True, max_length=10, null=True)),
                ('auth_end_time', models.CharField(blank=True, max_length=10, null=True)),
                ('headcount', models.IntegerField(blank=True, null=True)),
                ('requirement', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'official_personal_campaign_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=45)),
                ('content', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('eco_point', models.IntegerField(blank=True, null=True)),
                ('reg_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProofMessageInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('regtime', models.DateTimeField(blank=True, null=True)),
                ('photo', models.CharField(max_length=45)),
                ('authenticated', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'proof_message_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuestBadge',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'quest_badge',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionCommentInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'question_comment_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('complete', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'question_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubCategoryInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'sub_category_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TagInfo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tag_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=45)),
                ('eco_point', models.IntegerField(blank=True, null=True)),
                ('exp', models.IntegerField(blank=True, null=True)),
                ('profile_image', models.CharField(blank=True, max_length=45, null=True)),
                ('introduce', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserAutority',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('authority', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user_autority',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserBadgeFavor',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'user_badge_favor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserQuestComplete',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('complete_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_quest_complete',
                'managed': False,
            },
        ),
    ]
