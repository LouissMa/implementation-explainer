# Implementation Explainer Skill

[English](README.md)

一个开源的 AI 工程 Skill 包，用来把代码修改产出为三类结果：

1. 实现本身
2. 面向人的解释说明
3. 可持续积累的项目文档

这个 Skill 适合希望使用 AI 编程、同时又不丢失架构清晰度和团队知识沉淀的团队。

## 它能做什么

当这个 Skill 被使用时，AI 助手应该：

- 在聊天中用教学式结构解释代码改动
- 在文件发生变化后更新 `docs/CHANGELOG.md`
- 在结构或数据流发生变化时更新 `docs/ARCHITECTURE.md`
- 解释执行流程、依赖关系和系统中的位置
- 给学习者提供推荐阅读顺序

## 仓库结构

```text
implementation-explainer/
|-- README.md
|-- README.zh-CN.md
|-- LICENSE
|-- .gitignore
|-- skill/
|   `-- implementation-explainer/
|       |-- SKILL.md
|       `-- references/
|           `-- documentation-rules.md
|-- scripts/
|   |-- install_skill.py
|   `-- validate_project.py
`-- docs/
    |-- ARCHITECTURE.md
    |-- CHANGELOG.md
    `-- RELEASE_CHECKLIST.md
```

## 安装

### 方式 1：用 Python 安装

```bash
python scripts/install_skill.py
```

默认会把 Skill 复制到：

- Windows: `%USERPROFILE%\\.ai-skills\\implementation-explainer`
- macOS/Linux: `$HOME/.ai-skills/implementation-explainer`

### 方式 2：安装到自定义目录

```bash
python scripts/install_skill.py --target-dir /path/to/skills/implementation-explainer
```

## 使用方式

安装完成后，当你希望 AI 编码工作流具备下面这些能力时，可以加入 `implementation-explainer`：

- 写代码的同时解释代码
- 强制补充 changelog
- 保留架构记忆
- 用适合学习的方式讲清楚改动

## GitHub 开源建议

1. 从当前目录创建一个新的 GitHub 仓库。
2. 将代码推送到仓库。
3. 用标签或 release 管理后续版本。
4. 分享仓库地址，让其他人可以 clone 并安装这个 Skill。

## 开源前验证

先运行内置校验脚本：

```bash
python scripts/validate_project.py
```

然后做一次干净的安装测试：

```bash
python scripts/install_skill.py --target-dir .ai-skills-test/implementation-explainer
```

最后可以按照 [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md) 做人工检查。

## 为什么要做这个 Skill

AI 编程真正有价值，不只是因为它能写代码，还因为它应该留下：

- 清晰的设计理由
- 架构知识
- 适合新人上手的解释
- 可以长期积累的项目记忆

这个 Skill 的目标，就是把这些行为明确化、标准化、可复用化。

## 当前具备的能力

目前这个 Skill 可以：

- 强制输出结构化的改动解释
- 在实现后要求更新 `docs/CHANGELOG.md`
- 在结构或数据流变化时要求更新 `docs/ARCHITECTURE.md`
- 在解释中区分新增文件和修改文件
- 解释执行流程、模块交互和系统位置
- 提供面向学习者的阅读顺序
- 记录设计决策、风险和假设
- 通过安装脚本以可复用仓库的形式分发