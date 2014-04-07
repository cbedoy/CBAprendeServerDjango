from django.db import models

# Create your models here.

class question(models.Model):
    option_list = (
        (1, 'A)'),
        (2, 'B)'),
        (3, 'C)'),
        (4, 'D)'),
    )
    question = models.TextField(max_length=250, help_text='Are you developer')
    answer1 = models.TextField(max_length=200, help_text='YES')
    answer2 = models.TextField(max_length=200, help_text='maybe')
    answer3 = models.TextField(max_length=200, help_text='why?')
    answer4 = models.TextField(max_length=200, help_text='Yes django music lol')
    correct = models.IntegerField(choices=option_list, help_text='correct answer :p')
    feedback = models.TextField(max_length=200, help_text='everythin')
    source = models.ImageField(upload_to='sources', help_text='image resource for examen', null=True)

    def __unicode__(self):
        return self.question


class course(models.Model):
    name = models.CharField(max_length=45, help_text='name of course')
    image = models.ImageField(upload_to='courses_image', null=True, help_text='image of course')

    def __unicode__(self):
        return self.name


class theme(models.Model):
    name = models.CharField(max_length=50, help_text='Algorithms')
    description = models.TextField(max_length=100, help_text='short description about theme')
    course = models.ForeignKey(course)

    def __unicode__(self):
        return self.name


class stadistics(models.Model):
    level = models.IntegerField(help_text='quantity of questions')
    correct = models.IntegerField(help_text='number of corrects :D')
    wrongs = models.IntegerField(help_text='wrongs :(')
    points = models.FloatField(help_text='number of points')
    date = models.DateField(help_text='date created')
    unicode(date)

    def __unicode__(self):
        return self._get_pk_val + ' -> ' + self.date


class user(models.Model):
    username = models.CharField(max_length=45, help_text='for example carlos.bedoy@gmail.com')
    password = models.CharField(max_length=45, help_text='nomeacuerdo password')
    first_name = models.CharField(max_length=45, help_text='yesica')
    last_name = models.CharField(max_length=45, help_text='martinez')
    birthday = models.DateField(help_text='your birthday is important')
    image = models.ImageField(upload_to='user_images', help_text='selfie :v')
    age = models.IntegerField(help_text='you age lol')
    points = models.FloatField(help_text='how many points')
    plays = models.IntegerField(help_text='you are junior?')
    unicode(birthday)

    def __unicode__(self):
        return self.username




