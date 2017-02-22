# from twisted.test.process_echoer import data
# from django.db import models
# test model
import datetime
from django.utils import timezone
from time import time
from django.db import models
from django.contrib.auth.models import User

# from django.core.files.storage import FileSystemStorage
from django.conf import settings
from CRS import settings
# from gtk._gtk import widget_set_default_colormap


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     # this is added to notify that what is created recently, a filter is used in admin.py so as to differentiate as per the date published for the object 'Question'
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#
#
# def __unicode__(self):  # __unicode__ on Python 2
#     return self.question_text
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __unicode__(self):  # __unicode__ on Python 2
#         return self.choice_text
#
#
# STATUS_CHOICES = enumerate(("solid", "squishy", "liquid"))
#
#
# class IceCream(models.Model):
#     flavor = models.CharField(max_length=50)
#     status = models.IntegerField(choices=STATUS_CHOICES)
#
#     def __unicode__(self):  # __unicode__ on Python 2
#         return self.flavor


# Comment model

class Comment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    # employee = user.username()
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):  # __unicode__ on Python 2
        return self.user.username + " "+ self.body

        # userprofile model


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __unicode__(self):
        # return u'%s,%s,%s' % self.user.username, self.last_name, self.first_name
        return self.user.first_name

    class Meta:
        verbose_name_plural = u'User profiles'

        # -----------------------------------------------------------------------------------------------------
        # employee information form model
        # -----------------------------------------------------------------------------------------------------

# def get_upload_file_name(instance, filename):
#     return settings.UPLOAD_FILE_PATTERN % (str(time()).replace('.', '_'), filename)


class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    your_name = models.CharField(max_length=100, default=None)
    dob = models.DateTimeField(blank=True, null=True, default=timezone.now())
    city = models.CharField(max_length=50, default=None)
    country = models.CharField(max_length=50, default=None)
    highest_degree = models.CharField(max_length=100, default=None)
    doj = models.DateTimeField(blank=True, null=True, default=timezone.now())
    designation = models.CharField(max_length=100, default=None)
    # Profile_Pic = models.ImageField(upload_to="img/documents/", null=True, blank=True)

    # NT_skill = models.TextField(max_length=500, null=True, blank=True, default=None)
    # T_skill = models.CharField(max_length=500, default=None)

    def __unicode__(self):
        # return u'%s,%s,%s' % self.user.username, self.last_name, self.first_name
        return self.your_name

STATUS = (
    ('R', 'Rejected'),
    ('S', 'Scheduled'),
    ('H', 'Hired')
)

SCHEDULE_2 = (
    ('HN', 'Harshal'),
    ('RP', 'Richa')

    )

SCHEDULE_3 = (
    ('SG', 'Siddhart'),
    ('BB', 'Bharat')

    )

class Candidate(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    # pub_date = models.DateTimeField(auto_now_add=True, null=True)
    candidate_name = models.CharField(max_length=100, default=None)
    job_title = models.CharField(max_length=100, default=None)
    experience = models.CharField(max_length=2, default=None)
    highest_degree = models.CharField(max_length=100, default=None)
    city = models.CharField(max_length=50, default=None)
    country = models.CharField(max_length=50, default=None)
    source = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    contact_number = models.CharField(max_length=50, default=None)
    screening_score_1 = models.CharField(max_length=2, default=None)
    status_1 = models.CharField(max_length=3, choices=STATUS)
    # status_2 = models.CharField(max_length=3, choices=STATUS)
    # scheduled_with = models.CharField(max_length=50,choices=STATUS)

    # # # next round2 details to be updated in the profile of scheduled person
    # screening_score_2 = models.CharField(max_length=2, default=None)
    # status_2 = models.CharField(max_length=3, choices=STATUS)
    # final_schedule = models.CharField(max_length=2, choices=SCHEDULE_3)
    #
    # # next round3 details to be updated in the profile of scheduled person
    # screening_score_3 = models.CharField(max_length=2, default=None)
    # status_3 = models.CharField(max_length=3, choices=STATUS)
    # final_score = models.CharField(max_length=2, default=None)


    # doj = models.DateTimeField(blank=True, null=True, default=timezone.now())
    # Profile_Pic = models.ImageField(upload_to="img/documents/", null=True, blank=True)