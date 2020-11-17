from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math

DEPARTMENT_OPTIONS = (
        ('IT', 'IT'),
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('ME', 'ME'),
        ('EE', 'EE'),
        ('CE', 'CE')
    )

YEAR = (
    ('Freshie', 1),
    ('2nd', 2),
    ('3rd', 3),
    ('Godfather', 4),
    ('Alumni', 5)
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Transgender', 'Transgender')
)

COLOR = (
    ('purple', 'purple'),
    ('orange', 'orange'),
    ('blue', 'blue'),
    ('teal', 'teal'),
    ('yellow', 'yellow'),
    ('red', 'red')
)

TYPE = (
    ('tshirt', 'tshirt'),
    ('checkbox', 'checkbox'),
    ('heart', 'heart'),
    ('gift', 'gift'),
)

class Contactus(models.Model):
    """
    Entity for Contact us
    """
    name = models.CharField(max_length=25)
    email = models.EmailField()
    department = models.CharField(default='IT', choices=DEPARTMENT_OPTIONS, max_length=25)
    year = models.CharField(default='Freshie', choices=YEAR, max_length=25)
    subject = models.CharField(max_length=50)
    comments = models.TextField(max_length=1000)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " ---- " + self.email

    class Meta:
        verbose_name_plural = 'Contact us Records'


class Level(models.Model):

    number = models.IntegerField(default=0)
    title = models.CharField(max_length=25, blank=True, null=True)
    picture = models.ImageField(upload_to='level_images', blank=True, null=True)
    audio = models.FileField(upload_to='level_images', blank=True, null=True)
    author = models.CharField(max_length=25, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    quote = models.CharField(max_length=100, blank=True, null=True)
    hint = models.TextField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_last = models.BooleanField(default=False)
    # answer = models.CharField(max_length=25)

    def __str__(self):
        if self.title is None:
            return "Untitled"
        else:
            return self.title

    def yearpublished(self):
        return self.created.strftime('%Y')

    def monthpublished(self):
        return self.created.strftime('%b')

    def daypublished(self):
        return self.created.strftime('%d')

    class Meta:
        ordering = ['created', ]

class Answer(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clear = models.IntegerField(default=0)
    department = models.CharField(default='IT', choices=DEPARTMENT_OPTIONS, max_length=25)
    year = models.CharField(default='Freshie', choices=YEAR, max_length=25)
    college = models.CharField(default='JGEC', max_length=60)
    gender = models.CharField(choices=GENDER, max_length=25)
    picture_url = models.URLField(null=True, blank=True)
    picture = models.ImageField(null=True, upload_to='profile_images', default='/dummyuser.jpg')
    dark_mode = models.BooleanField(default=True)
    color_mode = models.CharField(choices=COLOR, max_length=25, default=COLOR[4][0])
    is_previously_logged = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        words = self.college.lower().split()
        if len(words)>1:
            self.college = ""
            for word in words:
                self.college += word[0].upper()
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class QuizTakers(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    correct_answers = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user.username


class Response(models.Model):
     quiztaker = models.ForeignKey(QuizTakers, on_delete=models.CASCADE)
     level = models.ForeignKey(Level, on_delete=models.CASCADE)
     answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)

     def __str__(self):
        return self.level.title


class LevelPublish(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.userprofile.user.username + "---" + str(self.publish)

    class Meta:
        verbose_name_plural = 'Level Published'


class Goodie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    type = models.CharField(choices=TYPE, max_length=25, default=TYPE[0][0])

    def __str__(self):
        return self.title


class Customize(models.Model):
    title = models.CharField(max_length=20, default="Elementary", null=False)
    picture = models.ImageField(null=False, upload_to='elementary_logo', default='/elementary_logo/t20-logomark-white.svg')
    mottos = models.CharField(null=False, default="Ready.,Active.,Creative.", max_length=50)
    contact = models.CharField(max_length=30, default="Name: Mobile Number", null=False)
    email = models.EmailField(default="example@example.com", null=False)
    fb = models.CharField(default='https://www.facebook.com/jeclatT20.jgec/', null=False, max_length=100)
    instagram = models.CharField(default='https://www.instagram.com/jeclat2k19/', null=False, max_length=100)

    def __str__(self):
        return self.title


class Notification(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    message = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.admin.username

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.pub_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"

            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds / 60)

            if minutes == 1:
                return str(minutes) + " minute ago"

            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds / 3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days / 30)

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years = math.floor(diff.days / 365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"
