# Git 与 GitHub 实战教程

> 适合：软件测试/自动化测试初学者  
> 目标：掌握提交、分支、PR 和协作流程，建立工程化开发思维

## 一、为什么要学 Git

Git 是软件项目协作的基础，是每个开发和测试人员都必须掌握的技能。你需要知道：

- 如何创建分支
- 如何提交代码
- 如何查看差异
- 如何回滚错误提交
- 如何创建 Pull Request
- 如何协作解决冲突
- 如何基于 issue 或需求设计提交内容

## 二、Git 基础命令

```bash
git init
git status
git add .
git commit -m "feat: add test case"
git branch
git checkout -b feature/test-login
git push origin feature/test-login
git pull
git log
```

## 三、常用分支策略

建议采用简单的分支流程：

```text
main
  └── feature/login-test
  └── feature/api-testing
  └── bugfix/fix-search-case
```

实践中，最好遵循：

- `main`：主分支
- `feature/*`：新功能分支
- `bugfix/*`：修复分支

## 四、提交信息规范

推荐格式：

```text
feat: add login test cases
fix: fix empty keyword search issue
test: add API parameterized tests
docs: add SQL guide for testing
```

这样大家看提交记录时就能快速理解内容。

## 五、Pull Request 流程

一个标准 PR 流程：

```text
功能开发
  ↓
提交到分支
  ↓
推送到 GitHub
  ↓
创建 Pull Request
  ↓
代码审核
  ↓
合并到主分支
```

也应该写清楚：

- 修改了什么
- 为什么改
- 如何验证
- 是否有测试截图或报告

## 六、实习中常见的 Git 面试题

- 什么是 rebase 和 merge 的区别？
- 什么是冲突？如何解决？
- 为什么要写清晰提交信息？
- 什么是 git checkout / git switch？
- GitHub 的 PR 是做什么的？

## 七、Git 与测试结合的典型场景

- 添加一个新的用例提交到 feature 分支
- 修复一个失败的测试并提交 commit
- 通过 PR 记录自动化测试结果
- 合并到主分支前跑冒烟测试
- 更新 README 与学习文档

## 八、建议练习

1. 创建一个新分支
2. 修改 README
3. 提交一次 commit
4. 推到 GitHub
5. 创建 PR
6. 合并到主分支
7. 删除测试分支

## 九、GitHub 基础术语

- Repo：仓库
- Commit：提交
- Branch：分支
- PR：Pull Request
- Merge：合并
- Fork：分叉

## 十、结论

Git 和 GitHub 是软件工程协作的核心，测试人员不只需要“会跑测试”，还需要“会做版本管理、会提交改动、会参与协作”。这对实际实习和校招都非常重要。

