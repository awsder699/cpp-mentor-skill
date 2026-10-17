# cpp-mentor — C++ 专业老师

> 一个让 AI Agent 变身资深 C++ 教师的 Skill：先评估水平与盲点，再循序渐进、举例类比、提问引导、即时反馈地讲解，配简洁易懂且注释清晰的代码示例。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agent Skill](https://img.shields.io/badge/format-Agent%20Skill-blue.svg)](https://code.visualstudio.com/)

---

## 这是什么

**cpp-mentor** 是一个遵循 [Agent Skill](https://code.claude.com/docs/en/agents-and-tools/agent-skills) 通用规范的技能包。安装后，任何支持该规范的 Agent 平台（WorkBuddy、Claude Code 等）在遇到 C++ 相关问题时，都会以「资深 C++ 教师」的模式响应：

- 讲概念前先评估你的水平和知识盲点，不堆术语、不超纲；
- 用生活类比建立直觉，再给出准确术语与规则；
- 通过提问引导你自己得出结论，而不是直接甩答案；
- 每讲完一小步即时验证理解，收尾必附要点回顾 + 常见坑 + 自测题；
- 代码示例最小可运行、注释解释「为什么」，默认 C++17。

它的设计目标只有一个：**最大化你对所求问题相关知识的吸收率**。

## 核心教学理念

教师能力模型综合自国内特级教师评选细则、教学名师指标体系与一线教学访谈，提炼为可执行的七条原则：

| # | 原则 | 含义 |
|---|------|------|
| 1 | 先评估后讲解 | 开口讲题前，用 2-3 个诊断问题定位水平（L0-L3）与盲点 |
| 2 | 循序渐进，一次一新 | 每次只引入一个新概念，且必须挂在已有认知上 |
| 3 | 类比先行，术语随后 | 先用生活例子建直觉，术语首次出现必附中文释义 |
| 4 | 提问引导，不给直答 | 卡壳时给阶梯提示；作业/竞赛题坚持引导思路 |
| 5 | 即时反馈，小步验证 | 每步让用户预测结果或复述要点，确认后再前进 |
| 6 | 暴露迷思，正面击破 | 用最小反例 + 运行结果证伪 C++ 经典误区 |
| 7 | 保护信心，累积成功 | 先肯定对的部分，把大问题拆成可攻克的小步骤 |

## 功能特性

- **五步教学流程**：诊断 → 定位 → 建构 → 引导 → 巩固，每步有明确的操作手册与话术；
- **水平评估题库**：覆盖程序基础、函数、指针内存、引用 const、OOP、拷贝移动、STL、模板、现代 C++（11/14/17/20）、调试、算法竞赛共 11 个主题域的诊断问题；
- **讲解技巧库**：20+ 个核心类比（含类比失效边界说明）、四级脚手架、三类提问话术、18 条 C++ 经典迷思概念的击破方法；
- **教学代码规范**：最小可运行、一次一知识点、注释解释「为什么」、预期输出必附；
- **分场景策略**：概念讲解 / 编译调试 / 代码 Review / 竞赛题 / 课设项目 / 学习规划六类场景各有针对性策略。

## 快速开始

### 安装

**方式一：直接拷贝（推荐，跨平台通用）**

```bash
# 克隆本仓库
git clone https://github.com/awsder699/cpp-mentor-skill.git

# WorkBuddy：拷贝到用户级技能目录（所有项目可用）
cp -r cpp-mentor-skill/cpp-mentor ~/.workbuddy/skills/

# 或拷贝到项目级目录（随项目共享）
cp -r cpp-mentor-skill/cpp-mentor <your-project>/.workbuddy/skills/
```

**方式二：下载分发包**

从 [Releases](../../releases) 页面下载 `cpp-mentor.zip`，解压后将 `cpp-mentor/` 目录放入目标平台的技能目录。

### 验证安装

在任意对话中提出一个 C++ 问题，例如：

> 「讲讲指针和引用的区别」

如果回复以评估/提问开头（而非长篇大论），说明 Skill 已生效。

## 使用方式

Skill 由问题自动触发，无需显式调用。以下场景均可触发：

| 你可以这样问 | Skill 的行为 |
|--------------|--------------|
| 「`vector` 扩容后迭代器失效是什么意思？」 | 先评估你对迭代器的了解 → 类比 + 最小代码演示失效过程 → 让你预测后果 → 收尾附自测题 |
| 「这段代码为什么崩了？」（附代码/报错） | 引导你读报错三要素 → 提出假设 → 分步验证，而不是直接改代码 |
| 「帮我 Review 这个类写得怎么样」 | 先肯定优点 → 按严重度排序问题 → 每处给最小修改示例 + 原因 |
| 「蓝桥杯这道题怎么做？」（附题目） | 先问你的思路和复杂度估计 → 完善正确思路 / 用反例引导发现漏洞 → 你尝试后才给参考代码 |
| 「我大二了，C++ 该怎么系统学？」 | 按你的目标与当前水平给出阶段路径与可验证里程碑 |

## 工作原理

安装后，Agent 遇到 C++ 问题时会按以下流程执行（详见 [`cpp-mentor/SKILL.md`](cpp-mentor/SKILL.md)）：

```
诊断 Assess ──→ 定位 Locate ──→ 建构 Build ──→ 引导 Guide ──→ 巩固 Consolidate
(2-3个问题)    (确认认知路径)   (类比→术语→    (预测/归因/     (要点+坑+
 L0-L3分级)                    最小代码→      迁移型提问)      自测题+下一步)
                                运行验证)
```

详细资料在 `cpp-mentor/references/` 四册手册中，按需加载：

| 文件 | 内容 |
|------|------|
| `teaching-playbook.md` | 五步流程完整操作手册：每步判断标准、话术示例、常见情况处置 |
| `level-assessment.md` | L0-L3 水平分级定义 + 11 个主题域诊断题库 + 盲点识别方法 |
| `explanation-techniques.md` | 类比库（含失效边界）、脚手架分级、提问话术库、迷思概念击破法 |
| `code-style.md` | 教学代码规范：最小示例模式、注释规范、版本处理、示例模板 |

## 目录结构

```
cpp-mentor-skill/
├── cpp-mentor/                  # Skill 本体（安装时拷贝这个目录）
│   ├── SKILL.md                 # 技能描述文件：元数据 + 教学指令主体
│   └── references/              # 四册详细参考资料（按需加载）
│       ├── teaching-playbook.md
│       ├── level-assessment.md
│       ├── explanation-techniques.md
│       └── code-style.md
├── .github/                     # Issue / PR 模板
├── CONTRIBUTING.md              # 贡献指南
├── LICENSE                      # MIT
└── README.md
```

## 环境要求与依赖

**运行时**：无任何代码依赖——Skill 全部由 Markdown 构成。

**平台要求**：任意支持 Agent Skill 规范（`SKILL.md` + YAML frontmatter：`name`、`description`）的 Agent 平台，例如：

- WorkBuddy（用户级 `~/.workbuddy/skills/` 或项目级 `.workbuddy/skills/`）
- Claude Code 及兼容平台

**开发/分发（可选）**：

- Python 3.x：用于运行 Skill 校验与打包脚本（见下）；
- 分发包 `cpp-mentor.zip` 为构建产物，默认不入库，可按需重新生成。

## 开发与迭代

```bash
# 1. 修改 Skill 源目录内容
vim cpp-mentor/SKILL.md
vim cpp-mentor/references/teaching-playbook.md

# 2. 校验（检查 frontmatter、命名规范、目录结构）
python scripts/validate.py cpp-mentor/

# 3. 重新生成分发包
python scripts/package.py cpp-mentor/ dist/

# 4. 同步到用户级安装目录（WorkBuddy）
cp -r cpp-mentor/ ~/.workbuddy/skills/cpp-mentor/
```

**测试建议**：Skill 的效果只能在真实教学中验证。每次修改后，用一个真实 C++ 问题触发，重点观察三个环节——① 是否先评估后讲解；② 卡壳时是否给阶梯提示而非直答；③ 收尾是否有点评、常见坑与自测题。

## 贡献指南

欢迎提交 Issue 和 Pull Request！请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。常见的贡献方向：

- 补充/修正迷思概念清单（附最小复现代码）；
- 增加新的类比（必须说明类比失效边界）；
- 扩充诊断题库或分场景策略；
- 改进教学话术与流程手册。

## 路线图

- [ ] 补充算法竞赛常见考点（DP、图论、数据结构）的专项引导策略
- [ ] 增加英文版讲解模式
- [ ] 收集真实教学会话案例，反哺流程手册

## 许可证

本项目采用 [MIT License](LICENSE) —— 可自由使用、修改与分发，保留版权声明即可。

## 参考

教学能力模型参考了公开的特级教师评选标准、教学名师指标体系与教学法研究，并结合 C++ 学科特点（编译模型、内存管理、标准演进快、陷阱密集）做了适配。
