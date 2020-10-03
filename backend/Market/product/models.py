from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BadgeInfo(models.Model):
    no = models.AutoField(primary_key=True)
    badge_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'badge_info'


class CampaignBadge(models.Model):
    no = models.AutoField(primary_key=True)
    campaign_no = models.ForeignKey('CampaignInfo', models.DO_NOTHING, db_column='campaign_no')
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
    proof_message_no = models.ForeignKey('ProofMessageInfo', models.DO_NOTHING, db_column='proof_message_no')

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


class CampaignUser(models.Model):
    no = models.AutoField(primary_key=True)
    campaign_no = models.ForeignKey(CampaignInfo, models.DO_NOTHING, db_column='campaign_no')
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'campaign_user'


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
    description = models.CharField(max_length=500)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_quest_info'


class DjangoAdminLog(models.Model):

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainCategoryInfo(models.Model):
    no = models.AutoField(primary_key=True)
    main_category_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_category_info'


class MediumCategoryInfo(models.Model):
    no = models.AutoField(primary_key=True)
    medium_category_name = models.CharField(max_length=45, blank=True, null=True)
    main_category_no = models.ForeignKey(MainCategoryInfo, models.DO_NOTHING, db_column='main_category_no', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medium_category_info'


class OfficialPersonalCampaignInfo(models.Model):
    no = models.AutoField(primary_key=True)
    campaign_no = models.ForeignKey(CampaignInfo, models.DO_NOTHING, db_column='campaign_no')
    mission = models.CharField(max_length=100, blank=True, null=True)
    auth_process = models.CharField(max_length=100, blank=True, null=True)
    auth_start_time = models.CharField(max_length=20, blank=True, null=True)
    auth_end_time = models.CharField(max_length=20, blank=True, null=True)
    headcount = models.IntegerField(blank=True, null=True)
    requirement = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'official_personal_campaign_info'


class ProductInfo(models.Model):
    no = models.AutoField(primary_key=True)
    writer = models.ForeignKey('User', models.DO_NOTHING, db_column='writer', to_field="username")
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=500)
    contact = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.CharField(max_length=45, blank=True, null=True)
    eco_point = models.IntegerField(blank=True, null=True)
    main_category_no = models.ForeignKey(MainCategoryInfo, models.DO_NOTHING, db_column='main_category_no')
    medium_category_no = models.ForeignKey(MediumCategoryInfo, models.DO_NOTHING, db_column='medium_category_no')
    sub_category_no = models.ForeignKey('SubCategoryInfo', models.DO_NOTHING, db_column='sub_category_no')
    status = models.IntegerField(blank=True, null=True)
    reg_time = models.DateTimeField(blank=True, null=True, auto_now=True)

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


class PurchaseDetails(models.Model):
    no = models.AutoField(primary_key=True)
    seller = models.ForeignKey('User', models.DO_NOTHING, db_column='seller', related_name='seller')
    buyer = models.ForeignKey('User', models.DO_NOTHING, db_column='buyer', related_name='buyer')
    product_no = models.ForeignKey(ProductInfo, models.DO_NOTHING, db_column='product_no')

    class Meta:
        managed = False
        db_table = 'purchase_details'


class QuestBadge(models.Model):
    no = models.AutoField(primary_key=True)
    badge_no = models.ForeignKey(BadgeInfo, models.DO_NOTHING, db_column='badge_no')
    quest_no = models.ForeignKey(DailyQuestInfo, models.DO_NOTHING, db_column='quest_no')

    class Meta:
        managed = False
        db_table = 'quest_badge'



class SubCategoryInfo(models.Model):
    no = models.AutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=45, blank=True, null=True)
    medium_category_no = models.ForeignKey(MediumCategoryInfo, models.DO_NOTHING, db_column='medium_category_no', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_category_info'


class TagInfo(models.Model):
    no = models.AutoField(primary_key=True)
    tag_name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'tag_info'


class User(models.Model):
    no = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=45)
    nickname = models.CharField(max_length=50)
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


class UserAuthority(models.Model):
    no = models.AutoField(primary_key=True)
    user_no = models.ForeignKey(User, models.DO_NOTHING, db_column='user_no')
    authority = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user_authority'


class UserQuestComplete(models.Model):
    no = models.AutoField(primary_key=True)
    user_no = models.ForeignKey(User, models.DO_NOTHING, db_column='user_no')
    quest_no = models.ForeignKey(DailyQuestInfo, models.DO_NOTHING, db_column='quest_no')
    complete_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_quest_complete'


class ViewDetails(models.Model):
    no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', to_field="username")
    product_no = models.ForeignKey(ProductInfo, models.DO_NOTHING, db_column='product_no')
    sub_category_no = models.ForeignKey(SubCategoryInfo, models.DO_NOTHING, db_column='sub_category_no')
    reg_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'view_details'
        