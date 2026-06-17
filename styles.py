import streamlit as st

FONT_LINK = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
"""

PREMIUM_CSS = """
<style>
* { box-sizing: border-box; }

html, body {
    font-family: 'Inter', sans-serif !important;
    background: #DDE3ED !important;
}

[class*="css"], .stApp, .main {
    font-family: 'Inter', sans-serif !important;
    background: #DDE3ED !important;
    color: #1e2d3d !important;
}

.stApp {
    background: #DDE3ED !important;
    background-image:
        radial-gradient(ellipse at 20% 20%, rgba(59,130,246,0.05) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 80%, rgba(139,92,246,0.05) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 50%, rgba(16,185,129,0.03) 0%, transparent 70%) !important;
}


footer { visibility: hidden; }

header,
header[data-testid="stHeader"],
[data-testid="stHeader"],
.stApp > header,
div[class*="stAppHeader"],
div[class*="AppHeader"],
[data-testid="stAppViewContainer"] > header {
    background: transparent !important;
    background-color: transparent !important;
    background-image: none !important;
    border-bottom: none !important;
    box-shadow: none !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
}

header::before,
header::after,
[data-testid="stHeader"]::before,
[data-testid="stHeader"]::after {
    background: transparent !important;
    display: none !important;
}

[data-testid="stToolbar"],
[data-testid="stToolbarActions"],
[data-testid="stStatusWidget"] {
    background: transparent !important;
    background-color: transparent !important;
}

[data-testid="stDecoration"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
}

.block-container {
    padding: 1.5rem 2.5rem 3rem 2.5rem !important;
    max-width: 1440px !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #D4DAE8 0%, #CBD2E2 100%) !important;
    border-right: 1px solid rgba(150,170,210,0.25) !important;
    box-shadow: 4px 0 30px rgba(30,60,120,0.07) !important;
}

[data-testid="stSidebarNav"] a {
    border-radius: 6px !important;
    padding: 0.5rem 0.8rem !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.92rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
    color: #6b7d94 !important;
    margin: 2px 0 !important;
    transition: all 0.2s ease !important;
    border: 1px solid transparent !important;
    text-transform: uppercase !important;
}

[data-testid="stSidebarNav"] a:hover {
    background: rgba(59,130,246,0.08) !important;
    color: #2563EB !important;
    border-color: rgba(59,130,246,0.2) !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg, rgba(59,130,246,0.14), rgba(59,130,246,0.04)) !important;
    color: #2563EB !important;
    border-left: 2px solid #2563EB !important;
    box-shadow: 0 0 15px rgba(59,130,246,0.1) !important;
}

[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .stMarkdown div {
    color: #6b7d94 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.82rem !important;
}

[data-testid="collapsedControl"] { display: flex !important; visibility: visible !important; }

h1, h2, h3,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    font-family: 'Orbitron', monospace !important;
    letter-spacing: 0.05em !important;
}

h1, [data-testid="stMarkdownContainer"] h1 {
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    color: #111827 !important;
    margin-bottom: 0.25rem !important;
}

h2, [data-testid="stMarkdownContainer"] h2 {
    font-size: 1.15rem !important;
    font-weight: 600 !important;
    color: #1e2d3d !important;
}

h3, [data-testid="stMarkdownContainer"] h3 {
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    color: #2d3f52 !important;
}

p, li { color: #3d5068; line-height: 1.7; }

.nc-kpi-card {
    background: linear-gradient(135deg, rgba(236,241,250,0.98) 0%, rgba(224,231,244,0.98) 100%);
    border: 1px solid rgba(170,190,220,0.5);
    border-left: 3px solid;
    border-radius: 10px;
    padding: 1.1rem 1.2rem;
    margin-bottom: 0.5rem;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    cursor: default;
    box-shadow: 0 1px 6px rgba(30,60,120,0.08);
}

.nc-kpi-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.35) 0%, transparent 60%);
    pointer-events: none;
}

.nc-kpi-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(30,60,120,0.12);
}

.nc-kpi-icon { font-size: 1.2rem; margin-bottom: 0.5rem; display: block; }

.nc-kpi-label {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.65rem;
    font-weight: 700;
    color: #6b7d94;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    margin-bottom: 0.4rem;
    display: block;
}

