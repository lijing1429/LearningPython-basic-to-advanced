-- '''database manipulate'''
/* show databases; */
/* create database Hud_ASIS;
create database Hud_BS;
create database Hud_Plan; */
/* drop database brightspace;
drop database asis; */



/* show databases;
show tables in mevaluation; */
/* select * from mevaluation.module_result; */
/* create table mevaluation.test (id int primary key, information varchar(255)); */
/* insert into mevaluation.module_result (SPRcode,candidaNumber,studentMarks) values ('1234580980', ' ',80); */
/* update mevaluation.module_result set SPRcode = '798915641' where studentMarks = 80; */
/* drop tables mevaluation.test; */
/* drop database sakila; */
/* select * from mevaluation.module_result where studentMarks in (select max(studentMarks) from mevaluation.module_result); */
/* select * from mevaluation.module_result where candidaNumber is not null; */
/* select * from mevaluation.module_result where studentMarks limit 3; */
/* /* select * from mevaluation.users; */
select * from Hud_BS.users; 
/* CREATE PROCEDURE mevaluation.Moduleresult @SPRcode nvarchar(30)
AS
SELECT * FROM mevaluation.module_result WHERE SPRcode = @SPRcode
GO;
EXEC Moduleresult @SPRcode = '123458'; */