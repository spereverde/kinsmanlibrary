import datetime

from django.db import models
from django.utils import timezone

class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateTimeField('date of birth')

	def __str__(self):
		name = '{} {}'.format(self.first_name, self.last_name)
		return name

	def was_born_recently(self):
		return self.date_of_birth >= timezone.now() - datetime.timedelta(days=1)

class Book(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	book_title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.book_title
