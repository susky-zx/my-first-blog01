from django.db import models
from django.utils import timezone


# 所有以from或import开始的所有行，都是需要从其他文件中添加一些内容。
# 所以与其复制和粘贴同样的内容，我们可以用form....import....来导入这些文件

# Create your models here.
class Post(models.Model):
    # 用来定义一个模型（这是一个对象）
    # class是一个特殊关键字，表明我们在定义一个对象
    # post是我们模型的名字
    # models.Model 表明Post是一个Django模型，所以Django知道它应该保存在数据库中

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 指向另一个模型的连接
    title = models.CharField(max_length=200)
    # 如何用为数有限的字符来定义一个文本
    text = models.TextField()
    # 没有长度限制的长文本，用在博客的内容上
    created_date = models.DateTimeField(default=timezone.now)
    # 日期和时间
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # def表示一个函数或者方法 publish是这个方法的名字（命名规则是小写字母及下划线）
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        # 返回文本标题
