from django.db import models


class Account(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    pwd = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    gender = models.BooleanField()
    photo = models.TextField(blank=True, null=True)
    birth = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class Book(models.Model):
    no = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, models.DO_NOTHING)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'book'


class BookTag(models.Model):
    no = models.AutoField(primary_key=True)
    book_no = models.IntegerField()
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'book_tag'
