# Phase 0《现有方案盘点》

- 项目：Bit浪浪 + X 公开交易者 + 经典流派 → 可复用股票分析/预测 Skill / Agent 资产
- 阶段：Phase 0（强制先行）
- 取证日期：2026-11-08（Asia/Shanghai）
- 研究范围：开源仓库官方 GitHub/API/README、产品官网/定价页、公开论文与知识产品索引
- 证据标记：`【原】` 官方仓库/官网/论文；`【推】` 基于公开功能归纳；`【待验证】` 尚未有一手证据

## 1. 一页结论

1. **已经有人做了人格化交易 Agent，但尚未完成“可信方法蒸馏”。** `virattt/ai-hedge-fund` 明确提供 Buffett/Munger/Cathie Wood 等 analyst personas；它把人格作为分析视角，最终由 portfolio manager 决策，但不能证明这些人物的真实方法已被严格还原。TradingAgents 也有 analyst / bull-bear / trader / risk / portfolio manager 角色，但更多是组织结构，不是某位交易者的可验证策略。
2. **规则的成熟度分层明显。** Qlib、FinRL-X、freqtrade、Nautilus、Zipline、Lumibot 的规则/回测/执行骨架较强；LLM 多智能体项目大多是自然语言分析、工具调用和辩论，回测逐步补齐，但“预测准确率”不是统一、可外推的结论。
3. **许可上可复用，但不能混用。** Apache-2.0/MIT/CC0 适合二次开发；GPL/AGPL/LGPL 需要按动态/静态链接、修改分发和网络服务边界做合规评估；`NOASSERTION`（如 TradingAgents-CN、OpenBB API 元数据）不能直接当作许可已确认。
4. **项目的真正差异化：** 建立“方法来源 → 可执行规则 → 最小回测 → 失效条件 → 证据等级 → 版本化 Skill”的蒸馏流水线；每个大师都必须能被审计，而不是只输出一段像大师口吻的文本。
5. **十位大师的第一版应是角色化研究组合，不是十个自动下单机器人。** 先做股票大盘/行业/个股研究与概率区间，统一经过风险闸门和回测，默认纸面研究。

## 2. 开源项目盘点

> Star、更新时间来自 GitHub REST API 快照；功能来自官方 README。Star 是采用度线索，不等于质量或收益证明。

