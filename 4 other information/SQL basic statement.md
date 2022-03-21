# SQL Syntax

The aim of this file is to summary the SQL basic syntax, which could remind us for quick checking.

## **Common sense**
- Case insensitive: `select` same with `Select`
- Comments: `/* */` , `--` , `#`
- Line split: `;`
- 

## **Major commands**
| Commands | How to use | Other Syntax |
| ----------- | ----------- | ------ |
| `select` | `select` * `from` table_name `WHERE` condition | `distinct` , `top` , `count`, `sum`, `group by` , `order by` |
| `select into` | `SELECT` * `INTO` CustomersGermany `FROM` Customers `WHERE` Country = 'Germany'; | copies data from one table into a new table|
| `insert into` | `INSERT INTO` table_name (column1, column2, column3, …) `VALUES` (value1, value2, value3, …)| |
| `insert into select` | `INSERT INTO` table2 `SELECT` * `FROM` table1 `WHERE` condition;| copies data from one table and inserts it into another table |
| `update` | `UPDATE` table_name `SET` column1 = value1, column2 = value2, … `WHERE` condition |  |
| `delete` | `DELETE FROM` table_name `WHERE` condition | |
| `create` | `CREATE TABLE` table_name (name VARCHAR(255) `PRIMARY KEY`, address VARCHAR(255)) |`PRIMARY KEY` , see more about data types and constraints |
| `drop` | `DROP TABLE` Shippers | drops the existing table "Shippers"|
| `truncate` | `TRUNCATE TABLE` Shippers | delete the data inside a table, but not the table itself|
| `alter` | `ALTER TABLE` Customers `ADD` Email varchar(255);` | add, delete, or modify columns in an existing table.|

## **Condition commands**
- Condition commands always follow to the `where`  or `having` clause.
 
| operators | Operation | Operation |
| ----------- | ----------- | ----------- |
| `=` | Equal | `WHERE` column1 = value1 |
| `>`, `>=` | Greater than, Greater than or equal | `WHERE` column1 > value1 |
| `<`, `<=` | Less than, less than or equal | `WHERE` column1 < value1 |
| `<>`, `!=` | Not equal | `WHERE` column1 <> value1 |
| `is null` , `is not null` | To get the NULL values | `WHERE` column1 `is null` |
| `between` | Between a certain range | `WHERE` column_name `BETWEEN` value1 `AND` value2 |
| `like` | Search for a pattern (see detailed **Wildcard**) | `WHERE` CustomerName `LIKE` '_r%' |
| `and`, `or` | filter records based on more than one condition | `WHERE` condition1 `and` condition2 |
| `not` | To specify multiple possible values for a column | `WHERE` `not` column1 = value1 |
| `in` | To specify multiple possible values for a column | `WHERE` column_name `IN` (value1, value2, ...); `WHERE` column_name `IN` (`SELECT` statement) |
| `exists` | To test for the existence of any record in a subquery | `WHERE EXISTS` (`SELECT` column_name `FROM` table_name `WHERE` condition) |
| `all` , `any` | To perform a comparison between a single column value and a range of other values | `WHERE` ProductID = `ANY` (`SELECT` ProductID `FROM` orderDetails `WHERE` Quantity = 10) |


## **`Join` and `union` clause**
Here are the different types of the `JOIN`s in SQL:

- `(INNER) JOIN`: Returns records that have matching values in both tables
- `LEFT (OUTER) JOIN`: Returns all records from the left table, and the matched  records from the right table
- `RIGHT (OUTER) JOIN`: Returns all records from the right table, and the matched records from the left table
- `FULL (OUTER) JOIN`: Returns all records when there is a match in either left or right table
  
```
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```
```
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City
ORDER BY A.City;
```
`Union` , `union all`: combine the result-set of two or more SELECT statements
- Every `SELECT` statement within `UNION` must have the same number of columns
- The columns must also have similar data types
- The columns in every `SELECT` statement must also be in the same order

```
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

## **`Group by` clause**
The `GROUP BY` statement is often used with aggregate functions (`COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`) to group the result-set by one or more columns.
```
SELECT COUNT(CustomerID) as num, Country
FROM Customers
GROUP BY Country
ORDER BY num;
```
The `HAVING` clause was used to aggregate functions.
```
SELECT COUNT(CustomerID), Country
FROM Customers
WHERE Country = 'USA' or Country = 'UK'
GROUP BY Country
HAVING COUNT(CustomerID) > 5
ORDER BY COUNT(CustomerID) DESC;
```
## **`CASE` clause**
The `CASE` statement goes through conditions and returns a value when the first  condition is met (like an if-then-else statement). 
```
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;
```
```
SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;
```
## **Constraints**
| Constraints | Description |
| ----------- | ----------- |
| `NOT NULL` | Ensures that a column cannot have a NULL value |
| `UNIQUE` | Ensures that all values in a column are different |
| `PRIMARY KEY`| A combination of a `NOT NULL` and `UNIQUE`. Uniquely identifies each row in a table |
| `FOREIGN KEY` | Prevents actions that would destroy links between tables |
| `CHECK`| Ensures that the values in a column satisfies a specific condition |
| `DEFAULT`| Sets a default value for a column if no value is specified |
| `CREATE INDEX` | Used to create and retrieve data from the database very quickly |

```
CREATE TABLE Orders (
    OrderID int NOT NULL AUTO_INCREMENT,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
```
## **View**
A view is a virtual table based on the result-set of an SQL statement.
```
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```


## **Stored procedure**
A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.
### Stored Procedure Syntax
```
CREATE PROCEDURE procedure_name
AS
sql_statement
GO;
```
### Execute a Stored Procedure
```
EXEC procedure_name;
```