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
/* select * from Hud_BS.bs_login;  */
/* drop table testdata; */
/* SELECT * FROM Hud_BS.bs_login e2 GROUP BY u_UserID,uas_SCE_Course_Code, startime HAVING COUNT(*) > 1 */

/* SELECT * FROM hud_bs.bs_login LIMIT 1000; */
/* select count(*) from Hud_BS.bs_login; 
ALTER TABLE bs_login MODIFY uas_SCE_Course_Code varchar(255); */


ALTER TABLE Hud_BS.bs_login ADD PRIMARY KEY(u_UserID,uas_SCE_Course_Code, startime); */
commit; 
/* ALTER TABLE Hud_BS.users MODIFY startime DATE;
commit; */
/* CREATE PROCEDURE mevaluation.Moduleresult @SPRcode nvarchar(30)
AS
SELECT * FROM mevaluation.module_result WHERE SPRcode = @SPRcode
GO;
EXEC Moduleresult @SPRcode = '123458'; */


/* DELETE e.*FROM Hud_BS.bs_login e WHERE u_UserName IN (select id from (
    SELECT min(u_UserName) as id
          FROM Hud_BS.bs_login e2
          GROUP BY u_UserID,uas_SCE_Course_Code, startime
          HAVING COUNT(*) > 1) f); */