"""
Builds the SVG header / paper card / project cards used in README.md.
Each asset is written twice (light, dark). Edit CARDS below and rerun:

    python assets/make_assets.py
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).parent

SANS = ("-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Apple SD Gothic Neo', "
        "'Malgun Gothic', 'Noto Sans KR', Helvetica, Arial, sans-serif")
MONO = "'SF Mono', ui-monospace, Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "light": dict(bg="#F6F8FA", border="#D1D9E0", text="#1F2328", body="#3B434B",
                  muted="#6E7781", faint="#D8DEE4", accent="#2F5BD3", rust="#C2552E",
                  chip="#FFFFFF", curve="#8C959F"),
    "dark": dict(bg="#151B23", border="#3D444D", text="#E6EDF3", body="#C9D1D9",
                 muted="#8B949E", faint="#2A313A", accent="#7AA2F7", rust="#F08A5D",
                 chip="#0D1117", curve="#6E7681"),
}


# ---------- helpers ----------
def text_w(s, size, mono=False):
    if mono:
        return len(s) * size * 0.61
    w = 0.0
    for ch in s:
        o = ord(ch)
        if 0xAC00 <= o <= 0xD7A3 or 0x3130 <= o <= 0x318F:
            w += 0.93
        elif ch == " ":
            w += 0.28
        elif ch in "ilI.,:;|!'()[]·/":
            w += 0.3
        elif ch.isupper() or ch in "mwMW":
            w += 0.68
        elif ch.isdigit():
            w += 0.57
        else:
            w += 0.54
    return w * size


def wrap(s, size, max_w):
    lines, cur = [], ""
    for word in s.split(" "):
        trial = (cur + " " + word).strip()
        if text_w(trial, size) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    return lines


def smooth(pts):
    """Catmull-Rom through pts -> cubic bezier path."""
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d


def scale(pts, x0, y0, sx, sy):
    return [(x0 + x * sx, y0 + y * sy) for x, y in pts]


# normalized bubble shapes (x 0..1, y 0..1, y down)
MINSKY = [(0, .97), (.12, .92), (.25, .83), (.37, .64), (.46, .40), (.53, .18),
          (.59, .06), (.64, .10), (.70, .30), (.77, .58), (.85, .82), (.93, .93), (1, .95)]
DOTCOM = [(.02, .99), (.14, .94), (.27, .86), (.38, .70), (.47, .47), (.54, .24),
          (.58, .14), (.63, .20), (.69, .40), (.76, .66), (.84, .86), (.93, .95), (1, .96)]
AI = [(.02, 1.0), (.14, .95), (.26, .87), (.37, .69), (.45, .47), (.51, .27), (.555, .17)]


def svg(w, h, body, style=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" fill="none">\n<style>{style}</style>\n{body}\n</svg>\n')


def t(x, y, s, size, color, weight=400, mono=False, anchor="start", extra=""):
    fam = MONO if mono else SANS
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}" {extra}>'
            f'{escape(s)}</text>')


# ---------- header ----------
def header(c):
    W, H = 1000, 230
    cx0, cy0, cw, ch = 610, 40, 370, 150
    grid = "".join(
        f'<line x1="{cx0}" x2="{cx0 + cw}" y1="{cy0 + i * ch / 4:.1f}" y2="{cy0 + i * ch / 4:.1f}" '
        f'stroke="{c["faint"]}" stroke-dasharray="2 5"/>' for i in range(5))
    dot = smooth(scale(DOTCOM, cx0, cy0, cw, ch))
    ai_pts = scale(AI, cx0, cy0, cw, ch)
    ai = smooth(ai_pts)
    nx, ny = ai_pts[-1]
    px, py = scale([(.58, .14)], cx0, cy0, cw, ch)[0]
    stages = ["DISPLACEMENT", "BOOM", "EUPHORIA", "PROFIT TAKING", "PANIC"]
    labels = "".join(
        t(cx0 + cw * (i + .5) / 5, cy0 + ch + 24, s, 8.5, c["muted"], mono=True, anchor="middle",
          extra='letter-spacing="0.6"') for i, s in enumerate(stages))
    style = (".pulse{transform-origin:%.1fpx %.1fpx;animation:p 2.4s ease-out infinite}"
             "@keyframes p{0%%{opacity:.7;transform:scale(1)}80%%,100%%{opacity:0;transform:scale(3)}}"
             % (nx, ny))
    body = f"""
{t(8, 64, "UNIST · INDUSTRIAL ENGINEERING", 12, c["accent"], 600, mono=True, extra='letter-spacing="2"')}
{t(4, 124, "Minsung Park", 54, c["text"], 700, extra='letter-spacing="-1.8"')}
{t(8, 166, "박민성", 19, c["text"], 600)}
{t(76, 166, "금융 데이터와 텍스트로 시장을 읽는 방법을 공부합니다", 17, c["muted"])}
{grid}
<path d="{dot}" stroke="{c["rust"]}" stroke-width="2" stroke-linecap="round" opacity=".75"/>
<path d="{ai}" stroke="{c["accent"]}" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="{nx:.1f}" cy="{ny:.1f}" r="5" fill="{c["accent"]}" class="pulse"/>
<circle cx="{nx:.1f}" cy="{ny:.1f}" r="4.5" fill="{c["accent"]}"/>
<g>
{t(nx - 12, ny + 4, "2026", 10, c["accent"], 600, mono=True, anchor="end")}
{t(px + 10, py - 6, "2000", 10, c["rust"], 600, mono=True)}
</g>
{labels}
"""
    return svg(W, H, body, style)


# ---------- featured paper ----------
def paper(c):
    W, H = 1000, 340
    L = 40
    out = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>']
    out.append(t(L, 50, "FEATURED PAPER  ·  UNIST IE412  ·  2026.06", 11, c["accent"], 600, mono=True,
                 extra='letter-spacing="1.6"'))
    out.append(t(L, 90, "Comparing the Dot-com Bubble and the Current", 25, c["text"], 700, extra='letter-spacing="-0.4"'))
    out.append(t(L, 121, "Semiconductor/AI Bubble", 25, c["text"], 700, extra='letter-spacing="-0.4"'))
    out.append(t(L, 150, "Diagnosing Bubble Stages via LLM Sentiment Analysis and Quantitative Indicators",
                 13.5, c["muted"], extra='font-style="italic"'))
    desc = ("버핏지수, Shiller CAPE, VIX, NASDAQ에 Qwen2.5-1.5B로 분류한 뉴스 100건의 감성을 더해 "
            "닷컴버블과 지금의 반도체·AI 장세를 같은 잣대로 비교하고, 민스키 5단계 위에서 현재 위치를 진단했습니다.")
    for i, line in enumerate(wrap(desc, 14.5, 560)):
        out.append(t(L, 186 + i * 23, line, 14.5, c["body"]))

    stats = [("249%", "버핏지수", "닷컴 정점 144%"),
             ("40%", "EUPHORIC 뉴스 비율", "닷컴 34%"),
             ("92%", "종합 버블 점수", "닷컴 정점 대비")]
    sx = L
    for i, (big, lab, sub) in enumerate(stats):
        x = sx + i * 190
        if i:
            out.append(f'<line x1="{x - 22}" x2="{x - 22}" y1="254" y2="310" stroke="{c["border"]}"/>')
        out.append(t(x, 284, big, 32, c["accent"] if i != 1 else c["rust"], 700, extra='letter-spacing="-1"'))
        out.append(t(x, 306, lab, 12, c["text"], 600))
        out.append(t(x + text_w(lab, 12) * 1.08 + 8, 306, sub, 11.5, c["muted"]))

    # mini Minsky chart
    cx0, cy0, cw, ch = 662, 70, 300, 196
    bands = ""
    for i in range(5):
        if i == 2:
            bands += (f'<rect x="{cx0 + cw * i / 5:.1f}" y="{cy0 - 8}" width="{cw / 5:.1f}" height="{ch + 8}" '
                      f'fill="{c["accent"]}" opacity=".07"/>')
    out.append(bands)
    out.append(t(cx0, 52, "MINSKY 5-STAGE MODEL", 10, c["muted"], 600, mono=True, extra='letter-spacing="1.2"'))
    out.append(f'<line x1="{cx0}" x2="{cx0 + cw}" y1="{cy0 + ch}" y2="{cy0 + ch}" stroke="{c["border"]}"/>')
    out.append(f'<path d="{smooth(scale(MINSKY, cx0, cy0, cw, ch))}" stroke="{c["curve"]}" stroke-width="3" opacity=".55"/>')
    out.append(f'<path d="{smooth(scale(DOTCOM, cx0, cy0, cw, ch))}" stroke="{c["rust"]}" stroke-width="2" stroke-dasharray="5 4"/>')
    ai_pts = scale(AI, cx0, cy0, cw, ch)
    out.append(f'<path d="{smooth(ai_pts)}" stroke="{c["accent"]}" stroke-width="2.4" stroke-dasharray="5 4"/>')
    nx, ny = ai_pts[-1]
    out.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="5" fill="{c["accent"]}"/>')
    out.append(t(nx - 10, ny - 10, "NOW · EUPHORIA", 9.5, c["accent"], 700, mono=True, anchor="end"))
    for i, s in enumerate(["DISP.", "BOOM", "EUPH.", "PROFIT", "PANIC"]):
        out.append(t(cx0 + cw * (i + .5) / 5, cy0 + ch + 18, s, 8.5, c["muted"], mono=True, anchor="middle"))
    # legend
    ly = cy0 + ch + 44
    for j, (col, lab) in enumerate([(c["rust"], "Dot-com 1997–2000"), (c["accent"], "Semi/AI 2023–")]):
        lx = cx0 + 2 + j * 160
        out.append(f'<line x1="{lx}" x2="{lx + 18}" y1="{ly}" y2="{ly}" stroke="{col}" stroke-width="2" stroke-dasharray="4 3"/>')
        out.append(t(lx + 24, ly + 3.5, lab, 10, c["muted"], mono=True))
    return svg(W, H, "\n".join(out))


# ---------- project cards ----------
CARDS = [
    ("upbit", "QUANT · PERSONAL", "upbit-spread-rl",
     "업비트 Open API로 페어 스프레드와 호가 스프레드 전략을 PPO로 학습하는 자동매매 시스템과 대시보드",
     ["PPO", "Upbit API", "Python", "Vercel"]),
    ("journal", "FINTECH · PERSONAL", "AI Investment Journal",
     "투자 판단 과정을 기록하고, 그 기록에서 편향과 반복되는 패턴을 찾아내는 다이어리 MVP",
     ["Next.js", "TypeScript", "LLM"]),
    ("alphapick", "LLM AGENT · TEAM", "αlpha Pick",
     "HCX로 검색어를 정제하고 실제 쇼핑몰 검색 순위를 반영해 상품을 추천하는 Google ADK 8단계 에이전트",
     ["HyperCLOVA X", "Google ADK", "FastAPI"]),
    ("rag", "MULTIMODAL RAG · TEAM", "Multimodal RAG",
     "애널리스트 리포트 PDF를 페이지 유형별로 나눠 추출하고 하나의 DB로 합친 RAG와 KOSPI200 종목 스코어링",
     ["YOLOv11n", "MinerU", "VLM", "Supabase"]),
    ("keyphrase", "NLP · TEAM", "Keyphrase Extraction",
     "어휘 불일치 문제를 겨냥해 present/absent 키프레이즈를 함께 생성하고 TF-IDF, KeyBERT, KeyBART와 비교",
     ["KeyBERT", "KeyBART", "Transformers"]),
    ("oibc", "FORECASTING · COMPETITION", "OIBC 2026 Solar Forecast",
     "태양광 발전소를 두 개의 집합자원(VPP)으로 묶고 각 집합자원의 하루 전 발전량을 예측",
     ["Time Series", "VPP", "Python"]),
    ("glip", "DIGITAL HEALTH · HACKATHON", "GLIP",
     "GLP-1 약물 사용자를 위한 아바타 기반 셀프케어 서비스 기획. 4th UU Digital Healthcare Hackathon 2026",
     ["Service Design", "Digital Health"]),
    ("dil", "RESEARCH LOG · LAB", "Data Intelligence Lab",
     "UNIST AIGS Data Intelligence Lab 학부연구생 기록. 논문 리뷰, 랩미팅 발표 자료, TIL",
     ["Paper Review", "TIL"]),
]


def card(c, cat, title, desc, tags):
    W, H = 480, 176
    L = 26
    out = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" fill="{c["bg"]}" stroke="{c["border"]}"/>']
    out.append(t(L, 38, cat, 10.5, c["accent"], 600, mono=True, extra='letter-spacing="1.3"'))
    out.append(t(W - 26, 40, "↗", 15, c["muted"], anchor="end"))
    out.append(t(L, 70, title, 20, c["text"], 700, extra='letter-spacing="-0.3"'))
    lines = wrap(desc, 13.5, W - 2 * L)
    assert len(lines) <= 2, (title, lines)
    for i, line in enumerate(lines):
        out.append(t(L, 98 + i * 21, line, 13.5, c["body"]))
    x = L
    for tag in tags:
        tw = text_w(tag, 11, mono=True) + 18
        out.append(f'<rect x="{x:.1f}" y="134" width="{tw:.1f}" height="22" rx="11" '
                   f'fill="{c["chip"]}" stroke="{c["border"]}"/>')
        out.append(t(x + tw / 2, 149, tag, 11, c["muted"], mono=True, anchor="middle"))
        x += tw + 7
    return svg(W, H, "\n".join(out))


# ---------- experience timeline ----------
EXPERIENCE = [
    ("2026.09 – 현재", "Data Intelligence Lab, UNIST AIGS", "학부연구생 · 논문 리뷰와 랩미팅 발표"),
    ("수료", "멋쟁이사자처럼 AI Plus NLP 5기", "NLP 기초부터 임베딩, RAG, LLM 에이전트까지 · 팀 프로젝트 3건"),
    ("2023.03 – 06", "Financial Data Science Lab", "학부연구생 · 금융 시계열 클러스터링, 통계적 차익거래 전략, 백테스팅 파이프라인"),
    ("재학 중", "UNIST 산업공학과", "AI융합대학 학사과정 · 금융공학, LLM 기반 추천 시스템"),
]


def experience(c):
    W, row, top = 1000, 74, 34
    H = top * 2 + row * (len(EXPERIENCE) - 1) + 30
    lx = 176
    out = [f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>']
    y_last = top + row * (len(EXPERIENCE) - 1)
    out.append(f'<line x1="{lx}" x2="{lx}" y1="{top + 6}" y2="{y_last + 6}" stroke="{c["border"]}" stroke-width="2"/>')
    for i, (date, org, desc) in enumerate(EXPERIENCE):
        y = top + i * row
        first = i == 0
        out.append(t(lx - 26, y + 11, date, 12, c["accent"] if first else c["muted"], 600, mono=True, anchor="end"))
        out.append(f'<circle cx="{lx}" cy="{y + 6}" r="6" fill="{c["accent"] if first else c["bg"]}" '
                   f'stroke="{c["accent"] if first else c["curve"]}" stroke-width="2"/>')
        out.append(t(lx + 28, y + 13, org, 17, c["text"], 700, extra='letter-spacing="-0.2"'))
        out.append(t(lx + 28, y + 37, desc, 13.5, c["body"]))
    return svg(W, H, "\n".join(out))


if __name__ == "__main__":
    (OUT / "cards").mkdir(exist_ok=True)
    for mode, c in THEMES.items():
        (OUT / f"header-{mode}.svg").write_text(header(c))
        (OUT / f"paper-{mode}.svg").write_text(paper(c))
        (OUT / f"experience-{mode}.svg").write_text(experience(c))
        for key, cat, title, desc, tags in CARDS:
            (OUT / "cards" / f"{key}-{mode}.svg").write_text(card(c, cat, title, desc, tags))
    print("done")
