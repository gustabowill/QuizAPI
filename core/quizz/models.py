from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Quizz(models.Model):
    cateogry = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default=_('New Quizz'),verbose_name=_('Quizz Title'))
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quizz'
        verbose_name_plural = 'Quizzes'
        ordering = ['id']

    def __str__(self):
        return self.title

class Update(models.Model):
    date_updated = models.DateField(verbose_name=_('Last Updated'), auto_now_add=True)

    class Meta:
        abstract = True

class Question(Update):
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermidiate')),
        (3, _('Advanced')),
        (4, _('Expert'))
    )

    TYPE = (
        (0, _('Multiple Choices')),
    )


    quizz = models.ForeignKey(Quizz, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250, verbose_name=_('Title'))
    question_type = models.IntegerField(choices=TYPE, verbose_name=_('Type of question'))
    difficulty = models.IntegerField(choices=SCALE, verbose_name=_('Question Difficulty'))
    date_created = models.DateField(auto_now_add=True, verbose_name=_('Date Created'))
    is_active = models.BooleanField(default=False, verbose_name=_('Active status'))

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    def __str__(self):
        return self.title

class Answer(Update):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=250, verbose_name=_('Answer Text'))
    is_right = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ['id']

    def __str__(self):
        return self.answer_text