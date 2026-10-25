# 学习室工程维护

共同源为 `/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship`。桌面包为 `/Users/rouen/Desktop/ICT 2022 学习室.app`。

## 数据与维护源

| 维护源 | 作用与产物 |
| --- | --- |
| `references/framework.json` | 阶段、原则、sessionPolicy与选学材料；构建生成framework.md和App体系数据。 |
| `references/lesson-evidence.json` | 已核读的字幕片段、来源hash与显式图片引用；归因流程见 [证据规范](evidence-and-extensions.md)。 |
| `references/frame-manifest.json` | 关键帧元数据；图注保留视觉核验状态。 |
| `references/practice.json` | 合成练习、policyVersion和参考动作；旧回答保留。 |
| `transcript_io.py` | 唯一字幕解析与片段校验实现；空稿、错误时间或不匹配证据应失败。 |
| `framework_extensions.py` | Macro时钟、时长、训练时段交集；不产生方向或交易权限。 |

构建链：`build_course_data.py` → 根目录 `courseData.json` → `build_study_room.py` → `study-room/{library-data,distill-data,course,version}.js` 与 `version.json`。

修改维护源，不直接修改生成数据；也不要误将已标待核验的旧讲义或旧模板重新导入为有效教学规则。`references/legacy-teaching-drafts.json`及历史讲义保留供对照。

## 正式笔记与恢复

StudyDataPath固定绑定正式数据目录，兼容旧包StudyRootPath。页面资源可回退到包内，笔记目录不能随页面可用性改变。绑定目录缺失时停止写入，不创建空白替代目录；只有无数据路径配置的独立分发包才使用Application Support/ICT2022Study。

保存通过requestId、内容token与revision确认，持有跨进程锁后检查版本，先保留有效快照再原子写正式文件。初始化不得自动写默认值；版本冲突、损坏、超限或备份失败时保留当前编辑并停止覆盖。

- **原生保存失败／超时**：先导出当前编辑，再核对正式文件与快照；不能循环重试同一覆盖。
- **缓存损坏**：保留原始字节，恢复副本写入成功后才替换缓存；原生仍可读取有效磁盘文件。
- **重读磁盘**：使用“保留编辑副本并重读磁盘笔记”，不自行回填旧快照。浏览器异常缓存可导出原文或保留副本后启用当前记录。
- **运行中的旧App**：先正常保存退出再重开；不要用killall强杀未保存编辑。

## 按改动验证

纯Skill／说明文档整理只做frontmatter、链接与差异检查，不重建课程或App。数据、行为或原生代码改变时，运行覆盖该改动的现有检查；没有新问题时不反复扩大验证。

从共同源执行必要的内容／前端检查：

```bash
python3 build_course_data.py
python3 build_study_room.py
python3 -m unittest discover -s tests -p 'test_*.py'
node tests/frontend.test.cjs
```

原生或打包相关变更需要隔离验收，使用独立目录：

```bash
ict_qa_dir=$(mktemp -d "${TMPDIR:-/tmp}/ict-qa.XXXXXX")
./study-room/native/build.sh "$ict_qa_dir/ICT 2022 学习室.app"
"$ict_qa_dir/ICT 2022 学习室.app/Contents/MacOS/ICT2022Study" --qa
```

QA读取包内Resources，使用统一真实路径、临时笔记和非持久WebView缓存；不得传入正式笔记作为fixture。有25秒上限，检查课程、题库、图片、扩展展示与两次保存／重载；失败返回非零。它验证工程行为，不验证交易理论。

`build.sh`先完成staging构建、签名和包校验，再归档同标识旧App并替换；失败恢复旧包。目标必须为绝对.app路径，不能是符号链接。必要检查通过后再安装桌面版；临时目录和旧包保留，清理遵循共享删除规则。

## 图解与版本

新增图解先核读片段、按需截帧、视觉确认并保留videoId、视频版本、时间与hash。用独立临时路径，不把大体积视频放入仓库；B站时间映射未核验时只链接分集。

版本包含source commit、dirty状态与课程／框架／练习内容指纹；Git不可读返回unknown。不同提交按祖先关系判断，不用时间先后。同步检查默认启动一次和手动检查，有超时与单次在途限制，不后台循环。
