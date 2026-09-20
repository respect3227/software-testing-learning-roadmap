# 接口测试练习

本目录用于练习 `requests + pytest`。练习时请替换为经过授权的测试环境地址。

## 安装

```bash
pip install requests pytest
```

## 建议练习顺序

1. 发送 GET 请求
2. 检查状态码
3. 解析 JSON
4. 参数化测试多个关键词
5. 测试错误参数
6. 添加认证信息
7. 使用 fixture 管理请求会话
8. 关联前后接口数据

## 安全

不要把真实 Token 写在代码中。可以使用环境变量：

```bash
export API_TOKEN="your-test-token"
```

Windows PowerShell：

```powershell
$env:API_TOKEN = "your-test-token"
```
