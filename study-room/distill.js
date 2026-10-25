(function () {
  function getDistillRoot() {
    return window.LESSON_DISTILL || { framework: { chain: [], principles: [] }, lessons: {} };
  }

  function escapeText(value) {
    return String(value || '')
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;');
  }

  function principleMap(framework) {
    return Object.fromEntries((framework.principles || []).map((item) => [item.id, item]));
  }

  function stageMap(framework) {
    const list = framework.chain || framework.stages || [];
    return Object.fromEntries(list.map((item) => [item.id, { id: item.id, name: item.title || item.name, question: item.question }]));
  }

  function renderRichRuleCase(c, lessonId) {
    if (typeof c === 'string') {
      return `<p class="dscene">${escapeText(c)}</p>`;
    }
    const figures = Array.isArray(c.figures) && c.figures.length
      ? `
        <div class="dfigure-grid">
          ${c.figures.map((fig) => `
            <figure class="dfigure">
              <img src="${escapeText(fig.src)}" alt="${escapeText(fig.caption || c.title || '课程原图')}" loading="lazy" />
              <figcaption>${escapeText(fig.caption || '')}</figcaption>
            </figure>
          `).join('')}
        </div>
      `
      : '';
    const readItems = c.read || c.reading || [];
    const reading = Array.isArray(readItems) && readItems.length
      ? `
        <div class="dblock">
          <strong>图与原片怎么读（按顺序）</strong>
          <ol class="dread">
            ${readItems.map((item) => `
              <li><span class="who who-${escapeText(item.who || '主模型')}">${escapeText(item.who || '拆解')}</span>${escapeText(item.text || item.point || '')}</li>
            `).join('')}
          </ol>
        </div>
      `
      : '';
    const plan = Array.isArray(c.plan) && c.plan.length
      ? `
        <div class="dblock">
          <strong>落到你的计划</strong>
          <ul class="dplan">
            ${c.plan.map((item) => `<li>${escapeText(item)}</li>`).join('')}
          </ul>
        </div>
      `
      : '';
    const trap = c.trap
      ? `<div class="dtrap"><strong>易错：</strong>${escapeText(c.trap)}</div>`
      : '';
    const figureGuide = c.figureGuide
      ? `<div class="dfig-guide"><strong>看图抓手：</strong>${escapeText(c.figureGuide)}</div>`
      : '';
    return `
      <div class="dcase" data-lesson="${escapeText(lessonId)}">
        ${c.scene ? `<p class="dscene">${escapeText(c.scene)}</p>` : ''}
        ${figureGuide}
        ${figures}
        ${reading}
        ${plan}
        ${trap}
      </div>
    `;
  }

  window.renderFrameworkExtensions = function renderFrameworkExtensions() {
    const extensions = getDistillRoot().framework?.extensions;
    if (!extensions || (!extensions.macros?.length && !extensions.htf)) return '';
    const spans = list => (list || []).map(pair => pair.join('–')).join('、') || '无';
    const macros = (extensions.macros || []).map(item => `
      <tr data-macro-id="${escapeText(item.id)}">
        <td><strong>${escapeText(item.time)}</strong><br><small>${escapeText(item.session)}</small></td>
        <td>${escapeText(item.durationMinutes)}分钟</td>
        <td>${escapeText(item.focus)}<br><small>来源待核对</small></td>
        <td>${escapeText(spans(item.entryIntersections))}</td>
        <td>${escapeText(spans(item.outsideEntryWindows))}</td>
      </tr>`).join('');
    const htf = extensions.htf;
    return `
      <details class="framework-extensions" data-study-extensions>
        <summary>选学补充 · Macro 时间窗口与高周期偏向（来源待核对）</summary>
        <p>${escapeText(extensions.notice)}</p>
        <p class="muted">时区：America/New_York。年份与具体原课片段待核验；窗口时长分别计算。</p>
        ${macros ? `<div class="extension-table-wrap"><table class="extension-table"><thead><tr><th>观察时段</th><th>时长</th><th>观察重点</th><th>训练新开仓时间交集</th><th>不新增交易的部分</th></tr></thead><tbody>${macros}</tbody></table></div>` : ''}
        <p class="muted">交集仅说明时间条件，仍需满足完整入场规则；右端点不含。已有持仓按事前计划管理。</p>
        <p class="muted">NYSE主板15:50开始公布收盘竞价不平衡，16:00开始收盘竞价。Macro观察窗口与该流程分别记录。<a href="https://www.nyse.com/trade/auctions" target="_blank" rel="noopener">查看NYSE官方时间表 ↗</a></p>
        ${htf ? `<div class="extension-htf"><strong>高周期分析笔记 · 待原课核验</strong><p>${escapeText(htf.dailyBiasAnchor)}</p><p>${escapeText(htf.dealingRangeExpansion)}</p><small>${escapeText(htf.source)}</small></div>` : ''}
      </details>`;
  };

  window.renderLessonDistill = function renderLessonDistill(lesson) {
    const root = getDistillRoot();
    const framework = root.framework || {};
    const lessonsMap = root.lessons || {};
    const key = lesson.rawId || (`ep${String(lesson.id).padStart(2, '0')}`);
    const item = lessonsMap[key] || lessonsMap[lesson.id];
    if (!item) return '';
    const pMap = principleMap(framework);
    const sMap = stageMap(framework);

    const cases = item.cases || item.rules || [];
    const stageIds = new Set(item.stages || []);
    cases.forEach((c) => {
      (c.principles || []).forEach((pid) => {
        if (pMap[pid] && pMap[pid].stage) stageIds.add(pMap[pid].stage);
      });
    });

    const stages = Array.from(stageIds)
      .map((id) => sMap[id])
      .filter(Boolean)
      .map((stage) => `<span class="dstage" title="${escapeText(stage.question)}">${escapeText(stage.name)}</span>`)
      .join('');

    const rulesHtml = cases.map((c, index) => {
      const pills = (c.principles || [])
        .map((id) => pMap[id])
        .filter(Boolean)
        .map((p) => `<button class="dpill" type="button" data-open-map="${escapeText(p.id)}">${escapeText(p.id)} ${escapeText(p.title)}</button>`)
        .join('');
      const summaryLabel = c.title ? `看例子：${c.title}` : '看本课例子 / 原片拆解';
      const detailOpen = index === 0 ? ' open' : '';
      return `
        <div class="drule">
          <div class="dgist">
            <span><b class="dnum">${index + 1}</b>${escapeText(c.gist || c.title || '')}</span>
            <span class="dpills">${pills}</span>
          </div>
          <details class="dexample"${detailOpen}>
            <summary>${escapeText(summaryLabel)}</summary>
            ${renderRichRuleCase(c, lesson.id)}
          </details>
        </div>
      `;
    }).join('');

    return `
      <section class="distill" aria-label="本课提炼">
        <div class="dhead">
          <div>
            <p class="eyebrow">本课提炼 · 先抓骨架，再往下读原片图解与双语讲义</p>
            <strong>本课在 ICT 2022 体系里的位置</strong>
          </div>
          <div class="dstages">${stages}</div>
        </div>
        <p class="muted"><strong>核验范围：</strong>${escapeText(item.gaps || '待核验')}</p>
        <p class="dcore"><strong>本课状态：</strong>${escapeText(item.core)}</p>
        <div class="drules">${rulesHtml}</div>
        <div class="ddrill">
          <span><strong>自测一问：</strong>${escapeText(item.drill)}</span>
          <button class="ghost small" type="button" data-open-map="">查看完整体系地图</button>
        </div>
      </section>
    `;
  };

  window.openSystemMap = function openSystemMap(focusPrincipleId, onSelectLesson) {
    const dialog = document.getElementById('systemMap');
    const body = document.getElementById('systemMapBody');
    if (!dialog || !body) return;
    const root = getDistillRoot();
    const framework = root.framework || {};
    const sMap = stageMap(framework);
    const lessonByPrinciple = {};
    Object.entries(root.lessons || {}).forEach(([lessonKey, data]) => {
      const numId = String(lessonKey).replace(/^ep/i, '').padStart(2, '0');
      (data.cases || data.rules || []).forEach((c) => {
        (c.principles || []).forEach((pid) => {
          lessonByPrinciple[pid] = lessonByPrinciple[pid] || new Set();
          lessonByPrinciple[pid].add(numId);
        });
      });
    });

    const chainList = framework.chain || framework.stages || [];
    body.innerHTML = `
      <div>
        <p class="eyebrow">学习室条件分析框架 v2 · 证据不足时可以停在任一步</p>
        <div class="map-stages">
          ${chainList.map((stage) => `
            <div class="map-stage">
              <span>${escapeText(stage.id)}</span>
              <strong>${escapeText(stage.title || stage.name)}</strong>
              <small>${escapeText(stage.question)}</small>
            </div>
          `).join('')}
        </div>
      </div>
      <div>
        <p class="eyebrow">12 条训练原则 · 主模型归纳，非市场必然规律</p>
        <div class="map-principles">
          ${(framework.principles || []).map((p) => {
            const stage = sMap[p.stage];
            const lessons = Array.from(lessonByPrinciple[p.id] || []);
            return `
              <article class="map-p ${p.id === focusPrincipleId ? 'focus' : ''}" id="map-${escapeText(p.id)}">
                <div class="map-p-head">
                  <strong>${escapeText(p.id)} · ${escapeText(p.title)}</strong>
                  <span class="dstage">${escapeText(stage ? stage.name : p.stage)}</span>
                </div>
                <p>${escapeText(p.rule || p.summary || '')}</p>
                <p class="muted"><strong>常见陷阱：</strong>${escapeText(p.trap || p.action || '')}</p>
                <div class="map-links">
                  ${lessons.map((id) => `<button class="ghost small" type="button" data-map-lesson="${escapeText(id)}">Ep.${escapeText(id)}</button>`).join('')}
                </div>
              </article>
            `;
          }).join('')}
        </div>
      </div>
    `;

    body.innerHTML += window.renderFrameworkExtensions();

    body.querySelectorAll('[data-map-lesson]').forEach((btn) => {
      btn.addEventListener('click', () => {
        const id = btn.dataset.mapLesson;
        dialog.close();
        if (onSelectLesson) onSelectLesson(id);
      });
    });

    if (!dialog.open) dialog.showModal();
    if (focusPrincipleId) {
      const target = document.getElementById(`map-${focusPrincipleId}`);
      if (target) target.scrollIntoView({ block: 'center', behavior: 'smooth' });
    }
  };
})();
