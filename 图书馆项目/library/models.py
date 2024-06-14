from django.db import models

# Create your models here.
'''
创建一个项目，用来说明出版社，书籍和作者的关系。
假定关系：作者：书籍 =>1:n（一本书由一个作者完成，一个作者可以创作多本书）
出版社：书籍 >n:n（一个出版社可以出版多本书，一本书可以由多个出版社出版）
要求：
1. 在书籍的book_index.htm1中有一个"查看所有书籍”的超链接按钮，点击进入书籍列表book_1ist.html页面.
2.在书籍的book_1ist.htm1中显示所有书名，点击书名可以进入书籍详情book_detail.htm1（通过书籍id）
3.在书籍book_detail.htm1中可以点击该书的作者和出版社，
进入作者详情的author_detai1.htm1和出版社详情的publisher_detai1.html页面
'''

class Author(models.Model):
    name = models.CharField(max_length=50,unique=True,primary_key=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publisher = models.ManyToManyField('Publisher', related_name='publisher')

    def __str__(self):
        return f'title: {self.title}, authors: {self.author}, publishers: {self.publisher}'

