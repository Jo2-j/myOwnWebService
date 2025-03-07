import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="대명상호저축은행 수익성 강화 전략 보고서",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 기본 스타일 설정
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem;}
    .section-header {font-size: 1.8rem; font-weight: bold; margin-top: 2rem; margin-bottom: 1rem; color: #1E3A8A;}
    .subsection-header {font-size: 1.4rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.8rem; color: #2563EB;}
    .caption {font-size: 0.8rem; font-style: italic; color: #6B7280;}
    .proposal-box {background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #3B82F6;}
    .proposal-header {font-weight: bold; color: #1E3A8A; margin-bottom: 0.5rem;}
</style>
""", unsafe_allow_html=True)

# 데이터 정의
financial_data = pd.DataFrame({
    'Year': ['2023년 3분기', '2024년 3분기'],
    'Total_Assets': [2575, 2365],
    'Loans': [2078, 2245],
    'Deposits': [2157, 2008],
    'Capital': [330, 287],
    'ROA': [-0.13, -0.75],
    'NIM': [1.21, 1.69]
})

loan_portfolio_data = pd.DataFrame({
    '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
    '금액(억원)': [1015, 689, 91],
    '비율(%)': [56.55, 38.38, 5.07]
})

collateral_data = pd.DataFrame({
    '담보유형': ['부동산', '예수금', '기타'],
    '금액(억원)': [823, 7, 959],
    '비율(%)': [45.85, 0.39, 53.43]
})

management_metrics = pd.DataFrame({
    '지표': ['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율', '순고정이하여신비율', '총자산순수익률'],
    '2024년 3분기': [16.81, 12.13, 15.52, 10.46, -0.75],
    '2023년 3분기': [17.86, 12.81, 16.61, 3.62, -0.13]
})

deposit_data = pd.DataFrame({
    '구분': ['거치식예금', '적립식예금', '요구불예금'],
    '금액(억원)': [1972, 26, 10],
    '비율(%)': [98.21, 1.29, 0.5]
})

deposit_trend = pd.DataFrame({
    '구분': ['2023년 3분기', '2024년 3분기'],
    '예수금(억원)': [2157, 2008]
})

asset_quality_data = pd.DataFrame({
    '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
    '2023년 3분기': [91, 3, 60],
    '2024년 3분기': [271, 29, 125],
})

delinquency_data = pd.DataFrame({
    '구분': ['연체대출비율', '순고정이하여신비율'],
    '2023년 3분기': [2.30, 3.62],
    '2024년 3분기': [10.00, 10.46]
})

comparison_data = pd.DataFrame({
    '은행명': ['대명', 'CK', '오투', '청주', '한성'],
    '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '충북 - 청주, 천안', '충남 - 대전, 청주, 옥천'],
    'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
    'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
    'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
    'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
    '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
    '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
    'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
    '연체비율 총합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70],
    '카드(2024)': [0, 17, 6, 1547, 0],
    '카드(2023)': [0, 0, 4, 11178, 0]
})

# 색상 테마 정의
COLOR_2023 = '#1E3A8A'  # 진한 파란색 (2023년 데이터)
COLOR_2024 = '#2563EB'  # 밝은 파란색 (2024년 데이터)
COLOR_PIE = ['#1E3A8A', '#2563EB', '#3B82F6']  # 파이 차트 색상

# 사이드바 메뉴
st.sidebar.title("대명상호저축은행")
st.sidebar.subheader("수익성 강화 전략 보고서")
menu = st.sidebar.radio("목차", [
    "현황",
    "비교",
    "제안"
])

st.sidebar.divider()
st.sidebar.info("""
**2024년 9월말 주요 지표**
- 총자산: 2,365억 원
- 대출금: 2,245억 원
- 예수금: 2,008억 원
- BIS 자기자본비율: 16.81%
""")
st.sidebar.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# 현황
if menu == "현황":
    st.markdown('<p class="main-header">현황</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">주요 재무지표</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(management_metrics[management_metrics['지표'].isin(['BIS 자기자본비율', '총자산순수익률'])],
                     x='지표', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='BIS 자기자본비율 및 ROA 추이', height=400,
                     color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        asset_liability_data = pd.DataFrame({'구분': ['자산', '부채', '자본'], '2023년 3분기': [2575, 2245, 330], '2024년 3분기': [2365, 2078, 287]})
        fig = px.bar(asset_liability_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산/부채/자본 변화 (단위: 억원)', height=400,
                     color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<p class="subsection-header">대출 포트폴리오</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(loan_portfolio_data, values='금액(억원)', names='구분', title='용도별 대출 구성 (2024년 3분기)', height=400,
                     color_discrete_sequence=COLOR_PIE)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.pie(collateral_data, values='금액(억원)', names='담보유형', title='담보별 대출 구성 (2024년 3분기)', height=400,
                     color_discrete_sequence=COLOR_PIE)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<p class="subsection-header">예수금 현황</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(deposit_data, values='금액(억원)', names='구분', title='예수금 구성 (2024년 3분기)', height=400,
                     color_discrete_sequence=COLOR_PIE)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400,
                     text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"),
                     color_discrete_sequence=[COLOR_2023, COLOR_2024])
        fig.update_traces(textposition='auto')
        percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
        fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
        fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<p class="subsection-header">자산 건전성</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(asset_quality_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산건전성 지표 (단위: 억원)', height=400,
                     color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400,
                     color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
        st.plotly_chart(fig, use_container_width=True)
    st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# 비교
elif menu == "비교":
    st.markdown('<p class="main-header">비교</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='총자산순수익률(ROA) 비교', height=400,
                     color_discrete_map={'ROA(%) 2023': COLOR_2023, 'ROA(%) 2024': COLOR_2024})
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(comparison_data, x='은행명', y=['연체대출비율(%) 2024'], barmode='group', title='연체대출비율 비교 (2024)', height=400,
                     color_discrete_sequence=[COLOR_2024])
        st.plotly_chart(fig, use_container_width=True)
    
    col3, col4 = st.columns(2)
    with col3:
        fig = px.bar(comparison_data, x='은행명', y=['부동산 대출금(%) 2024'], barmode='group', title='부동산 대출금 비율 비교 (2024)', height=400,
                     color_discrete_sequence=[COLOR_2024])
        st.plotly_chart(fig, use_container_width=True)
    with col4:
        fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024', '연체비율 총합계(%) 2024'], barmode='group', title='PF대출 및 연체비율 총합계 비교 (2024)', height=400,
                     color_discrete_map={'PF대출(%) 2024': COLOR_2023, '연체비율 총합계(%) 2024': COLOR_2024})
        st.plotly_chart(fig, use_container_width=True)
    
    col5, col6 = st.columns(2)
    with col5:
        fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400,
                     color_discrete_map={'BIS 자기자본비율(%) 2023': COLOR_2023, 'BIS 자기자본비율(%) 2024': COLOR_2024})
        st.plotly_chart(fig, use_container_width=True)
    with col6:
        fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='카드 비교', height=400,
                     color_discrete_map={'카드(2023)': COLOR_2023, '카드(2024)': COLOR_2024})
        st.plotly_chart(fig, use_container_width=True)
    
    st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# 제안
elif menu == "제안":
    st.markdown('<p class="main-header">제안</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">대명상호저축은행의 지속 가능한 성장 전략</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="proposal-box">', unsafe_allow_html=True)
        st.markdown('<p class="proposal-header">체크카드 활성화를 통한 지역 기반 강화</p>', unsafe_allow_html=True)
        st.write("""
        대명상호저축은행의 지속 가능한 성장을 위해 체크카드 활성화 전략을 제안합니다. 충청권 저축은행들의 경영공시를 분석한 결과, 대명상호저축은행은 2024년 카드 발급 건수가 0건으로, 경쟁사인 CK(17건), 오투(6건) 등과 비교해도 카드 활용이 미비한 상황입니다. 이는 지역 내 고객 경험을 강화할 수 있는 기회로 작용할 수 있습니다. 대규모 광고가 제한된 환경에서 체크카드 서비스를 통해 고객들이 지역 가맹점에서 결제할 때마다 자연스럽게 대명상호저축은행의 인지도를 높일 수 있을 것입니다.

        현재 온라인 금융상품 비교 사이트가 많아진 상황에서 특판 전략은 효과가 미미하거나 운용 규모가 큰 금융기관에 더 적합하다고 판단됩니다. 이에 저는 초기에는 이율 경쟁보다 체크카드와 같은 차별화된 서비스를 통해 지역 내 충성도 높은 고객 기반을 구축하고, 이를 바탕으로 장기적인 수익성을 확보하고자 합니다.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='체크카드 발급 건수 비교', height=400,
                     color_discrete_map={'카드(2023)': COLOR_2023, '카드(2024)': COLOR_2024})
        st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="proposal-box">', unsafe_allow_html=True)
        st.markdown('<p class="proposal-header">지역 기반 전략과 단계적 확장</p>', unsafe_allow_html=True)
        st.write("""
        지역 기반 전략을 통해 대명상호저축은행의 안정적인 성장 토대를 마련하고자 합니다. 상호저축은행법상 영업구역 내 개인 및 중소기업 대출 비율 요건을 준수하며, 지역별 산업 특성과 위험 요인을 세밀히 분석하여 수익성과 건전성을 동시에 추구하는 균형 잡힌 포트폴리오를 구성하겠습니다.

        탄탄한 지역 기반을 확보한 후에는 강원도와 충청북도처럼 저축은행 밀집도가 낮은 지역(50만 명당 1개사 수준)으로 점진적인 확장을 추진하고, 온라인 채널을 활용해 매력적인 상품군을 제공함으로써 물리적 한계를 넘어선 영업 확대를 도모하겠습니다. 아래 표를 통해 각 권역의 성과와 리스크를 비교하며 적절한 확장 지역을 판단할 수 있을 것입니다. 이러한 단계적 접근을 통해 대명상호저축은행의 지속 가능한 성장을 실현하겠습니다.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        region_data = comparison_data[['권역', 'ROA(%) 2024', '연체대출비율(%) 2024', 'BIS 자기자본비율(%) 2024']].rename(columns={
            '권역': '권역',
            'ROA(%) 2024': 'ROA (%)',
            '연체대출비율(%) 2024': '연체대출비율 (%)',
            'BIS 자기자본비율(%) 2024': 'BIS 자기자본비율 (%)'
        })
        st.markdown("**권역별 저축은행 밀집도 및 성과 비교**")
        st.dataframe(region_data, use_container_width=True)
    
    st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")