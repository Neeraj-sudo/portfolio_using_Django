from django.db import models

# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	technology = models.CharField(max_length=20)
	#image = models.FilePathField(path="/img")
	image = models.ImageField(upload_to='images/')


class About(models.Model):
	name = models.CharField(max_length=100)
	bio = models.TextField()
	#profile_pic = models.FilePathField(path="/img")
	profile_pic = models.ImageField(upload_to='images/')
	linkedin_url = models.URLField(max_length = 200, default='SOME STRING') 
	email = models.EmailField(max_length = 254, default='mandare.neeraj5@gmail.com')
	address = models.TextField(default='SOME STRING')



class Education(models.Model):
	school = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	pass_year = models.DateField()



class Skills(models.Model):
	skill = models.CharField(max_length=100)


class Certification(models.Model):
	course = models.CharField(max_length=100)
	desc = models.TextField()
	certi = models.ImageField(upload_to='images/', default='media/images/sentiment.jpg')


class Work_experience(models.Model):
	company = models.CharField(max_length=100)
	task = models.TextField()
		