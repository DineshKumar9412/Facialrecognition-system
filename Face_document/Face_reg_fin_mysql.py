MYSQL database and table details

MySQL connectivity in terminal

step 1

ssh troondxadmin@129.151.44.205 -p22

step 2

TrdX@dM!!9#4132$

step 3

sudo mysql -u oasys  -p

TrdX@dM!!9#4132$

mysql password:Oasys@123!*

step 4

show databases;

           aimp_sep_2021            - Not  use

           information_schema  - default

           mysql                                - default

           oasys                                 - Using face recognition

           performance_schema - default

            sys                                      -default

use oasys;

show tables;

          login           - using face recognition login api

          report        -testing face recognition 

           test            -using face recognition checkin and checkout api

           train_2017- using oasys_viz for duckdb 

           traincsv       - using oasys-viz 

Create Table query

create table login (name VARCHAR(255),id int(255),password int (255),endroll int (255));

Add one column query

ALTER TABLE  login ADD COLUMN Email VARCHAR(255);

Drop single column query

ALTER TABLE login  DROP COLUMN name;

Empty table query

truncate table dly_login;

Insert query

INSERT INTO login(name,id,password,endroll) values ('Raja',1716,1716,0);

INSERT INTO test values ('Raja',1716,1716,0);

Update one row query

UPDATE login SET endroll=0 WHERE id=1719;

All rows value changed in particular column query

UPDATE login SET endroll=0 WHERE endroll=1 AND !isnull (IDCOLUMN)

Delete one row values query

DELETE FROM dly_login WHERE id=1718;

Delete one column query

ALTER TABLE login DROP COLUMN Age;

updates column types in table 

ALTER TABLE test Modify column break TIMESTAMP;

Time calculate total break time

SELECT  SEC_TO_TIME( SUM( TIME_TO_SEC(break ) ) ) AS totaltime FROM test WHERE id = 1717;

Show table query

select * from test;

show one particular employee

SELECT * FROM login WHERE id = 1717";

