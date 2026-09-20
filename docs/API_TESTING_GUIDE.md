# 接口测试学习路线与实践指南

> 这是零基础软件测试路线的接口测试补充部分。建议完成基础测试、Python 和 pytest 入门后开始学习；不必等 UI 自动化全部学完。

## 一、为什么要学习接口测试

接口测试直接验证前后端之间的数据交互，通常比 UI 测试更快、更稳定，也更容易定位问题。

接口测试可以检查：

- 请求方法是否正确
- 参数校验是否正确
- HTTP 状态码是否正确
- 返回 JSON 结构是否正确
- 错误信息是否清晰
- 权限和认证是否生效
- 数据是否正确保存、修改和查询
- 接口是否满足幂等性和边界条件

推荐学习顺序：

```text
HTTP 基础
  ↓
请求方法和状态码
  ↓
JSON 与接口文档
  ↓
Postman / Apifox 手工调试
  ↓
Python requests
  ↓
pytest 接口自动化
  ↓
认证、数据关联和参数化
  ↓
接口与 UI 联合验证
  ↓
CI 持续集成
```

## 二、必须掌握的 HTTP 基础

| 内容 | 说明 |
|---|---|
| GET | 查询资源 |
| POST | 创建资源或提交操作 |
| PUT | 整体更新资源 |
| PATCH | 部分更新资源 |
| DELETE | 删除资源 |
| 2xx | 请求成功 |
| 3xx | 重定向 |
| 4xx | 客户端请求错误 |
| 5xx | 服务端错误 |

常见状态码：

- `200 OK`：查询或操作成功
- `201 Created`：资源创建成功
- `204 No Content`：成功但没有返回内容
- `400 Bad Request`：参数格式或内容错误
- `401 Unauthorized`：未认证或 Token 无效
- `403 Forbidden`：已认证但没有权限
- `404 Not Found`：资源不存在
- `409 Conflict`：资源冲突
- `422 Unprocessable Entity`：参数校验失败
- `500 Internal Server Error`：服务端异常

## 三、如何阅读接口文档

每看到一个接口，至少确认这些信息：

1. 接口名称和业务目的
2. 请求方式和 URL
3. 是否需要登录或 Token
4. Path 参数、Query 参数、Header 参数和 Body 参数
5. 参数类型、是否必填、长度和取值范围
6. 成功响应的状态码和 JSON 结构
7. 失败响应的状态码和错误信息
8. 是否会修改数据
9. 是否支持分页、排序和筛选
10. 是否存在频率限制、幂等性或权限要求

推荐把接口文档放在仓库的 `docs/api/` 目录，和测试用例保持对应关系。

## 四、接口测试设计方法

以“非遗文化项目搜索接口”为例，可以设计：

### 正常场景

- 使用已知关键词查询
- 不传关键词查询全部数据
- 使用合法分页参数
- 使用合法排序字段

### 异常场景

- 关键词类型错误
- 页码为 0
- 页码为负数
- 页大小超过最大限制
- 传入不存在的分类 ID
- 缺少必填参数
- Token 无效或过期
- 无权限访问接口

### 数据与协议场景

- 返回状态码正确
- 返回 Content-Type 正确
- JSON 字段类型正确
- 空结果返回结构稳定
- 响应时间满足要求
- 多次重复提交不会产生重复数据

## 五、requests + pytest 示例

```python
import pytest
import requests

BASE_URL = "http://example.test/api"


@pytest.mark.api
@pytest.mark.smoke
def test_search_projects_returns_success():
    response = requests.get(
        f"{BASE_URL}/projects",
        params={"keyword": "汉绣", "page": 1, "page_size": 10},
        timeout=10,
    )

    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert isinstance(body["data"], list)


@pytest.mark.api
@pytest.mark.parametrize("page", [0, -1])
def test_search_projects_rejects_invalid_page(page):
    response = requests.get(
        f"{BASE_URL}/projects",
        params={"page": page},
        timeout=10,
    )

    assert response.status_code in (400, 422)
```

> 示例中的地址是占位地址。练习时必须替换为实际测试环境，并且不要在公开仓库提交真实 Token、密码或生产数据。

## 六、接口自动化断言层次

不要只断言状态码。建议从外到内逐层验证：

```text
HTTP 状态码
  ↓
响应头
  ↓
JSON 顶层结构
  ↓
字段类型和必填字段
  ↓
业务字段值
  ↓
数据库或后续接口结果（必要时）
```

例如：

```python
assert response.status_code == 200
assert response.headers["content-type"].startswith("application/json")
assert body["code"] == 0
assert isinstance(body["data"], list)
```

## 七、接口与 UI 的联合测试

一个完整业务流程可以拆成：

1. 使用接口准备测试数据
2. 使用 Playwright 操作页面
3. 使用接口或数据库验证结果
4. 清理测试数据

例如商城下单：

```text
接口创建测试商品
  ↓
UI 搜索商品并加入购物车
  ↓
UI 提交订单
  ↓
接口查询订单状态
  ↓
接口删除测试数据
```

接口测试和 UI 测试各有职责：

- 接口测试：快速验证业务规则和数据交互
- UI 测试：验证真实用户操作、页面展示和核心链路

## 八、接口学习交付物

建议新增以下文件：

```text
docs/api/
├── README.md
├── api-document-template.md
├── api-test-case-template.md
└── project-api-spec.md

learning/api_basics/
├── test_projects_api.py
└── README.md
```

学习完成后应能回答：

- GET 和 POST 有什么区别？
- 401 和 403 有什么区别？
- 如何测试分页？
- 如何测试 Token 过期？
- 如何校验 JSON 字段？
- 如何关联前后接口的数据？
- 为什么接口测试通常比 UI 测试更快？
- 如何避免把真实密钥提交到 GitHub？

## 九、安全注意事项

- 不要提交真实账号、密码、Token、Cookie 和密钥
- 使用环境变量或本地 `.env` 文件
- `.env` 必须加入 `.gitignore`
- 不要对没有授权的系统进行接口扫描或压力测试
- 只在测试环境执行会修改或删除数据的用例
- 测试数据使用专用账号和可清理的数据
