from django.db import models
import datetime


class Question(models.Model):

    title = models.CharField(max_length=200, verbose_name="Вопрос")
    date_published = models.DateTimeField(verbose_name="Дата", default=datetime.datetime.now)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос с выбором ответа'
        verbose_name_plural = 'Вопросы с выбором ответа'


class Answer(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False, blank=True, verbose_name='')
    answer = models.CharField(max_length=200, verbose_name="Ответ")
    votes = models.IntegerField(verbose_name="Голосов", default=0)

    def __unicode__(self):
        return self.answer

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class QuestionText(models.Model):
    title = models.CharField(max_length=200, verbose_name="Вопрос")
    date_published = models.DateTimeField(verbose_name="Дата", default=datetime.datetime.now)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос ответ текстом'
        verbose_name_plural = 'Вопросы ответ текстом'


class Text(models.Model):
    question_id = models.ForeignKey(QuestionText, on_delete=models.CASCADE)
    answer = models.TextField(verbose_name="Ответ")

    def __unicode__(self):
        return self.answer

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ текстом'
        verbose_name_plural = 'Ответы текстом'

