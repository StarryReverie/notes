---
tags:
	- computer-science
	- database
---
- **数据定义**
	- **模式**
		- **定义**
			- ```sql
			  CREATE SCHEMA [<schema-name>] AUTHORIZATION <username>
			  [<table-definition-clause>]
			  [<view-definition-clause>]
			  [<authorization-definition-clause>];
			  ```
			- 如果没有提供模式名，则默认使用用户名。
		- **删除**
			- ```sql
			  DROP SCHEMA <schema-name> CASCADE|RESTRICT
			  ```
			- 使用 `CASCADE` 时，同时删除模式和模式下的基本表、视图等对象。
			- 使用 `RESTRICT` 时，若模式下仍有对象，则报错。
	- **基本表**
		- **定义**
			- ```sql
			  CREATE TABLE [<table-name>] (
			      <column-name> <type> <column-constraint>,
			      ...,
			      <table-constraint>
			  );
			  ```
			- 主要列级完整性约束：`PRIMARY KEY`、`UNIQUE`、`NOT NULL`。
			- 主要表级完整性约束：
				- 联合主键：`PRIMARY KEY (<attribute1>, <attribute2>, ...>)`。
				- 外键：`FOREIGN KEY (<foreign-key>) REFERENCES <referenced-table>(<primary-key>)`。
			- 建表时，默认将表加入到当前的模式下。可以使用 `<schema-name>.<table-name>` 来指定模式。
		- **修改**
			- ```sql
			  ALTER TABLE <table-name>
			  [ADD [COLUMN] <column-name> <type> <column-constraint>]
			  [ADD <column-constraint>(<column-name>)]
			  [ADD <table-constraint>]
			  [DROP [COLUMN] <table-name> CASCADE|RESTRICT]
			  [DROP CONSTRAINT <constraint-name> CASCADE|RESTRICT]
			  [ALTER COLUMN <column-name> <type>];
			  ```
		- **删除**
			- ```sql
			  DROP TABLE <table-name> CASCADE|RESTRICT;
			  ```
	- **索引**
		- **定义**
			- ```sql
			  CREATE [UNIQUE] [CLUSTER] INDEX <index-name>
			  ON <table-name>(<column-name> [ASC|DESC], ...);
			  ```
			- `UNIQUE` 表示唯一索引，要求对应列中的取值唯一。
			- `CLUSTER` 表示聚簇索引，索引中元组的顺序与储存的顺序一致。
			- `ASC` 和 `DESC` 为索引值的排序，默认为升序。
		- **修改**
			- ```sql
			  ALTER INDEX <index-name> RENAME TO <new-index-name>;
			  ```
		- **删除**
			- ```sql
			  DROP INDEX <index-name>;
			  ```
- **数据查询**
	- **通用语法**
		- ```sql
		  SELECT [ALL|DISTINCT] <expression>, ...
		  FROM <table-name>, ... | (<subquery>) [AS] <alias>
		  [WHERE <predicate>]
		  [GROUP BY <column-name> [HAVING <predicate>]]
		  [ORDER BY <column-name>]
		  ```
