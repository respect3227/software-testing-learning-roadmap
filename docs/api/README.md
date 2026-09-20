# 接口文档目录

这里用于维护学习项目中的接口相关资料。

## 建议文件

- `../API_TESTING_GUIDE.md`：接口测试学习路线和实践方法
- `../api-document-template.md`：单个接口文档模板
- `../api-test-case-template.md`：接口测试用例模板

## 文档和测试的对应关系

每个接口最好都有：

```text
接口文档
  ↓
接口测试用例
  ↓
手工调试记录
  ↓
pytest 自动化测试
  ↓
测试报告 / Bug 记录
```

## 推荐工具

- Apifox 或 Postman：接口手工调试和文档维护
- Python `requests`：发送 HTTP 请求
- pytest：组织和执行自动化测试
- JSON Schema：校验响应结构

不要把真实密钥、生产 Token、个人隐私数据提交到仓库。
