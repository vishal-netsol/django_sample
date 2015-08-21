from django.db import models

# Create your models here.

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    sb = []
    for key in self.__dict__:
      if key != '_state':
        sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))
 
    return ', '.join(sb)

  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  question = models.ForeignKey(Question)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    sb = []
    for key in self.__dict__:
      if key != '_question_cache' and key != '_state':
        sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))
 
    return ', '.join(sb)

class User(models.Model):
  email = models.EmailField()
  username = models.CharField(max_length=20)

  def __str__(self):
    sb = []
    for key in self.__dict__:
      if key != '_state':
        sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))
 
    return ', '.join(sb)


class UserDetail(models.Model):
  user = models.OneToOneField(User)
  address = models.CharField(max_length=500)

  def __str__(self):
    sb = []
    for key in self.__dict__:
      if key != '_user_cache' and key != '_state':
        sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))
 
    return ', '.join(sb)

class Contact(models.Model):
  users = models.ManyToManyField(User)
  email = models.EmailField()
  name = models.CharField(max_length=50)

  def __str__(self):
    sb = []
    for key in self.__dict__:
      if key != '_user_cache' and key != '_state':
        sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))
 
    return ', '.join(sb)
