---
title: 数据库完整性
weight: 800
math: false
---

- **完整性**
    - **定义**
        - 确保数据的正确性和相容性，防止不符合语义的数据。
    - **分类**
        - 实体完整性
        - 参照完整性
        - 用户定义完整性
    - **完整性约束分类**
        - 列级约束：对属性的类型、格式、范围等的约束。
        - 元组约束：对元组内部属性之间的约束。
        - [关系](/docs/computer-science/database/relational-database#fjalge)约束：对多个关系的联系的约束。
    - **实现方法**
        - 默认值：如常量、自增值、数学表达式等。
        - 约束：定义关系列允许值的规则，优先级高于其他实现方法。
        - 规则：需要单独创建的对象，再绑定到列上，不常用。
        - 触发器：在操作之后自动执行的过程。
- **实体完整性**
    - **定义**
        - 参考[此处](/docs/computer-science/database/relational-database#adjndf)。
    - **语法**
        - 对主键值进行约束，使用 `PRIMARY KEY` 标注。
        - 单个属性作为主键：在列定义处使用 `<column> <type> PRIMARY KEY`。
        - 多个属性作为主键：在表定义范围内使用 `PRIMARY KEY (<column>, ...)`。
    - **检查**
        - 在每次与主键有关的操作后，通过扫描全表或使用索引判断是否存在主键。
- **参照完整性**
    - **定义**
        - 参考[此处](/docs/computer-science/database/relational-database#goajgo)。
    - **语法**
        - ```sql
          ROREIGN KEY <foreign-key> REFERENCES <table>(<primary-key>)
            [[ON INSERT|UPDATE|DELETE NO ACTION] | [ON INSERT|UPDATE|DELETE CASCADE], ...]
          ```
    - **参照关系外键空值检查**
        - 需要定义是否允许外键为空。
        - 若外键是主键组成部分，则不为空，否则按照被参照关系中的要求。
    - **参照关系插入/修改元组检查**
        - 受限插入：如果被参照关系不存在对应值，则拒绝插入。
        - 级联插入：如果被参照关系不存在对应值，则同时插入被参照的元组。
    - **被参照关系删除元组检查**
        - 受限删除：如果被参照，则拒绝删除。
        - 级联删除：删除的同时删除所有参照此属性的元组。
        - 置空值删除：删除次元组后，将所有参照的外键设为空（如果可以）。
- **用户定义完整性**
    - **语法**
        - ```sql
          UNIQUE|NOT NULL|DEFAULT|CHECK (<expr>)
          ```
        - 限制可以放置在列定义后和表定义内，分别作为列级和元组约束。
    - **检查**
        - 如果不满足条件，则拒绝执行。
- **完整性约束命名**
    - **创建**
        - ```sql
          CONSTRAINT <constraint> <constraint-clause>
          ```
    - **修改**
        - ```sql
          ALTER TABLE <table>
            [ADD CONSTRAINT <constraint> <constraint-clause>] | [DROP CONSTRAINT <constraint>];
          ```
        - 没有直接的修改语句，用先删除再添加实现。
- **触发器**
    - **定义**
        - 触发器是特殊的储存过程，在 `UPDATE`、`INSERT`、`DELETE` 前后执行。
    - **分类**
        - 行级触发器：对每一个元组修改都触发触发器。
        - 语句级触发器：仅在执行一个更新语句时触发触发器。
    - **创建语法**
        - ```sql
          CREATE TRIGGER <trigger>
            BEFORE|AFTER <operation> ON <table>
            FOR EACH ROW|STATEMENT
            [WHEN <condition>]
            AS BEGIN
              <statements>
            END;
          ```
        - `<operation>` 可以是 `UPDATE`、`INSERT`、`DELETE`，可以用 `OR` 连接多个。
        - `<statements>` 中可以用 `new` 引用新的元组，用 `old` 引用旧的元组。
        - 对于 `BEFORE` 触发器，执行时 `new` 还没有替换 `old`，修改 `new` 会影响更新结果。
    - **删除语法**
        - ```sql
          DROP TRIGGER <trigger> ON <table>;
          ```
