---
title: SQL 语言
weight: 400
math: false
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
          FROM <table-name>|(<subquery>) [AS] <alias>, ...
          [WHERE <predicate>]
          [GROUP BY <column-name> [HAVING <predicate>]]
          [ORDER BY <column-name> [ASC|DESC]]
          [[INNER | [LEFT|RIGHT] OUTER] JOIN <table-name> ON <predicate>];
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
