# Git 常用指令与工作流说明书

本说明书旨在提供一份全面、实用的 Git 操作指南，帮助开发人员快速掌握版本控制的核心操作。

---

## 1. 基础配置 (Configuration)

在使用 Git 之前，需要先配置个人标识（用户名与邮箱）：

```bash
# 配置全局用户名
git config --global user.name "Your Name"

# 配置全局邮箱
git config --global user.email "your.email@example.com"

# 查看所有配置项
git config --list
```

---

## 2. 仓库初始化与获取 (Repository Init & Clone)

```bash
# 在当前目录下初始化一个新的 Git 本地仓库
git init

# 克隆远程仓库到本地
git clone <repository-url>
```

---

## 3. 日常开发工作流 (Daily Workflow)

最常用的提交流程包括查看状态、添加缓存、提交和查看历史。

```bash
# 查看工作区与暂存区的状态
git status

# 将修改过的文件添加到暂存区 (Staging Area)
git add <file-name>    # 添加指定文件
git add .              # 添加当前目录下所有修改及新文件

# 将暂存区的内容提交到本地仓库
git commit -m "commit message"

# 撤销工作区的修改（恢复到最近一次提交的状态）
git restore <file-name>

# 比较工作区与暂存区的差异
git diff
```

---

## 4. 分支管理 (Branching)

分支是 Git 的核心功能，允许同时进行多线开发。

```bash
# 查看本地所有分支（带 * 的为当前分支）
git branch

# 查看本地和远程的所有分支
git branch -a

# 创建新分支
git branch <branch-name>

# 切换到指定分支
git checkout <branch-name>
# 或者使用较新的 switch 命令
git switch <branch-name>

# 创建并直接切换到新分支
git checkout -b <branch-name>
# 或者
git switch -c <branch-name>

# 合并指定分支到当前分支
git merge <branch-name>

# 删除本地分支（需切换到其他分支后操作）
git branch -d <branch-name>     # 安全删除（已合并）
git branch -D <branch-name>     # 强制删除（未合并）
```

---

## 5. 远程操作 (Remote Operations)

与 GitHub/GitLab 等云端托管服务交互。

```bash
# 查看关联的远程仓库信息
git remote -v

# 添加远程仓库关联
git remote add origin <repository-url>

# 从远程获取最新版本，但不自动合并
git fetch origin

# 从远程获取最新版本并与当前分支合并
git pull origin <branch-name>

# 将本地分支推送到远程仓库
git push origin <branch-name>

# 第一次推送新分支时，建立本地分支与远程分支的追踪关系
git push -u origin <branch-name>
```

---

## 6. 版本回退与暂存 (Undo & Stash)

用于处理回退、误操作和临时保存修改的场景。

### 6.1 历史回退
> [!CAUTION]
> 在执行 reset 尤其是 `--hard` 选项时，未提交的修改会被丢弃，请务必谨慎操作！

```bash
# 仅回退 commit 信息，保留代码修改在工作区
git reset --soft HEAD~1

# 彻底回退到上一个版本，丢弃所有未提交的修改
git reset --hard HEAD~1

# 回退到指定的 commit id 状态
git reset --hard <commit-id>

# 撤销某次历史提交（通过创建一个新的提交来抵消它的修改）
git revert <commit-id>
```

### 6.2 暂存修改
当你想切换分支但当前分支的工作尚未完成、不想提交时，可以使用暂存：

```bash
# 保存当前工作进度，清空工作区
git stash

# 查看所有暂存的记录
git stash list

# 恢复最近一次暂存的内容，并在暂存列表中删除该记录
git stash pop

# 恢复最近一次暂存的内容，但保留暂存列表中的记录
git stash apply

# 清空所有暂存记录
git stash clear
```

---

## 7. 提交日志查看 (Commit History)

```bash
# 查看提交历史
git log

# 以单行且图形化树状展示提交历史（推荐）
git log --oneline --graph --all
```

---

## 8. Git 最佳实践建议 (Best Practices)

1. **小步快跑，频繁提交**：每次 Commit 只解决一个问题或实现一个完整子功能，这能让回溯和代码评审更轻松。
2. **规范的 Commit Message**：推荐使用约定式提交（Conventional Commits），例如：
   - `feat: 新增...功能`
   - `fix: 修复...问题`
   - `docs: 更新文档`
   - `refactor: 代码重构`
3. **保持 main/master 分支稳定**：不要直接向主分支 push 代码，应通过功能分支开发，经过测试后通过 PR/MR 合并。
