# 常用操作
**新建分支**： git switch -c 新分支名

**添加改动**：git add .

**提交代码**：git commit -m "说明"

**上传远端**：git push -u origin 新分支名（第一次创建分支）之后直接用git push就行

# 所有指令
**git branch**
查看本地有哪些分支。
当前所在分支前面会有 *。

**git branch -a**
查看所有分支，包括本地分支和远端分支。
远端分支通常会显示成 remotes/origin/...。

**git switch <分支名>**
切换到指定分支。
例如：git switch main

**git switch -c <新分支名>**
新建一个分支，并立刻切换过去。
例如：git switch -c feature/add-md

**git status**
查看当前仓库状态。
能看到有没有改动、有没有未提交文件、当前在哪个分支。

**git remote -v**
查看远程仓库地址。
一般可以确认 origin 指向哪个 GitHub 仓库。

**git branch -vv**
查看本地分支和远端分支的对应关系。
可以看到当前分支是否已经绑定到远端分支。

**git add .**
把当前目录下的改动加入暂存区。
. 表示把所有改动都加入。

**git commit -m "说明"**
把暂存区里的内容提交到本地仓库。
-m 后面是提交说明，例如：git commit -m "add new md file"

**git pull**
从远端拉取最新代码到本地。
常用于先同步别人更新，再继续自己修改。

**git fetch**
只把远端更新拉到本地记录里，不自动合并。
适合先看看远端有没有新内容。

**git push**
把本地提交上传到远端仓库。
前提是当前分支通常已经设置了上游分支。

**git push -u origin <分支名>**
把本地分支第一次推送到远端，并建立关联。
以后在这个分支上可以直接用 git push。
例如：git push -u origin feature/add-md

**git merge <分支名>**
把另一个分支的内容合并到当前分支。
例如先切到 main，再执行 git merge 要合并的分支。
一般不用这个功能，因为这是强行合并，如果更新的内容有问题会污染main。
合并一般使用github的Pull requests功能，这样可以检测有误错误，还可以留痕。


**git log --oneline --decorate -5**
查看最近几条提交记录。
--oneline 简洁显示，--decorate 显示分支标签，-5 只看最近 5 条。