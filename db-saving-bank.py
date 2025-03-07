import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt

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
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1.5rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #1E3A8A;
    }
    .subsection-header {
        font-size: 1.4rem;
        font-weight: bold;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
        color: #2563EB;
    }
    .caption {
        font-size: 0.8rem;
        font-style: italic;
        color: #6B7280;
    }
    .highlight {
        background-color: #FEF3C7;
        padding: 0.2rem;
        border-radius: 0.2rem;
    }
    .insight-box {
        background-color: #E0F2FE;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .table-wrapper {
        margin: 1.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 대명상호저축은행 재무 데이터 (2023-2024)
financial_data = pd.DataFrame({
    'Year': ['2023년 3분기', '2024년 3분기'],
    'Total_Assets': [2078, 2365],
    'Loans': [1894, 1795],
    'Deposits': [2008, 2157],
    'Capital': [271, 287],
    'ROA': [-0.75, -0.13],
    'NIM': [2.30, 3.62]
})

# 대출 포트폴리오 데이터 (2024년 3분기)
loan_portfolio_data = pd.DataFrame({
    '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
    '금액(억원)': [1015, 689, 91],
    '비율(%)': [56.55, 38.38, 5.07]
})

# 담보별 대출 현황 (2024년 3분기)
collateral_data = pd.DataFrame({
    '담보유형': ['부동산', '신용', '보증', '기타'],
    '금액(억원)': [959, 823, 7, 6],
    '비율(%)': [53.43, 45.85, 0.39, 0.33]
})

# 경영지표 데이터
management_metrics = pd.DataFrame({
    '지표': ['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율', '순고정이하여신비율', '총자산순수익률'],
    '2024년 3분기': [12.13, 12.14, 11.52, 2.30, -0.75],
    '2023년 3분기': [16.81, 13.03, 15.52, 3.62, -0.13]
})

# 실행 로드맵 데이터
roadmap_data = pd.DataFrame({
    '영역': ['상품개발', '디지털전환', '지점개편', '리스크관리'],
    '2025 Q1': ['AI 신용평가 도입', '모바일앱 리뉴얼', '셀프코너 확대', '부실채권 20% 상각'],
    '2025 Q2': ['중소기업 특화대출', '클라우드 전환', '1개 지점 통폐합', '신용평가시스템 고도화'],
    '2025 Q3': ['정기예금 금리 개편', '전자계약 시스템 도입', '24시간 CD기능 강화', '부실채권 30% 상각'],
    '2025 Q4': ['충북 특화펀드 조성', '빅데이터 분석 도입', '디지털존 구축', '부실채권 50% 상각']
})

# 사이드바 메뉴
st.sidebar.title("대명상호저축은행")
st.sidebar.subheader("수익성 강화 전략 보고서")
# 사이드바 메뉴 수정
menu = st.sidebar.radio("목차", [
    "1. 은행 현황 및 과제",
    "2. 재무 현황 분석",
    "3. 수익성 강화 전략",
    "4. 비용 최적화 방안",
    "5. 실행 로드맵",
    "6. 결론 및 기대효과",
    "7. 동종업권 비교분석 및 전략 제언" # 새로 추가된 메뉴
])


# 사이드바에 정보 추가
st.sidebar.divider()
st.sidebar.info("""
**2024년 9월말 주요 지표**
- 총자산: 2,365억 원
- 총대출: 1,795억 원
- 총예금: 2,157억 원
- BIS 자기자본비율: 12.13%
""")

st.sidebar.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# 1. 은행 현황 및 과제
if menu == "1. 은행 현황 및 과제":
    st.markdown('<p class="main-header">1. 대명상호저축은행 현황 및 과제</p>', unsafe_allow_html=True)
    
    # 은행 개요
    st.markdown('<p class="subsection-header">1.1 은행 개요</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.write("""
        **대명상호저축은행**은 1972년 2월 설립된 충북 제천 지역 기반 저축은행으로, 50여 년의 역사를 가진 지역 금융기관입니다.
        '勤勉 誠實, 內和 外親, 親切 奉事'의 경영이념 아래 '지역사회의 발전과 함께하는 지역 최고 금융기관'을 목표로 하고 있습니다.
        
        현재 본점과 충주지점을 포함하여 2개 영업점을 운영하고 있으며, 임직원은 총 29명입니다.
        2024년 9월말 기준 총자산 2,365억 원, 총대출 1,795억 원, 총예금 2,157억 원 규모의 경영 현황을 보이고 있습니다.
        
        특히 1996년 설립한 재단법인 대명장학회를 통해 지역사회 공헌활동에 적극적으로 참여하고 있으며,
        고객 제일주의, 지역과 함께하는 경영, 인재 제일주의 경영, 선진 금융기법 도입이라는 경영방침을 
        실천하고 있습니다.
        """)

    with col2:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 주요 연혁
        
        - 1972년: 대명상호신용금고 개점
        - 1997년: 주식회사 전환
        - 2002년: 상호저축은행으로 명칭 변경
        - 2002년: 충주지점 개점
        - 2013년: 이정재 대표이사 취임
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
    
    # 조직 구조
    st.markdown('<p class="subsection-header">1.2 조직 구조</p>', unsafe_allow_html=True)
    st.image("https://mermaid.ink/img/pako:eNp1kl1rgzAUhv_KIQMFoV3Xl3RAP6AUCttl7cVgFxFJaozU1BDTrZT-940am266eZXD-zznnJyEFFBIlgJP-Ju86JLPhheVUo2NJ63g6EQnaaXYKhNyzR7LWhS8weyn55NhCLxdCuWldNku_icvZeQ5ylP2aomsc9Xw02PLM97UQnEFs0wcdlJDlJa8wPDPPPciRZZJq3iDoa6kbRFsDZsfwrYGwx5_YzhaQCtYECPz5HlDPlfFkk-I-EoWV4ltWLpbdxrxNUCLvkVbdKMjaY2rWYBRNsXoFmVLUfHAwOTCbhE_GRjVc5d6PxnOzA1h9M7AXLiFTBwaWG38u4ds-zMf9n_bLpp9ym7Ge6Gu8dgRrTD-OKCzIqCOk5ipQ7fJBt0DO0Eq9tieYag7mPJU6JJX9PWiSo6EbgFP4biRGUIByVNSYYGKg0Qx9UlYhSTaoyT0Q3-3ExT_KnABexIG4YHglwbxHB9yySl-AQ6NsJw", caption="대명상호저축은행 조직도")
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
    
    # 주요 과제
    st.markdown('<p class="subsection-header">1.3 현안 및 과제</p>', unsafe_allow_html=True)
    
    st.write("""
    대명상호저축은행의 2024년 현재 직면하고 있는 주요 과제는 다음과 같습니다:
    
    1. **수익성 개선 필요**
       - 총자산순수익률(ROA) -0.75%로 적자 상태 지속
       - 순이자마진(NIM) 2.30%로 업계 평균 대비 저조
       - 세전이익 감소 추세
    
    2. **자산 포트폴리오 최적화**
       - 중소기업 대출 비중 56.55%로 상대적으로 높음
       - 담보대출과 신용대출 간 균형 조정 필요
       - 자산 건전성 지표 관리 필요
    
    3. **디지털 역량 강화**
       - 디지털 뱅킹 서비스 경쟁력 부족
       - 핀테크 기업 및 대형 금융기관과의 경쟁 심화
       - 고객 접점의 디지털화 필요
    
    4. **지역 밀착형 사업모델 강화**
       - 충북 지역 특화 금융 서비스 개발 필요
       - 지역 고객층의 니즈 맞춤형 상품 부족
       - 지역 내 경쟁력 있는 차별화 포인트 발굴
    """)

    # 경쟁 환경 분석
    st.markdown('<p class="subsection-header">1.4 경쟁 환경 분석</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **저축은행 산업 현황:**
        
        저축은행 산업은 2024년 현재 금리 인하 사이클 진입으로 인한 마진 압박과
        핀테크 기업들의 금융업 진출로 경쟁이 심화되고 있습니다. 특히 예대마진이
        주 수익원인 저축은행들은 디지털 전환 압력과 수익성 악화 문제를 동시에
        해결해야 하는 과제를 안고 있습니다.
        
        지방 저축은행의 경우 지역 밀착형 서비스와 디지털 역량 강화라는 두 가지
        방향성을 균형 있게 발전시켜야 하는 상황입니다.
        """)
        
    with col2:
        st.write("""
        **충북 지역 금융 환경:**
        
        충북 제천 및 충주 지역은 제조업과 서비스업이 고루 발전한 지역으로,
        중소기업에 대한 금융 수요가 높습니다. 특히 제천은 한방산업 클러스터를
        중심으로 바이오 관련 중소기업들이 성장하고 있어 특화된 금융 서비스 기회가
        있습니다.
        
        하지만 지역 내 시중은행과 농협의 경쟁이 치열하고, 인구 감소 및 고령화로
        인한 시장 규모 정체도 주요 도전 과제입니다.
        """)
    
    # SWOT 분석
    st.markdown("### 대명상호저축은행 SWOT 분석")
    
    swot_data = pd.DataFrame({
        '강점(Strengths)': [
            '- 50년 이상의 지역 기반 신뢰도',
            '- 우수한 BIS 자기자본비율(12.13%)',
            '- 지역밀착형 고객 서비스',
            '- 충주지점을 포함한 지역 네트워크'
        ],
        '약점(Weaknesses)': [
            '- 수익성 지표 부진(ROA -0.75%)',
            '- 디지털 금융 역량 부족',
            '- 제한된 영업망(2개 지점)',
            '- 고령 고객 비중 높음'
        ],
        '기회(Opportunities)': [
            '- 충북 중소기업 금융 수요 증가',
            '- 제천 한방산업 클러스터 성장',
            '- 디지털 전환을 통한 효율화 가능성',
            '- 지역 특화 금융상품 개발 여지'
        ],
        '위협(Threats)': [
            '- 시중은행의 지역 영업 강화',
            '- 핀테크 기업의 금융업 진출',
            '- 지역 인구 감소 및 고령화',
            '- 저금리 환경에서의 마진 압박'
        ]
    })
    
    st.table(swot_data)
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석")

# 2. 재무 현황 분석
elif menu == "2. 재무 현황 분석":
    st.markdown('<p class="main-header">2. 재무 현황 분석</p>', unsafe_allow_html=True)
    
    # 주요 재무지표
    st.markdown('<p class="subsection-header">2.1 주요 재무지표 현황</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.write("""
        대명상호저축은행의 2024년 3분기 재무지표를 분석한 결과, 자본건전성은 양호한 상태를 유지하고 있으나
        수익성 측면에서 개선이 필요한 상황입니다.
        
        자본적정성 측면에서는 BIS 자기자본비율이 12.13%로 법정 최소 요구치인 8%를 크게 상회하고 있어
        안정적인 자본구조를 갖추고 있습니다. 다만, 전년 동기(16.81%) 대비 약 4.68%p 하락한 점은
        주시할 필요가 있습니다.
        
        수익성 지표인 총자산순수익률(ROA)은 -0.75%로 적자 상태를 보이고 있으며, 이는 전년 동기(-0.13%) 
        대비 악화된 수치입니다. 순이자마진(NIM)은 2.30%로 전년 동기(3.62%) 대비 1.32%p 하락하였습니다.
        
        자산 규모는 총 2,365억 원으로 전년 동기 대비 13.8% 증가하였으며, 
        예수금은 2,157억 원으로 7.4% 증가했습니다. 반면 대출금은 1,795억 원으로 5.2% 감소했습니다.
        """)
        
    with col2:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 주요 재무지표
        
        - 총자산: 2,365억 원 (+13.8%)
        - 총대출: 1,795억 원 (-5.2%)
        - 총예수금: 2,157억 원 (+7.4%)
        - BIS 자기자본비율: 12.13% (-4.68%p)
        - ROA: -0.75% (-0.62%p)
        - NIM: 2.30% (-1.32%p)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
    
    # 재무지표 시각화
    st.markdown("### 주요 재무지표 추이")
    
    # BIS 자기자본비율 시각화
    tab1, tab2 = st.tabs(["자본적정성", "수익성"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(
                management_metrics[management_metrics['지표'].isin(['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율'])],
                x='지표',
                y=['2023년 3분기', '2024년 3분기'],
                barmode='group',
                title='자본적정성 지표 변화',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
            
        with col2:
            # 자산/부채 변화 시각화
            asset_liability_data = pd.DataFrame({
                '구분': ['자산', '부채', '자본'],
                '2023년 3분기': [2078, 1807, 271],
                '2024년 3분기': [2365, 2078, 287]
            })
            
            fig = px.bar(
                asset_liability_data,
                x='구분',
                y=['2023년 3분기', '2024년 3분기'],
                barmode='group',
                title='자산/부채/자본 변화 (단위: 억원)',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            profitability_data = pd.DataFrame({
                '지표': ['ROA', 'NIM'],
                '2023년 3분기': [-0.13, 3.62],
                '2024년 3분기': [-0.75, 2.30]
            })
            
            fig = px.bar(
                profitability_data,
                x='지표',
                y=['2023년 3분기', '2024년 3분기'],
                barmode='group',
                title='수익성 지표 변화',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
            
        with col2:
            # 이자율 현황
            interest_rate_data = pd.DataFrame({
                '구분': ['조달 평균이자율', '운용 평균이자율', '이자마진'],
                '2023년 3분기': [3.01, 4.63, 1.62],
                '2024년 3분기': [3.02, 4.26, 1.24]
            })
            
            fig = px.bar(
                interest_rate_data,
                x='구분',
                y=['2023년 3분기', '2024년 3분기'],
                barmode='group',
                title='이자율 추이 (%)',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
            st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
    
    # 대출 포트폴리오 분석
    st.markdown('<p class="subsection-header">2.2 대출 포트폴리오 분석</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 용도별 대출 시각화
        fig = px.pie(
            loan_portfolio_data,
            values='금액(억원)',
            names='구분',
            title='용도별 대출 구성 (2024년 3분기)',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
        
    with col2:
        # 담보별 대출 시각화
        fig = px.pie(
            collateral_data,
            values='금액(억원)',
            names='담보유형',
            title='담보별 대출 구성 (2024년 3분기)',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
    
    st.write("""
    대명상호저축은행의 대출 포트폴리오를 분석한 결과, 용도별로는 기업자금대출이 1,015억 원(56.55%)으로
    가장 높은 비중을 차지하고 있으며, 가계자금대출은 689억 원(38.38%), 공공 및 기타자금 대출은
    91억 원(5.07%)입니다.
    
    담보별로는 부동산담보대출이 959억 원(53.43%)으로 가장 높은 비중을 차지하고 있으며,
    신용대출은 823억 원(45.85%)입니다. 이는 업계 평균과 비교할 때 신용대출 비중이 다소 높은 편으로,
    리스크 관리 측면에서 주의가 필요한 부분입니다.
    
    중소기업 대출 비중은 50.37%로, 지역 기반 저축은행으로서 지역 내 중소기업 지원에 주력하고 있음을
    알 수 있습니다. 다만, 부동산 업종에 대한 신용공여 비중이 상대적으로 높아 부동산 경기 변동에
    따른 리스크 관리가 중요한 상황입니다.
    """)
    
    # 예수금 현황
    st.markdown('<p class="subsection-header">2.3 예수금 현황 분석</p>', unsafe_allow_html=True)
    
    # 예수금 구성 데이터
    deposit_data = pd.DataFrame({
        '구분': ['거치식예금', '적립식예금', '요구불예금'],
        '금액(억원)': [2128, 19, 10],
        '비율(%)': [98.66, 0.86, 0.48]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 예수금 구성 시각화
        fig = px.pie(
            deposit_data,
            values='금액(억원)',
            names='구분',
            title='예수금 구성 (2024년 3분기)',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
        
    with col2:
        # 예수금 추이 시각화
        deposit_trend = pd.DataFrame({
            '구분': ['2023년 3분기', '2024년 3분기'],
            '예수금(억원)': [2008, 2157]
        })
        
        fig = px.bar(
            deposit_trend,
            x='구분',
            y='예수금(억원)',
            title='예수금 추이 (단위: 억원)',
            height=400
        )
        fig.update_traces(marker_color='rgb(55, 83, 109)')
        st.plotly_chart(fig, use_container_width=True)
        st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
    
    st.write("""
    예수금 구성을 분석한 결과, 2024년 3분기 기준 총 예수금 2,157억 원 중 거치식예금이 2,128억 원으로
    98.66%의 압도적인 비중을 차지하고 있습니다. 적립식예금은 19억 원(0.86%), 요구불예금은 10억 원(0.48%)에
    불과합니다.
    
    이는 고객 기반이 주로 고금리 정기예금 중심으로 형성되어 있음을 의미하며, 저원가성 예금 비중이
    매우 낮아 조달 비용 측면에서 개선의 여지가 있습니다.
    
    예수금은 전년 동기 대비 7.4% 증가한 2,157억 원을 기록하였으나, 예대율은 83.2%로
    업계 평균보다 낮은 수준입니다. 이는 대출 자산이 충분히 확대되지 못하고 있음을 시사하며,
    수익성 개선을 위해 적정 예대율 관리와 함께 대출 자산의 질적 성장이 필요한 상황입니다.
    """)
    
    # 건전성 및 리스크 현황
    st.markdown('<p class="subsection-header">2.4 자산건전성 및 리스크 현황</p>', unsafe_allow_html=True)
    
    # 자산건전성 데이터
    asset_quality_data = pd.DataFrame({
        '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
        '2023년 3분기': [91, 66, 175],
        '2024년 3분기': [60, 29, 125],
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 자산건전성 시각화
        fig = px.bar(
            asset_quality_data,
            x='구분',
            y=['2023년 3분기', '2024년 3분기'],
            barmode='group',
            title='자산건전성 지표 (단위: 억원)',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
        
    with col2:
        # 연체율 시각화
        delinquency_data = pd.DataFrame({
            '구분': ['연체대출비율', '순고정이하여신비율'],
            '2023년 3분기': [3.62, 3.62],
            '2024년 3분기': [2.30, 2.30]
        })
        
        fig = px.bar(
            delinquency_data,
            x='구분',
            y=['2023년 3분기', '2024년 3분기'],
            barmode='group',
            title='연체율 추이 (%)',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
    
    st.write("""
    자산건전성 측면에서는 고정이하분류여신이 60억 원으로 전년 동기(91억 원) 대비 34.1% 감소하였으며,
    부실여신도 29억 원으로 전년 동기(66억 원) 대비 56.1% 감소하여 건전성이 개선된 모습을 보이고 있습니다.
    
    연체대출비율은 2.30%로 전년 동기(3.62%) 대비 1.32%p 감소하였으며, 순고정이하여신비율 역시
    2.30%로 전년 동기(3.62%) 대비 개선되었습니다.
    
    다만, 대손충당금은 125억 원으로 전년 동기(175억 원) 대비 28.6% 감소하였으나, 
    이는 부실여신 감소에 따른 자연스러운 현상으로 보입니다. 충당금적립률은 여전히 
    적정 수준을 유지하고 있어 잠재적 손실 흡수 능력은 양호한 상태입니다.
    """)

# 3. 수익성 강화 전략
elif menu == "3. 수익성 강화 전략":
    st.markdown('<p class="main-header">3. 수익성 강화 전략</p>', unsafe_allow_html=True)
    
    # 수익성 강화 전략 개요
    st.markdown('<p class="subsection-header">3.1 전략 개요</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.write("""
        대명상호저축은행의 수익성을 개선하기 위해 다음과 같은 4가지 핵심 전략을 제안합니다.
        이 전략들은 은행의 현재 재무상태와 경쟁 환경, 그리고 지역적 특성을 고려하여 설계되었습니다.
        
        1. **대출 포트폴리오 최적화**
           - 기업대출과 개인대출의 비중 조정
           - 중소기업 특화 대출 상품 개발
           - 부동산 담보대출 다각화
        
        2. **예대금리차 개선**
           - 예금 상품 재설계를 통한 조달비용 절감
           - 특정 고객층 타겟팅을 통한 저원가성 예금 확대
           - 대출 상품별 금리 체계 최적화
        
        3. **비이자수익 확대**
           - 수수료 수입 확대를 위한 신규 서비스 도입
           - 자산관리 서비스 강화
           - 지역 기반 특화 부가서비스 개발
        
        4. **디지털 전환을 통한 효율성 제고**
           - 모바일뱅킹 서비스 강화
           - 업무 프로세스의 자동화
           - 데이터 기반 의사결정 체계 구축
        """)
        
    with col2:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 기대 효과
        
        - ROA: -0.75% → 0.3% 개선
        - NIM: 2.30% → 3.0% 확대
        - 비이자수익 비중: 5% → 15% 확대
        - 고정이하여신비율: 2.30% → 1.8% 개선
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 대출 포트폴리오 최적화
    st.markdown('<p class="subsection-header">3.2 대출 포트폴리오 최적화</p>', unsafe_allow_html=True)
    
    # 현재 VS 목표 대출 포트폴리오
    current_vs_target_loan = pd.DataFrame({
        '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
        '현재 비중(%)': [56.55, 38.38, 5.07],
        '목표 비중(%)': [60.00, 35.00, 5.00]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 현재 VS 목표 대출 포트폴리오 시각화
        fig = px.bar(
            current_vs_target_loan,
            x='구분',
            y=['현재 비중(%)', '목표 비중(%)'],
            barmode='group',
            title='대출 포트폴리오 조정 계획',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        # 담보별 대출 목표 시각화
        collateral_target = pd.DataFrame({
            '담보유형': ['부동산', '신용', '보증', '기타'],
            '현재 비중(%)': [53.43, 45.85, 0.39, 0.33],
            '목표 비중(%)': [60.00, 35.00, 4.00, 1.00]
        })
        
        fig = px.bar(
            collateral_target,
            x='담보유형',
            y=['현재 비중(%)', '목표 비중(%)'],
            barmode='group',
            title='담보별 대출 포트폴리오 조정 계획',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    **세부 실행 방안:**
    
    1. **중소기업 특화 대출 확대**
       - 현재 중소기업 대출 비중: 50.37% → 목표: 60%
       - 충북 제조업 중소기업 대상 '스마트공장 설비투자 대출' 신설
       - 제천 한방산업 클러스터 입주기업 대상 '바이오기업 성장 대출' 개발
       - 창업 7년 이내 혁신기업 대상 '스타트업 성장 지원 대출' 도입
    
    2. **부동산 담보대출 다각화**
       - 담보대출 비중 53.43% → 60%로 확대하여 리스크 관리 강화
       - 가계 부동산담보대출은 선별적으로 취급하여 건전성 유지
       - 사업용 부동산 담보대출의 경우 지역 상권분석 강화
       - 부동산 담보 감정평가 프로세스 고도화
    
    3. **보증부 대출 확대**
       - 현재 보증부 대출 비중: 0.39% → 목표: 4%
       - 지역신용보증재단, 신용보증기금과의 협약 확대
       - '충북 소상공인 특별보증' 프로그램 도입
       - 보증서 담보대출에 대한 우대금리 적용으로 고객 유인
    """)
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석 기반")
    
    # 예대금리차 개선
    st.markdown('<p class="subsection-header">3.3 예대금리차 개선</p>', unsafe_allow_html=True)
    
    # 금리 구조 데이터
    interest_structure = pd.DataFrame({
        '구분': ['조달 평균이자율', '운용 평균이자율', '이자마진'],
        '현재(%)': [3.02, 4.26, 1.24],
        '목표(%)': [2.70, 5.00, 2.30]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 금리 구조 시각화
        fig = px.bar(
            interest_structure,
            x='구분',
            y=['현재(%)', '목표(%)'],
            barmode='group',
            title='금리 구조 개선 계획',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 예대금리차 개선 핵심 전략
        
        **예금 상품 개편**
        - 정기예금 평균금리: 3.02% → 2.70%
        - 저원가성 핵심예금 비중: 1.34% → 10%
        
        **대출 상품 금리 최적화**
        - 평균 대출금리: 4.26% → 5.00%
        - 리스크 기반 금리체계 고도화
        
        **순이자마진**
        - 현재: 1.24% → 목표: 2.30%
        - 업계 평균 수준으로 회복
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("""
    **세부 실행 방안:**
    
    1. **예금 상품 재구성**
       - 거치식예금 의존도 축소 (현재 98.66% → 목표 90%)
       - 핵심예금(Core Deposit) 유치를 위한 '지역사랑 입출금통장' 출시
       - 디지털채널 전용 예금상품 도입으로 조달비용 절감
       - 고객 특성별 맞춤형 예금상품 개발 (청년층, 노년층, 자영업자 등)
    
    2. **대출 금리체계 최적화**
       - 신용등급별 차등금리 체계 고도화
       - 거래실적 연동 금리 할인 제도 도입
       - 지역 중소기업 및 소상공인 대상 프리미엄 대출 상품 개발
       - 상품별 원가 분석을 통한 최적 금리 설정 체계 구축
    
    3. **고객관계 기반 금리 전략**
       - 주거래 고객 우대제도 강화 (예적금, 대출 교차판매)
       - 주거래 정도에 따른 등급별 금리 혜택 패키지 도입
       - 장기거래 고객에 대한 로열티 프로그램 운영
       - 가족고객 우대 금리 제도 도입
    """)
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석 기반")
    
    # 비이자수익 확대
    st.markdown('<p class="subsection-header">3.4 비이자수익 확대</p>', unsafe_allow_html=True)
    
    # 비이자수익 목표
    non_interest_income = pd.DataFrame({
        '수익원': ['송금 및 결제 수수료', '펀드/보험 판매', '자산관리 서비스', 'PB 서비스', '기타 부가서비스'],
        '현재(억원)': [3, 2, 0, 0, 1],
        '목표(억원)': [5, 8, 4, 3, 5]
    })
    
    # 비이자수익 목표 시각화
    fig = px.bar(
        non_interest_income,
        x='수익원',
        y=['현재(억원)', '목표(억원)'],
        barmode='group',
        title='비이자수익 확대 계획',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    **세부 실행 방안:**
    
    1. **지역 특화 금융서비스 개발**
       - 충북 소상공인 대상 '사업자 종합금융 패키지' 출시
         (결제계좌, POS 연동, 매출관리, 세무지원 등 통합 서비스)
       - 지역 자영업자 대상 '상권분석 보고서' 유료 서비스 도입
       - 지역 내 부동산 중개업체와 연계한 '원스톱 부동산 금융 서비스' 제공
    
    2. **자산관리 서비스 도입**
       - 자산 5억 이상 고객 대상 '프리미엄 자산관리 서비스' 도입
       - 은퇴설계 상담 및 절세 컨설팅 서비스 유료화
       - 지역 내 전문가 네트워크 구축 (세무사, 변호사, 부동산 전문가 등)
       - 자산관리 전문인력 채용 및 양성
    
    3. **펀드/보험 판매 확대**
       - 증권사, 보험사와의 제휴를 통한 판매 채널 다변화
       - 고객 맞춤형 포트폴리오 추천 서비스 도입
       - 저축은행 특화 ELS, DLS 상품 개발 및 판매
       - 지역 특화 투자상품 개발 (충북 개발 프로젝트 연계 상품 등)
    
    4. **디지털 기반 부가서비스**
       - 모바일뱅킹 내 유료 부가서비스 도입
         (계좌 통합관리, 자산현황 분석, 예산관리 등)
       - 비대면 상담 서비스 유료화
       - 금융교육 프로그램 운영 (청소년, 은퇴자 등 대상)
    """)
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석 기반")
    
    # 디지털 전환
    st.markdown('<p class="subsection-header">3.5 디지털 전환을 통한 효율성 제고</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.write("""
        대명상호저축은행의 디지털 역량 강화를 통해 고객 경험을 개선하고 운영 효율성을 높이는 전략을 추진합니다.
        특히 지역 기반 소형 저축은행의 특성을 살려, 디지털과 대면 서비스의 조화를 통해 차별화된 서비스를
        제공하는 데 중점을 둡니다.
        
        **세부 실행 방안:**
        
        1. **모바일뱅킹 서비스 고도화**
           - 현재 기초 수준에서 종합 금융 플랫폼으로 확장
           - 직관적인 UI/UX로 고령층도 쉽게 이용 가능한 앱 설계
           - 계좌 개설부터 대출 실행까지 비대면 프로세스 완성
           - 지역 생활정보 및 혜택 연계 서비스 도입
        
        2. **업무 프로세스 자동화**
           - RPA(Robotic Process Automation) 도입으로 반복 업무 자동화
           - 대출 심사 프로세스 자동화 (서류 검토, 신용평가 등)
           - AI 기반 고객 응대 시스템 구축 (챗봇, 음성 상담 등)
           - 내부 업무 시스템 클라우드 전환으로 운영비용 절감
        
        3. **데이터 기반 의사결정 체계 구축**
           - 고객 데이터 통합 관리 시스템 구축
           - AI 기반 신용평가 모델 도입으로 리스크 관리 고도화
           - 고객 세그먼테이션을 통한 타겟 마케팅 강화
           - 데이터 분석 역량 강화를 위한 전문인력 확보
        """)
        
    with col2:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 디지털 전환 기대 효과
        
        **효율성 제고**
        - 업무처리 시간: 30% 단축
        - 운영비용: 15% 절감
        - 직원당 생산성: 20% 향상
        
        **고객 경험 개선**
        - 대출 처리 시간: 3일→1일
        - 고객만족도: 20% 향상
        - 모바일뱅킹 이용률: 30% 증가
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 디지털 전환 로드맵
    digital_roadmap = pd.DataFrame({
        '단계': ['1단계(2025 Q1-Q2)', '2단계(2025 Q3-Q4)', '3단계(2026 Q1-Q2)'],
        '주요과제': [
            '모바일앱 리뉴얼, RPA 일부 도입', 
            '비대면 대출 프로세스 완성, 데이터 분석 기반 구축', 
            'AI 기반 신용평가, 종합 금융 플랫폼화'
        ],
        '투자비용(억원)': [3, 5, 7]
    })
    
    st.table(digital_roadmap)
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석 기반")

# 4. 비용 최적화 방안
elif menu == "4. 비용 최적화 방안":
    st.markdown('<p class="main-header">4. 비용 최적화 방안</p>', unsafe_allow_html=True)
    
    # 비용 구조 분석
    st.markdown('<p class="subsection-header">4.1 현재 비용 구조 분석</p>', unsafe_allow_html=True)
    
    # 비용 구조 데이터
    cost_structure = pd.DataFrame({
        '비용항목': ['인건비', '점포운영비', 'IT시스템 유지비', '마케팅비', '기타 관리비'],
        '금액(억원)': [151, 83, 37, 22, 41],
        '비중(%)': [45.2, 24.9, 11.1, 6.6, 12.2]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 비용 구조 시각화
        fig = px.pie(
            cost_structure,
            values='금액(억원)',
            names='비용항목',
            title='비용 구조 현황 (2024년 3분기)',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        # 예상 비용 절감액 시각화
        savings_data = pd.DataFrame({
            '비용항목': ['인건비', '점포운영비', 'IT시스템 유지비', '마케팅비', '기타 관리비'],
            '현재 비용(억원)': [151, 83, 37, 22, 41],
            '목표 비용(억원)': [135, 63, 30, 25, 32]
        })
        
        fig = px.bar(
            savings_data,
            x='비용항목',
            y=['현재 비용(억원)', '목표 비용(억원)'],
            barmode='group',
            title='비용 최적화 목표',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    대명상호저축은행의 비용 구조를 분석한 결과, 인건비가 전체의 45.2%로 가장 큰 비중을 차지하고 있으며,
    점포운영비(24.9%), IT시스템 유지비(11.1%) 순으로 높은 비중을 보이고 있습니다.
    
    비용 효율성 측면에서 개선의 여지가 있는 영역을 식별하고, 이를 중심으로 비용 최적화 방안을
    수립하고자 합니다. 특히 디지털 전환과 연계한 운영 효율화를 통해 비용 절감과 서비스 품질 향상을
    동시에 달성하는 전략이 필요합니다.
    """)
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석 기반")
    
    # 효율화 방안
    st.markdown('<p class="subsection-header">4.2 비용 효율화 방안</p>', unsafe_allow_html=True)
    
    st.write("""
    1. **인력 운영 효율화**
       - **현황**: 직원 수 29명, 1인당 관리자산 81.6억원
       - **개선 방향**:
         - 업무 자동화를 통한 인력 운영 효율성 제고
         - 핵심 업무와 비핵심 업무 구분을 통한 인력
         - 성과 기반 보상체계 강화로 생산성 향상 유도
         - 전문 인력 확보를 통한 1인당 관리자산 증대
       - **기대효과**: 인건비 151억 원 → 135억 원 (10.6% 절감)
    
    2. **점포 운영 효율화**
       - **현황**: 본점과 충주지점 2개 영업점 운영
       - **개선 방향**:
         - 충주지점의 효율성 제고를 위한 공간 리노베이션
         - 셀프뱅킹 존(Self Banking Zone) 확대로 운영인력 최적화
         - 지점별 운영시간 최적화 (시간대별 고객 방문 분석 기반)
         - 복합 금융 공간으로 전환 (금융+커뮤니티 공간)
       - **기대효과**: 점포운영비 83억 원 → 63억 원 (24.1% 절감)
    
    3. **IT 시스템 비용 최적화**
       - **현황**: 자체 서버 운영, 레거시 시스템 유지 부담
       - **개선 방향**:
         - 클라우드 기반 시스템으로 단계적 전환
         - 오픈소스 솔루션 활용 확대
         - 금융 클라우드 특화 서비스 도입으로 보안성 강화와 비용 절감 동시 달성
         - IT 시스템 통합 및 표준화
       - **기대효과**: IT시스템 유지비 37억 원 → 30억 원 (18.9% 절감)
    
    4. **마케팅 효율성 제고**
       - **현황**: 전통적 마케팅 중심, 효과 측정 한계
       - **개선 방향**:
         - 디지털 마케팅 비중 확대 (전체 마케팅 예산의 60%)
         - 타겟 마케팅 강화를 통한 고객 획득비용 절감
         - 지역 특화 이벤트 및 프로모션으로 효율성 제고
         - 마케팅 성과 측정 체계화
       - **기대효과**: 마케팅 효율 20% 향상, 신규 고객 유치 30% 증가
    
    5. **기타 관리비용 절감**
       - **현황**: 경비 관리 체계 미흡, 비효율적 지출 존재
       - **개선 방향**:
         - 통합 비용관리 시스템 도입
         - 페이퍼리스 오피스 구현으로 소모품비 절감
         - 에너지 효율화를 통한 관리비 절감
         - 업무용 차량 운영 최적화
       - **기대효과**: 기타 관리비 41억 원 → 32억 원 (22.0% 절감)
    """)
    
    # 비용 절감 로드맵
    st.markdown('<p class="subsection-header">4.3 비용 절감 추진 로드맵</p>', unsafe_allow_html=True)
    
    # 비용 절감 로드맵 데이터
    cost_roadmap = pd.DataFrame({
        '추진 과제': [
            '인력 운영 효율화',
            '점포 운영 효율화',
            'IT 시스템 비용 최적화',
            '마케팅 효율성 제고',
            '기타 관리비용 절감'
        ],
        '2025 Q1': [
            '업무 프로세스 진단',
            '셀프뱅킹 존 설계',
            '클라우드 전환 계획 수립',
            '디지털 마케팅 전략 수립',
            '통합 비용관리 시스템 도입'
        ],
        '2025 Q2': [
            '인력 재배치 계획 시행',
            '충주지점 리노베이션',
            '일부 시스템 클라우드 전환',
            '타겟 마케팅 캠페인 시행',
            '페이퍼리스 시스템 도입'
        ],
        '2025 Q3': [
            '성과 기반 보상체계 도입',
            '운영시간 최적화 시행',
            '레거시 시스템 통합',
            '성과 측정 체계 도입',
            '에너지 효율화 사업'
        ],
        '2025 Q4': [
            '성과 평가 및 보완',
            '복합 금융 공간 구축',
            '전체 시스템 최적화 완료',
            '마케팅 ROI 분석 및 고도화',
            '전사 비용절감 체계 완성'
        ]
    })
    
    st.table(cost_roadmap)
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석 기반")
    
    # 비용 절감 효과
    st.markdown('<p class="subsection-header">4.4 비용 최적화 기대 효과</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 비용 효율화 기대효과 시각화
        savings_summary = pd.DataFrame({
            '비용항목': ['인건비', '점포운영비', 'IT시스템 유지비', '마케팅비', '기타 관리비', '총계'],
            '절감액(억원)': [16, 20, 7, -3, 9, 49],
            '절감률(%)': [10.6, 24.1, 18.9, -13.6, 22.0, 14.7]
        })
        
        fig = px.bar(
            savings_summary[savings_summary['비용항목'] != '총계'],
            x='비용항목',
            y='절감액(억원)',
            text='절감률(%)',
            title='항목별 비용 절감 효과',
            height=400
        )
        fig.update_traces(texttemplate='%{text}%', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        # 비용효율성 지표 개선 효과
        efficiency_metrics = pd.DataFrame({
            '효율성 지표': ['비용수익비율(%)', '1인당 관리자산(억원)', '1인당 순이익(백만원)', '점포당 수익(억원)'],
            '현재': [78.5, 81.6, -61.2, -11.8],
            '목표': [63.2, 105.3, 32.5, 14.7]
        })
        
        fig = px.bar(
            efficiency_metrics,
            x='효율성 지표',
            y=['현재', '목표'],
            barmode='group',
            title='효율성 지표 개선 효과',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    비용 최적화 방안을 통해 총 49억 원(14.7%)의 비용 절감 효과가 예상됩니다. 특히 점포운영비(24.1%)와
    기타 관리비(22.0%)에서 큰 폭의 절감이 가능할 것으로 보입니다. 반면, 마케팅비는 디지털 전환 및
    타겟 마케팅 강화를 위해 오히려 13.6% 증액하여 신규 고객 유치와 기존 고객의 거래 활성화를 도모할 계획입니다.
    
    이러한 비용 최적화를 통해 비용수익비율(Cost Income Ratio)을 현재 78.5%에서 목표 63.2%로 개선하여
    업계 평균 수준으로 향상시킬 수 있을 것으로 전망됩니다. 또한 1인당 관리자산은 81.6억 원에서 105.3억 원으로,
    1인당 순이익은 -61.2백만 원에서 32.5백만 원으로 개선될 것으로 예상됩니다.
    """)
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석 기반")

# 5. 실행 로드맵
elif menu == "5. 실행 로드맵":
    st.markdown('<p class="main-header">5. 실행 로드맵</p>', unsafe_allow_html=True)
    
    # 전체 로드맵
    st.markdown('<p class="subsection-header">5.1 전체 실행 로드맵</p>', unsafe_allow_html=True)
    
    # 로드맵 시각화 (간트 차트)
    gantt_data = pd.DataFrame([
        dict(Task="대출 포트폴리오 최적화", Start='2025-01-01', Finish='2025-12-31', Resource="핵심"),
        dict(Task="예대금리차 개선", Start='2025-01-01', Finish='2025-09-30', Resource="핵심"),
        dict(Task="비이자수익 확대", Start='2025-03-01', Finish='2025-12-31', Resource="우선"),
        dict(Task="디지털 전환", Start='2025-01-01', Finish='2026-06-30', Resource="핵심"),
        dict(Task="점포 운영 효율화", Start='2025-02-01', Finish='2025-10-31', Resource="우선"),
        dict(Task="인력 운영 효율화", Start='2025-01-01', Finish='2025-12-31', Resource="우선"),
        dict(Task="IT 시스템 최적화", Start='2025-03-01', Finish='2025-12-31', Resource="일반"),
        dict(Task="마케팅 효율성 제고", Start='2025-04-01', Finish='2025-09-30', Resource="일반"),
        dict(Task="지역 특화 상품 개발", Start='2025-02-01', Finish='2025-07-31', Resource="핵심")
    ])
    
    fig = px.timeline(
        gantt_data, 
        x_start="Start", 
        x_end="Finish", 
        y="Task",
        color="Resource",
        color_discrete_map={"핵심": "rgb(46, 134, 193)", "우선": "rgb(142, 68, 173)", "일반": "rgb(243, 156, 18)"},
        title="대명상호저축은행 수익성 강화 전략 실행 로드맵"
    )
    fig.update_layout(height=450)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("출처: 전략 실행 계획 분석")
    
    # 분기별 주요 과제
    st.markdown('<p class="subsection-header">5.2 분기별 주요 과제</p>', unsafe_allow_html=True)
    
    st.table(roadmap_data)
    
    st.write("""
    2025년 수익성 강화 전략은 4개 분기로 나누어 체계적으로 실행할 계획입니다. 각 영역별 주요 과제는 다음과 같습니다:
    
    **2025년 1분기 (1~3월)**
    - 상품개발: AI 기반 신용평가 시스템 도입
    - 디지털전환: 모바일앱 리뉴얼 및 UI/UX 개선
    - 지점개편: 셀프코너 확대 및 디지털 기기 도입
    - 리스크관리: 부실채권 20% 상각 및 관리체계 개선
    
    **2025년 2분기 (4~6월)**
    - 상품개발: 중소기업 특화 대출 상품 출시
    - 디지털전환: 클라우드 시스템 전환 및 레거시 시스템 통합
    - 지점개편: 충주지점 통폐합 검토 및 효율화 방안 시행
    - 리스크관리: 신용평가시스템 고도화 및 여신심사 프로세스 개선
    
    **2025년 3분기 (7~9월)**
    - 상품개발: 정기예금 금리 체계 개편 및 핵심예금 확대
    - 디지털전환: 전자계약 시스템 도입으로 페이퍼리스 업무 구현
    - 지점개편: 24시간 CD/ATM 기능 강화 및 무인 영업점 테스트
    - 리스크관리: 부실채권 추가 30% 상각 및 자산건전성 강화
    
    **2025년 4분기 (10~12월)**
    - 상품개발: 충북 지역 특화 펀드 조성 및 출시
    - 디지털전환: 빅데이터 분석 시스템 도입으로 고객 통찰력 강화
    - 지점개편: 디지털존 구축 및 복합 금융 공간으로 전환
    - 리스크관리: 부실채권 50% 상각 완료 및 리스크 관리 체계 고도화
    """)
    st.caption("출처: 전략 실행 계획 분석")
    
    # 주요 투자 계획
    st.markdown('<p class="subsection-header">5.3 주요 투자 계획</p>', unsafe_allow_html=True)
    
    # 투자 계획 데이터
    investment_plan = pd.DataFrame({
        '투자 영역': ['디지털 시스템', '지점 리노베이션', '상품 개발', '인력 역량 강화', '브랜드 마케팅'],
        '투자액(억원)': [15, 10, 5, 3, 7],
        'ROI(%)': [35, 25, 40, 30, 20]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 투자액 시각화
        fig = px.bar(
            investment_plan,
            x='투자 영역',
            y='투자액(억원)',
            title='영역별 투자 계획',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        # ROI 시각화
        fig = px.bar(
            investment_plan,
            x='투자 영역',
            y='ROI(%)',
            title='영역별 투자 수익률 전망',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    수익성 강화 전략 실행을 위한 총 투자금액은 40억 원으로 계획되어 있습니다. 이 중 가장 큰 비중을
    차지하는 것은 디지털 시스템 투자(15억 원)로, 모바일뱅킹 고도화와 업무 자동화 시스템 구축에
    집중 투자할 예정입니다.
    
    지점 리노베이션에 10억 원을 투자하여 디지털 기기 도입 및 고객 경험 개선을 추진하고,
    상품 개발에 5억 원, 인력 역량 강화에 3억 원, 브랜드 마케팅에 7억 원을 각각 투자할 계획입니다.
    
    투자 영역별 ROI(투자수익률)은 상품 개발이 40%로 가장 높을 것으로 예상되며,
    디지털 시스템(35%), 인력 역량 강화(30%) 순으로 높은 수익률이 기대됩니다.
    
    투자 재원은 기존 유보이익 및 운영 효율화를 통한 비용 절감분으로 충당할 예정이며,
    필요 시 자본 확충을 검토할 계획입니다.
    """)
    st.caption("출처: 전략 실행 계획 분석")
    
    # 실행 조직 및 거버넌스
    st.markdown('<p class="subsection-header">5.4 실행 조직 및 거버넌스</p>', unsafe_allow_html=True)
    
    st.write("""
    전략 실행의 효과적인 추진을 위해 다음과 같은 실행 체계를 구축합니다:
    
    1. **전략실행위원회 구성**
       - 대표이사를 위원장으로 하는 전사적 실행 조직 구성
       - 영업, IT, 리스크, 재무, 인사 등 핵심부서장 참여
       - 월 1회 정기 회의를 통한 진행 상황 점검 및 이슈 해결
    
    2. **전담 태스크포스팀(TFT) 운영**
       - '수익성 강화 TFT' 신설 (실무진 중심 5~7명 구성)
       - 3개 중점 과제별 서브 TFT 구성 (대출 포트폴리오 / 예대금리차 / 디지털)
       - 주 1회 실무 회의를 통한 세부 과제 추진
    
    3. **성과 관리 체계**
       - KPI 중심의 월별/분기별 성과 측정 체계 구축
       - 핵심 지표: ROA, NIM, 비이자수익 비중, 비용수익비율, 고정이하여신비율
       - 실시간 성과 대시보드 구축으로 가시성 확보
    
    4. **보상 연계 체계**
       - 전략 실행 성과를 인센티브 체계와 연동
       - 핵심 성과 지표 달성 정도에 따른 차등 보상
       - 혁신적 아이디어 제안 및 실행에 대한 별도 포상
    """)
    
    # 실행 조직도 시각화
    st.image("https://mermaid.ink/img/pako:eNp1kk1vgzAMhv9K5DMTEkPLR6UDJKZNmrtPFYhFaqCJlEBVVf3vM2RdC9N8sb0-r-1jpDXUirWAM_EmbkZxx_W-UjQpDqSs7RFPTkZViu9yqdYi3TdCClYHa3P_GyaXeTi5-DwLrP8ZmEVutMshUH5qTgu968VJLWrTvT4qOAjD9kLDtpS7FlBUnC0DSU7fDGm7TTQ6EPCdGuKshrqkQmjArCuRisQ2X-4ADxkSTcYbZEipniyCB3XrZLc-W7xGVtNXsHXNbceyLbrTkewm1CzAKHti9Ii6pFQiMLBxYGkF6NciHGUbZOPMzWGMHg3MJlyaLAgNG0789Glzu1Q24e9C861Z6dC9fp-5811mzY_4FCJ6gXnCY2YHbsFbdA_sOdJkj-0Z2r6Elec9wMyIWvS_uOxOhJ6Jzxv-aWWJpGJF3oQ9HunEoZh4NNMDS-KIPyRxEC9fK_x1xnLC83gRx2dCvzrEUX9NW0rlu1vEFn8ADLrpYw", caption="전략 실행 조직도")
    st.caption("출처: 전략 실행 계획 분석")

# 6. 결론 및 기대효과
elif menu == "6. 결론 및 기대효과":
    st.markdown('<p class="main-header">6. 결론 및 기대효과</p>', unsafe_allow_html=True)
    
    # 재무적 기대효과
    st.markdown('<p class="subsection-header">6.1 재무적 기대효과</p>', unsafe_allow_html=True)
    
    # 재무 지표 개선 예상치
    financial_projection = pd.DataFrame({
        '지표': ['총자산순수익률(ROA)', '순이자마진(NIM)', '비이자수익 비중', '비용수익비율', 'BIS 자기자본비율', '고정이하여신비율'],
        '현재(2024 Q3)': [-0.75, 2.30, 5.0, 78.5, 12.13, 2.30],
        '목표(2025 Q4)': [0.30, 3.00, 15.0, 63.2, 13.50, 1.80],
        '개선폭': [1.05, 0.70, 10.0, -15.3, 1.37, -0.50]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 수익성 지표 개선 시각화
        profitability_projection = financial_projection[financial_projection['지표'].isin(['총자산순수익률(ROA)', '순이자마진(NIM)', '비이자수익 비중'])]
        
        fig = px.bar(
            profitability_projection,
            x='지표',
            y=['현재(2024 Q3)', '목표(2025 Q4)'],
            barmode='group',
            title='수익성 지표 개선 전망',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        # 안정성 지표 개선 시각화
        stability_projection = financial_projection[financial_projection['지표'].isin(['비용수익비율', 'BIS 자기자본비율', '고정이하여신비율'])]
        
        fig = px.bar(
            stability_projection,
            x='지표',
            y=['현재(2024 Q3)', '목표(2025 Q4)'],
            barmode='group',
            title='효율성 및 안정성 지표 개선 전망',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # 손익 개선 효과
    st.write("""
    제안된 수익성 강화 전략을 성공적으로 실행할 경우, 2024년 3분기 현재 적자 상태인 재무 상황을
    2025년 말까지 흑자로 전환시킬 수 있을 것으로 예상됩니다.
    
    주요 개선 효과는 다음과 같습니다:
    
    1. **이자이익 증대**
       - 순이자마진(NIM) 0.7%p 개선을 통한 연간 약 16억 원 수익 증가
       - 예대금리차 확대를 통한 이자이익 증가 약 23억 원
    
    2. **비이자수익 확대**
       - 비이자수익 비중 10%p 확대를 통한 연간 약 25억 원 수익 증가
       - 수수료 수입 확대 및 자산관리 서비스 도입 효과
    
    3. **비용 절감**
       - 비용수익비율 15.3%p 개선을 통한 연간 약 49억 원 비용 절감
       - 운영 효율화 및 디지털 전환을 통한 생산성 향상
    
    이러한 개선 효과에 따라, 2025년 말 기준 연간 약 7억 원의 당기순이익 달성이 가능할 것으로
    전망합니다. 이는 총자산순수익률(ROA) 0.3% 수준에 해당합니다.
    """)
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석 기반")
    
    # 비재무적 기대효과
    st.markdown('<p class="subsection-header">6.2 비재무적 기대효과</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **1. 고객 관점**
        - 디지털 서비스 강화로 고객 편의성 향상
        - 지역 특화 상품을 통한 고객 로열티 제고
        - 맞춤형 금융 서비스로 고객 만족도 향상
        - 자산관리 서비스를 통한 고객 가치 제고
        - 연령대별 맞춤형 금융 솔루션 제공
        
        **2. 내부 프로세스 관점**
        - 업무 효율성 30% 향상
        - 리스크 관리 체계 고도화
        - 의사결정 속도 및 정확성 개선
        - 신상품 개발 프로세스 체계화
        - 데이터 기반 경영 인프라 구축
        """)
        
    with col2:
        st.write("""
        **3. 임직원 관점**
        - 직무 만족도 향상 및 업무 몰입도 증가
        - 핵심 역량 중심의 인력 운영 실현
        - 성과 중심 문화 정착
        - 전문성 강화를 위한 교육 기회 확대
        - 혁신 마인드 및 변화 수용성 향상
        
        **4. 지역사회 관점**
        - 지역 중소기업 성장 지원 강화
        - 지역 금융 접근성 향상
        - 지역사회 공헌 활동 확대
        - 충북 지역 내 금융 리더십 확보
        - 지역 경제 활성화에 기여
        """)
    
    # 경영 지표 개선 시뮬레이션 결과
    st.markdown('<p class="subsection-header">6.3 주요 지표 개선 시뮬레이션</p>', unsafe_allow_html=True)
    
    # 분기별 수익성 개선 시뮬레이션 데이터
    quarterly_projection = pd.DataFrame({
        '분기': ['2024 Q4', '2025 Q1', '2025 Q2', '2025 Q3', '2025 Q4'],
        'ROA(%)': [-0.65, -0.40, -0.10, 0.15, 0.30],
        'NIM(%)': [2.35, 2.50, 2.70, 2.85, 3.00],
        '비용수익비율(%)': [77.0, 74.0, 70.0, 66.5, 63.2]
    })
    
    # 분기별 개선 추이 시각화
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=quarterly_projection['분기'],
        y=quarterly_projection['ROA(%)'],
        name='ROA(%)',
        mode='lines+markers',
        line=dict(color='rgb(26, 118, 255)', width=3),
        marker=dict(size=8)
    ))
    fig.add_trace(go.Scatter(
        x=quarterly_projection['분기'],
        y=quarterly_projection['NIM(%)'],
        name='NIM(%)',
        mode='lines+markers',
        line=dict(color='rgb(46, 204, 113)', width=3),
        marker=dict(size=8)
    ))
    fig.add_trace(go.Scatter(
        x=quarterly_projection['분기'],
        y=quarterly_projection['비용수익비율(%)'],
        name='비용수익비율(%)',
        mode='lines+markers',
        line=dict(color='rgb(231, 76, 60)', width=3),
        marker=dict(size=8),
        yaxis='y2'
    ))
    fig.update_layout(
        title='분기별 주요 지표 개선 시뮬레이션',
        xaxis=dict(title='분기'),
        yaxis=dict(title='ROA/NIM(%)', side='left'),
        yaxis2=dict(title='비용수익비율(%)', side='right', overlaying='y', range=[60, 80]),
        legend=dict(x=0.01, y=0.99),
        height=450
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption("출처: 전략 시뮬레이션 분석")
    
    # 수익구조 개선 효과
    st.markdown("### 수익 구조 개선 효과")
    
    # 현재 vs 목표 수익구조
    income_structure = pd.DataFrame({
        '수익 구조': ['이자이익', '수수료수익', '기타영업수익', '기타'],
        '현재(%)': [92, 3, 2, 3],
        '목표(%)': [82, 10, 5, 3]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 현재 수익구조
        fig = px.pie(
            values=income_structure['현재(%)'],
            names=income_structure['수익 구조'],
            title='현재 수익 구조(2024 Q3)'
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        # 목표 수익구조
        fig = px.pie(
            values=income_structure['목표(%)'],
            names=income_structure['수익 구조'],
            title='목표 수익 구조(2025 Q4)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # 결론
    st.markdown('<p class="subsection-header">6.4 결론 및 향후 방향</p>', unsafe_allow_html=True)
    
    st.write("""
    대명상호저축은행은 50여 년의 역사와 지역사회에서의 신뢰를 바탕으로, 새로운 도약을 위한
    전환점에 서 있습니다. 본 보고서에서 제안한 수익성 강화 전략은 단순한 재무적 성과 개선을 넘어,
    디지털 시대에 지속가능한 성장 기반을 구축하기 위한 포괄적인 혁신 방안입니다.
    
    이 전략의 성공적인 실행을 통해 다음과 같은 중장기적 목표 달성이 가능할 것으로 기대됩니다:
    
    1. **지속가능한 수익 구조 확립**
       - 이자이익과 비이자수익의 균형적인 성장
       - 안정적인 ROA 0.5% 이상 달성 (2026년 목표)
       - 경기 변동에 강한 다각화된 수익 구조 구축
    
    2. **디지털 역량 기반의 경쟁우위 확보**
       - 디지털과 대면 서비스의 차별화된 융합 모델 구축
       - 데이터 기반 의사결정을 통한 경영 효율성 제고
       - 기술 혁신을 통한 신규 비즈니스 모델 개발
    
    3. **지역 금융의 중심으로 위상 강화**
       - 충북 지역 금융 허브로서의 브랜드 가치 제고
       - 지역 중소기업 및 소상공인과의 상생 관계 구축
       - ESG 경영을 통한 사회적 가치 창출 선도
    
    4. **임직원 역량 및 조직문화 혁신**
       - 디지털 역량과 전문성을 갖춘 인재 육성
       - 혁신적이고 유연한 조직문화 정착
       - 미래 금융환경 변화에 선제적으로 대응할 수 있는 조직 역량 강화
    
    본 전략의 실행은 대명상호저축은행의 현재 상황을 근본적으로 개선하는 동시에,
    미래 지향적인 금융기관으로의 변화를 가져올 것입니다. 이를 통해 주주 가치 제고,
    고객 만족도 향상, 임직원 자부심 증대, 그리고 지역사회 발전에 기여하는
    선순환적 성장 모델을 구축할 수 있을 것입니다.
    
    '지역사회의 발전과 함께하는 지역 최고 금융기관'이라는 비전을 실현하기 위한
    이 여정에 모든 이해관계자들의 적극적인 참여와 지지가 필요합니다.
    """)
    
    # 마무리 인사이트
    st.markdown('<div class="insight-box">', unsafe_allow_html=True)
    st.markdown("""
    ### 핵심 인사이트
    
    대명상호저축은행은 지역 밀착형 서비스와 디지털 혁신의 균형을 통해 수익성 회복과
    지속가능한 성장을 동시에 달성할 수 있습니다. 이러한 변화는 단순한 수익성 개선을 넘어
    지역 금융 생태계 전반에 긍정적인 영향을 미칠 수 있는 중요한 전환점이 될 것입니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 종합 분석")

# # 7. 동종업권 비교분석 및 전략 제언
# elif menu == "7. 동종업권 비교분석 및 전략 제언":
#     st.markdown('<p class="main-header">7. 동종업권 비교분석 및 전략 제언</p>', unsafe_allow_html=True)
    
#     # 충청·강원권 저축은행 업계 현황
#     st.markdown('<p class="subsection-header">7.1 충청·강원권 저축은행 업계 현황</p>', unsafe_allow_html=True)
    
#     # 비교 데이터 시각화
#     comparison_data = pd.DataFrame({
#         '은행명': ['대명', 'CK', 'KB', 'BNK', '오투', '청주'],
#         '자본총계(억)': [2365, 4795, 19552, 8352, 3956, 4519],
#         '부채총계(억)': [2078, , 15653, 8352, 3222, 3239],
#         '예수금(억)': [2157, 5785, 17173, 8201, 3294, 3940],
#         'NIM(%)': [2.30, 2.86, 3.05, 2.78, 2.50, 2.15],
#         'ROA(%)': [-0.75, -0.40, 0.30, -0.25, -1.53, -0.85]
#     })
#     comparison_data2 = pd.DataFrame({
#         '은행명': ['대명', 'CK', 'KB', 'BNK', '오투', '청주'],
#         '자본총계(억)': [2365, 4795, 19552, 8352, 3956, 4519],
#         '부채총계(억)': [2078, , 15653, 8352, 3222, 3239],
#         '예수금(억)': [2157, 5785, 17173, 8201, 3294, 3940],
#         'NIM(%)': [2.30, 2.86, 3.05, 2.78, 2.50, 2.15],
#         'ROA(%)': [-0.75, -0.40, 0.30, -0.25, -1.53, -0.85]
#     })

#     col1, col2 = st.columns(2)
    
#     with col1:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['NIM(%)', 'ROA(%)'],
#             barmode='group',
#             title='지역 저축은행 수익성 비교',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)
        
#     with col2:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['총자산(억)', '대출금(억)', '예수금(억)'],
#             barmode='group',
#             title='지역 저축은행 규모 비교',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)
    
#     st.caption("출처: 각 저축은행 2024년 3분기 경영공시자료")

#     # 경쟁사 성공 사례 분석
#     st.markdown('<p class="subsection-header">7.2 경쟁사 성공 사례 분석</p>', unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("""
#         ### KB저축은행 사례
        
#         **핵심 전략:**
#         - 디지털 전환 가속화
#         - 모바일뱅킹 고도화
#         - AI 기반 여신심사 시스템 도입
        
#         **주요 성과:**
#         - 2024년 3분기 순이익 7억 원 흑자 전환
#         - NIM 3.05% (업계 평균 2.5~2.8% 상회)
#         - 디지털 채널 신규고객 유입비중 43% 달성
#         - 대출심사 시간 60% 단축
#         """)
        
#     with col2:
#         st.markdown("""
#         ### BNK저축은행 사례
        
#         **핵심 전략:**
#         - 대출 포트폴리오 재편
#         - 기업대출 비중 축소 (55.49% → 46.58%)
#         - 가계대출 확대 (53.29% → 63.5%)
        
#         **주요 성과:**
#         - 부실채권비율 개선 (3.75% → 2.30%)
#         - 수수료수익 34% 증가
#         - 고정이하여신비율 1.2%p 개선
#         """)
    
#     st.caption("출처: KB저축은행, BNK저축은행 2024년 3분기 실적보고서")

#     # 대명저축은행 전략적 제언
#     st.markdown('<p class="subsection-header">7.3 대명저축은행 전략적 제언</p>', unsafe_allow_html=True)
    
#     # 고객 유치 강화 방안
#     st.markdown("#### A. 고객 유치 강화 방안")
    
#     # 지역 인구구조 분석
#     population_data = pd.DataFrame({
#         '연령대': ['20대', '30대', '40대', '50대', '60대 이상'],
#         '비중(%)': [18.2, 22.1, 25.4, 19.8, 14.5]
#     })
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         fig = px.pie(
#             population_data,
#             names='연령대',
#             values='비중(%)',
#             title='충북 지역 인구구조 분석',
#             hole=0.3
#         )
#         st.plotly_chart(fig, use_container_width=True)
        
#     with col2:
#         st.markdown("""
#         **실행 방안:**
        
#         1. **MZ 세대 타겟팅**
#            - 모바일 청년특화 상품 개발
#            - 간편 신용평가 시스템 도입
#            - 증권사 제휴 CMA 통합관리 서비스
        
#         2. **1:1 금융컨설팅 시스템**
#            - AI 기반 맞춤형 포트폴리오 추천
#            - 지역 소상공인 무료 세무컨설팅
#            - 실시간 상담 챗봇 서비스
#         """)
    
#     st.caption("출처: 한국은행 지역경제동향보고서 충북편 (2024.11)")
    
#     # 리스크 관리 선진화
#     st.markdown("#### B. 리스크 관리 선진화")
    
#     risk_roadmap = pd.DataFrame({
#         '단계': ['1Q 2025', '2Q 2025', '3Q 2025', '4Q 2025'],
#         '주요과제': ['AI 예측모델 구축', '부동산 LTV 강화', '산업별 리스크 분류', '스트레스 테스트 체계화'],
#         '투자액(억)': [3.2, 1.5, 2.1, 1.8]
#     })
    
#     st.table(risk_roadmap)
    
#     st.write("""
#     **부실채권 관리 강화:**
#     - 현황: 고정이하분류여신 60억 원 (총대출의 3.34%)
#     - 목표: 2025년 말까지 1.8% 이하 감축
#     - 산업별 차별화된 리스크 관리 체계 구축
#     """)
    
#     # 수익성 혁신 전략
#     st.markdown("#### C. 수익성 혁신 전략")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("""
#         **핵심과제: 비이자수익 비중 확대**
#         1. 충북 특화 상품 개발
#            - 한방산업 클러스터 지원 펀드
#            - 지역 농축산물 유통 플랫폼
#            - 바이오산업 특화 대출상품
#         """)
        
#     with col2:
#         st.markdown("""
#         **금융제휴 확대 계획**
#         | 제휴사 | 협력내용 | 예상수익(억) |
#         |---------|---------|-------------|
#         | KB증권 | 연계CMA 서비스 | 2.3 |
#         | DB손해보험 | 맞춤형 보험판매 | 1.8 |
#         | 제천창조경제혁신센터 | 스타트업 성장패키지 | 1.2 |
#         """)
    
#     # 참고문헌
#     st.markdown('<p class="subsection-header">8. 참고문헌</p>', unsafe_allow_html=True)
    
#     st.write("""
#     1. 대명상호저축은행 2024 / 3분기 경영공시 (2024.11)
#     2. 한성저축은행 2024 / 3분기 경영공시 (2024.11)
#     3. 아산저축은행 2024 / 3분기 경영공시 (2024.11)
#     4. 오투저축은행 2024 / 3분기 경영공시 (2024.11)
#     5. 청주저축은행 2024 / 3분기 경영공시 (2024.11)
#     6. 한국은행 「지역경제동향보고서」 충북편 (2024.11)
#     7. 금융감독원 「저축은행업 경영분석」 (2024.10)
#     8. 서울대학교 인구연구소 「지역별 인구전망 보고서」 (2024)
#     """)
# 7. 동종업권 비교분석 및 전략 제언
# elif menu == "7. 동종업권 비교분석 및 전략 제언":
#     st.markdown('<p class="main-header">7. 동종업권 비교분석 및 전략 제언</p>', unsafe_allow_html=True)
    
#     # 충청·강원권 저축은행 업계 현황
#     st.markdown('<p class="subsection-header">7.1 충청·강원권 저축은행 업계 현황</p>', unsafe_allow_html=True)
    
#     # 비교 데이터 (사용자가 제공한 데이터 기반)
#     comparison_data = pd.DataFrame({
#         '은행명': ['대명', 'CK', '오투', '청주', '한성'],
#         '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '청주, 천안', '대전, 청주, 옥천'],
#         'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
#         'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
#         'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
#         'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
#         '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
#         '연체대출비율(%) 2023': [2.30, 2.26, 4.83, 5.34, 6.84],
#         '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
#         '부동산 대출금(%) 2023': [33.74, 93.28, 63.60, 13.04, 51.00],
#         'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
#         '카드(건) 2024': [0, 17, 6, 1547, 0],
#         '카드(건) 2023': [0, 0, 4, 11178, 0]
#     })

#     st.write("""
#     충청·강원권 저축은행의 2024년 3분기 데이터를 분석한 결과, 대명상호저축은행은 수익성(ROA)과 연체대출비율에서 경쟁사 대비 열위에 있으며,
#     BIS 자기자본비율은 안정적이지만 개선 여지가 있는 것으로 나타났습니다. 아래 시각화를 통해 주요 지표를 비교합니다.
#     """)

#     # 비교 시각화
#     col1, col2 = st.columns(2)
    
#     with col1:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['ROA(%) 2024', 'ROA(%) 2023'],
#             barmode='group',
#             title='총자산순수익률(ROA) 비교 (2023 vs 2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)
        
#     with col2:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['연체대출비율(%) 2024', '연체대출비율(%) 2023'],
#             barmode='group',
#             title='연체대출비율 비교 (2023 vs 2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     col3, col4 = st.columns(2)
    
#     with col3:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'],
#             barmode='group',
#             title='BIS 자기자본비율 비교 (2023 vs 2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)
        
#     with col4:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['부동산 대출금(%) 2024', '부동산 대출금(%) 2023'],
#             barmode='group',
#             title='부동산 대출금 비율 비교 (2023 vs 2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     st.caption("출처: 각 저축은행 2024년 3분기 경영공시자료 및 사용자 제공 데이터")

#     # 경쟁사 분석 및 인사이트
#     st.markdown('<p class="subsection-header">7.2 경쟁사 분석 및 인사이트</p>', unsafe_allow_html=True)
    
#     st.write("""
#     아래는 동종업권 내 주요 은행들의 성과와 특징을 분석한 결과입니다. 대명상호저축은행의 전략 수립에 참고할 수 있는 인사이트를 도출했습니다.
#     """)

#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("""
#         ### CK저축은행 (강원도 - 강릉, 춘천)
#         - **특징**: 2024년 ROA 1.64%로 동종업권 내 높은 수익성을 기록했으나, 2023년 4.01% 대비 감소.
#         - **성공 요인**: 부동산 대출 비중을 93.28%에서 43.35%로 대폭 축소하며 리스크를 관리하고, 자산 건전성을 강화.
#         - **인사이트**: 부동산 의존도를 낮추고 다양한 대출 포트폴리오를 구축하면 수익성과 안정성을 동시에 확보 가능.
#         """)
        
#     with col2:
#         st.markdown("""
#         ### 오투저축은행 (충청남도 - 대전, 천안)
#         - **특징**: ROA가 -1.53%로 저조하며, 연체대출비율 12.92%로 리스크가 높음.
#         - **문제점**: 부동산 대출 비중이 73.3%로 높아 부동산 시장 변동에 취약.
#         - **인사이트**: 과도한 부동산 대출 의존은 수익성과 자산 건전성을 악화시킬 수 있으므로, 대명은 이를 반면교사로 삼아야 함.
#         """)

#     col3, col4 = st.columns(2)
    
#     with col3:
#         st.markdown("""
#         ### 청주저축은행 (청주, 천안)
#         - **특징**: 카드 건수가 2023년 11,178건에서 2024년 1,547건으로 급감하며 사업 구조 변화 추정.
#         - **성공 요인**: 부동산 대출 비중을 13.04%에서 20.24%로 낮게 유지하며 안정적인 자산 관리.
#         - **인사이트**: 카드 사업 축소는 수익 다변화에 제약을 줄 수 있으나, 낮은 부동산 의존도는 안정성을 높이는 요인.
#         """)
        
#     with col4:
#         st.markdown("""
#         ### 한성저축은행 (대전, 청주, 옥천)
#         - **특징**: BIS 자기자본비율 22.49%로 동종업권 최고 수준, 안정적인 자본 구조.
#         - **성공 요인**: 연체대출비율을 6.84%에서 8.80%로 관리하며 자산 건전성을 유지.
#         - **인사이트**: 높은 자본비율과 적정 연체 관리의 조화는 장기적인 안정성을 담보할 수 있음.
#         """)

#     # 대명저축은행 전략적 제언
#     st.markdown('<p class="subsection-header">7.3 대명저축은행 전략적 제언</p>', unsafe_allow_html=True)
    
#     st.write("""
#     동종업권 분석을 기반으로 대명상호저축은행의 수익성 개선과 경쟁력 강화를 위한 전략을 다음과 같이 제안합니다.
#     """)

#     # A. 고객 유치 강화 방안
#     st.markdown("#### A. 고객 유치 강화 방안")
    
#     st.write("""
#     - **현황**: 대명은 카드 사업이 전무하며, 고객 기반 확대가 필요함.
#     - **제안**:
#       1. **디지털 기반 신규 고객 유치**: CK저축은행처럼 모바일뱅킹을 강화하여 젊은 층을 타겟팅.
#       2. **지역 특화 서비스**: 충북 제천·충주 지역의 중소기업 및 소상공인을 위한 맞춤형 대출 상품 개발.
#       3. **카드 사업 재도입 검토**: 청주의 카드 사업 축소 사례를 반면교사로 삼아, 소규모 지역 맞춤형 카드 서비스 도입.
#     """)

#     # B. 리스크 관리 선진화
#     st.markdown("#### B. 리스크 관리 선진화")
    
#     risk_roadmap = pd.DataFrame({
#         '단계': ['1Q 2025', '2Q 2025', '3Q 2025', '4Q 2025'],
#         '주요과제': [
#             '연체대출비율 10%에서 8%로 감축',
#             '부동산 대출 비중 45.85%에서 40%로 조정',
#             'PF대출 리스크 평가 강화',
#             'AI 기반 리스크 예측 시스템 도입'
#         ],
#         '목표': ['자산 건전성 개선', '부동산 의존도 감소', 'PF대출 관리 강화', '리스크 예측 정확도 20% 향상']
#     })
    
#     st.table(risk_roadmap)
    
#     st.write("""
#     - **현황**: 연체대출비율 10%로 동종업권 대비 높고, PF대출 비중 31.9%로 리스크 노출 우려.
#     - **제안**: 오투저축은행의 높은 연체율(12.92%)을 반면교사로 삼아, 부동산 및 PF대출 비중을 줄이고 AI 기반 리스크 관리 시스템을 도입.
#     """)

#     # C. 수익성 혁신 전략
#     st.markdown("#### C. 수익성 혁신 전략")
    
#     profitability_targets = pd.DataFrame({
#         '지표': ['ROA(%)', 'NIM(%)', '비이자수익 비중(%)'],
#         '현재(2024)': [-0.75, 2.30, 5.0],
#         '목표(2025)': [0.30, 3.00, 15.0]
#     })
    
#     fig = px.bar(
#         profitability_targets,
#         x='지표',
#         y=['현재(2024)', '목표(2025)'],
#         barmode='group',
#         title='수익성 개선 목표',
#         height=400
#     )
#     st.plotly_chart(fig, use_container_width=True)
    
#     st.write("""
#     - **현황**: ROA -0.75%로 적자 상태, CK(1.64%)와 큰 격차.
#     - **제안**:
#       1. **이자수익 강화**: 한성의 안정적인 BIS(22.49%)를 참고하여 자본을 활용한 대출 확대.
#       2. **비이자수익 확대**: 지역 특화 펀드 및 수수료 기반 서비스 도입으로 비중을 5%에서 15%로 증가.
#       3. **부동산 의존도 조정**: CK처럼 부동산 대출 비중을 줄여 리스크를 분산.
#     """)

#     # 참고문헌
#     st.markdown('<p class="subsection-header">7.4 참고문헌</p>', unsafe_allow_html=True)
    
#     st.write("""
#     1. 대명상호저축은행 2024 / 3분기 경영공시 (2024.11)
#     2. CK저축은행 2024 / 3분기 경영공시 (2024.11)
#     3. 오투저축은행 2024 / 3분기 경영공시 (2024.11)
#     4. 청주저축은행 2024 / 3분기 경영공시 (2024.11)
#     5. 한성저축은행 2024 / 3분기 경영공시 (2024.11)
#     6. 금융감독원 「저축은행업 경영분석」 (2024.10)
#     """)
# 7. 동종업권 비교분석 및 전략 제언
# elif menu == "7. 동종업권 비교분석 및 전략 제언":
#     st.markdown('<p class="main-header">7. 동종업권 비교분석 및 전략 제언</p>', unsafe_allow_html=True)
    
#     # 충청·강원권 저축은행 업계 현황
#     st.markdown('<p class="subsection-header">7.1 충청·강원권 저축은행 업계 현황</p>', unsafe_allow_html=True)
    
#     # 비교 데이터
#     comparison_data = pd.DataFrame({
#         '은행명': ['대명', 'CK', '오투', '청주', '한성'],
#         '권역': ['Unknown', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '청주, 천안', '대전, 청주, 옥천'],
#         'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
#         'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
#         'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
#         'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
#         '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
#         '연체대출비율(%) 2023': [2.30, 2.26, 4.83, 5.34, 6.84],
#         '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
#         '부동산 대출금(%) 2023': [33.74, 93.28, 63.60, 13.04, 51.00],
#         'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60]
#     })

#     st.write("""
#     충청·강원권 저축은행의 2024년 데이터를 분석한 결과, 대명상호저축은행은 ROA -0.75%로 동종업권 내 낮은 수익성을 보이며,
#     연체대출비율 10%로 리스크 관리에 취약한 모습을 보입니다. BIS 자기자본비율은 16.81%로 안정적이지만, 경쟁사 대비 개선 여지가 있습니다.
#     """)

#     # 비교 시각화
#     col1, col2 = st.columns(2)
    
#     with col1:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['ROA(%) 2024', 'ROA(%) 2023'],
#             barmode='group',
#             title='총자산순수익률(ROA) 비교 (2023 vs 2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)
        
#     with col2:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['연체대출비율(%) 2024', '연체대출비율(%) 2023'],
#             barmode='group',
#             title='연체대출비율 비교 (2023 vs 2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     col3, col4 = st.columns(2)
    
#     with col3:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'],
#             barmode='group',
#             title='BIS 자기자본비율 비교 (2023 vs 2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)
        
#     with col4:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['부동산 대출금(%) 2024', '부동산 대출금(%) 2023'],
#             barmode='group',
#             title='부동산 대출금 비율 비교 (2023 vs 2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     st.caption("출처: 사용자 제공 데이터 (2024년 3월 7일 기준)")

#     # 경쟁사 분석
#     st.markdown('<p class="subsection-header">7.2 경쟁사 분석</p>', unsafe_allow_html=True)
    
#     st.write("""
#     동종업권 내 주요 은행들의 데이터를 바탕으로 대명상호저축은행의 상대적 위치와 개선 방향을 분석합니다.
#     """)

#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("""
#         ### CK저축은행 (강원도 - 강릉, 춘천)
#         - **현황**: ROA 1.64% (2024), 4.01% (2023)로 수익성 우수. 부동산 대출 비중 43.35% (2024), 93.28% (2023).
#         - **분석**: 부동산 대출 비중을 대폭 줄이며 안정성을 확보. 연체대출비율 3.61%로 낮음.
#         """)
        
#     with col2:
#         st.markdown("""
#         ### 오투저축은행 (충청남도 - 대전, 천안)
#         - **현황**: ROA -1.53% (2024), 연체대출비율 12.92%. 부동산 대출 비중 73.3%.
#         - **분석**: 높은 부동산 의존도와 연체율로 수익성과 자산 건전성 모두 취약.
#         """)

#     col3, col4 = st.columns(2)
    
#     with col3:
#         st.markdown("""
#         ### 청주저축은행 (청주, 천안)
#         - **현황**: ROA -0.22% (2024), 부동산 대출 비중 20.24%, 카드 건수 1,547 (2024).
#         - **분석**: 낮은 부동산 의존도와 안정적인 BIS 비율(17.49%)로 자산 건전성 유지.
#         """)
        
#     with col4:
#         st.markdown("""
#         ### 한성저축은행 (대전, 청주, 옥천)
#         - **현황**: ROA -0.24% (2024), BIS 비율 22.49%, 연체대출비율 8.80%.
#         - **분석**: 높은 자본비율과 안정적인 부동산 대출 비중(50.9%)으로 안정성 확보.
#         """)

#     # 대명저축은행 전략적 제언
#     st.markdown('<p class="subsection-header">7.3 대명저축은행 전략적 제언</p>', unsafe_allow_html=True)
    
#     st.write("""
#     대명상호저축은행은 ROA -0.75%, 연체대출비율 10%로 수익성과 리스크 관리에서 경쟁사 대비 열위에 있습니다.
#     아래 전략을 통해 개선을 도모할 수 있습니다.
#     """)

#     # A. 수익성 개선
#     st.markdown("#### A. 수익성 개선")
    
#     profitability_targets = pd.DataFrame({
#         '지표': ['ROA(%)'],
#         '현재(2024)': [-0.75],
#         '목표(2025)': [0.50]  # CK의 성공 사례 참고, 현실적 목표 설정
#     })
    
#     fig = px.bar(
#         profitability_targets,
#         x='지표',
#         y=['현재(2024)', '목표(2025)'],
#         barmode='group',
#         title='수익성 개선 목표',
#         height=400
#     )
#     st.plotly_chart(fig, use_container_width=True)
    
#     st.write("""
#     - **방안**:
#       1. CK처럼 부동산 대출 비중(45.85%)을 40% 이하로 줄여 리스크 분산.
#       2. 청주의 카드 사업(1,547건)을 참고해 소규모 카드 서비스 도입으로 수익 다변화.
#     """)

#     # B. 리스크 관리 강화
#     st.markdown("#### B. 리스크 관리 강화")
    
#     risk_roadmap = pd.DataFrame({
#         '단계': ['1Q 2025', '2Q 2025', '3Q 2025', '4Q 2025'],
#         '주요과제': [
#             '연체대출비율 10%에서 8%로 감축',
#             'PF대출 비중 31.9%에서 20%로 축소',
#             '부동산 대출 비중 조정',
#             '연체대출 관리 강화'
#         ]
#     })
    
#     st.table(risk_roadmap)
    
#     st.write("""
#     - **방안**:
#       1. 오투의 높은 연체율(12.92%)을 반면교사로 삼아 연체대출비율을 한성 수준(8.80%)으로 낮춤.
#       2. PF대출 비중(31.9%)을 CK(0%)처럼 줄여 리스크 완화.
#     """)

#     # C. 자산 포트폴리오 최적화
#     st.markdown("#### C. 자산 포트폴리오 최적화")
    
#     portfolio_targets = pd.DataFrame({
#         '지표': ['부동산 대출금(%)', 'PF대출(%)'],
#         '현재(2024)': [45.85, 31.90],
#         '목표(2025)': [40.00, 20.00]
#     })
    
#     fig = px.bar(
#         portfolio_targets,
#         x='지표',
#         y=['현재(2024)', '목표(2025)'],
#         barmode='group',
#         title='자산 포트폴리오 조정 목표',
#         height=400
#     )
#     st.plotly_chart(fig, use_container_width=True)
    
#     st.write("""
#     - **방안**:
#       1. 청주처럼 부동산 대출 비중(20.24%)을 낮추는 방향으로 조정.
#       2. 한성의 안정적인 BIS 비율(22.49%)을 참고해 자본을 활용한 안전 자산 확대.
#     """)
# 7. 동종업권 비교분석 및 전략 제언
# elif menu == "7. 동종업권 비교분석 및 전략 제언":
#     st.markdown('<p class="main-header">7. 동종업권 비교분석 및 전략 제언</p>', unsafe_allow_html=True)
    
#     # 충청·강원권 저축은행 업계 현황
#     st.markdown('<p class="subsection-header">7.1 충청·강원권 저축은행 업계 현황</p>', unsafe_allow_html=True)
    
#     # 비교 데이터 (5번 항목 포함)
#     comparison_data = pd.DataFrame({
#         '은행명': ['대명', 'CK', '오투', '청주', '한성'],
#         '권역': ['Unknown', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '청주, 천안', '대전, 청주, 옥천'],
#         'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
#         'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
#         'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
#         'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
#         '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
#         '연체대출비율(%) 2023': [2.30, 2.26, 4.83, 5.34, 6.84],
#         '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
#         '부동산 대출금(%) 2023': [33.74, 93.28, 63.60, 13.04, 51.00],
#         'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
#         '자산건전성 합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70]
#     })

#     st.write("""
#     충청·강원권 저축은행의 2024년 데이터를 분석한 결과, 대명상호저축은행은 ROA -0.75%, 연체대출비율 10%, 
#     PF대출 비중 31.9%로 수익성과 자산 건전성에서 경쟁사 대비 열위에 있습니다. BIS 자기자본비율 16.81%는 안정적이지만 개선 여지가 있습니다.
#     """)

#     # 비교 시각화 (5번 항목 추가)
#     col1, col2 = st.columns(2)
    
#     with col1:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['ROA(%) 2024', 'ROA(%) 2023'],
#             barmode='group',
#             title='총자산순수익률(ROA) 비교 (2023 vs 2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)
        
#     with col2:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['연체대출비율(%) 2024', '연체대출비율(%) 2023'],
#             barmode='group',
#             title='연체대출비율 비교 (2023 vs 2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     col3, col4 = st.columns(2)
    
#     with col3:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['부동산 대출금(%) 2024', '부동산 대출금(%) 2023'],
#             barmode='group',
#             title='부동산 대출금 비율 비교 (2023 vs 2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)
        
#     with col4:
#         fig = px.bar(
#             comparison_data,
#             x='은행명',
#             y=['PF대출(%) 2024', '자산건전성 합계(%) 2024'],
#             barmode='group',
#             title='부동산 PF대출 및 자산건전성 비교 (2024)',
#             height=400
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     st.caption("출처: 사용자 제공 데이터 (2024년 3월 7일 기준)")

#     # 경쟁사 분석
#     st.markdown('<p class="subsection-header">7.2 경쟁사 분석</p>', unsafe_allow_html=True)
    
#     st.write("""
#     동종업권 내 주요 은행들의 데이터를 바탕으로 대명상호저축은행의 상대적 위치를 분석합니다.
#     """)

#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("""
#         ### CK저축은행 (강원도 - 강릉, 춘천)
#         - **현황**: ROA 1.64% (2024), 부동산 대출 43.35%, PF대출 0%, 자산건전성 합계 3.12%.
#         - **분석**: PF대출이 없고, 부동산 대출 비중을 93.28%에서 43.35%로 줄이며 자산 건전성 강화.
#         """)
        
#     with col2:
#         st.markdown("""
#         ### 오투저축은행 (충청남도 - 대전, 천안)
#         - **현황**: ROA -1.53% (2024), 연체대출비율 12.92%, PF대출 10.46%, 자산건전성 합계 24.59%.
#         - **분석**: 높은 부동산 대출(73.3%)과 PF대출로 자산 건전성과 수익성 모두 취약.
#         """)

#     col3, col4 = st.columns(2)
    
#     with col3:
#         st.markdown("""
#         ### 청주저축은행 (청주, 천안)
#         - **현황**: ROA -0.22% (2024), 부동산 대출 20.24%, PF대출 7.38%, 자산건전성 합계 12.32%.
#         - **분석**: 낮은 부동산 및 PF대출 비중으로 자산 건전성 유지.
#         """)
        
#     with col4:
#         st.markdown("""
#         ### 한성저축은행 (대전, 청주, 옥천)
#         - **현황**: ROA -0.24% (2024), BIS 22.49%, PF대출 10.6%, 자산건전성 합계 16.7%.
#         - **분석**: 안정적인 자본비율과 적정 PF대출 비중으로 건전성 확보.
#         """)

#     # 대명저축은행 전략적 제언
#     st.markdown('<p class="subsection-header">7.3 대명저축은행 전략적 제언</p>', unsafe_allow_html=True)
    
#     st.write("""
#     대명상호저축은행은 ROA -0.75%, 연체대출비율 10%, PF대출 31.9%로 수익성과 자산 건전성 개선이 시급합니다.
#     아래 전략을 제안합니다.
#     """)

#     # A. 수익성 개선
#     st.markdown("#### A. 수익성 개선")
    
#     profitability_targets = pd.DataFrame({
#         '지표': ['ROA(%)'],
#         '현재(2024)': [-0.75],
#         '목표(2025)': [0.50]
#     })
    
#     fig = px.bar(
#         profitability_targets,
#         x='지표',
#         y=['현재(2024)', '목표(2025)'],
#         barmode='group',
#         title='수익성 개선 목표',
#         height=400
#     )
#     st.plotly_chart(fig, use_container_width=True)
    
#     st.write("""
#     - **방안**:
#       1. CK처럼 부동산 대출 비중(45.85%)을 줄여 리스크 분산.
#       2. 청주의 낮은 PF대출(7.38%)을 참고해 PF대출 비중(31.9%) 축소.
#     """)

#     # B. 리스크 관리 및 자산 건전성 강화
#     st.markdown("#### B. 리스크 관리 및 자산 건전성 강화")
    
#     risk_roadmap = pd.DataFrame({
#         '단계': ['1Q 2025', '2Q 2025', '3Q 2025', '4Q 2025'],
#         '주요과제': [
#             '연체대출비율 10%에서 8%로 감축',
#             'PF대출 비중 31.9%에서 20%로 축소',
#             '자산건전성 합계 23.11%에서 15%로 개선',
#             '부동산 대출 비중 조정'
#         ]
#     })
    
#     st.table(risk_roadmap)
    
#     st.write("""
#     - **방안**:
#       1. 오투의 높은 연체율(12.92%)과 자산건전성 합계(24.59%)를 반면교사로 삼아 연체율과 PF대출 관리.
#       2. CK의 PF대출 0% 전략을 참고해 부동산 관련 리스크 축소.
#     """)

#     # C. 자산 포트폴리오 최적화
#     st.markdown("#### C. 자산 포트폴리오 최적화")
    
#     portfolio_targets = pd.DataFrame({
#         '지표': ['부동산 대출금(%)', 'PF대출(%)', '자산건전성 합계(%)'],
#         '현재(2024)': [45.85, 31.90, 23.11],
#         '목표(2025)': [40.00, 20.00, 15.00]
#     })
    
#     fig = px.bar(
#         portfolio_targets,
#         x='지표',
#         y=['현재(2024)', '목표(2025)'],
#         barmode='group',
#         title='자산 포트폴리오 조정 목표',
#         height=400
#     )
#     st.plotly_chart(fig, use_container_width=True)
    
#     st.write("""
#     - **방안**:
#       1. 청주(부동산 20.24%, PF대출 7.38%)처럼 부동산 및 PF대출 비중을 줄여 안정성 확보.
#       2. 한성의 자산건전성 합계(16.7%)를 목표로 PF대출과 연체 관리 강화.
#     """)
# 7. 동종업권 비교분석 및 전략 제언
elif menu == "7. 동종업권 비교분석 및 전략 제언":
    st.markdown('<p class="main-header">7. 동종업권 비교분석 및 전략 제언</p>', unsafe_allow_html=True)
    
    # 충청·강원권 저축은행 업계 현황
    st.markdown('<p class="subsection-header">7.1 충청·강원권 저축은행 업계 현황</p>', unsafe_allow_html=True)
    
    # 비교 데이터 (5번 항목 수정)
    comparison_data = pd.DataFrame({
        '은행명': ['대명', 'CK', '오투', '청주', '한성'],
        '권역': ['Unknown', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '청주, 천안', '대전, 청주, 옥천'],
        'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
        'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
        'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
        'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
        '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
        '연체대출비율(%) 2023': [2.30, 2.26, 4.83, 5.34, 6.84],
        '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
        '부동산 대출금(%) 2023': [33.74, 93.28, 63.60, 13.04, 51.00],
        'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
        '연체비율 총합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70]
    })

    st.write("""
    충청·강원권 저축은행의 2024년 데이터를 분석한 결과, 대명상호저축은행은 ROA -0.75%, 연체대출비율 10%, 
    PF대출 비중 31.9%, 연체비율 총합계 23.11%로 수익성과 자산 건전성에서 경쟁사 대비 열위에 있습니다.
    BIS 자기자본비율 16.81%는 안정적이지만 개선 여지가 있습니다.
    """)

    # 비교 시각화
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(
            comparison_data,
            x='은행명',
            y=['ROA(%) 2024', 'ROA(%) 2023'],
            barmode='group',
            title='총자산순수익률(ROA) 비교 (2023 vs 2024)',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        fig = px.bar(
            comparison_data,
            x='은행명',
            y=['연체대출비율(%) 2024', '연체대출비율(%) 2023'],
            barmode='group',
            title='연체대출비율 비교 (2023 vs 2024)',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)
    
    with col3:
        fig = px.bar(
            comparison_data,
            x='은행명',
            y=['부동산 대출금(%) 2024', '부동산 대출금(%) 2023'],
            barmode='group',
            title='부동산 대출금 비율 비교 (2023 vs 2024)',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col4:
        fig = px.bar(
            comparison_data,
            x='은행명',
            y=['PF대출(%) 2024', '연체비율 총합계(%) 2024'],
            barmode='group',
            title='2024년 PF대출 및 연체비율 총합계 비교',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    st.caption("출처: 사용자 제공 데이터 (2024년 3월 7일 기준)")

    # 경쟁사 분석
    st.markdown('<p class="subsection-header">7.2 경쟁사 분석</p>', unsafe_allow_html=True)
    
    st.write("""
    동종업권 내 주요 은행들의 데이터를 바탕으로 대명상호저축은행의 상대적 위치를 분석합니다.
    """)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### CK저축은행 (강원도 - 강릉, 춘천)
        - **현황**: ROA 1.64% (2024), 부동산 대출 43.35%, PF대출 0%, 연체비율 총합계 3.12%.
        - **분석**: PF대출이 없고, 부동산 대출 비중을 93.28%에서 43.35%로 줄여 자산 건전성 강화.
        """)
        
    with col2:
        st.markdown("""
        ### 오투저축은행 (충청남도 - 대전, 천안)
        - **현황**: ROA -1.53% (2024), 연체대출비율 12.92%, PF대출 10.46%, 연체비율 총합계 24.59%.
        - **분석**: 높은 부동산 대출(73.3%)과 연체비율 총합계로 자산 건전성과 수익성 취약.
        """)

    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        ### 청주저축은행 (청주, 천안)
        - **현황**: ROA -0.22% (2024), 부동산 대출 20.24%, PF대출 7.38%, 연체비율 총합계 12.32%.
        - **분석**: 낮은 부동산 및 PF대출 비중으로 자산 건전성 유지.
        """)
        
    with col4:
        st.markdown("""
        ### 한성저축은행 (대전, 청주, 옥천)
        - **현황**: ROA -0.24% (2024), BIS 22.49%, PF대출 10.6%, 연체비율 총합계 16.7%.
        - **분석**: 안정적인 자본비율과 적정 PF대출 비중으로 건전성 확보.
        """)

    # 대명저축은행 전략적 제언
    st.markdown('<p class="subsection-header">7.3 대명저축은행 전략적 제언</p>', unsafe_allow_html=True)
    
    st.write("""
    대명상호저축은행은 ROA -0.75%, 연체대출비율 10%, PF대출 31.9%, 연체비율 총합계 23.11%로 
    수익성과 자산 건전성 개선이 시급합니다. 아래 전략을 제안합니다.
    """)

    # A. 수익성 개선
    st.markdown("#### A. 수익성 개선")
    
    profitability_targets = pd.DataFrame({
        '지표': ['ROA(%)'],
        '현재(2024)': [-0.75],
        '목표(2025)': [0.50]
    })
    
    fig = px.bar(
        profitability_targets,
        x='지표',
        y=['현재(2024)', '목표(2025)'],
        barmode='group',
        title='수익성 개선 목표',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    - **방안**:
      1. CK처럼 부동산 대출 비중(45.85%)을 줄여 리스크 분산.
      2. 청주의 낮은 PF대출(7.38%)을 참고해 PF대출 비중(31.9%) 축소.
    """)

    # B. 리스크 관리 및 자산 건전성 강화
    st.markdown("#### B. 리스크 관리 및 자산 건전성 강화")
    
    risk_roadmap = pd.DataFrame({
        '단계': ['1Q 2025', '2Q 2025', '3Q 2025', '4Q 2025'],
        '주요과제': [
            '연체대출비율 10%에서 8%로 감축',
            'PF대출 비중 31.9%에서 20%로 축소',
            '연체비율 총합계 23.11%에서 15%로 개선',
            '부동산 대출 비중 조정'
        ]
    })
    
    st.table(risk_roadmap)
    
    st.write("""
    - **방안**:
      1. 오투의 높은 연체율(12.92%)과 연체비율 총합계(24.59%)를 반면교사로 삼아 관리 강화.
      2. CK의 PF대출 0% 전략을 참고해 PF대출 관련 리스크 축소.
    """)

    # C. 자산 포트폴리오 최적화
    st.markdown("#### C. 자산 포트폴리오 최적화")
    
    portfolio_targets = pd.DataFrame({
        '지표': ['부동산 대출금(%)', 'PF대출(%)', '연체비율 총합계(%)'],
        '현재(2024)': [45.85, 31.90, 23.11],
        '목표(2025)': [40.00, 20.00, 15.00]
    })
    
    fig = px.bar(
        portfolio_targets,
        x='지표',
        y=['현재(2024)', '목표(2025)'],
        barmode='group',
        title='자산 포트폴리오 조정 목표',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("""
    - **방안**:
      1. 청주(부동산 20.24%, PF대출 7.38%)처럼 부동산 및 PF대출 비중을 줄여 안정성 확보.
      2. 한성의 연체비율 총합계(16.7%)를 목표로 자산 건전성 개선.
    """)