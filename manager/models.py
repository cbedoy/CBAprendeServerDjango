from django.db import models

"""
    DEVELOP BY CARLOS BEDOY
    MOBILE AND WEB DEVELOPER
    carlos.bedoy@gmail.com
"""


class Course(models.Model):
    thumbnail = models.ImageField(upload_to='media/course_imgs/', default='media/course_imgs/None/no-img.jpg')
    name = models.CharField(max_length=45, help_text='name of course')
    description = models.TextField(max_length=100)
    popularity = models.FloatField()
    views = models.IntegerField()

    def __unicode__(self):
        return self.name


class Theme(models.Model):
    thumbnail = models.ImageField(upload_to='media/theme_imgs/', default='media/course_imgs/None/no-img.jpg')
    name = models.CharField(max_length=50, help_text='Algorithms')
    description = models.TextField(max_length=100, help_text='short description about theme')
    popularity = models.FloatField()
    views = models.IntegerField()
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    option_list = (
        (1, 'A)'),
        (2, 'B)'),
        (3, 'C)'),
        (4, 'D)'),
    )
    thumbnail = models.ImageField(upload_to='media/question_imgs/', default='media/question_imgs/None/no-img.jpg', null=True)
    question = models.CharField(max_length=250, help_text='Are you developer')
    answer1 = models.CharField(max_length=200, help_text='YES')
    answer2 = models.CharField(max_length=200, help_text='maybe')
    answer3 = models.CharField(max_length=200, help_text='why?')
    answer4 = models.CharField(max_length=200, help_text='Yes django music lol')
    correct = models.IntegerField(choices=option_list, help_text='correct answer :p')
    feedback = models.CharField(max_length=200, help_text='everythin')
    theme = models.ForeignKey(Theme)

    def __unicode__(self):
        return self.question


class User(models.Model):
    thumbnail = models.ImageField(upload_to='media/user_imgs/', default='media/course_imgs/None/no-img.jpg', null=True)
    username = models.CharField(max_length=45, help_text='for example carlos.bedoy@gmail.com')
    password = models.CharField(max_length=45, help_text='nomeacuerdo password')
    first_name = models.CharField(max_length=45, help_text='yesica', null=True)
    last_name = models.CharField(max_length=45, help_text='martinez', null=True)
    facebook = models.CharField(max_length=100, null=True, help_text='carlos.bedoy')
    twitter = models.CharField(max_length=100, null=True, help_text='@carlos_bedoy')
    age = models.IntegerField(help_text='you age lol', null=True)
    points = models.FloatField(help_text='how many points')
    plays = models.IntegerField(help_text='you are junior?')

    def __unicode__(self):
        return self.username


class Statistics(models.Model):
    level = models.IntegerField(help_text='quantity of questions')
    correct = models.IntegerField(help_text='number of corrects :D')
    wrongs = models.IntegerField(help_text='wrongs :(')
    points = models.FloatField(help_text='number of points')
    date = models.DateField(help_text='date created')
    player = models.ForeignKey(User)
    unicode(date)

    def __unicode__(self):
        return unicode(self.date)




