# GitHub Notifier

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

一个强大的命令行工具，用于批量管理 GitHub 通知。支持查看统计、按组织过滤、批量取消订阅和一键标记已读。

## ✨ 功能特点

- **📊 全局统计**：一目了然地查看所有组织的通知数量、未读数及类型分布。
- **🏢 组织管理**：针对特定组织进行批量操作，支持取消订阅或仅标记已读。
- **🧹 一键清理**：支持取消订阅所有组织的通知，彻底释放你的收件箱。
- **✅ 批量已读**：快速将所有通知标记为已读，不取消订阅。
- **🔒 安全可靠**：Token 仅在本地使用，支持环境变量配置。

## 🚀 安装指南

确保您的系统已安装 Python 3.6 或更高版本。

### 源码安装

```bash
git clone https://github.com/hedeqiang/github-notifier.git
cd github-notifier
pip install .
```

### 开发模式安装

如果您想修改代码或参与贡献，推荐使用开发模式：

```bash
pip install -e .
```

## 📖 使用方法

安装完成后，您可以在终端直接运行：

```bash
github-notifier
```

### 配置 Token

首次运行需要提供 GitHub Personal Access Token (PAT)。

1. 访问 [GitHub Settings > Tokens](https://github.com/settings/tokens).
2. 生成新 Token (建议选择 **Classic**).
3. 勾选 `notifications` 权限.
4. 复制 Token 并粘贴到程序中.

> **推荐**：为了安全，您可以将 Token 设置为环境变量 `GITHUB_TOKEN`，程序会自动读取。
>
> ```bash
> export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"
> ```

## 🎮 菜单说明

程序启动后提供以下功能菜单：

1. **查看统计**
   列出所有包含通知的组织，显示通知总数、未读数及仓库列表。

2. **管理指定组织**
   输入组织名称（如 `google`），仅处理该组织的通知。支持：
   - 取消订阅 + 标记已读
   - 仅取消订阅
   - 仅标记已读

3. **取消订阅所有**
   ⚠️ **危险操作**：将取消订阅列表中的**所有**通知。适用于想要彻底清空通知列表的情况。

4. **全部标记已读**
   仅将所有通知标记为已读状态，保留订阅关系。

## ❓ 常见问题

**Q: 为什么取消订阅失败？**
A: 请检查您的 Token 是否具有 `notifications` 权限。

**Q: 取消订阅后还能收到通知吗？**
A: 取消订阅后，您将不再收到该 Issue/PR 的后续更新通知。但如果您再次被 @ 或分配任务，仍会收到新通知。

**Q: 为什么有些组织名称看起来是个人账号？**
A: GitHub 的通知归属是按仓库所有者划分的。如果仓库属于个人，组织名称即为该用户的用户名。

## 🛡️ 安全建议

- **不要泄露 Token**：Token 等同于您的密码，请勿分享给他人。
- **定期轮换**：建议定期重新生成 Token。
- **最小权限**：仅授予 `notifications` 权限即可。

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。

---

Copyright (c) 2024 hedeqiang