| 项目 | 链接 / 许可 / Star / 最近更新 | 核心能力 | 可执行规则 | 回测/验证 | 目标用户 | 主要缺陷 | 结论 |
|---|---|---|---|---|---|---|---|
| TradingAgents | [GitHub](https://github.com/TauricResearch/TradingAgents) · Apache-2.0 · 121,230 · 2026-11-08 | LangGraph 多智能体：基本面/技术/情绪分析、Bull/Bear、Trader、Risk、Portfolio | 中：结构化信号与决策日志；策略规则仍依赖 LLM | **有**：ticker/date-grid、point-in-time、基准与决策结算 | 研究者、开发者 | 数据供应商/模型依赖；研究结论不是收益保证 | **可直接复用骨架** |
| ai-hedge-fund | [GitHub](https://github.com/virattt/ai-hedge-fund) · MIT · 64,554 · 2026-11-08 | Buffett/Munger/Cathie Wood 等角色辩论，PM 汇总；纸面交易与回测 | 中：人格提示词+组合决策；非严格人物策略 | **有**：backtest、benchmark、hash-chained paper ledger | 教学、个人研究 | 明确是教育/PoC；不能证明人格方法与真实交易一致 | **可借鉴人格层** |
| FinRobot | [GitHub](https://github.com/AI4Finance-Foundation/FinRobot) · Apache-2.0 · 8,392 · 2026-11-08 | 金融 Agent 平台；基本面/估值/市场预测/报告；代码计算与代理编排分离 | 中高：DCF/财务计算可执行，LLM 负责解释与编排 | **有**：forecast notebook、strategy writing/backtesting、provenance/evaluation | 研究、投行、量化原型 | 版本多、组件复杂；数据和模型成本高 | **可直接复用计算/溯源思想** |
| FinRL（原） | [GitHub](https://github.com/AI4Finance-Foundation/FinRL) · MIT · 17,017 · 2026-11-08 | 深度强化学习训练-测试-交易教学框架 | 高（环境/奖励/策略），不适合直接等同投资规则 | **有**：基准、回测、论文/示例 | 学术、研究者 | 原仓库偏教育；生产方向已转 FinRL-X | **可借鉴，生产用 FinRL-X** |
| FinRL-X / FinRL-Trading | [GitHub](https://github.com/AI4Finance-Foundation/FinRL-Trading) · Apache-2.0 · 3,916 · 2026-11-08 | weight-centric 选择/配置/择时/风险覆盖；回测到 Alpaca 执行一致 | 高：权重接口、交易成本、风险检查 | **有**：bt 引擎、基准、多账户纸面/实盘路径 | 专业量化、机构 | 依赖 Alpaca/数据适配；仍需本地数据验证 | **可直接复用接口思想** |
| FinGPT | [GitHub](https://github.com/AI4Finance-Foundation/FinGPT) · MIT · 21,538 · 2026-11-08 | 开源金融 LLM、情绪/预测模型、FinGPT-Forecaster | 中：模型预测接口；规则不是人格方法 | 有：公开数据集/基准与 demo；需自行复现 | 模型研究者 | 训练市场主要是 US/DOW30；时效与泛化需重测 | **可借鉴模型/数据流程** |
| Qlib | [GitHub](https://github.com/microsoft/qlib) · MIT · 50,114 · 2026-11-08 | 从数据、特征、模型、策略、执行到报告的量化流水线 | **高**：Alpha158、策略/执行器、配置化 workflow | **强**：qrun、信号分析、回测、基准 | 量化研究者 | 学习成本高；默认数据/因子不等于未来有效 | **核心回测底座** |
| OpenBB | [GitHub](https://github.com/OpenBB-finance/OpenBB) · API 显示 NOASSERTION（需查仓库 LICENSE） · 75,221 · 2026-11-08 | 数据终端与 AI agent 数据接口 | 低：数据/工具层，不定义策略 | 验证偏数据访问，不是策略回测 | 分析师、Agent 开发者 | 数据源许可/商业条款复杂；API 许可字段未确认 | **数据层可借鉴，先做许可审计** |
| freqtrade | [GitHub](https://github.com/freqtrade/freqtrade) · GPL-3.0 · 56,622 · 2026-11-08 | 加密交易 bot、策略、回测、超参优化、FreqAI | **高**：买卖、仓位、保护、超参 | **强**：backtesting、lookahead/recursive analysis、paper/live | 加密量化用户 | GPL 合规；主要针对加密，不等同 A 股/美股 | **可借鉴执行/回测，隔离许可** |
| NautilusTrader | [GitHub](https://github.com/nautechsystems/nautilus_trader) · LGPL-3.0 · 31,353 · 2026-11-08 | Rust 原生事件驱动；同一策略跑回测与 live | **高**：事件、订单、风险、策略 | **强**：多市场、多精度、live/backtest 差异文档 | 专业交易系统 | 工程复杂；LGPL 边界与 live 差异仍需审计 | **后期执行底座** |
| backtrader | [GitHub](https://github.com/mementum/backtrader) · GPL-3.0 · 23,690 · 2026-11-08 | Python 策略与回测骨架 | 高 | 有：成熟回测，但项目元数据/仓库状态需持续复核 | 个人量化、教学 | GPL；生态较旧；不含 LLM/数据治理 | **可借鉴，非首选新底座** |
| zipline-reloaded | [GitHub](https://github.com/stefan-jansen/zipline-reloaded) · Apache-2.0 · 2,008 · 2026-11-08 | 事件驱动回测，PyData/ML4T 生态 | 高 | 有：回测与 pyfolio；新项目官方建议评估 ML4T Backtest | 教学、研究 | 维护重点转移；不适合作为新系统唯一底座 | **可借鉴历史接口** |
| awesome-trading-agents | [GitHub](https://github.com/LLMQuant/awesome-trading-agents) · CC0-1.0 · 987 · 2026-11-08 | 专门收录 LLM Agents、MCP、Skills、回测工具 | 取决于条目；目录本身不执行 | 目录标注 benchmark/backtesting，但需逐项核验 | 选型、研究 | 聚合清单，不是质量背书；条目许可证/活跃度不同 | **Phase 0 关键索引** |
| TradingAgents-CN | [GitHub](https://github.com/hsliuping/TradingAgents-CN) · API 为 NOASSERTION · 32,835 · 2026-11-08 | TradingAgents 中文增强、Tushare/AkShare、A 股语境 | 中：继承多智能体决策，不等于本土策略规则 | 有限：继承框架能力；本地化结果需单独验证 | 中文/A 股研究者 | 许可证未从 API 确认；数据与监管适配需实测 | **可借鉴中文适配，先做许可确认** |
| Trading-R1 | [GitHub](https://github.com/TauricResearch/Trading-R1) · Apache-2.0 · 582 · 2026-11-08 | 终端式金融研究/分析，research/analytical 模式、报告导出、工具/skills | 中：工具驱动分析，不是固定策略 | 目前更像研究终端；回测证据有限 | 研究者、分析师 | 依赖 Tauric API/密钥；早期访问阶段 | **可借鉴研究终端交互** |
| Vibe-Trading | [GitHub](https://github.com/HKUDS/Vibe-Trading) · MIT · 37,860 · 2026-11-08 | A 股/港股/美股/加密等多市场 personal trading agent，Skills+MCP，研究资产版本化 | 中高：策略/回测工作流与纸面模拟 | **有**：backtest、研究证据复用、A 股 paper simulation | 个人研究者 | 多市场依赖多供应商；AI 结论仍需独立验证 | **可直接借鉴工作流** |
| OpenAlice | [GitHub](https://github.com/TraderAlice/OpenAlice) · AGPL-3.0 · 7,430 · 2026-11-08 | 研究→进场→持仓管理→退出的单 Agent；Trading-as-Git | 中高：生命周期与审批工作流 | 有：backtest/paper/live 方向，但需逐项复现 | 个人/开发者 | AGPL；实盘风险；人格蒸馏仍较弱 | **可借鉴生命周期，不直接复制** |
| Lumibot | [GitHub](https://github.com/Lumiwealth/lumibot) · GPL-3.0 · 2,217 · 2026-11-07 | 股票/期权/期货/外汇/加密回测、paper/live、AI team | 高 | **强**：同一代码回测→live | 个人/小团队 | GPL；数据依赖 Polygon 等 | **可借鉴回测接口** |
| NOFX | [GitHub](https://github.com/NoFxAiOS/nofx) · AGPL-3.0 · 13,237 · 2026-11-08 | Frontier 审批 + Autopilot；策略、规模、限额、交易所运行时 | 中高 | 有：paper/live/leaderboard；成绩真实性要独立审计 | 个人加密交易 | AGPL；模型输出与真实边际未证 | **只借鉴硬风控/审批** |

### 开源选型结论

- **首选组合：** `TradingAgents`（多角色编排） + `FinRobot`（代码计算、来源和报告） + `Qlib`（研究/回测） + `FinRL-X` 的 weight-centric 合约（统一策略输出） + `Vibe-Trading` 的研究资产版本化思路。
- **后期可选：** NautilusTrader / Lumibot（执行与回测一致性）；freqtrade 仅用于加密实验。
- **许可证红线：** GPL/AGPL/LGPL 项目不能在未做分发与链接边界审查前直接嵌入闭源 Skill；`NOASSERTION` 项目不作为已许可依赖。

## 3. 付费产品盘点

| 产品 | 官方链接 | 公开价格/用户量 | 核心能力 | 可验证成绩/规则 | 主要缺陷 / 适用结论 |
|---|---|---|---|---|---|
| Fintwit.ai | [官网](https://fintwit.ai/) · [Plans](https://fintwit.ai/plans) | Premium $9/月或$69/年；Pro $19/月或$149/年（官网 meta/页面） | 实时追踪 X 投资者、AI 股票分析、信号/评级；Pro 提供 Claude/ChatGPT/Cursor MCP | 有信号追踪与 MCP；不是券商核验收益 | 适合做 X 信号抓取/研究接口，不代表交易者能力已验证 |
| Kinfo | [官网](https://kinfo.com/) | 价格以官网/账户为准，未在本次公开页确认 | 直连券商的 verified trading journal，跟踪/验证/分享绩效 | **强**：券商连接是可验证成绩的参考标准 | 覆盖范围与数据权限需核实；可作为 X 交易者证据门槛 |
| Composer | [官网](https://www.composer.trade/) | 本次网络环境未稳定抓取官方定价 | 自然语言/规则组合、自动化投资与回测 | 有策略回测/自动化概念；需核实数据和实盘口径 | 付费产品闭源，规则表达可借鉴但不可复制实现 |
| Tickeron | [官网](https://tickeron.com/) | 本次页面受 Cloudflare 影响，价格未核实 | AI 模式识别、预测、扫描器 | 有历史信号/模式展示；独立统计验证有限 | 预测营销风险较高，不能直接作为大师训练数据 |
| Danelfin | [官网](https://danelfin.com/) | 本次页面受 Cloudflare 影响，价格未核实 | AI 股票评分/选股 | 有评分历史叙事；需独立验证真实可交易收益 | 评分黑盒；适合当外部基准，不当方法来源 |
| Kavout | [官网](https://www.kavout.com/) · [Pricing](https://www.kavout.com/pricing-plans) | Free $0；公开页显示 $16/月、$39/月年付档 | InvestGPT、AI Stock Picker、Smart Signals、11,000+资产 | 有研究 credits/评分；非券商核验 | 可借鉴“研究 Agent + 信号”产品形态，规则透明度不足 |
| Boosted.ai | [官网](https://boosted.ai/) | 本次未稳定抓到定价 | 面向机构的 AI 投资/组合管理 | 机构产品通常有回测/组合分析，但未找到公开可复现规则 | 适合作为机构产品对标，不直接复用 |
| PortfolioPilot | [官网](https://portfoliopilot.com/) · [Pricing](https://portfoliopilot.com/pricing) | Free；Gold $20年付/$29月付；Platinum $49年付/$99月付；Pro $99年付/$149月付 | AI 财务顾问、组合跟踪、税务/资产分析 | 组合诊断与建议，不是公开交易者实盘核验 | 可借鉴组合级输出和分层付费，非方法来源 |
| Magnifi | [官网](https://www.magnifi.com/) | 本次未稳定抓到定价 | 投资搜索、组合/交易辅助、对话式投资工具 | 规则与绩效透明度有限 | 作为产品体验对标，不作为证据来源 |
| eToro Popular Investors | [官网](https://www.etoro.com/copytrader/) | 费用/地区规则按官网 | 公开账户、CopyTrader、Popular Investor 体系 | **有**：账户级历史表现、风险指标（需逐账户核验） | 平台绩效受选择/费用/市场影响；可做公开成绩样本 |
| Darwinex | [官网](https://www.darwinex.com/) | 费用/条款按官网 | 可投资策略、风险标准化、交易者评价 | **强**：策略级 track record / 风险指标 | 产品/资产/地区限制；可借鉴“策略可投资化+风险标准化” |
| Collective2 | [官网](https://collective2.com/) | 费用按策略/订阅 | 策略市场、信号订阅、绩效页 | **有**：公开策略历史与统计 | 需警惕选择性披露和订阅费；可做验证样本 |

## 4. 已被人提炼的知识产品/论文

| 知识产品 | 链接 | 已提炼内容 | 规则/验证判断 | 我们能否直接用 |
|---|---|---|---|---|
| TradingAgents 论文与仓库 | [论文](https://arxiv.org/abs/2412.20138) | 多角色金融研究/交易流程、辩论与组合决策 | 有框架与实验，但不是某位大师的真实交易记录 | 可复用架构，不能宣称大师复现 |
| AI Hedge Fund README/论文式实现 | [仓库](https://github.com/virattt/ai-hedge-fund) | Buffett/Munger/Cathie Wood 等人格分析师 | 有 backtest/paper ledger，但人格规则主要是提示词与代码逻辑 | 可借鉴人格层，必须重建来源与规则 |
| FinRobot whitepaper | [论文](https://arxiv.org/abs/2405.14767) | 代码计算、Agent 编排、报告与验证分层 | 强调 provenance/evaluation；具体收益需自行复现 | 可直接借鉴工程原则 |
| FinGPT-Forecaster | [仓库](https://github.com/AI4Finance-Foundation/FinGPT/tree/master/fingpt/FinGPT_Forecaster) | 新闻+财务的市场预测模型与 DOW30 数据集 | 有模型/数据集/benchmark；市场范围有限 | 可借鉴预测评测，不作为大师方法 |
| FinRL / FinRL-X 论文与示例 | [仓库](https://github.com/AI4Finance-Foundation/FinRL) | RL 环境、奖励、回测、基准和部署一致性 | 可执行规则强，但依赖数据与奖励设定 | 可借鉴验证管线 |
| Qlib / Alpha158 | [文档](https://qlib.readthedocs.io/) | 因子、预测、策略、执行、回测工作流 | 规则可执行、实验可重复；不能跳过数据泄露与容量检查 | 核心研究底座候选 |
| ML4T / Zipline 生态 | [Zipline](https://github.com/stefan-jansen/zipline-reloaded) | 事件驱动回测、因子研究、PyData | 回测成熟，维护重点已转 ML4T Backtest | 只借鉴接口与教材方法 |
| Awesome Trading Agents | [仓库](https://github.com/LLMQuant/awesome-trading-agents) | Agent/MCP/Skill/回测生态索引 | 目录本身不提供验证；每个条目要单独复核 | Phase 0 选型入口 |
| 经典流派教材/访谈（O'Neil、海龟、Livermore、Buffett 等） | 需逐条建立原始书籍/访谈索引 | 原则、筛选条件、风险与执行纪律 | 常是叙事与经验，参数需回测；二手内容混杂 | 作为“原始方法假设”而非事实收益 |

## 5. 四个必须回答的问题

### 5.1 是否有人把具体人的方法蒸馏成 Agent/Skill？

**有雏形，没有完成品。**

- `ai-hedge-fund` 已把 Buffett/Munger/Cathie Wood 等人格放入 Agent roster；这是“人物视角/提示词角色”，不是经过原始访谈、交易记录、时间序列和反事实检验的严格方法蒸馏。
- `TradingAgents` 的 Analyst/Researcher/Trader/Risk/Portfolio Manager 是岗位人格，不是具体交易者。
- `awesome-trading-agents` 已收录人格化与 Skill/MCP 项目，但目录也明确它是索引，不是验证层。
- 对 X 公开交易者而言，本次尚未找到满足 Kinfo/Darwinex/eToro/Collective2 或长时间可交叉验证序列的统一公开数据库；在 Phase 2 前一律 `待验证`，不得进入最终资产。

### 5.2 规则是真规则还是自然语言复述？

- **真规则/可回测：** Qlib、FinRL-X、freqtrade、Nautilus、Zipline、Lumibot 的策略、权重、订单、成本、回测接口；TradingAgents/ai-hedge-fund 目前是“分析流程+部分回测”。
- **半规则：** FinRobot 的 DCF/财务计算、Vibe-Trading 的研究/回测工作流、Kavout 的研究 credits/信号输出。
- **自然语言为主：** 多数人格提示词、X 交易者观点、经典流派的二手解读；没有触发条件、过滤条件、仓位、止损与失效条件就不能称为可执行规则。

### 5.3 许可是否允许二次开发？

- **友好：** Apache-2.0（TradingAgents、FinRobot、FinRL-X、Zipline、Trading-R1）、MIT（ai-hedge-fund、FinRL、Qlib、FinGPT、Vibe-Trading）、CC0（awesome-trading-agents）。仍需保留 NOTICE/版权与数据源条款。
- **需隔离/审查：** GPL-3.0（freqtrade、backtrader、Lumibot）、AGPL-3.0（OpenAlice、NOFX）、LGPL-3.0（Nautilus）。能否作为服务、是否分发衍生代码、链接方式都要让法务/工程复核。
- **未确认：** TradingAgents-CN 与 OpenBB API 返回 `NOASSERTION`；必须直接查 LICENSE 文件与依赖条款，不能凭星标或 fork 推断。
- **付费产品：** 闭源、条款驱动，只能使用公开功能/接口，不复制内部实现或内容。

### 5.4 我们的差异化

不是再造一个 TradingAgents，而是做五件现有项目通常没有同时完成的事：

1. **来源可追溯：** 每条方法规则绑定课程文件/课节、原书/访谈、原始推文或账户证据。
2. **规则编译：** 把“观点/金句”编译成输入字段、触发条件、过滤器、仓位、退出和失效状态。
3. **证据分级：** `【原】`、`【转】`、`【推】`、`【待验证】`，把宣传和收益证据分开。
4. **统一回测契约：** 所有大师输出同一结构，至少有样本期、基准、交易成本、胜率、盈亏比、最大回撤、期望值和容量限制。
5. **时代适配：** 把人工盯盘、信息差、T+0、散户结构变化等“时代依赖”显式放进 L4 失效层，禁止把旧方法直接当成今日信号。

## 6. 六维评分表（1–5 分）

评分维度：相关性 / 可复用性 / 许可友好度 / 维护活跃度 / 规则可执行性 / 验证严谨度。总分为简单平均，供选型使用，不代表投资收益。

| 项目 | 相 | 复 | 许 | 活 | 规 | 验 | 均分 | 结论 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| TradingAgents | 5 | 5 | 5 | 5 | 3 | 4 | 4.5 | **可直接复用**：多角色/回测/时间点基础 |
| ai-hedge-fund | 5 | 4 | 5 | 5 | 3 | 3 | 4.2 | **可借鉴思路**：人格层与 paper ledger |
| FinRobot | 5 | 5 | 5 | 5 | 3 | 4 | 4.5 | **可直接复用**：计算与溯源原则 |
| Qlib | 5 | 5 | 5 | 5 | 5 | 5 | 5.0 | **可直接复用**：量化研究/回测底座 |
| FinRL-X | 4 | 5 | 5 | 4 | 5 | 4 | 4.5 | **可直接复用**：权重契约与部署一致性 |
| Vibe-Trading | 5 | 5 | 5 | 5 | 4 | 4 | 4.7 | **可直接复用**：Skills/MCP/研究资产版本化 |
| FinGPT | 4 | 4 | 5 | 3 | 3 | 3 | 3.7 | **可借鉴思路**：金融模型/预测评测 |
| freqtrade | 3 | 4 | 2 | 5 | 5 | 4 | 3.8 | **可借鉴思路**：执行/回测；许可隔离 |
| NautilusTrader | 3 | 5 | 3 | 5 | 5 | 5 | 4.3 | **可借鉴思路**：后期执行底座 |
| Zipline-reloaded | 3 | 3 | 5 | 4 | 5 | 4 | 4.0 | **可借鉴思路**：历史回测接口 |
| awesome-trading-agents | 5 | 5 | 5 | 5 | 1 | 1 | 3.7 | **可直接复用为索引**，不当验证证据 |
| TradingAgents-CN | 5 | 4 | 1 | 5 | 3 | 3 | 3.5 | **可借鉴思路**，先确认许可证 |
| Fintwit.ai | 5 | 4 | 闭源 | 4 | 3 | 2 | 3.6 | **可借鉴思路**：X 信号/MCP |
| Kinfo | 4 | 3 | 闭源 | 4 | 4 | 5 | 4.0 | **可直接借鉴证据标准** |
| eToro/Darwinex/Collective2 | 4 | 3 | 闭源 | 4 | 4 | 5 | 4.0 | **可借鉴验证机制** |
| Tickeron/Danelfin/Kavout | 3 | 3 | 闭源 | 4 | 2 | 2 | 2.8 | **明确放弃作为方法来源** |
| PortfolioPilot/Magnifi/Boosted.ai | 3 | 3 | 闭源 | 3 | 2 | 2 | 2.6 | **可借鉴产品形态**，不作规则来源 |

## 7. 对“十个股票分析/大盘预测大师”的建议形态

第一版不是十个互相独立的“喊涨跌模型”，而是十个有明确边界的研究角色，统一输出概率、证据、失效条件和回测接口：

1. 大盘趋势/市场状态（趋势跟踪）
2. 宏观流动性与利率
3. 价值/质量
4. 成长/盈利加速
5. CANSLIM/相对强度
6. 技术结构/波段
7. 订单流/微观结构（数据允许时）
8. 情绪周期/A 股风格
9. 量化因子/统计信号
10. 风险与组合裁判（不追求预测，负责否决、降权和失效检测）

每个角色必须共用：`假设 → 数据 → 信号 → 触发 → 过滤 → 仓位建议（纸面）→ 退出 → 失效 → 证据 → 回测`。最终由一个“证据裁判”汇总，而不是让十个角色简单投票。

## 8. 当前阶段门禁与下一步

**Phase 0 结论：有条件进入 Phase 1。**

进入条件：你确认接受上述开源复用边界、许可证分层和“X 交易者未验证不入库”规则。

Phase 1 开始后才做：

- 盘点 `N:\Bit浪浪学习视频等多个文件` 全部文件；按核心课程/辅助材料/重复无关聚类；估算转写成本。
- 只抽样转写，不全量硬啃 36.5GB。
- 建立第一版来源索引和课程级结构化笔记。

本报告不包含投资建议，不构成买入/卖出或收益承诺。
