# EV Hub 内容创作 Backlog

> 持续任务：北京时间 19:00 → 次日 7:00 不间断执行。
> 窗口：UTC 11:00 (19:00 CST) → UTC 23:00 (次日 7:00 CST)。
> 写作 skill：`deep-research-human-writer`（证据工程 + human 写作 + 立场块 + SEO/AIO/E-E-A-T + schema + QA）。
> 编排 skill：`content-cluster-upgrade`（每簇一个 collector 子代理并行）。
> 每篇完成后必须二次检查（红线/事实/立场块/来源/schema/内链）。

## 质量契约（每篇文章必须包含）
1. Quick Answer（1-2 句可抽取）
2. 定义块
3. ≥1 张结构化表（税率/参数/对比矩阵）
4. `## The Author's Take`（Position / Reasoning / Disclosure，第一人称）
5. 来源（编号 + 发布方 + URL + 日期）
6. 按实体关系做上下文内链
7. 零编造：抓不到标 UNKNOWN，证据优先
8. 红线词表命中 0（不编造价格/评级/测试结果/市场数据）

## 红线词表（grep 命中必须为 0）
- 编造类：`our test` / `we tested` / `我们的测试` / `根据我们工厂`（除非真有一手数据）
- 空洞 AI 腔：`In today's rapidly` / `It is important to note` / `In conclusion` / `Furthermore` / `Moreover` / `This comprehensive guide`

---

## 批次计划

### 批次 1 — Pillar C 高关税市场（5 篇）
状态：`pending`
- [ ] turkey-import-guide —— Import Chinese EV to Turkey（40% 关税 + 20% VAT + ÖTV）
- [ ] mexico-import-guide —— Import Chinese EV to Mexico（50% 关税 2026 新政）
- [ ] brazil-import-guide —— Import Chinese EV to Brazil（35% BEV 进口税）
- [ ] indonesia-import-guide —— Import Chinese EV to Indonesia（50% 关税，EV 免税到期）
- [ ] south-africa-import-guide —— Import Chinese EV to South Africa（25% 关税）

### 批次 2 — Pillar C 零/低关税市场（3 篇）
状态：`pending`
- [ ] norway-import-guide —— Import Chinese EV to Norway（0% 关税 + EV 免税，北欧标杆）
- [ ] switzerland-import-guide —— Import Chinese EV to Switzerland（4% 关税 + 8.1% VAT）
- [ ] canada-import-guide —— Import Chinese EV to Canada（100% 附加税废止，现 6.1%）

### 批次 3 — Pillar B 品牌 CVD 矩阵（20.7% 配合公司品牌，5 篇）
状态：`pending`
- [ ] chery-countervailing-duty —— Chery 20.7% CVD
- [ ] changan-countervailing-duty —— Changan 20.7% CVD
- [ ] nio-xpeng-leapmotor-countervailing-duty —— 新势力 20.7% CVD 群像
- [ ] zeekr-countervailing-duty —— Zeekr 18.8% CVD（Geely 系）
- [ ] xiaomi-hongqi-countervailing-duty —— 小米/红旗 20.7% CVD

### 批次 4 — Pillar D 车型旗舰对比（4 篇）
状态：`pending`
- [ ] byd-seal-vs-tesla-model-3 —— BYD Seal vs Tesla Model 3 landed cost
- [ ] byd-han-vs-tesla-model-s —— BYD Han vs Model S
- [ ] xiaomi-su7-vs-tesla-model-3 —— Xiaomi SU7 vs Model 3
- [ ] zeekr-001-vs-tesla-model-s —— Zeekr 001 vs Model S

---

## 数据源（文章可直接引用，无需重新研究）
- `src/data/tariffs.json` —— 30 国关税/VAT/注册费
- `src/data/market-master.json` —— 30 国完整税率 + notes
- `src/data/brand-master.json` —— 72 品牌 + vehicle_count
- `src/data/vehicle-master.json` —— 517 车
- `src/content/vehicles/*.md` —— 每车 30 市场 landed_cost_markets

## 进度追踪
- 每完成一篇，子代理返回后主 agent 二次检查，通过则 commit。
- 本文件用 `[x]` 标记已完成文章。