.nc-kpi-value {
    font-family: 'Orbitron', monospace !important;
    font-size: 1.55rem;
    font-weight: 700;
    line-height: 1;
    display: block;
}

.nc-kpi-delta {
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.72rem;
    color: #6b7d94;
    margin-top: 0.4rem;
    display: block;
}

.nc-section-header {
    font-family: 'Orbitron', monospace !important;
    font-size: 0.72rem;
    font-weight: 700;
    color: #2563EB;
    margin: 2rem 0 0.9rem 0;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid rgba(59,130,246,0.18);
    letter-spacing: 0.15em;
    text-transform: uppercase;
}

.nc-chart-label {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.92rem;
    font-weight: 700;
    color: #1e2d3d;
    margin-bottom: 0.2rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

.nc-chart-sub {
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    color: #6b7d94;
    margin-bottom: 0.5rem;
}

.nc-insight {
    border-left: 3px solid;
    border-radius: 8px;
    padding: 0.8rem 1rem;
    margin-bottom: 0.65rem;
    font-size: 0.875rem;
    line-height: 1.65;
    color: #3d5068;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(236,241,250,0.98), rgba(224,231,244,0.98)) !important;
    border: 1px solid rgba(170,190,220,0.5) !important;
    border-radius: 10px !important;
    padding: 1rem 1.25rem !important;
    transition: transform 0.2s ease !important;
    box-shadow: 0 1px 6px rgba(30,60,120,0.07) !important;
}

[data-testid="stMetric"]:hover { transform: translateY(-2px) !important; }

[data-testid="stMetricLabel"] {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.68rem !important;
    font-weight: 700 !important;
    color: #6b7d94 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
}

[data-testid="stMetricValue"] {
    font-family: 'Orbitron', monospace !important;
    font-size: 1.4rem !important;
    font-weight: 700 !important;
    color: #111827 !important;
}

.stButton > button {
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    background: rgba(220,228,242,0.9) !important;
    color: #4b6080 !important;
    border: 1px solid rgba(150,175,215,0.4) !important;
    border-radius: 6px !important;
    font-size: 0.82rem !important;
    padding: 0.45rem 1.1rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 1px 4px rgba(30,60,120,0.07) !important;
}

.stButton > button:hover {
    background: rgba(59,130,246,0.1) !important;
    border-color: #2563EB !important;
    color: #2563EB !important;
    box-shadow: 0 0 12px rgba(59,130,246,0.15) !important;
}

.stTextInput > div > div > input,
.stDateInput > div > div > input {
    background: rgba(224,231,244,0.85) !important;
    border: 1px solid rgba(150,175,215,0.4) !important;
    border-radius: 6px !important;
    color: #111827 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.9rem !important;
}

.stSelectbox > div > div {
    background: rgba(224,231,244,0.85) !important;
    border: 1px solid rgba(150,175,215,0.4) !important;
    border-radius: 6px !important;
    color: #111827 !important;
}

/* DataFrame Header */
[data-testid="stDataFrame"] [role="columnheader"] {
    background: #D8E0EE !important;
    color: #1E2D3D !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 700 !important;
    border-bottom: 1px solid #BFCDE3 !important;
}

/* DataFrame Cells */
[data-testid="stDataFrame"] [role="gridcell"] {
    background: #E6EBF5 !important;
    color: #2D3F52 !important;
}

/* Entire Grid */
[data-testid="stDataFrame"] {
    background: #E6EBF5 !important;
    border: 1px solid rgba(170,190,220,0.5) !important;
    border-radius: 10px !important;
}

[data-testid="stExpander"] {
    background: rgba(224,231,244,0.7) !important;
    border: 1px solid rgba(170,190,220,0.45) !important;
    border-radius: 10px !important;
    box-shadow: 0 1px 4px rgba(30,60,120,0.05) !important;
}

.stTabs [data-baseweb="tab-list"] {
    background: rgba(210,220,238,0.7);
    border-radius: 8px;
    padding: 3px;
    gap: 3px;
    border: 1px solid rgba(170,190,220,0.45);
}

.stTabs [data-baseweb="tab"] {
    font-family: 'Rajdhani', sans-serif !important;
    background: transparent !important;
    color: #6b7d94 !important;
    border-radius: 6px !important;
    padding: 0.35rem 1rem !important;
    font-size: 0.88rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    transition: all 0.2s ease !important;
}

.stTabs [aria-selected="true"] {
    background: rgba(236,241,250,0.95) !important;
    color: #2563EB !important;
    box-shadow: 0 1px 4px rgba(30,60,120,0.1) !important;
}

.stDownloadButton > button {
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    background: rgba(59,130,246,0.08) !important;
    color: #2563EB !important;
    border: 1px solid rgba(59,130,246,0.22) !important;
    border-radius: 6px !important;
}

.stDownloadButton > button:hover {
    background: rgba(59,130,246,0.15) !important;
    border-color: #2563EB !important;
    box-shadow: 0 0 10px rgba(59,130,246,0.15) !important;
}

.stSuccess {
    background: rgba(16,185,129,0.08) !important;
    border: 1px solid rgba(16,185,129,0.22) !important;
    border-radius: 8px !important;
}
.stInfo {
    background: rgba(59,130,246,0.08) !important;
    border: 1px solid rgba(59,130,246,0.2) !important;
    border-radius: 8px !important;
}
.stWarning {
    background: rgba(245,158,11,0.08) !important;
    border: 1px solid rgba(245,158,11,0.2) !important;
    border-radius: 8px !important;
}
.stError {
    background: rgba(239,68,68,0.08) !important;
    border: 1px solid rgba(239,68,68,0.2) !important;
    border-radius: 8px !important;
}

hr {
    border: none !important;
    border-top: 1px solid rgba(160,180,215,0.45) !important;
    margin: 1.5rem 0 !important;
}

::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: rgba(210,220,238,0.6); }
::-webkit-scrollbar-thumb { background: rgba(59,130,246,0.28); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(59,130,246,0.5); }

