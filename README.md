# 数据库原理实验大作业

该仓库用于存放数据库原理实验大作业代码

---



## 使用

1. 若还无该项目文件，使用git clone命令将该仓库克隆到本地；
2. 在命令行或任意可以执行sql语句的编译器执行如下sql语句：

```sql
CREATE USER 'admin'@'%' identified by '123456';
grant all privileges on studentxj.* to 'admin'@'%';
flush privileges;
```

执行该语句的原因是由于支付不起云数据库，在本地编写数据库时，运行studentxj库需要该用户权限。

3. 创建studentxj库（名字必须相同），并把数据库备份文件目录下的studentxj.sql导入其中；

4. 双击执行可执行文件目录下的学生学籍管理系统.exe；
5. 在登录界面输入id为admin，密码为123456，或者输入id为root，密码为自己本地数据库连接的密码即可；
6. 后续使用依照界面指示进行即可。

## 版本管理

git

## 语言

python+sql

## 开发工具

vscode+pycharm

## 源代码

源代码存于src目录下，若要进行阅读，推荐使用vscode或pycharm打开src文件夹