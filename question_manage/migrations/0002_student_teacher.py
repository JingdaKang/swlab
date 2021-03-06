# Generated by Django 2.2.12 on 2020-05-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=4, verbose_name='性别')),
                ('dept', models.CharField(choices=[('计算机与通信学院', '计算机与通信学院'), ('电气与自动化学院', '电气与自动化学院'), ('外国语学院', '外国语学院'), ('理学院', '理学院')], default=None, max_length=20, verbose_name='学院')),
                ('major', models.CharField(default=None, max_length=20, verbose_name='专业')),
                ('password', models.CharField(default='111', max_length=20, verbose_name='密码')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='邮箱')),
                ('birth', models.DateField(verbose_name='出生日期')),
            ],
            options={
                'verbose_name_plural': '学生',
                'db_table': 'student',
                'verbose_name': '学生',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='教工号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=4, verbose_name='性别')),
                ('dept', models.CharField(choices=[('计算机与通信学院', '计算机与通信学院'), ('电气与自动化学院', '电气与自动化学院'), ('外国语学院', '外国语学院'), ('理学院', '理学院')], default=None, max_length=20, verbose_name='学院')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='邮箱')),
                ('password', models.CharField(default='000000', max_length=20, verbose_name='密码')),
                ('birth', models.DateField(verbose_name='出生日期')),
            ],
            options={
                'verbose_name_plural': '教师',
                'db_table': 'teacher',
                'verbose_name': '教师',
            },
        ),
    ]