[data-testid="stFileUploader"] {
    background: rgba(224,231,244,0.7) !important;
    border: 1px dashed rgba(59,130,246,0.28) !important;
    border-radius: 10px !important;
    padding: 1rem !important;
}

[data-testid="stSlider"] [role="slider"] {
    background: #2563EB !important;
    box-shadow: 0 0 8px rgba(37,99,235,0.4) !important;
}

[data-testid="stSlider"] [data-baseweb="slider"] div[class*="thumb"] {
    background: #2563EB !important;
}
</style>
"""

COLORS = {
    "blue":   "#3B82F6",
    "cyan":   "#0EA5E9",
    "purple": "#8B5CF6",
    "green":  "#10B981",
    "amber":  "#F59E0B",
    "red":    "#EF4444",
    "pink":   "#EC4899",
}
COLOR_SEQ = list(COLORS.values())

PLOT_LAYOUT = dict(
    template="plotly_white",
    paper_bgcolor="rgba(221,227,237,0)",
    plot_bgcolor="rgba(221,227,237,0)",
    font=dict(family="'Rajdhani', sans-serif", color="#3d5068", size=13),
    xaxis=dict(
        gridcolor="rgba(150,175,215,0.35)",
        zeroline=False,
        linecolor="rgba(150,175,215,0.45)",
        tickfont=dict(family="Rajdhani, sans-serif", size=12, color="#6b7d94"),
    ),
    yaxis=dict(
        gridcolor="rgba(150,175,215,0.35)",
        zeroline=False,
        linecolor="rgba(150,175,215,0.45)",
        tickfont=dict(family="Rajdhani, sans-serif", size=12, color="#6b7d94"),
    ),
    margin=dict(l=16, r=16, t=40, b=16),
    legend=dict(
        bgcolor="rgba(224,231,244,0.85)",
        bordercolor="rgba(150,175,215,0.4)",
        borderwidth=1,
        font=dict(family="Rajdhani, sans-serif", size=12, color="#3d5068"),
    ),
    hoverlabel=dict(
        bgcolor="rgba(210,220,238,0.97)",
        bordercolor="rgba(59,130,246,0.35)",
        font=dict(family="Rajdhani, sans-serif", size=13, color="#111827"),
    ),
)


def inject_css():
    st.markdown(FONT_LINK, unsafe_allow_html=True)
    st.markdown(PREMIUM_CSS, unsafe_allow_html=True)


def sidebar_brand():
    st.sidebar.markdown("""
        <div style="padding:0.5rem 0 1.25rem 0;">
            <div style="font-family:'Orbitron',monospace;font-size:0.95rem;font-weight:800;
                        color:#2563EB;letter-spacing:0.1em;">
                Customer Segmentation & Consumer Behaviour
            </div>
            <div style="font-family:'Rajdhani',sans-serif;font-size:0.68rem;
                        color:#6b7d94;margin-top:4px;letter-spacing:0.15em;
                        text-transform:uppercase;">
                 Intelligence Platform
            </div>
        </div>
        <div style="height:1px;background:linear-gradient(90deg,transparent,rgba(59,130,246,0.25),transparent);margin-bottom:0.75rem;"></div>
    """, unsafe_allow_html=True)


def page_header(title: str, subtitle: str = "", icon: str = ""):
    icon_html = f'<span style="margin-right:0.4rem;">{icon}</span>' if icon else ""
    st.markdown(f"""
        <div style="margin-bottom:1.75rem;padding-bottom:1rem;
                    border-bottom:1px solid rgba(160,180,215,0.45);">
            <div style="font-family:'Orbitron',monospace;font-size:1.55rem;font-weight:700;
                        color:#111827;letter-spacing:0.06em;line-height:1.2;">
                {icon_html}{title}
            </div>
            {"<div style='font-family:Rajdhani,sans-serif;color:#6b7d94;font-size:0.85rem;margin-top:0.4rem;letter-spacing:0.08em;text-transform:uppercase;'>" + subtitle + "</div>" if subtitle else ""}
        </div>
    """, unsafe_allow_html=True)


def section_header(title: str):
    st.markdown(f'<div class="nc-section-header">{title}</div>', unsafe_allow_html=True)


def chart_label(title: str, sub: str = ""):
    st.markdown(
        f'<div class="nc-chart-label">{title}</div>'
        + (f'<div class="nc-chart-sub">{sub}</div>' if sub else ""),
        unsafe_allow_html=True,
    )


def kpi_card(col, title: str, value: str, delta: str = "", icon: str = "", color: str = "#2563EB"):
    with col:
        st.markdown(f"""
            <div class="nc-kpi-card" style="border-color:{color};
                 box-shadow:0 2px 12px {color}18,0 1px 6px rgba(30,60,120,0.08);">
                <span class="nc-kpi-icon">{icon}</span>
                <span class="nc-kpi-label">{title}</span>
                <span class="nc-kpi-value" style="color:{color};">{value}</span>
                {"<span class='nc-kpi-delta'>" + delta + "</span>" if delta else ""}
            </div>
        """, unsafe_allow_html=True)


def insight_card(text: str, kind: str = "info"):
    palettes = {
        "success": ("#10B981", "rgba(16,185,129,0.08)"),
        "warning": ("#F59E0B", "rgba(245,158,11,0.08)"),
        "error":   ("#EF4444", "rgba(239,68,68,0.08)"),
        "info":    ("#3B82F6", "rgba(59,130,246,0.08)"),
    }
    bc, bg = palettes.get(kind, palettes["info"])
    st.markdown(
        f'<div class="nc-insight" style="border-color:{bc};background:{bg};">{text}</div>',
        unsafe_allow_html=True
    )


def chart_note(text: str):
    st.markdown(f"""
        <div style="font-family:'Inter',sans-serif;
                    font-size:0.76rem;
                    color:#3d5068;
                    margin-top:-0.1rem;
                    margin-bottom:0.9rem;
                    line-height:1.55;
                    padding:0.45rem 0.75rem;
                    border-left:2px solid rgba(59,130,246,0.3);
                    background:rgba(59,130,246,0.05);
                    border-radius:0 4px 4px 0;">
            {text}
        </div>
    """, unsafe_allow_html=True)


def apply_plot_layout(fig, height: int = 380):
    fig.update_layout(height=height, **PLOT_LAYOUT)
    return fig


def footer():
    st.markdown("""
        <div style="margin-top:3.5rem;padding-top:1rem;
                    border-top:1px solid rgba(160,180,215,0.45);">
            <div style="display:flex;justify-content:space-between;align-items:center;">
                <div style="font-family:'Orbitron',monospace;font-size:0.6rem;
                            color:#6b7d94;letter-spacing:0.15em;">
                    © Customer Segmentation & Consumer Behaviour
                </div>
                <div style="font-family:'Orbitron',monospace;font-size:0.6rem;
                            color:#6b7d94;letter-spacing:0.15em;">
                    INTELLIGENCE PLATFORM
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)