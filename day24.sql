# 求第n页的数据
select * from students limit 5,5;

# 假如每页显示5条数据，计算总页数，并查出第2页的数据
select count(*)/5 from students;  # 3页
select * from students limit 5,5;

# 关联查询
# 内连接
select * from students s inner join classes c on s.cls_id = c.id;
# 左连接
select  * from students s left join classes c on s.cls_id = c.id;
# 右连接
select  * from students s right join classes c on s.cls_id = c.id;

# 自关联
create table areas(
    aid int primary key,
    atitle varchar(100),
    pid int
);
select count(*) from areas where pid is null;
select * from areas where atitle='山西省';
# 查询省的名称为“山西省”的所有城市
select c.aid,c.atitle,p.atitle from areas c inner join areas p on c.pid=p.aid where p.atitle='山西省';
# 查询市的名称为“广州市”的所有区县
select c.aid,c.atitle,p.atitle from areas c inner join areas p on c.pid =p.aid where p.atitle='深圳市';

# 子查询
# 标量子查询
# 查询班级哪些学生的身高大于平均身高
select * from students where height > (select avg(height) from students);
# 列级子查询
# 查询还有学生在班的所有班级名字
select * from classes where id in (select distinct cls_id from students);
# 行级子查询
# 查找班级年龄最大，身高最高的学生
select * from students where(height, age)=(select max(height), max(age) from students);


# 创建一个商品goods数据表
create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(150) not null,
    cate_name varchar(40) not null,
    brand_name varchar(40) not null,
    price decimal(10,3) not null default 0,
    is_show bit not null default 1,
    is_saleoff bit not null default 0
);

# 向goods表中插入数据
insert into goods values(0,'r510vc 15.6英寸笔记本','笔记本','华硕','3399',default,default);
insert into goods values(0,'y400n 14.0英寸笔记本电脑','笔记本','联想','4999',default,default);
insert into goods values(0,'g150th 15.6英寸游戏本','游戏本','雷神','8499',default,default);
insert into goods values(0,'x550cc 15.6英寸笔记本','笔记本','华硕','2799',default,default);
insert into goods values(0,'x240 超极本','超级本','联想','4880',default,default);
insert into goods values(0,'u330p 13.3英寸超极本','超级本','联想','4299',default,default);
insert into goods values(0,'svp13226scb 触控超极本','超级本','索尼','7999',default,default);
insert into goods values(0,'ipad mini 7.9英寸平板电脑','平板电脑','苹果','1998',default,default);
insert into goods values(0,'ipad air 9.7英寸平板电脑','平板电脑','苹果','3388',default,default);
insert into goods values(0,'ipad mini 配备 retina 显示屏','平板电脑','苹果','2788',default,default);
insert into goods values(0,'ideacentre c340 20英寸一体电脑 ','台式机','联想','3499',default,default);
insert into goods values(0,'vostro 3800-r1206 台式电脑','台式机','戴尔','2899',default,default);
insert into goods values(0,'imac me086ch/a 21.5英寸一体电脑','台式机','苹果','9188',default,default);
insert into goods values(0,'at7-7414lp 台式电脑 linux ）','台式机','宏碁','3699',default,default);
insert into goods values(0,'z220sff f4f06pa工作站','服务器/工作站','惠普','4288',default,default);
insert into goods values(0,'poweredge ii服务器','服务器/工作站','戴尔','5388',default,default);
insert into goods values(0,'mac pro专业级台式电脑','服务器/工作站','苹果','28888',default,default);
insert into goods values(0,'hmz-t3w 头戴显示设备','笔记本配件','索尼','6999',default,default);
insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default);
insert into goods values(0,'x3250 m4机架式服务器','服务器/工作站','ibm','6888',default,default);
insert into goods values(0,'商务双肩背包','笔记本配件','索尼','99',default,default);

# 查询类型cate_name为’超极本’的商品名称、价格
select name, price from goods where cate_name='超级本';
# 显示商品的种类
select cate_name from goods group by cate_name;
# 求所有电脑产品的平均价格,并且保留两位小数
select round(avg(price), 2) as avg_price from goods;
# 显示每种商品的平均价格
select cate_name, avg(price) from goods group by cate_name;
# 查询每种类型的商品中最贵、最便宜、平均价、数量
select cate_name, max(price), min(price), avg(price), count(*) from goods group by cate_name;
# 查询所有价格大于平均价格的商品，并且按价格降序排序
select id, name, price from goods where price>(select round(avg(price), 2) as avg_price from goods) order by price desc;
# 查询每种类型中最贵的电脑信息
select g.* from goods g inner join
(select
        cate_name,
        max(price) as max_price,
        min(price) as min_price,
        avg(price) as avg_price,
        count(*) from goods group by cate_name) r on g.cate_name=r.cate_name and g.price=r.max_price;

# 创建商品分类表
create table if not exists goods_cates(
    id int unsigned primary key auto_increment,
    name varchar(40) not null
);

# 查询goods表中商品的种类
select cate_name from goods group by cate_name;

# 将分组结果写入到goods_cates数据表
insert into goods_cates(name) select cate_name from goods group by cate_name;

# 通过goods_cates数据表来更新goods表
update goods g inner join goods_cates c on g.cate_name=c.name set g.cate_name=c.id;

desc goods;

# 在创建数据表的时候一起插入数据
create table goods_brands (
    id int unsigned primary key auto_increment,
    name varchar(40) not null) select brand_name as name from goods
    group by brand_name;

# 通过goods_brands数据表来更新goods数据表
update goods as g inner join goods_brands gb on g.brand_name = gb.name set g.brand_name=gb.id;

# 通过alter table语句修改表结构
alter table goods
change cate_name cate_id int unsigned not null,
change brand_name brand_id int unsigned not null;