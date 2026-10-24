# 教学复盘点评与个人网站同步规范

> **Created by Xiao Ang** · 用于点评 `study-room/notebook.json` 学习记录及同步 `/Users/rouen/Documents/rouen-docs-site/docs/kol/ict/`。

---

## 一、如何点评用户的「复制接续请求」(`notebook.json`)

当用户在「06 我的笔记」点击「复制接续请求」发来提示时：

1. **读取本地正式记录**：
   - 路径：`/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room/notebook.json`
2. **四维诊断顺序**：
   - **① 分课笔记与总结 (`summaryNote` / `lessonNotes`)**：检查用户是否真正理解了「散户突破 = 算法扫损燃料」与「必须先扫高周期流动性池，再看低周期 MSS + FVG」，而不是把 FVG 当成孤立的 K 线形态。
   - **② 引导练习原答 (`answers` / `attemptHistory`)**：
     - 对比用户选择的动作（`Wait / Armed / Execute / Cancel / Exit`）与标准答案；
     - 重点看用户写的 `reason` 是否包含三个硬证据：**哪侧流动性池被扫 (`BSL/SSL`) + 哪个周期出现位移结构破坏 (`BMS/MSS`) + FVG 是否位于 `0.5` 均衡线以外的折价/溢价区**。
   - **③ Ep.04 复盘手帐 (`journalEntries`)**：
     - 检查入场价 (E)、止损位 (S) 与目标位 (T) 的盈亏比（R:R）是否合理，评论中是否注明了纽约时间窗口（`08:30–11:00` 或 `13:30–16:00`）且避开了 `12:00–13:00` 午休禁区。
   - **④ 下一步训练处方**：
     - 每次只聚焦纠正 1–2 个最核心的执行偏差，并指定下一集要看的重点时间戳或下一组练习题。

---

## 二、同步更新个人网站专栏 (`rouen-docs-site`)

当新增了后续集数（如 `Ep.06–Ep.12`）的图文精读手册时：

1. 将新增的 `lesson-assets/*.png` 同步复制到 `/Users/rouen/Documents/rouen-docs-site/docs/kol/ict/assets/`。
2. 在 `/Users/rouen/Documents/rouen-docs-site/docs/kol/ict/` 下新增或更新对应 Markdown 文档（图片统一使用 `./assets/xxx.png` 相对路径，顶部保留 `Created by Xiao Ang` 署名）。
3. 如新增了独立章节页面，同步在 `/Users/rouen/Documents/rouen-docs-site/docs/.vitepress/config.mjs` 的 `kolSidebar`（`🎯 ICT 2022 体系` 分组）和 `docs/kol/ict/index.md` 中添加链接。
4. 在 `/Users/rouen/Documents/rouen-docs-site` 下运行 `npm run docs:build`，确认搜索索引安全守卫（`[guard] ✅`）全部通过后再 `git commit` 与 `git push origin main`。
