---
title: SQL 语言
weight: 400
math: false
---

- **数据定义**
    - **模式**
        - **定义**
            - ```sql
              CREATE SCHEMA [<schema>] AUTHORIZATION <username>
              [<table-definition-clause>]
              [<view-definition-clause>]
              [<authorization-definition-clause>];
              ```
            - 如果没有提供模式名，则默认使用用户名。
        - **删除**
            - ```sql
              DROP SCHEMA <schema> CASCADE|RESTRICT
              ```
            - 使用 `CASCADE` 时，同时删除模式和模式下的基本表、视图等对象。
            - 使用 `RESTRICT` 时，若模式下仍有对象，则报错。
    - **基本表**
        - **定义**
            - ```sql
              CREATE TABLE [<table>] (
                  <column> <type> <column-constraint>,
                  ...,
                  <table-constraint>
              );
              ```
            - 主要列级完整性约束：`PRIMARY KEY`、`UNIQUE`、`NOT NULL`。
            - 主要表级完整性约束：
                - 联合主键：`PRIMARY KEY (<attribute1>, <attribute2>, ...>)`。
                - 外键：`FOREIGN KEY (<foreign-key>) REFERENCES <referenced-table>(<primary-key>)`。
            - 建表时，默认将表加入到当前的模式下。可以使用 `<schema>.<table>` 来指定模式。
        - **修改**
            - ```sql
              ALTER TABLE <table>
              [ADD [COLUMN] <column> <type> <column-constraint>]
              [ADD <column-constraint>(<column>)]
              [ADD <table-constraint>]
              [DROP [COLUMN] <table> CASCADE|RESTRICT]
              [DROP CONSTRAINT <constraint> CASCADE|RESTRICT]
              [ALTER COLUMN <column> <type>];
              ```
        - **删除**
            - ```sql
              DROP TABLE <table> CASCADE|RESTRICT;
              ```
    - **索引**
        - **定义**
            - ```sql
              CREATE [UNIQUE] [CLUSTER] INDEX <index>
              ON <table>(<column> [ASC|DESC], ...);
              ```
            - `UNIQUE` 表示唯一索引，要求对应列中的取值唯一。
            - `CLUSTER` 表示聚簇索引，索引中元组的顺序与储存的顺序一致。
            - `ASC` 和 `DESC` 为索引值的排序，默认为升序。
        - **修改**
            - ```sql
              ALTER INDEX <index> RENAME TO <new-index>;
              ```
        - **删除**
            - ```sql
              DROP INDEX <index>;
              ```
    - **视图**
    	- a
