# Training Repository / 训练仓库

欢迎来到本训练仓库！本项目已经过结构重构，新增了猜数字小游戏、单元测试以及 CI/CD 自动化工作流。

---

## 📁 仓库结构 (Repository Structure)

重构后的仓库结构如下所示：

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD 工作流配置文件
├── docs/
│   └── markdown_training.md   # Markdown 全功能练习与语法向导（原 README 迁移并完善）
├── guess_game/
│   ├── __init__.py            # 游戏包初始化文件
│   └── game.py                # 猜数字小游戏的核心逻辑与 CLI 启动器
├── tests/
│   └── test_game.py           # 针对小游戏逻辑和 CLI 的单元测试
├── README.md                  # 本说明文件
└── requirements.txt           # 依赖项声明（开发/测试相关依赖）
```

---

## 🎮 猜数字小游戏 (Guess Number Game)

我们在 [guess_game/game.py](file:///D:/Study/code/other/training/guess_game/game.py) 中实现了一个非常基础且有趣的猜大小数字游戏。

### 游戏规则
1. 游戏启动后，程序会随机生成一个 1 到 100 之间的整数（你可以通过参数自定义范围）。
2. 你一共有 10 次机会进行猜测（可通过参数自定义最大猜测次数）。
3. 每次输入猜测的数字后，程序会提示你的猜测是 **太大** 还是 **太小**。
4. 如果你在次数限制内猜中数字，则获得胜利；否则游戏结束。

### 运行游戏
确保你安装了 Python 3 并处于仓库根目录下，运行以下命令即可启动游戏：
```bash
python -m guess_game.game
```

---

## 🧪 单元测试 (Unit Tests)

所有的单元测试均在 [tests/test_game.py](file:///D:/Study/code/other/training/tests/test_game.py) 中编写，使用了 Python 标准库的 `unittest` 模块，无需额外安装依赖即可运行。

### 运行测试
在仓库根目录下，使用以下命令运行测试：
```bash
python -m unittest discover -s tests
```

---

## 🚀 CI/CD 持续集成 (Continuous Integration)

本仓库配置了基于 **GitHub Actions** 的 CI/CD 自动化工作流：
- **配置文件**: [.github/workflows/ci.yml](file:///D:/Study/code/other/training/.github/workflows/ci.yml)
- **触发条件**: 
  - 当有代码推送（`push`）到 `main` 或 `chengtianxu/helper` 分支时。
  - 当针对 `main` 分支提交拉取请求（`pull_request`）时。
- **工作内容**: 自动化拉取代码、配置 Python 环境、安装 `requirements.txt` 中的依赖，并自动运行单元测试确保代码质量。

---

## 📝 Markdown 学习文档
原本位于根目录的 Markdown 语法练习文件已迁移并完善，请参阅：
- [Markdown 语法全功能练习向导](file:///D:/Study/code/other/training/docs/markdown_training.md)