# GitHub 通知管理工具 - 完整使用教程

## 📋 目录

1. [工具简介](#工具简介)
2. [功能特点](#功能特点)
3. [前置要求](#前置要求)
4. [安装步骤](#安装步骤)
5. [快速开始](#快速开始)
6. [详细使用说明](#详细使用说明)
7. [使用场景示例](#使用场景示例)
8. [安全建议](#安全建议)
9. [故障排查](#故障排查)
10. [API 技术说明](#api-技术说明)

---

## 工具简介

这是一个强大的 GitHub 通知管理工具，可以帮助你批量管理 GitHub 的通知提醒。当你被某些组织的大量通知困扰，但 GitHub 网页界面无法批量取消订阅时，这个工具就能派上用场。

**适用场景：**
- 被某个组织的大量通知淹没（如 gitcoin-co 的各种提醒）
- 想要批量取消订阅多个仓库的通知
- 需要查看所有组织的通知统计
- 想要一键标记所有通知为已读

---

## 功能特点

✅ **查看统计** - 列出所有组织及其通知数量、类型分布、仓库列表
✅ **精准过滤** - 按组织名称过滤通知
✅ **批量操作** - 支持批量取消订阅和标记已读
✅ **灵活选择** - 可选择"取消订阅"、"标记已读"或"两者都执行"
✅ **全局操作** - 支持一键处理所有组织的通知
✅ **详细日志** - 显示处理进度和结果统计
✅ **安全确认** - 执行操作前需要用户确认
✅ **交互式菜单** - 友好的命令行交互界面

---

## 前置要求

### 系统要求
- Python 3.6 或更高版本
- 稳定的网络连接

### Python 库依赖
- `requests` - 用于 HTTP 请求

### GitHub 要求
- 有效的 GitHub 账号
- Personal Access Token (具有 notifications 权限)

---

## 安装步骤

### 第一步：检查 Python 版本

打开终端，运行：

```bash
python3 --version
```

确保版本 ≥ 3.6。如果没有安装 Python，请访问 [python.org](https://www.python.org/downloads/) 下载安装。

### 第二步：安装依赖库

```bash
pip install requests
```

或者使用 pip3：

```bash
pip3 install requests
```

### 第三步：下载脚本

将 `github_notification_manager.py` 保存到你的电脑。

### 第四步：添加执行权限（可选，macOS/Linux）

```bash
chmod +x github_notification_manager.py
```

### 第五步：创建 GitHub Personal Access Token

这是最重要的步骤！

1. **登录 GitHub**
   访问 [https://github.com](https://github.com)

2. **进入 Settings**
   点击右上角头像 → Settings

3. **打开 Developer settings**
   左侧菜单最底部 → Developer settings
# GitHub Notifier

一个简单的命令行工具，用于管理 GitHub 通知。支持查看统计、批量取消订阅和标记已读。

## 功能

- 📊 **查看统计**：按组织分类显示通知数量、未读数和类型分布。
- 🏢 **组织管理**：针对特定组织批量取消订阅或标记已读。
- 🧹 **一键清理**：支持取消订阅所有组织的通知。
- ✅ **批量已读**：一键标记所有通知为已读。

## 安装

确保已安装 Python 3.6+。

```bash
git clone <repository-url>
cd github-notifier
pip install .
```

或者直接安装开发模式：

```bash
pip install -e .
```

## 使用方法

安装完成后，直接在终端运行：

```bash
github-notifier
```

首次运行需要输入 GitHub Personal Access Token (PAT)。

### 获取 Token

1. 访问 [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens).
2. 生成新 Token (Classic 或 Fine-grained).
3. 确保勾选 `notifications` 权限 (如果是 Classic Token) 或 `Notifications` (Read and Write) (如果是 Fine-grained Token).

## 菜单说明

1. **查看统计**: 列出所有有通知的组织概况。
2. **管理指定组织**: 输入组织名称，仅处理该组织的通知。
3. **取消订阅所有**: ⚠️ 危险操作，将取消订阅列表中的所有通知。
4. **全部标记已读**: 仅标记已读，不取消订阅。

## 许可证

MIT


---

## 参考资料

- [GitHub REST API - Notifications](https://docs.github.com/en/rest/activity/notifications)
- [GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [GitHub API Rate Limiting](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)
- [Requests 库文档](https://requests.readthedocs.io/)

---

## 更新日志

### v2.0.0 (2025-01-19)
- ✨ 新增交互式菜单
- ✨ 支持查看组织统计
- ✨ 支持批量标记所有通知为已读
- ✨ 优化显示性能（只显示部分详情）
- ✨ 添加操作确认机制
- 🐛 修复组织名称过滤问题

### v1.0.0 (2025-01-19)
- 🎉 初始版本发布
- ✨ 基础的取消订阅功能
- ✨ 支持标记已读

---

## 开源协议

MIT License

---

## 贡献

欢迎提交 Issues 和 Pull Requests!

如有问题或建议，请联系作者。

---

**祝使用愉快！清理通知，保持专注！** 🚀
