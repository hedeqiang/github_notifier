#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 通知管理工具

提供 GitHub 通知的获取、统计、筛选及批量处理功能。
"""

import sys
import requests
from typing import List, Dict, Optional, Any
from collections import defaultdict


class GitHubNotificationClient:
    """GitHub 通知 API 客户端"""

    def __init__(self, token: str):
        """
        初始化客户端

        Args:
            token: GitHub Personal Access Token
        """
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get_notifications(self, all_notifications: bool = True) -> List[Dict[str, Any]]:
        """
        获取通知列表

        Args:
            all_notifications: 是否包含已读通知

        Returns:
            通知数据列表
        """
        url = f"{self.base_url}/notifications"
        params = {
            "all": str(all_notifications).lower(),
            "per_page": 100
        }

        notifications_list = []
        page = 1

        print("正在获取通知", end="", flush=True)

        while True:
            params["page"] = page
            try:
                response = requests.get(url, headers=self.headers, params=params)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"\n请求失败: {e}")
                break

            data = response.json()
            if not data:
                break

            notifications_list.extend(data)
            print(".", end="", flush=True)
            
            if len(data) < 100:
                break
                
            page += 1

        print(" 完成")
        return notifications_list

    def unsubscribe_thread(self, thread_id: str) -> bool:
        """取消订阅通知线程"""
        url = f"{self.base_url}/notifications/threads/{thread_id}/subscription"
        try:
            response = requests.delete(url, headers=self.headers)
            return response.status_code == 204
        except requests.RequestException:
            return False

    def mark_thread_as_read(self, thread_id: str) -> bool:
        """标记通知线程为已读"""
        url = f"{self.base_url}/notifications/threads/{thread_id}"
        try:
            response = requests.patch(url, headers=self.headers)
            return response.status_code == 205
        except requests.RequestException:
            return False

    def mark_all_as_read(self) -> bool:
        """标记所有通知为已读"""
        url = f"{self.base_url}/notifications"
        try:
            response = requests.put(url, headers=self.headers)
            return response.status_code == 205
        except requests.RequestException:
            return False


def analyze_notifications(notifications: List[Dict]) -> Dict[str, Dict]:
    """
    统计各组织的通知情况

    Args:
        notifications: 通知列表

    Returns:
        按组织分类的统计数据
    """
    stats = defaultdict(lambda: {
        "count": 0,
        "repos": set(),
        "unread": 0,
        "types": defaultdict(int),
        "notifications": []
    })

    for notif in notifications:
        repo_full_name = notif.get("repository", {}).get("full_name", "")
        if "/" not in repo_full_name:
            continue
            
        org_name, repo_name = repo_full_name.split("/", 1)

        stats[org_name]["count"] += 1
        stats[org_name]["repos"].add(repo_name)
        stats[org_name]["notifications"].append(notif)

        if notif.get("unread", False):
            stats[org_name]["unread"] += 1

        subject_type = notif.get("subject", {}).get("type", "Unknown")
        stats[org_name]["types"][subject_type] += 1

    return dict(stats)


def print_stats(org_stats: Dict[str, Dict]):
    """打印统计信息"""
    if not org_stats:
        print("无通知数据")
        return

    total = sum(s["count"] for s in org_stats.values())
    print(f"\n{'='*40}")
    print(f"总计: {total} 条通知 | {len(org_stats)} 个组织")
    print(f"{'='*40}")

    sorted_orgs = sorted(org_stats.items(), key=lambda x: x[1]["count"], reverse=True)

    for i, (org, data) in enumerate(sorted_orgs, 1):
        print(f"\n{i}. {org}")
        print(f"   数量: {data['count']} (未读: {data['unread']})")
        
        types = ", ".join([f"{k}: {v}" for k, v in data['types'].items()])
        print(f"   类型: {types}")
        
        repos = sorted(data['repos'])
        repo_str = ", ".join(repos[:5])
        if len(repos) > 5:
            repo_str += f" ... (+{len(repos)-5})"
        print(f"   仓库: {repo_str}")


def filter_notifications(notifications: List[Dict], org_name: str) -> List[Dict]:
    """筛选指定组织的通知"""
    return [
        n for n in notifications 
        if n.get("repository", {}).get("full_name", "").startswith(f"{org_name}/")
    ]


def process_batch(client: GitHubNotificationClient, notifications: List[Dict], 
                 unsubscribe: bool = False, mark_read: bool = False):
    """批量处理通知"""
    if not notifications:
        return

    action_names = []
    if unsubscribe: action_names.append("取消订阅")
    if mark_read: action_names.append("标记已读")
    
    print(f"\n即将对 {len(notifications)} 条通知执行: {' + '.join(action_names)}")
    if input("确认执行? (y/n): ").lower() != 'y':
        print("已取消")
        return

    success = 0
    for i, notif in enumerate(notifications, 1):
        tid = notif["id"]
        repo = notif.get("repository", {}).get("full_name", "")
        
        # 仅显示部分进度
        if i <= 5 or i > len(notifications) - 5:
            print(f"处理 [{i}/{len(notifications)}] {repo}")
        elif i == 6:
            print("...")

        ok = True
        if unsubscribe:
            if not client.unsubscribe_thread(tid):
                ok = False
        
        if mark_read and ok:
            if not client.mark_thread_as_read(tid):
                ok = False
        
        if ok:
            success += 1

    print(f"\n完成: 成功 {success}/{len(notifications)}")


def run_cli():
    """交互式命令行入口"""
    print("GitHub 通知管理工具")
    token = input("请输入 GitHub Token: ").strip()
    if not token:
        print("Token 不能为空")
        return

    client = GitHubNotificationClient(token)
    
    while True:
        print(f"\n{'='*30}")
        print("1. 查看统计")
        print("2. 管理指定组织")
        print("3. 取消订阅所有")
        print("4. 全部标记已读")
        print("5. 退出")
        
        choice = input("请选择: ").strip()
        
        if choice == '5':
            break
            
        print("\n正在同步数据...")
        notifications = client.get_notifications()
        if not notifications and choice != '1':
            print("暂无通知")
            continue

        if choice == '1':
            stats = analyze_notifications(notifications)
            print_stats(stats)
            
        elif choice == '2':
            stats = analyze_notifications(notifications)
            print_stats(stats)
            org = input("\n输入组织名: ").strip()
            if not org: continue
            
            target_notifs = filter_notifications(notifications, org)
            if not target_notifs:
                print("未找到该组织的通知")
                continue
                
            print("\n1. 取消订阅 + 标记已读")
            print("2. 仅取消订阅")
            print("3. 仅标记已读")
            sub_choice = input("操作: ").strip()
            
            if sub_choice == '1':
                process_batch(client, target_notifs, unsubscribe=True, mark_read=True)
            elif sub_choice == '2':
                process_batch(client, target_notifs, unsubscribe=True)
            elif sub_choice == '3':
                process_batch(client, target_notifs, mark_read=True)

        elif choice == '3':
            print("警告: 将取消订阅所有通知")
            process_batch(client, notifications, unsubscribe=True)
            
        elif choice == '4':
            if input("确认标记所有为已读? (y/n): ").lower() == 'y':
                client.mark_all_as_read()
                print("已发送请求")


if __name__ == "__main__":
    try:
        run_cli()
    except KeyboardInterrupt:
        print("\n已退出")
