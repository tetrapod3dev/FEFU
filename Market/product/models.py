from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete
# Feel free to rename the models, but don't rename db_table values or field names.



class BadgeInfo(models.Model):
    no = models.AutoField(primary_key=True)
    badge_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'badge_info'


class CampaignBadge(models.Model):
    no = models.AutoField(primary_key=True)
    campaign_no = models.ForeignKey('CampaignInfo', models.DO_NOTHING, db_column='campaign_no'
    badge_no = models.ForeignKey(BadgeInfo, models.DO_NOTHING, db_column='badge_no')

    class Meta:
        managed = False
        db_table = 'campaign_badge'


class CampaignInfo(models.Model):
    no = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45)
    writer = models.ForeignKey('User', models.DO_NOTHING, db_column='writer')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    photo = models.CharField(max_length=45, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'campaign_info'


class CampaignProofMessage(models.Model):
    no = models.AutoField(primary_key=True)
    campaign_no = models.ForeignKey(CampaignInfo, models.DO_NOTHING, db_column='campaign_no')
    proof_message_no = models.ForeignKey('ProofMessageInfo', models.DO_NOTHING, db_column='proo')

    class Meta:
        managed = False
        db_table = 'campaign_proof_message'


class CampaignTag(models.Model):
    no = models.AutoField(primary_key=True)
    campaign_no = models.ForeignKey(CampaignInfo, models.DO_NOTHING, db_column='campaign_no')
    tag_no = models.ForeignKey('TagInfo', models.DO_NOTHING, db_column='tag_no')

    class Meta:
        managed = False
        db_table = 'campaign_tag'


class CompanyCampaignInfo(models.Model):
    no = models.AutoField(primary_key=True)
    campaign_no = models.ForeignKey(CampaignInfo, models.DO_NOTHING, db_column='campaign_no')
    company_name = models.CharField(max_length=45, blank=True, null=True)
    campaign_link = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_campaign_info'


class DailyQuestInfo(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_quest_info'


class MainCategoryInfo(models.Model):
    no = models.AutoField(primary_key=True)
    main_category_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_category_info'


class OfficialPersonalCampaignInfo(models.Model):
    no = models.AutoField(primary_key=True)
    campaign_no = models.ForeignKey(CampaignInfo, models.DO_NOTHING, db_column='campaign_no')
    mission = models.CharField(max_length=100, blank=True, null=True)
    auth_process = models.CharField(max_length=100, blank=True, null=True)
    auth_start_time = models.CharField(max_length=10, blank=True, null=True)
    auth_end_time = models.CharField(max_length=10, blank=True, null=True)
    headcount = models.IntegerField(blank=True, null=True)
    requirement = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'official_personal_campaign_info'


class ProductInfo(models.Model):
    no = models.AutoField(primary_key=True)
    writer = models.ForeignKey('User', models.DO_NOTHING, db_column='writer')
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=500)
    contact = models.CharField(max_length=100)
    price = models.IntegerField()
    eco_point = models.IntegerField(blank=True, null=True)
    main_category_no = models.ForeignKey(MainCategoryInfo, models.DO_NOTHING, db_column='main_)
    sub_category_no = models.ForeignKey('SubCategoryInfo', models.DO_NOTHING, db_column='sub_c
    reg_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_info'


class ProofMessageInfo(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    regtime = models.DateTimeField(blank=True, null=True)
    photo = models.CharField(max_length=45)
    writer = models.ForeignKey('User', models.DO_NOTHING, db_column='writer')
    authenticated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proof_message_info'


class QuestBadge(models.Model):
    no = models.AutoField(primary_key=True)
    badge_no = models.ForeignKey(BadgeInfo, models.DO_NOTHING, db_column='badge_no')
    quest_no = models.ForeignKey(DailyQuestInfo, models.DO_NOTHING, db_column='quest_no')

    class Meta:
        managed = False
        db_table = 'quest_badge'


class QuestionCommentInfo(models.Model):
    no = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    writer = models.ForeignKey('User', models.DO_NOTHING, db_column='writer')
    question_no = models.ForeignKey('QuestionInfo', models.DO_NOTHING, db_column='question_no'

    class Meta:
        managed = False
        db_table = 'question_comment_info'


class QuestionInfo(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    complete = models.IntegerField(blank=True, null=True)
    writer = models.ForeignKey('User', models.DO_NOTHING, db_column='writer')
    campaign_no = models.ForeignKey(CampaignInfo, models.DO_NOTHING, db_column='campaign_no')

    class Meta:
        managed = False
        db_table = 'question_info'


class SubCategoryInfo(models.Model):
    no = models.AutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=45, blank=True, null=True)
    main_category_no = models.ForeignKey(MainCategoryInfo, models.DO_NOTHING, db_column='main_)

    class Meta:
        managed = False
        db_table = 'sub_category_info'


class TagInfo(models.Model):
    no = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tag_info'


class User(models.Model):
    no = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=45)
    eco_point = models.IntegerField(blank=True, null=True)
    exp = models.IntegerField(blank=True, null=True)
    profile_image = models.CharField(max_length=45, blank=True, null=True)
    introduce = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserAutority(models.Model):
    no = models.AutoField(primary_key=True)
    user_no = models.ForeignKey(User, models.DO_NOTHING, db_column='user_no')
    authority = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user_autority'


class UserBadgeFavor(models.Model):
    no = models.AutoField(primary_key=True)
    user_no = models.ForeignKey(User, models.DO_NOTHING, db_column='user_no')
    badge_no = models.ForeignKey(BadgeInfo, models.DO_NOTHING, db_column='badge_no')

    class Meta:
        managed = False
        db_table = 'user_badge_favor'


class UserQuestComplete(models.Model):
    no = models.AutoField(primary_key=True)
    user_no = models.ForeignKey(User, models.DO_NOTHING, db_column='user_no')
    quest_no = models.ForeignKey(DailyQuestInfo, models.DO_NOTHING, db_column='quest_no')
    complete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_quest_complete'
