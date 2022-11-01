-- Question 1

create table city_master
(id int primary key,
city_name varchar(22),
city_state varchar(25),
added_date date)


-- create user_master table
create table user_master
(id int primary key,
name varchar(30),
contact_number bigint,
email_id varchar(20),
blood_group varchar(10),
city_id int,
FOREIGN KEY (city_id) REFERENCES city_master(id));
