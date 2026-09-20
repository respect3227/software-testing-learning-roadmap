# SQL 与接口测试实战学习路线

> 适合：软件测试初学者、实习生、测试开发方向入门者  
> 目标：掌握接口测试基础 + SQL 查询能力 + 工程化协作思维

## 一、为什么要学 SQL

接口测试经常需要验证：

- 接口返回的数据是否正确
- 是否写入数据库成功
- 是否更新、删除、查询到了目标记录
- 是否存在脏数据、重复数据、状态错误问题

很多真实的缺陷并不在页面上，而在数据库中。尤其是：

- 下单失败但页面提示成功
- 用户信息未写入
- 数据状态错误
- 搜索接口查询结果与数据库不一致

所以，掌握 SQL 非常关键。它能让你从“接口返回看起来没问题”升级到“能验证数据层真实状态”。

## 二、SQL 学习顺序

建议从最实用的 6 个点开始：

```text
SELECT 基础
  ↓
WHERE 条件筛选
  ↓
INSERT / UPDATE / DELETE
  ↓
JOIN 多表关联
  ↓
GROUP BY / 聚合函数
  ↓
子查询与排序
```

## 三、最常见的 SQL 语句

### 1. 查询数据

```sql
SELECT * FROM users;
SELECT id, username, status FROM users WHERE status = 'active';
```

### 2. 条件筛选

```sql
SELECT * FROM orders WHERE total_price > 100;
SELECT * FROM products WHERE name LIKE '%汉绣%';
```

### 3. 插入数据

```sql
INSERT INTO products (name, category_id, price)
VALUES ('汉绣', 1, 99.99);
```

### 4. 更新数据

```sql
UPDATE users SET status = 'inactive' WHERE id = 5;
```

### 5. 删除数据

```sql
DELETE FROM products WHERE id = 10;
```

### 6. 多表关联

```sql
SELECT o.id, u.username, o.total_price
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE o.status = 'paid';
```

### 7. 聚合查询

```sql
SELECT COUNT(*) FROM orders;
SELECT category_id, COUNT(*)
FROM products
GROUP BY category_id;
```

### 8. 分页查询

```sql
SELECT * FROM products LIMIT 10 OFFSET 0;
```

## 四、SQL 与接口测试的结合

接口测试中最常见的场景：

### 场景 1：创建用户后检查数据库

```sql
SELECT * FROM users WHERE username = 'tester001';
```

### 场景 2：下单后查看订单状态

```sql
SELECT * FROM orders WHERE user_id = 10 ORDER BY created_at DESC LIMIT 1;
```

### 场景 3：删除接口后确认数据库已删除

```sql
SELECT COUNT(*) FROM products WHERE id = 5;
```

### 场景 4：搜索接口校验真实结果

```sql
SELECT * FROM products WHERE name LIKE '%汉绣%';
```

## 五、SQL 学习练习建议

创建一个假设数据库表：

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    status VARCHAR(20)
);

CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    total_price DECIMAL(10,2),
    status VARCHAR(20)
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    category_id INT,
    price DECIMAL(10,2)
);
```

然后自行练习：

- 查询所有激活用户
- 查询大于 100 的订单
- 按分类统计商品数量
- 根据用户 ID 查询订单
- 查询所有商品中价格最高的前 5 个

## 六、推荐学习顺序和任务

### 第 1 步：基础查询

```sql
SELECT * FROM users;
SELECT username FROM users WHERE status = 'active';
```

### 第 2 步：条件过滤

```sql
SELECT * FROM orders WHERE total_price > 500;
SELECT * FROM products WHERE category_id = 2;
```

### 第 3 步：排序和分页

```sql
SELECT * FROM products ORDER BY price DESC LIMIT 10;
SELECT * FROM products LIMIT 10 OFFSET 20;
```

### 第 4 步：聚合查询

```sql
SELECT COUNT(*) FROM products;
SELECT AVG(price) FROM products;
SELECT category_id, SUM(price)
FROM products
GROUP BY category_id;
```

### 第 5 步：多表联查

```sql
SELECT u.username, o.total_price
FROM users u
JOIN orders o ON u.id = o.user_id;
```

## 七、接口测试与 SQL 的协同关系

一个真实测试场景如下：

```text
接口创建订单
  ↓
检查接口返回 200
  ↓
查询数据库中是否存在该订单
  ↓
验证订单状态是否正确
  ↓
验证用户余额或库存是否更新
```

这是测试工程师在真实项目中非常重要的能力：

- 不是只看页面是否更新
- 而是要验证数据层也符合预期

## 八、实战建议

- 接口测试时，尽量只用测试环境数据
- 不要在生产库中执行测试 SQL
- 每次写 SQL 前先判断“我想验证什么业务结果”
- SQL 语句要尽量简洁，避免复杂嵌套一开始就学太深
- 最好把 SQL 练习记录到笔记或仓库中，每周复盘

## 九、推荐资料

- SQL 基础课程：SELECT、WHERE、JOIN、GROUP BY
- MySQL 官方文档
- PostgreSQL 官方文档
- 与接口测试结合的数据库用例设计

## 十、总结

对测试从业者来说，SQL 是“看数据、判断对错、验证业务状态”的关键能力。接口测试和 SQL 结合之后，你会从单纯“检查返回值”升级到“验证真实业务结果”。

这也是很多自动化测试岗位对初学者真正看重的能力之一。

