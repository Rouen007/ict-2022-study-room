import React, { useState, useRef, useEffect, useMemo } from 'react';
import {
  Play,
  BookOpen,
  Layers,
  CheckCircle2,
  Circle,
  Search,
  ExternalLink,
  Maximize2,
  ChevronLeft,
  ChevronRight,
  Clock,
  Sparkles,
  FileText,
  ClipboardCheck,
  Eye,
  EyeOff,
  X,
  PanelLeftClose,
  PanelLeftOpen,
  Film,
  Tv,
  Trash2,
  PlusCircle
} from 'lucide-react';
import rawCourseData from './data/courseData.json';

interface KeyPoint {
  timeStr: string;
  seconds: number;
  titleZh: string;
  detailZh: string;
}

interface Keyframe {
  id: string;
  file: string;
  timeStr: string;
  seconds: number;
  timeframe: string;
  mtfOrder?: number;
  titleZh: string;
  captionZh: string;
}

interface TranscriptSegment {
  range: string;
  startSec: number;
  text: string;
}

interface Episode {
  ep: number;
  videoId: string;
  biliUrl: string;
  youtubeUrl: string;
  hasLocalVideo: boolean;
  localVideoUrl: string | null;
  titleEn: string;
  titleZh: string;
  module: string;
  tags: string[];
  summaryZh: string;
  durationSec: number;
  wordCount: number;
  keyPoints: KeyPoint[];
  keyframes: Keyframe[];
  segments: TranscriptSegment[];
}

interface GlossaryItem {
  term: string;
  nameZh: string;
  category: string;
  definition: string;
  episodes: number[];
}

interface JournalEntry {
  id: string;
  date: string;
  symbol: 'NQ' | 'ES' | 'MNQ' | 'MES';
  direction: 'SHORT (溢价区做空)' | 'LONG (折价区做多)';
  mssToEntryMins: string;
  entryToTargetMins: string;
  heatHandles: string;
  capturedHandles: string;
  notes: string;
}

const courseData = rawCourseData as {
  courseTitle: string;
  bilibiliUrl: string;
  youtubePlaylistUrl: string;
  totalEpisodes: number;
  glossary: GlossaryItem[];
  episodes: Episode[];
};

const CHECKLIST_ITEMS = [
  {
    id: 'step1',
    title: '1. 纽约时区与主力合约检查 (NY Time & Open Interest)',
    desc: 'TradingView 右下角已锁定 New York (UTC-5/4)；若临近 3/6/9/12 月第 3 个周五前一周，已在 Barchart 核对 Open Int 完成换月。'
  },
  {
    id: 'step2',
    title: '2. 周/日线偏向与流动性磁铁 (HTF Draw on Liquidity)',
    desc: '明确今日日线价格是被吸向上方的买方止损 (BSL) / 看跌失衡区，还是下方的卖方止损 (SSL) / 看涨失衡区。'
  },
  {
    id: 'step3',
    title: '3. 15m 风向标高低点与时间窗口 (Bellwether & Killzones)',
    desc: '已画出 08:30 垂直线与 12:00–13:00 午休禁区，标出亚盘、伦敦盘及 08:30 左侧最近的 15m 波段高点与波段低点（尤其留意相对等高点）。'
  },
  {
    id: 'step4',
    title: '4. 止损猎杀 + 高能量位移 MSS (Stop Raid & Displacement)',
    desc: '08:30/09:30（或下午 13:30）后价格已刺穿关键 BSL/SSL，并在 5m/2m/1m 图上以“大象跳进儿童泳池”式大 K 线反向突破短期波段高/低点，突破连续阳/阴线订单块开盘价。'
  },
  {
    id: 'step5',
    title: '5. 50% 均衡点过滤 + 干净三K线 FVG 挂单 (Equilibrium & FVG)',
    desc: '拉取当前波段 0–100% 斐波那契：做空进场点必须位于 >50% 溢价区 (Premium) 的看跌 FVG 内（阳线回抽卖出）；做多必须位于 <50% 折价区 (Discount) 的看涨 FVG 内（阴线回踩买入）。若首波回落无 FVG 坚决放弃！'
  },
  {
    id: 'step6',
    title: '6. 止损锚定与内外流动性分批止盈 (Risk & Targets)',
    desc: '止损置于猎杀极值或位移大 K 线外；第一止盈挂在 50% 另一侧的内部反向 FVG，第二止盈挂在外部波段高低点止损池。严守 12:00–13:00 午休不持险单。'
  }
];

const HIGHLIGHT_REGEX = new RegExp(
  '\\b(fair value gap|fvg|imbalance|buyside|buy stops|sellside|sell stops|liquidity|market structure shift|market structure|equilibrium|discount|premium|order block|state of delivery|displacement|spooling|relative equal highs|three drives|open interest|market on close)\\b',
  'gi'
);

function formatDuration(sec: number): string {
  const m = Math.floor(sec / 60);
  const s = sec % 60;
  return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
}

function highlightTranscriptText(text: string) {
  const parts = text.split(HIGHLIGHT_REGEX);
  return parts.map((part, idx) => {
    if (HIGHLIGHT_REGEX.test(part)) {
      return (
        <span key={idx} className="term-highlight">
          {part}
        </span>
      );
    }
    return part;
  });
}