- **数据查询**
    - **通用语法**
        - ```sql
          SELECT [ALL|DISTINCT] <expression>, ...
          FROM <table-name>|(<subquery>) [AS] <alias>, ...
          [WHERE <predicate>]
          [GROUP BY <column> [HAVING <predicate>]]
          [ORDER BY <column> [ASC|DESC]]
          [[INNER | [LEFT|RIGHT] OUTER] JOIN <table> ON <predicate>];
          ```
    - **单表查询**
        - `ALL|DISTINCT` 表示是否不对结果去重，默认为 `ALL`。
        - `GROUP BY` 子句中使用 `HAVING <predicate>` 筛选分组后的结果。
    - **连接查询**
        - `WHERE` 子句中使用 `[<table1>.]<column1> = [<table2>.]<column2>` 表示等值连接。
    - **嵌套查询**
        - `WHERE` 子句中可以加入子查询。
        - 子查询分为不相关子查询和相关子查询，相关子查询需要对每个依赖的元组依次运行。
        - 使用 `WHERE <attribute> IN (<subquery>)` 筛选属性在子查询中出现的元组，`<subquery>` 仅返回一个属性的投影。
            - 如果子查询返回的关系仅包含一个值，则可以把结果从关系隐式转换为值，使用 `=` 等普通运算符比较。
            - 子查询都在表达式的后半部分，如 `= (<subquery>)`。
        - 使用 `WHERE <attribute> <operator> ANY|ALL (<subquery>)` 从子查询结果中选取其中一个/所有值进行判断。
        - 使用 `WHERE EXISTS (<subquery>)` 筛选子查询有结果的元组。
            - `EXISTS (<subquery>)` 的子查询一般是相关子查询。
            - `WHERE EXISTS (SELECT * FROM ... WHERE <predicate>)` 表示 $\exists x P(x)$ 的语义。
            - `WHERE NOT EXISTS (SELECT * FROM WHERE NOT <predicate>)` 表示 $\forall x P(x)$ 的语义。
    - **集合查询**
        - `UNION`、`INTERSECT`、`MINUS`、`EXCEPT` 表示[集合运算](/notes/docs/mathematics/discrete-mathematics/set#qtjafh)。
        - 只有 `UNION` 是标准的 SQL 操作。
        - 集合运算要求两个关系的元组相同。
        - `<query1> UNION [ALL] <query2>` 将两个查询的结果取并集。
- **数据更新**
	- **插入**
		- ```sql
		  INSERT INTO <table> [(<column1>, <column2>, ...)]
		  VALUES (<value1>, <value2>, ...) | <select-clause>;
		  ```
		- 属性的元组可以与表定义的顺序不同，不强制要求的属性可以省略。
		- 被插入的元组可以是字面的元组，也可以是 `SELECT` 子查询。
		- 无法满足[完整性约束](/notes/docs/computer-science/database/relational-database#masdfo)的元组不会被插入。
	- **修改**
		- ```sql
		  UPDATE <table> SET <colum> = <expression> [WHERE <predicate>];
		  ```
		- 与查询相同，`WHERE` 子句中可以加入子查询。
	- **删除**
		- ```sql
		  DELETE FROM <table> [WHERE <predicate>];
		  ```
- **视图**
	- **定义**
    	- ```sql
    	  CREATE VIEW <view> [<column1>, <column2>, ...]
    	  AS <subquery>
    	  [WITH CHECK OPTION];
    	  ```
		- 视图本身不包括数据，只有在每次查询和更新时，按照子查询获取一定数据。
		- 列名省略时，视图使用子查询中选择的列，列名不省略时，必须全部指定，与子查询一一对应。
		- 加上 `WITH CHECK OPTION` 时，更新操作必须满足子查询中 `WHERE` 子句的条件。
		- 子查询中最好只选择必要的属性，防止基表结构变化带来的影响。
	- **删除**
		- ```sql
		  DROP VIEW <view>;
		  ```
	- **查询**
		- 查询时，视图对于用户是透明的。
		- 实现方法：
			- 实体化视图：对视图查询时，首先根据视图定义生成临时表，然后在临时表上进行查询。
			- 视图消解：将对视图的查询条件和视图定义的子查询条件结合，直接在基表上查询。
		- 并不是所有的对视图查询都可以用视图消解实现。
	- **更新**
		- 实现方法上与视图的查询类似。
- **权限控制**
    - **授予**
        - ```sql
          GRANT <permission1>, <permission2>, ...
          ON TABLE <table>|<view>
          TO <user1>, <user2>, ... | PUBLIC
          [WITH GRANT OPTION];
          ```
        - 可以授予的权限有 `SELECT`、`INSERT`、`UPDATE`、`DELETE` 等。
        - 可以枚举用户名来指定被授权的用户，也可以使用 `PUBLIC` 指定所有用户。
        - 只有加上 `WITH GRANT OPTION` 时，被授权用户才可以将权限授予其他用户。
    - **回收**
        - ```sql
          REVOKE <permission1>, <permission2>, ...
          ON TABLE <table>|<view>
          FROM <user1>, <user2>, ... | PUBLIC
          RESTRICT|CASCADE;
          ```
- **嵌入式 SQL**
    - 嵌入式 SQL 直接写在编程语言源代码中，由预处理器转换为普通代码。
	- 游标：SQL 操作集合，而编程语言操作一个元组，在编程语言中可以通过游标来迭代集合元素。
