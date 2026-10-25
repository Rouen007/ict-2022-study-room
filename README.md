# ICT 2022 学习室

本地 No-Rant 37 集原稿、62 张关键帧、条件分析框架与练习，以及 macOS WKWebView 学习室。

## 当前证据范围

2026-10-25 修复了课程归因、保存和构建问题。37集全部可读，但只对 Ep.03、22、29 的所列部分字幕要点完成本轮核读。其他旧中文讲义、图注保留为待复核资料，折叠显示；不把资料覆盖数当成教学验证数。

- [当前训练框架](references/framework.md)（由 framework.json 生成）
- [核读证据](references/lesson-evidence.json)
- [工程维护与测试](references/study-app-architecture.md)
- [修复报告](REPAIR_REPORT.md)

## 使用

浏览器直接打开 `study-room/index.html`。浏览器笔记保存在当前浏览器缓存，请导出备份；原生正式笔记是独立的数据来源。

macOS安装需要 Xcode Command Line Tools：

```bash
./study-room/native/build.sh
open "$HOME/Desktop/ICT 2022 学习室.app"
```

构建先生成完整新包，再把旧包移入桌面 `.ict-app-archives/`。不会删除旧App；编译失败不影响旧包。若旧App正在运行，先正常保存退出，再打开新版，不要强制终止带有未保存笔记的进程。

## 修改与验证

```bash
python3 build_course_data.py
python3 build_study_room.py
python3 -m unittest discover -s tests -p 'test_*.py'
node tests/frontend.test.cjs
```

原生 `--qa` 使用临时笔记与独立缓存，检查37课、3题、62张图和两次保存重载；失败返回非零退出。完整命令见工程维护文档。

新课证据在 `references/lesson-evidence.json` 中显式绑定原稿hash与时间；图片使用frameId，不再按数组位置自动配图。B站中配尚未核对时间偏移，仅提供分集链接。

## 笔记与恢复

开发安装固定绑定 `study-room/notebook.json`，即使源码页面缺失也不切换数据目录。只有未配置数据路径的独立分发包才使用 `~/Library/Application Support/ICT2022Study/`；已绑定目录不可用时停止写入。每次保存先核对内容token，保留前后快照并原子写入。冲突或损坏时阻止覆盖；可导出当前编辑或点击“保留编辑副本并重读磁盘笔记”。恢复副本在该WebView的本地缓存中，仍应导出JSON作为持久备份。

手帐区分计划、已平仓、取消、未成交和无交易；计划毛目标不等于实际盈利。既有笔记与旧版回答不会被迁移脚本改写或删除。旧版回答不与新版合成题重新评分。

课程材料仅作为教学与条件分析；Execute是练习状态，不代表真实成交或下单授权。