export default function App() {
  const [selectedEpNum, setSelectedEpNum] = useState<number>(2); // Default to Ep.02 (Core Model Overview with 7 MTF frames)
  const [sidebarOpen, setSidebarOpen] = useState<boolean>(true);
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [epFilter, setEpFilter] = useState<'all' | 'illustrated' | 'uncompleted'>('all');

  // Persisted state
  const [completedEps, setCompletedEps] = useState<number[]>(() => {
    try {
      const saved = localStorage.getItem('ict2022_completed_eps');
      return saved ? JSON.parse(saved) : [1, 2];
    } catch {
      return [1, 2];
    }
  });

  const [epNotes, setEpNotes] = useState<Record<number, string>>(() => {
    try {
      const saved = localStorage.getItem('ict2022_ep_notes');
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  const [journalEntries, setJournalEntries] = useState<JournalEntry[]>(() => {
    try {
      const saved = localStorage.getItem('ict2022_journal');
      return saved
        ? JSON.parse(saved)
        : [
            {
              id: 'sample-1',
              date: '2022-01-21 (Ep.02 示范)',
              symbol: 'NQ',
              direction: 'SHORT (溢价区做空)',
              mssToEntryMins: '4 分钟',
              entryToTargetMins: '18 分钟',
              heatHandles: '3.50 pts',
              capturedHandles: '122.50',
              notes: '15m 扫掉 14,820 相对等高点 BSL，2m 跌破 14,808 触发 BMS，回抽溢价区 FVG 在 14,798 空，折价区内部 FVG 14,675 平仓。'
            }
          ];
    } catch {
      return [];
    }
  });

  // Video & MTF stage state
  const [videoSource, setVideoSource] = useState<'local' | 'youtube'>('local');
  const [currentTime, setCurrentTime] = useState<number>(0);
  const [ytStartSec, setYtStartSec] = useState<number>(0);
  const [activeKeyframeIdx, setActiveKeyframeIdx] = useState<number>(0);
  const [blindQuizMode, setBlindQuizMode] = useState<boolean>(false);
  const [quizRevealed, setQuizRevealed] = useState<boolean>(false);
  const [lightboxFrame, setLightboxFrame] = useState<Keyframe | null>(null);

  // Right panel tabs
  const [rightTab, setRightTab] = useState<'notes' | 'transcript' | 'checklist'>('notes');
  const [transcriptSearch, setTranscriptSearch] = useState<string>('');
  const [checkedSteps, setCheckedSteps] = useState<Record<string, boolean>>({});
  const [glossaryOpen, setGlossaryOpen] = useState<boolean>(false);

  // New journal form state
  const [jSymbol, setJSymbol] = useState<'NQ' | 'ES' | 'MNQ' | 'MES'>('NQ');
  const [jDir, setJDir] = useState<'SHORT (溢价区做空)' | 'LONG (折价区做多)'>('SHORT (溢价区做空)');
  const [jMssTime, setJMssTime] = useState('');
  const [jHoldTime, setJHoldTime] = useState('');
  const [jHeat, setJHeat] = useState('');
  const [jHandles, setJHandles] = useState('');
  const [jNotes, setJNotes] = useState('');

  const videoRef = useRef<HTMLVideoElement | null>(null);

  const currentEp = useMemo(
    () => courseData.episodes.find((e) => e.ep === selectedEpNum) || courseData.episodes[0],
    [selectedEpNum]
  );

  // Reset frame index & video source when switching episode
  useEffect(() => {
    setActiveKeyframeIdx(0);
    setQuizRevealed(false);
    setCurrentTime(0);
    setYtStartSec(0);
    if (currentEp.hasLocalVideo) {
      setVideoSource('local');
    } else {
      setVideoSource('youtube');
    }
  }, [currentEp.ep, currentEp.hasLocalVideo]);

  useEffect(() => {
    localStorage.setItem('ict2022_completed_eps', JSON.stringify(completedEps));
  }, [completedEps]);

  useEffect(() => {
    localStorage.setItem('ict2022_ep_notes', JSON.stringify(epNotes));
  }, [epNotes]);

  useEffect(() => {
    localStorage.setItem('ict2022_journal', JSON.stringify(journalEntries));
  }, [journalEntries]);

  const toggleEpisodeDone = (ep: number, e: React.MouseEvent) => {
    e.stopPropagation();
    setCompletedEps((prev) => (prev.includes(ep) ? prev.filter((x) => x !== ep) : [...prev, ep]));
  };

  // Seek video & sync MTF keyframe
  const seekToSeconds = (sec: number) => {
    setCurrentTime(sec);
    if (videoSource === 'local' && videoRef.current) {
      videoRef.current.currentTime = sec;
      videoRef.current.play().catch(() => {});
    } else {
      setYtStartSec(sec);
    }
    // Also match closest keyframe if episode has keyframes
    if (currentEp.keyframes.length > 0) {
      let bestIdx = 0;
      let bestDiff = Infinity;
      currentEp.keyframes.forEach((kf, idx) => {
        const diff = Math.abs(kf.seconds - sec);
        if (diff < bestDiff) {
          bestDiff = diff;
          bestIdx = idx;
        }
      });
      setActiveKeyframeIdx(bestIdx);
    }
  };

  // Filtered episodes for sidebar
  const filteredEpisodes = useMemo(() => {
    const q = searchQuery.trim().toLowerCase();
    return courseData.episodes.filter((ep) => {
      if (epFilter === 'illustrated' && ep.keyframes.length === 0) return false;
      if (epFilter === 'uncompleted' && completedEps.includes(ep.ep)) return false;
      if (!q) return true;
      const inMeta =
        ep.titleZh.toLowerCase().includes(q) ||
        ep.titleEn.toLowerCase().includes(q) ||
        ep.summaryZh.toLowerCase().includes(q) ||
        ep.tags.some((t) => t.toLowerCase().includes(q));
      if (inMeta) return true;
      return ep.segments.some((seg) => seg.text.toLowerCase().includes(q));
    });
  }, [searchQuery, epFilter, completedEps]);

  // Group filtered episodes by module
  const groupedEpisodes = useMemo(() => {
    const groups: Record<string, Episode[]> = {};
    filteredEpisodes.forEach((ep) => {
      if (!groups[ep.module]) groups[ep.module] = [];
      groups[ep.module].push(ep);
    });
    return groups;
  }, [filteredEpisodes]);

  const activeKeyframe: Keyframe | null =
    currentEp.keyframes.length > 0
      ? currentEp.keyframes[Math.min(activeKeyframeIdx, currentEp.keyframes.length - 1)]
      : null;

  // Determine currently active transcript segment based on video currentTime
  const activeSegmentIdx = useMemo(() => {
    let idx = 0;
    for (let i = 0; i < currentEp.segments.length; i++) {
      if (currentTime >= currentEp.segments[i].startSec) {
        idx = i;
      } else {
        break;
      }
    }
    return idx;
  }, [currentEp.segments, currentTime]);

  const filteredSegments = useMemo(() => {
    const q = transcriptSearch.trim().toLowerCase();
    if (!q) return currentEp.segments;
    return currentEp.segments.filter((s) => s.text.toLowerCase().includes(q));
  }, [currentEp.segments, transcriptSearch]);

  const checkedCount = Object.values(checkedSteps).filter(Boolean).length;

  const handleAddJournal = (e: React.FormEvent) => {
    e.preventDefault();
    if (!jHandles.trim()) return;
    const newEntry: JournalEntry = {
      id: Date.now().toString(),
      date: new Date().toISOString().slice(0, 10) + ` (Ep.${String(currentEp.ep).padStart(2, '0')})`,
      symbol: jSymbol,
      direction: jDir,
      mssToEntryMins: jMssTime || '3 分钟',
      entryToTargetMins: jHoldTime || '15 分钟',
      heatHandles: jHeat || '2.0 pts',
      capturedHandles: jHandles,
      notes: jNotes
    };
    setJournalEntries([newEntry, ...journalEntries]);
    setJMssTime('');
    setJHoldTime('');
    setJHeat('');
    setJHandles('');
    setJNotes('');
  };

  const calcDollarValue = (symbol: 'NQ' | 'ES' | 'MNQ' | 'MES', handlesStr: string) => {
    const num = parseFloat(handlesStr);
    if (isNaN(num)) return null;
    const mult = symbol === 'ES' ? 50 : symbol === 'NQ' ? 20 : symbol === 'MES' ? 5 : 2;
    return (num * mult).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
  };

  return (
    <div className="app-shell">
      {/* Top Bar */}
      <header className="top-header">
        <div className="brand-group">
          <button
            className="btn btn-sm"
            onClick={() => setSidebarOpen(!sidebarOpen)}
            title={sidebarOpen ? '收起课程目录' : '展开课程目录'}
          >
            {sidebarOpen ? <PanelLeftClose size={15} /> : <PanelLeftOpen size={15} />}
          </button>
          <span className="brand-badge">ICT 2022 NO RANT</span>
          <h1 className="brand-title">沉浸式精读工作台 · 37集全库 & 多周期图谱终端</h1>
        </div>

        <div className="header-controls">
          <div className="progress-pill">
            <span>学习进度</span>
            <div className="progress-bar-wrap">
              <div
                className="progress-bar-fill"
                style={{ width: `${Math.round((completedEps.length / 37) * 100)}%` }}
              />
            </div>
            <span className="mono">
              {completedEps.length}/37 ({Math.round((completedEps.length / 37) * 100)}%)
            </span>
          </div>

          <button className="btn btn-amber" onClick={() => setGlossaryOpen(true)}>
            <BookOpen size={15} />
            <span>ICT 核心概念词典 (12)</span>
          </button>

          <a
            href={currentEp.biliUrl}
            target="_blank"
            rel="noreferrer"
            className="btn"
            title="在 B 站打开当前集数的 AI 中配版"
          >
            <Tv size={14} />
            <span>B站 P{currentEp.ep}</span>
            <ExternalLink size={12} />
          </a>

          <a
            href={currentEp.youtubeUrl}
            target="_blank"
            rel="noreferrer"
            className="btn"
            title="在 YouTube 打开 SirTrader 无废话原片"
          >
            <Film size={14} />
            <span>YouTube 原片</span>
            <ExternalLink size={12} />
          </a>
        </div>
      </header>

      {/* Main 3-Column Workspace */}
      <div className={`main-workspace ${sidebarOpen ? '' : 'sidebar-collapsed'}`}>
        {/* Left Sidebar: 37 Episodes */}
        <aside className="sidebar">
          <div className="sidebar-search-box">
            <div className="search-input-wrap">
              <Search size={14} />
              <input
                type="text"
                className="search-input"
                placeholder="搜全 37 集标题 / 概念 / 英文原词..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
            </div>
            <div className="filter-pills">
              <button
                className={`filter-pill ${epFilter === 'all' ? 'active' : ''}`}
                onClick={() => setEpFilter('all')}
              >
                全部 (37)
              </button>
              <button
                className={`filter-pill ${epFilter === 'illustrated' ? 'active' : ''}`}
                onClick={() => setEpFilter('illustrated')}
              >
                📸 含1080p图谱 (Ep 1-5)
              </button>
              <button
                className={`filter-pill ${epFilter === 'uncompleted' ? 'active' : ''}`}
                onClick={() => setEpFilter('uncompleted')}
              >
                未学完 ({37 - completedEps.length})
              </button>
            </div>
          </div>

          <div className="episode-list">
            {Object.entries(groupedEpisodes).map(([modName, eps]) => (
              <div key={modName}>
                <div className="module-header">{modName}</div>
                {eps.map((ep) => {
                  const isDone = completedEps.includes(ep.ep);
                  const isActive = ep.ep === selectedEpNum;
                  return (
                    <div
                      key={ep.ep}
                      className={`ep-item ${isActive ? 'active' : ''}`}
                      onClick={() => setSelectedEpNum(ep.ep)}
                    >
                      <button
                        className={`ep-check-btn ${isDone ? 'done' : ''}`}
                        onClick={(e) => toggleEpisodeDone(ep.ep, e)}
                        title={isDone ? '标记为未学' : '标记为已掌握'}
                      >
                        {isDone ? <CheckCircle2 size={16} /> : <Circle size={16} />}
                      </button>
                      <div className="ep-item-body">
                        <div className="ep-item-top">
                          <span className="ep-num">EP.{String(ep.ep).padStart(2, '0')}</span>
                          <div className="ep-badges">
                            {ep.keyframes.length > 0 && (
                              <span className="badge-mini">📸 {ep.keyframes.length}图</span>
                            )}
                            <span className="badge-duration">{formatDuration(ep.durationSec)}</span>
                          </div>
                        </div>
                        <div className="ep-title-zh">{ep.titleZh}</div>
                        <div className="ep-title-en">{ep.titleEn}</div>
                      </div>
                    </div>
                  );
                })}
              </div>
            ))}
          </div>
        </aside>

        {/* Center Visual Stage: Video Player + Multi-Timeframe Chart Slider */}
        <section className="visual-stage">
          <div className="stage-toolbar">
            <div className="tab-group">
              {currentEp.hasLocalVideo && (
                <button
                  className={`tab-btn ${videoSource === 'local' ? 'active' : ''}`}
                  onClick={() => setVideoSource('local')}
                >
                  <Film size={14} />
                  <span>本地 1080p 原片流 (离线秒开)</span>
                </button>
              )}
              <button
                className={`tab-btn ${videoSource === 'youtube' ? 'active' : ''}`}
                onClick={() => setVideoSource('youtube')}
              >
                <Play size={14} />
                <span>YouTube 嵌入源 (全37集同步)</span>
              </button>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <span className="mono" style={{ fontSize: 12, color: 'var(--accent-cyan)' }}>
                <Clock size={12} style={{ verticalAlign: '-2px', marginRight: 4 }} />
                当前联动时间: {formatDuration(Math.floor(currentTime))}
              </span>
            </div>
          </div>

          {/* Video Player Box */}
          <div className="video-container">
            {videoSource === 'local' && currentEp.localVideoUrl ? (
              <video
                ref={videoRef}
                key={currentEp.localVideoUrl}
                src={currentEp.localVideoUrl}
                controls
                onTimeUpdate={(e) => setCurrentTime(e.currentTarget.currentTime)}
              />
            ) : (
              <iframe
                key={`${currentEp.videoId}-${ytStartSec}`}
                src={`https://www.youtube.com/embed/${currentEp.videoId}?start=${Math.floor(
                  ytStartSec
                )}&autoplay=${ytStartSec > 0 ? 1 : 0}&rel=0`}
                title={currentEp.titleEn}
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              />
            )}
          </div>

          {/* Multi-Timeframe Keyframe Deck */}
          <div className="mtf-deck">
            {currentEp.keyframes.length > 0 && activeKeyframe ? (
              <>
                <div className="mtf-header-bar">
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <Layers size={16} color="var(--accent-amber)" />
                    <span style={{ fontSize: 13.5, fontWeight: 700 }}>
                      多周期关键帧滑块 ({activeKeyframeIdx + 1} / {currentEp.keyframes.length})
                    </span>
                  </div>

                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <button
                      className={`btn btn-sm ${blindQuizMode ? 'btn-amber' : ''}`}
                      onClick={() => {
                        setBlindQuizMode(!blindQuizMode);
                        setQuizRevealed(false);
                      }}
                      title="遮挡下方 ICT 文字解析，先自己看图找流动性池与 FVG"
                    >
                      {blindQuizMode ? <EyeOff size={13} /> : <Eye size={13} />}
                      <span>{blindQuizMode ? '盘感自测模式：开启' : '开启盘感盲测'}</span>
                    </button>

                    <button
                      className="btn btn-sm"
                      disabled={activeKeyframeIdx === 0}
                      onClick={() => {
                        const nextIdx = Math.max(0, activeKeyframeIdx - 1);
                        setActiveKeyframeIdx(nextIdx);
                        setQuizRevealed(false);
                      }}
                    >
                      <ChevronLeft size={14} />
                      <span>上一帧</span>
                    </button>
                    <button
                      className="btn btn-sm"
                      disabled={activeKeyframeIdx === currentEp.keyframes.length - 1}
                      onClick={() => {
                        const nextIdx = Math.min(
                          currentEp.keyframes.length - 1,
                          activeKeyframeIdx + 1
                        );
                        setActiveKeyframeIdx(nextIdx);
                        setQuizRevealed(false);
                      }}
                    >
                      <span>下一帧</span>
                      <ChevronRight size={14} />
                    </button>
                  </div>
                </div>

                {/* Timeframe Switcher Pills (1W -> 1D -> 1H -> 15m -> 2m) */}
                <div className="mtf-pills">
                  {currentEp.keyframes.map((kf, idx) => (
                    <button
                      key={kf.id}
                      className={`mtf-pill ${idx === activeKeyframeIdx ? 'active' : ''}`}
                      onClick={() => {
                        setActiveKeyframeIdx(idx);
                        setQuizRevealed(false);
                      }}
                    >
                      <span>{kf.timeframe}</span>
                      <span style={{ opacity: 0.65, fontSize: 10.5 }}>[{kf.timeStr}]</span>
                    </button>
                  ))}
                </div>

                {/* Smooth Slider Bar */}
                {currentEp.keyframes.length > 1 && (
                  <div className="mtf-slider-row">
                    <span className="mono" style={{ fontSize: 11, color: 'var(--text-muted)' }}>
                      HTF 宏观
                    </span>
                    <input
                      type="range"
                      min={0}
                      max={currentEp.keyframes.length - 1}
                      value={activeKeyframeIdx}
                      onChange={(e) => {
                        setActiveKeyframeIdx(Number(e.target.value));
                        setQuizRevealed(false);
                      }}
                      className="mtf-range-input"
                    />
                    <span className="mono" style={{ fontSize: 11, color: 'var(--accent-amber)' }}>
                      LTF 狙击
                    </span>
                  </div>
                )}

                {/* Active Keyframe Card */}
                <div className="keyframe-viewer-card">
                  <div
                    className="keyframe-img-wrap"
                    onClick={() => setLightboxFrame(activeKeyframe)}
                    title="点击放大查看 1080p 原图细节"
                  >
                    <img
                      src={`/frames/${activeKeyframe.file}`}
                      alt={activeKeyframe.titleZh}
                    />
                    <div className="keyframe-overlay-bar">
                      <button
                        className="keyframe-overlay-pill"
                        onClick={(e) => {
                          e.stopPropagation();
                          seekToSeconds(activeKeyframe.seconds);
                        }}
                      >
                        <Play size={12} color="var(--accent-amber)" />
                        <span>跳转视频 [{activeKeyframe.timeStr}]</span>
                      </button>

                      <button
                        className="keyframe-overlay-pill"
                        onClick={(e) => {
                          e.stopPropagation();
                          setLightboxFrame(activeKeyframe);
                        }}
                      >
                        <Maximize2 size={12} />
                        <span>全屏高清放大</span>
                      </button>
                    </div>
                  </div>

                  <div className="keyframe-meta">
                    {blindQuizMode && !quizRevealed ? (
                      <div
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'space-between',
                          gap: 12,
                          padding: '6px 0'
                        }}
                      >
                        <div style={{ fontSize: 13, color: 'var(--accent-amber)' }}>
                          🤔 <strong>盘感盲测思考</strong>：请先在上方图表中指出：1) 哪一侧止损池被猎杀？ 2) 波段突破位 (MSS) 在哪？ 3) 进场 FVG 与 50% 目标位在哪？
                        </div>
                        <button
                          className="btn btn-primary btn-sm"
                          onClick={() => setQuizRevealed(true)}
                        >
                          <Eye size={13} />
                          <span>揭晓 ICT 解析</span>
                        </button>
                      </div>
                    ) : (
                      <>
                        <div className="keyframe-meta-title">
                          <span>{activeKeyframe.titleZh}</span>
                          <span className="time-jump-badge" onClick={() => seekToSeconds(activeKeyframe.seconds)} style={{ cursor: 'pointer' }}>
                            <Play size={11} /> {activeKeyframe.timeStr}
                          </span>
                        </div>
                        <p className="keyframe-meta-desc">{activeKeyframe.captionZh}</p>
                      </>
                    )}
                  </div>
                </div>
              </>
            ) : (
              <div
                style={{
                  background: 'var(--bg-panel)',
                  border: '1px solid var(--border-subtle)',
                  borderRadius: 10,
                  padding: 20,
                  textAlign: 'center',
                  color: 'var(--text-secondary)'
                }}
              >
                <p style={{ fontSize: 13.5, marginBottom: 6 }}>
                  💡 当前集数（<strong>Ep.{String(currentEp.ep).padStart(2, '0')}</strong>）已接入 <strong>YouTube 原片视频流 + 全量英文时间戳逐字稿 + 中文核心提要</strong>。
                </p>
                <p style={{ fontSize: 12, color: 'var(--text-muted)' }}>
                  点击右侧任意 <code className="mono">[MM:SS]</code> 时间戳即可直接驱动上方视频跳转到对应秒数（前 5 集额外内置 22 张 1080p 多周期原片截图滑块）。
                </p>
              </div>
            )}
          </div>
        </section>

        {/* Right Panel: Bilingual Study Notes, Live Synced Transcript, Checklist & Journal */}
        <section className="study-panel">
          <div className="stage-toolbar">
            <div className="tab-group">
              <button
                className={`tab-btn ${rightTab === 'notes' ? 'active' : ''}`}
                onClick={() => setRightTab('notes')}
              >
                <Sparkles size={14} />
                <span>中文精读 & 时间戳</span>
              </button>
              <button
                className={`tab-btn ${rightTab === 'transcript' ? 'active' : ''}`}
                onClick={() => setRightTab('transcript')}
              >
                <FileText size={14} />
                <span>英文原片逐字稿 ({currentEp.segments.length}段)</span>
              </button>
              <button
                className={`tab-btn ${rightTab === 'checklist' ? 'active' : ''}`}
                onClick={() => setRightTab('checklist')}
              >
                <ClipboardCheck size={14} />
                <span>6步清单 & 复盘手帐</span>
              </button>
            </div>
          </div>

          <div className="study-content">
            {rightTab === 'notes' && (
              <>
                <div className="ep-hero-card">
                  <div className="ep-hero-tags">
                    <span className="tag-chip">{currentEp.module}</span>
                    {currentEp.tags.map((t) => (
                      <span key={t} className="tag-chip">
                        #{t}
                      </span>
                    ))}
                  </div>
                  <h2 className="ep-hero-title">
                    Ep.{String(currentEp.ep).padStart(2, '0')} · {currentEp.titleZh}
                  </h2>
                  <div className="ep-hero-sub mono">
                    {currentEp.titleEn} · 时长 {formatDuration(currentEp.durationSec)} · 词数{' '}
                    {currentEp.wordCount.toLocaleString()} words
                  </div>
                  <div className="ep-summary-box">{currentEp.summaryZh}</div>
                </div>

                <div className="section-heading">
                  <Clock size={14} color="var(--accent-amber)" />
                  <span>核心时间轴节点（点击卡片同步跳转视频 & 图谱）</span>
                </div>

                {currentEp.keyPoints.map((kp, i) => (
                  <div
                    key={i}
                    className="keypoint-card"
                    onClick={() => seekToSeconds(kp.seconds)}
                  >
                    <div className="keypoint-top">
                      <span className="time-jump-badge">
                        <Play size={10} />
                        {kp.timeStr}
                      </span>
                      <span className="keypoint-title">{kp.titleZh}</span>
                    </div>
                    <div className="keypoint-detail">{kp.detailZh}</div>
                  </div>
                ))}

                {currentEp.keyframes.length > 0 && (
                  <>
                    <div className="section-heading">
                      <Layers size={14} color="var(--accent-cyan)" />
                      <span>本集多周期图谱索引 ({currentEp.keyframes.length} 张 1080p 截图)</span>
                    </div>
                    {currentEp.keyframes.map((kf, idx) => (
                      <div
                        key={kf.id}
                        className="keypoint-card"
                        style={{
                          borderColor:
                            idx === activeKeyframeIdx ? 'var(--accent-amber)' : undefined
                        }}
                        onClick={() => {
                          setActiveKeyframeIdx(idx);
                          seekToSeconds(kf.seconds);
                        }}
                      >
                        <div className="keypoint-top">
                          <span className="time-jump-badge">{kf.timeframe}</span>
                          <span className="mono" style={{ fontSize: 11.5, color: 'var(--text-muted)' }}>
                            [{kf.timeStr}]
                          </span>
                          <span className="keypoint-title">{kf.titleZh}</span>
                        </div>
                        <div className="keypoint-detail">{kf.captionZh}</div>
                      </div>
                    ))}
                  </>
                )}

                <div className="section-heading">
                  <BookOpen size={14} color="var(--accent-emerald)" />
                  <span>本集个人复盘笔记（自动保存在浏览器本地）</span>
                </div>
                <textarea
                  rows={5}
                  style={{
                    width: '100%',
                    background: 'var(--bg-card)',
                    border: '1px solid var(--border-subtle)',
                    borderRadius: 8,
                    padding: 12,
                    color: 'var(--text-primary)',
                    fontSize: 13,
                    lineHeight: 1.6,
                    outline: 'none'
                  }}
                  placeholder={`在这里记录你学习 Ep.${String(currentEp.ep).padStart(
                    2,
                    '0'
                  )} 的心得、疑问或 TradingView 回测发现...`}
                  value={epNotes[currentEp.ep] || ''}
                  onChange={(e) =>
                    setEpNotes({ ...epNotes, [currentEp.ep]: e.target.value })
                  }
                />
              </>
            )}

            {rightTab === 'transcript' && (
              <>
                <div style={{ marginBottom: 14, display: 'flex', gap: 8 }}>
                  <div className="search-input-wrap" style={{ flex: 1 }}>
                    <Search size={14} />
                    <input
                      type="text"
                      className="search-input"
                      placeholder="在本集英文逐字稿中搜索关键词 (如 fair value gap, stops, equilibrium)..."
                      value={transcriptSearch}
                      onChange={(e) => setTranscriptSearch(e.target.value)}
                    />
                  </div>
                </div>

                <div style={{ fontSize: 12, color: 'var(--text-muted)', marginBottom: 12 }}>
                  💡 点击任意段落即可将左侧播放器精准跳转至该分钟；黄色高亮词为 ICT 核心机构订单流术语。
                </div>

                {filteredSegments.map((seg, idx) => {
                  const isCurrent =
                    !transcriptSearch && idx === activeSegmentIdx;
                  return (
                    <div
                      key={seg.range}
                      className={`transcript-segment ${isCurrent ? 'active-seg' : ''}`}
                      onClick={() => seekToSeconds(seg.startSec)}
                    >
                      <div className="seg-header">
                        <span className="time-jump-badge">
                          <Play size={10} /> [{seg.range}]
                        </span>
                        {isCurrent && (
                          <span
                            className="mono"
                            style={{ fontSize: 11, color: 'var(--accent-cyan)' }}
                          >
                            ● 当前播放段落
                          </span>
                        )}
                      </div>
                      <div className="seg-text">{highlightTranscriptText(seg.text)}</div>
                    </div>
                  );
                })}
              </>
            )}

            {rightTab === 'checklist' && (
              <>
                <div
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    marginBottom: 12
                  }}
                >
                  <div className="section-heading" style={{ margin: 0 }}>
                    <ClipboardCheck size={15} color="var(--accent-emerald)" />
                    <span>ICT 2022 实盘开仓 6 步核对清单 ({checkedCount}/6)</span>
                  </div>
                  <button
                    className="btn btn-sm"
                    onClick={() => setCheckedSteps({})}
                  >
                    重置清单
                  </button>
                </div>

                {CHECKLIST_ITEMS.map((item) => {
                  const isChecked = !!checkedSteps[item.id];
                  return (
                    <div
                      key={item.id}
                      className={`checklist-card ${isChecked ? 'checked' : ''}`}
                      onClick={() =>
                        setCheckedSteps({ ...checkedSteps, [item.id]: !isChecked })
                      }
                    >
                      <div style={{ paddingTop: 2 }}>
                        {isChecked ? (
                          <CheckCircle2 size={18} color="var(--accent-emerald)" />
                        ) : (
                          <Circle size={18} color="var(--text-muted)" />
                        )}
                      </div>
                      <div>
                        <div
                          style={{
                            fontSize: 13.5,
                            fontWeight: 600,
                            color: isChecked ? 'var(--accent-emerald)' : 'var(--text-primary)',
                            marginBottom: 4
                          }}
                        >
                          {item.title}
                        </div>
                        <div style={{ fontSize: 12.5, color: 'var(--text-secondary)', lineHeight: 1.5 }}>
                          {item.desc}
                        </div>
                      </div>
                    </div>
                  );
                })}

                {/* Ep.04 Standard Study Journal */}
                <div className="section-heading" style={{ marginTop: 24 }}>
                  <BookOpen size={15} color="var(--accent-amber)" />
                  <span>ICT Ep.04 标准四维复盘手帐记录器 (Study Journal)</span>
                </div>

                <form className="journal-form" onSubmit={handleAddJournal}>
                  <div className="form-field">
                    <label>合约品种</label>
                    <select
                      value={jSymbol}
                      onChange={(e) => setJSymbol(e.target.value as any)}
                    >
                      <option value="NQ">NQ (纳指标准 $20/点)</option>
                      <option value="ES">ES (标普标准 $50/点)</option>
                      <option value="MNQ">MNQ (微型纳指 $2/点)</option>
                      <option value="MES">MES (微型标普 $5/点)</option>
                    </select>
                  </div>

                  <div className="form-field">
                    <label>多空方向</label>
                    <select
                      value={jDir}
                      onChange={(e) => setJDir(e.target.value as any)}
                    >
                      <option value="SHORT (溢价区做空)">SHORT (溢价区做空)</option>
                      <option value="LONG (折价区做多)">LONG (折价区做多)</option>
                    </select>
                  </div>

                  <div className="form-field">
                    <label>1. MSS 到回抽 FVG 耗时</label>
                    <input
                      type="text"
                      placeholder="例: 4 分钟"
                      value={jMssTime}
                      onChange={(e) => setJMssTime(e.target.value)}
                    />
                  </div>

                  <div className="form-field">
                    <label>2. 进场到触及目标耗时</label>
                    <input
                      type="text"
                      placeholder="例: 18 分钟"
                      value={jHoldTime}
                      onChange={(e) => setJHoldTime(e.target.value)}
                    />
                  </div>

                  <div className="form-field">
                    <label>3. 最大逆向浮亏 (Heat Weathered)</label>
                    <input
                      type="text"
                      placeholder="例: 3.25 pts"
                      value={jHeat}
                      onChange={(e) => setJHeat(e.target.value)}
                    />
                  </div>

                  <div className="form-field">
                    <label>4. 捕获整点数 (Handles)</label>
                    <input
                      type="text"
                      placeholder="例: 45.0"
                      value={jHandles}
                      onChange={(e) => setJHandles(e.target.value)}
                      required
                    />
                  </div>

                  <div className="form-field full-width">
                    <label>复盘备注（猎杀池子 / 进场 FVG 价位 / 50% 均衡目标）</label>
                    <input
                      type="text"
                      placeholder="例: 09:30 扫掉 14,820 等高点 BSL，2m BMS + 溢价区 FVG 进场..."
                      value={jNotes}
                      onChange={(e) => setJNotes(e.target.value)}
                    />
                  </div>

                  <div className="form-field full-width">
                    <button type="submit" className="btn btn-primary" style={{ justifyContent: 'center' }}>
                      <PlusCircle size={15} />
                      <span>保存复盘记录到本地手帐</span>
                    </button>
                  </div>
                </form>

                <div style={{ marginTop: 14 }}>
                  {journalEntries.map((je) => {
                    const usd = calcDollarValue(je.symbol, je.capturedHandles);
                    return (
                      <div key={je.id} className="keypoint-card" style={{ cursor: 'default' }}>
                        <div
                          style={{
                            display: 'flex',
                            justifyContent: 'space-between',
                            alignItems: 'center',
                            marginBottom: 6
                          }}
                        >
                          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                            <span className="time-jump-badge">{je.symbol}</span>
                            <span
                              style={{
                                fontSize: 12,
                                fontWeight: 600,
                                color: je.direction.startsWith('SHORT')
                                  ? 'var(--accent-rose)'
                                  : 'var(--accent-emerald)'
                              }}
                            >
                              {je.direction}
                            </span>
                            <span className="mono" style={{ fontSize: 11.5, color: 'var(--text-muted)' }}>
                              {je.date}
                            </span>
                          </div>
                          <button
                            className="btn btn-sm"
                            onClick={() =>
                              setJournalEntries(journalEntries.filter((x) => x.id !== je.id))
                            }
                            title="删除此条记录"
                          >
                            <Trash2 size={12} />
                          </button>
                        </div>

                        <div
                          className="mono"
                          style={{
                            display: 'grid',
                            gridTemplateColumns: 'repeat(4, 1fr)',
                            gap: 6,
                            background: 'var(--bg-canvas)',
                            padding: '8px 10px',
                            borderRadius: 6,
                            fontSize: 11.5,
                            marginBottom: 8
                          }}
                        >
                          <div>
                            <div style={{ color: 'var(--text-muted)', fontSize: 10 }}>MSS→进场</div>
                            <div>{je.mssToEntryMins}</div>
                          </div>
                          <div>
                            <div style={{ color: 'var(--text-muted)', fontSize: 10 }}>持仓耗时</div>
                            <div>{je.entryToTargetMins}</div>
                          </div>
                          <div>
                            <div style={{ color: 'var(--text-muted)', fontSize: 10 }}>最大抗单Heat</div>
                            <div style={{ color: 'var(--accent-rose)' }}>{je.heatHandles}</div>
                          </div>
                          <div>
                            <div style={{ color: 'var(--text-muted)', fontSize: 10 }}>空间 / 单手价值</div>
                            <div style={{ color: 'var(--accent-emerald)', fontWeight: 600 }}>
                              +{je.capturedHandles} pts {usd ? `(${usd})` : ''}
                            </div>
                          </div>
                        </div>

                        {je.notes && <div className="keypoint-detail">{je.notes}</div>}
                      </div>
                    );
                  })}
                </div>
              </>
            )}
          </div>
        </section>
      </div>

      {/* Glossary Modal */}
      {glossaryOpen && (
        <div className="modal-backdrop" onClick={() => setGlossaryOpen(false)}>
          <div className="modal-window" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                <BookOpen size={18} color="var(--accent-amber)" />
                <h3 style={{ fontSize: 16, fontWeight: 700 }}>
                  ICT 2022 核心概念与 PD Array 词典（点击集数徽章直达对应课程）
                </h3>
              </div>
              <button className="btn btn-sm" onClick={() => setGlossaryOpen(false)}>
                <X size={15} />
              </button>
            </div>
            <div className="modal-body">
              {courseData.glossary.map((g) => (
                <div key={g.term} className="glossary-card">
                  <div
                    style={{
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'flex-start',
                      gap: 8,
                      marginBottom: 6
                    }}
                  >
                    <div>
                      <div className="mono" style={{ fontSize: 13.5, fontWeight: 700, color: 'var(--accent-cyan)' }}>
                        {g.term}
                      </div>
                      <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-primary)' }}>
                        {g.nameZh}
                      </div>
                    </div>
                    <span className="tag-chip">{g.category}</span>
                  </div>
                  <p style={{ fontSize: 12.5, lineHeight: 1.6, color: 'var(--text-secondary)', marginBottom: 10 }}>
                    {g.definition}
                  </p>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 6, flexWrap: 'wrap' }}>
                    <span style={{ fontSize: 11, color: 'var(--text-muted)' }}>重点讲解集数:</span>
                    {g.episodes.map((epNum) => (
                      <button
                        key={epNum}
                        className="btn btn-sm"
                        style={{ padding: '2px 7px', fontSize: 11 }}
                        onClick={() => {
                          setSelectedEpNum(epNum);
                          setGlossaryOpen(false);
                        }}
                      >
                        Ep.{String(epNum).padStart(2, '0')}
                      </button>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Fullscreen Lightbox Modal for 1080p Chart Inspection */}
      {lightboxFrame && (
        <div className="modal-backdrop" onClick={() => setLightboxFrame(null)}>
          <div
            className="modal-window"
            style={{ maxWidth: '94vw', maxHeight: '94vh' }}
            onClick={(e) => e.stopPropagation()}
          >
            <div className="modal-header">
              <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                <span className="time-jump-badge">{lightboxFrame.timeframe}</span>
                <span className="mono" style={{ fontSize: 12, color: 'var(--accent-cyan)' }}>
                  [{lightboxFrame.timeStr}]
                </span>
                <h3 style={{ fontSize: 15, fontWeight: 700 }}>{lightboxFrame.titleZh}</h3>
              </div>
              <div style={{ display: 'flex', gap: 8 }}>
                <button
                  className="btn btn-primary btn-sm"
                  onClick={() => {
                    seekToSeconds(lightboxFrame.seconds);
                    setLightboxFrame(null);
                  }}
                >
                  <Play size={13} />
                  <span>跳转到此秒数播放 [{lightboxFrame.timeStr}]</span>
                </button>
                <button className="btn btn-sm" onClick={() => setLightboxFrame(null)}>
                  <X size={15} />
                </button>
              </div>
            </div>
            <div style={{ overflow: 'auto', background: '#000', textAlign: 'center' }}>
              <img
                src={`/frames/${lightboxFrame.file}`}
                alt={lightboxFrame.titleZh}
                style={{ maxWidth: '100%', maxHeight: '78vh', objectFit: 'contain' }}
              />
            </div>
            <div style={{ padding: '12px 20px', fontSize: 13.5, color: 'var(--text-secondary)' }}>
              {lightboxFrame.captionZh}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
