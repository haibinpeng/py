select VERSION();

select now();

show databases;

show tables;

# 查看当前使用的数据库
select database();

# 创建数据库
create database demo charset='utf8';

# 查看数据库信息
show create database demo;

# 删除数据库
drop database demo;

# 查看当前数据库中所有的表
show tables;

# 查看表结构
desc student;
show create table student;

# 删除表
drop table student;

# -------------------DDL------------------

# 创建表
create table classes(id int unsigned auto_increment primary key not null,name varchar(10));
desc classes;
create table student(id int unsigned auto_increment primary key not null,name varchar(20) default '',
age tinyint unsigned default 0,height decimal(6,2),gender enum('男','女','中性','保密'),cls_id int unsigned default 0);
desc student;
show create table student;

# 修改表-添加字段
# alter table 表名 add 列名 类型
alter table student add birthday date;

# 修改表-修改字段：重命名版
# alter table 表名 change 原名 新名 类型及约束
alter table student change birthday birth date not null;

# 修改表-修改字段：不重命名版
# alter table 表名 modify 列名 类型及约束
alter table student modify birth datetime;

# -------------------DQL DML------------------

# 查询所有列
select * from classes;
select id,name from classes;
select * from student;

# 插入数据
# insert into 表名 values(...)
insert into classes values(0,'python5');
insert into classes values(0,'python6');
select * from classes;
# 枚举插入时，放的是1,2,3,4...
insert into student(id, name, age, height, gender, cls_id, birth) values(0,'郭靖',20,181,1,1,'2002-6-24');
select * from student;
insert into student(name,age) values('黄蓉',18);
# 一次插入多条数据
insert into classes values(0,'python1'),(0,'python2');
insert into student(name) values('杨康'),('杨过'),('小龙女');

# update 表名 set 列1=值1,列2=值2...where 条件
update student set birth='1998-3-5' where name='小龙女';

# delete from table_name [where 条件判断]
delete from student where id=4;

# 查询练习
drop table student;
create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','中性','保密') default '保密',
    cls_id int unsigned default 0,
    is_delete bit default 0
);
INSERT INTO students(name,age,height,gender,cls_id,is_delete)
VALUES
	( '小明', 18, 180.00, 2, 1, 0 ),
	( '小月月', 18, 180.00, 2, 2, 1 ),
	( '彭于晏', 29, 185.00, 1, 1, 0 ),
	( '刘德华', 59, 175.00, 1, 2, 1 ),
	( '黄蓉', 38, 160.00, 2, 1, 0 ),
	( '凤姐', 28, 150.00, 4, 2, 1 ),
	( '王祖贤', 18, 172.00, 2, 1, 1 ),
	( '周杰伦', 36, NULL, 1, 1, 0 ),
	( '程坤', 27, 181.00, 1, 2, 0 ),
	( '刘亦菲', 25, 166.00, 2, 2, 0 ),
	( '金星', 33, 162.00, 3, 3, 1 ),
	( '静香', 12, 180.00, 2, 4, 0 ),
	( '郭靖', 12, 170.00, 1, 4, 0 ),
	( '周杰', 34, 176.00, 2, 5, 0 );
select * from students;
# 截断表
truncate table classes;
# 截断表后再插入数据，会重新开始编号
insert into classes values (0, "python_01期"), (0, "python_02期");
# as
select id as `序号`,name as `姓名` from students;
select s.name,s.age from students s;
# 去重
select distinct age from students;
# 比较运算符
select * from students where id > 3;
select * from students where id <= 4;
select * from students where name != '黄蓉';
select * from students where is_delete = 0;
# 逻辑运算符
select * from students where id > 3 and gender=2;
select * from students where id < 4 or is_delete=0;
# 模糊查询
# 查询姓小的学生
select * from students where name like '小%';
# 查询姓小并且“名”是一个字的学生
select * from students where name like '小_';
# 范围查询
# in表示在一个非连续的范围内
select * from students where id in(1,3,8);
# between and
select * from students where id between 3 and 8;
select * from students where id between 3 and 8 and gender=1;
# 判空 is NULL
select * from students where height is NULL;
# 判非空 is not NULL
select * from students where height is not NULL;
select * from students where height is not NULL and gender=1;
# 排序:order by 默认升序
# 查询未删除的男生信息，按学号降序
select * from students where gender=1 and is_delete=0 order by id desc;
# 查询未删除学生信息，按名称升序
select * from students where is_delete=0 order by name;
# 显示所有的学生信息，先按照年龄从大-->小排序，当年龄相同时 按照身高从高-->矮排序
select * from students order by age desc,height desc;
# 聚合
# 查询学生总数
select count(*) from students;
# 查询女生的最大年龄
select max(age) from students where gender=2;
# 查询未删除的学生的最小编号
select min(id) from students where is_delete=0;
# 查询男生的总年龄
select sum(age) from students where gender=1;
# 查询未删除女生的平均年龄
select avg(age) from students where is_delete=0 and gender=2;
# 分组
# 每个性别的人数
select gender,count(*) from students group by gender;
# 每个性别的平均年龄
select gender,avg(age) from students group by gender;
# 身高不为空的人，不同性别的平均身高
select gender,avg(height) as avg_height from students where height is not null group by gender order by avg_height;
# group_concat
select gender,group_concat(name) from students group by gender;
# group by 后产生的字段再过滤，需要用having
select gender,count(*) as gender_num from students group by gender having gender_num >= 2;
# with rollup:在最后新增一行，来记录当前列里记录的总和
select gender,count(*) as gender_num from students group by gender with rollup;
select gender,group_concat(age) from students group by gender with rollup;
# 窗口函数
select *,rank() over (partition by cls_id order by age desc) as rank1,
        dense_rank() over (partition by cls_id order by age desc) as dese_rank,
		row_number() over (partition by cls_id order by age desc) as row_num from students;
select *,rank() over (order by age desc) as rank1,
		dense_rank() over (order by age desc) as dese_rank,
		row_number() over (order by age desc) as row_num  from students;
# 获得部分行
# select*from 表名 limit start，count：start开始，获取count条数据，最上面一行是第0行
# 查询前3行男生信息
select * from students where gender=1 limit 0,3;
select * from students where gender=1 limit 1,3;