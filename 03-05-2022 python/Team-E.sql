create database ITCOMPANIES;

USE ITCOMPANIES
;

create table service
(
Cname varchar(50) ,
Services varchar(500),
price varchar(50) default 'Not Available'
);
drop table service;

select * from service;
rollback;

insert into service values
('Wipro','Data, Analytics',default),
('Wipro','AI Applications',default),
('Wipro','Digital Operations and Platform',default),
('Wipro','Consulting',default),
('Wipro','Infrastructure Services',default),
('TCS','Analytics and Insights',default),
('TCS','Automation & AI',default),
('TCS','Blockchain',default),
('TCS','Cloud',default),
('TCS','Cognitive Business Operations',default),
('TCS','Consulting',default),
('TCS','Cyber Security',default),
('TCS','Enterprise Applications',default),
('TCS','IOT & Digital Engineering',default),
('TCS','Quality Engineering',default),
('TCS','TCS Interactive',default),
('TCS','Sustainability Service',default),
('IBM','Analytics',default),
('IBM','Application Services',default),
('IBM','AI',default),
('IBM','Block Chain',default),
('IBM','Cloud Computing',default),('IBM','IT Infrastructure',default),
('IBM','Hybrid Cloud',default),
('IBM','Cyber Security',default),
('IBM','E-Commerce',default),
('Accenture','Application Services',default),
('Accenture','Artificial Intelligence',default),
('Accenture','Automation',default),
('Accenture','Business Process Outsourcing',default),
('Accenture','Business Strategy',default),
('Accenture','Change Management',default),
('Accenture','Cloud',default),
('Accenture','Customer Experience',default),
('Accenture','Data & Analytics',default),
('Accenture','Digital Commerce',default),
('Accenture','Digital Engineering & Manufacturing',default),
('Accenture','Ecosystem Services',default),
('Accenture','Finance Consulting',default),
('Accenture','Infrastructure',default),
('Accenture','Marketing',default),
('Accenture','Mergers & Acquisitions (M&A)',default),
('Accenture','Metaverse',default),
('Accenture','Operating Models',default),
('Accenture','Security',default),
('Accenture','Supply Chain Management',default),
('Accenture','Sustainability',default),
('Accenture','Technology Consulting',default),
('Accenture','Technology Innovation',default),
('Accenture','Zero Based Budgeting (ZBB)',default)
;

CREATE TABLE company
(Cname varchar(50) primary key,
CEO varchar(50),
Founder varchar(50),
HeadQuarters varchar(50),
Contact int,
Email varchar(30),
Branches varchar(100),
EST int,
EmployeeStrength int,
Address varchar(250),
Revenue int,
About varchar(500)
)
;