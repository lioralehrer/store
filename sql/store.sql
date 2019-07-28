create database store;
use store;
create table categories(
id  int not null auto_increment primary key,
name varchar(50)
);
INSERT INTO categories VALUES (null,'novel');
create table products(
id int not null auto_increment primary key,
category int not null,
description varchar(100),
price float not null,
title  varchar(30) not null,
favorite int(5),
img_url varchar(300),
foreign key (category)
	references categories (id)
    on update cascade
    on delete restrict
);
INSERT INTO products VALUES (null,1,'Alber Kamie most popular book',60.4,'Hadever',1,'hadever.jpg');
select * from products;	 



