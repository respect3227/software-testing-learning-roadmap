# 软件测试学习任务大厅

这是一个面向零基础学习者的游戏化学习页面。打开 `game/index.html` 即可开始每日任务。

## 功能

- 12 周学习地图
- 每日任务和经验值（XP）
- 等级、连续学习天数和徽章
- 任务筛选：全部、待完成、已完成
- 任务详情、学习提示和交付物
- 浏览器 `localStorage` 保存进度，无需账号或后端
- 支持重置本地进度

## 在线使用

如果仓库启用了 GitHub Pages，访问：

```text
https://respect3227.github.io/software-testing-learning-roadmap/game/
```

## 本地使用

直接用浏览器打开 `game/index.html` 即可。也可以在仓库根目录启动一个静态服务器：

```bash
python -m http.server 8000
```

然后打开：<http://localhost:8000/game/>

## 重要说明

当前版本是纯前端静态网站，学习进度保存在当前浏览器中。如果清除浏览器数据或换设备，进度不会自动同步。后续可以增加 GitHub 登录、数据库和云端进度同步。
