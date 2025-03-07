import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
    .highlight {background-color: #FEF3C7; padding: 0.2rem; border-radius: 0.2rem;}
    .insight-box {background-color: #E0F2FE; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;}
    .table-wrapper {margin: 1.5rem 0;}
    .star-box {background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #3B82F6;}
    .star-header {font-weight: bold; color: #1E3A8A; margin-bottom: 0.5rem;}
</style>
""", unsafe_allow_html=True)

# 데이터 정의 (수정된 값 반영)
financial_data = pd.DataFrame({
    'Year': ['2023년 3분기', '2024년 3분기'],
    'Total_Assets': [2575, 2365],
    'Loans': [2078, 2245],
    'Deposits': [2157, 2008],  # 텍스트와 일치하도록 수정
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

# 사이드바 메뉴
st.sidebar.title("대명상호저축은행")
st.sidebar.subheader("수익성 강화 전략 보고서")
menu = st.sidebar.radio("목차", [
    "1. 은행 현황 및 PF 대출 연계 과제",
    "2. 재무 현황 분석",
    "3. 수익성 강화 전략",
    "7. 동종업권 비교분석 및 전략 제언"
])

st.sidebar.divider()
st.sidebar.info("""
**2024년 9월말 주요 지표**
- 총자산: 2,365억 원
- 대출금: 2,245억 원
- 예수금: 2,008억 원
- BIS 자기자본비율: 16.81%
""")
st.sidebar.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# 1. 은행 현황 및 PF 대출 연계 과제
if menu == "1. 은행 현황 및 PF 대출 연계 과제":
    st.markdown('<p class="main-header">1. 대명상호저축은행 현황 및 PF 대출 연계 과제</p>', unsafe_allow_html=True)
    
    # STAR 방식 적용 - 상황(Situation)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">상황(Situation)</p>', unsafe_allow_html=True)
    st.write("""
    대명상호저축은행은 충북 제천을 기반으로 하는 지역 저축은행으로, 현재 본점과 충주지점 등 2개 영업점을 운영하며 
    총자산 2,365억 원(2024년 9월말 기준) 규모를 보유하고 있습니다. 금융환경 변화와 부동산 시장 침체 속에서 
    2024년 3분기 기준 ROA -0.75%, 연체대출비율 10%, PF대출 비중 31.9%로 수익성과 자산 건전성 측면에서 
    일정 부분 도전적인 상황에 직면해 있는 것으로 판단됩니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 은행 현황 및 PF 대출 문제 소개
    st.markdown('<p class="subsection-header">1.1 대명상호저축은행 현황</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.write("""
        **대명상호저축은행**은 충북 제천을 기반으로 한 지역 저축은행으로, 현재 본점과 충주지점 등 2개 영업점을 운영하며 
        총자산 2,365억 원(2024년 9월말 기준) 규모를 유지하고 있습니다. 다만, 2024년 3분기 기준 ROA -0.75%, 
        연체대출비율 10%, PF대출 비중 31.9%로 수익성과 자산 건전성 측면에서 개선의 여지가 있는 것으로 보입니다. 
        특히, PF(프로젝트 파이낸싱) 대출의 상대적으로 높은 비중과 연체율 상승은 저축은행 업계 전반의 리스크와 
        연계되어 있어 전략적인 관리가 필요할 것으로 사료됩니다.
        
        저축은행 업계는 최근 금리 인하와 부동산 시장 조정으로 PF 대출 관련 리스크가 증가하는 추세이며, 
        대명상호저축은행 역시 이러한 외부 환경 변화에 민감할 수 있는 구조를 일부 보이고 있습니다. 
        BIS 자기자본비율은 16.81%로 상당히 양호한 수준이나, 수익성 개선과 자산 건전성 강화를 위한 
        선제적 전략 수립이 시의적절할 것으로 판단됩니다.
        """)
    
    with col2:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 주요 지표 요약
        - ROA: -0.75% (전년 대비 하락)
        - 연체대출비율: 10% (전년 대비 상승)
        - PF대출 비중: 31.9% (업계 평균 대비 다소 높음)
        - 예수금 변화: 2,157억 원 → 2,008억 원
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")
    
    # STAR 방식 적용 - 과제(Task)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">과제(Task)</p>', unsafe_allow_html=True)
    st.write("""
    본 분석의 핵심 과제는 대명상호저축은행의 수익성 개선과 자산 건전성 강화를 위한 전략적 방안을 도출하는 것입니다. 
    특히 PF 대출 비중 최적화, 연체율 관리, 예대금리차 개선, 비이자수익 확대 등을 통해 ROA를 개선하고 
    지속 가능한 성장 기반을 마련하는 것이 중요한 과제로 식별되었습니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # PF 대출과 저축은행 업계 현황
    st.markdown('<p class="subsection-header">1.2 저축은행 PF 대출 현황 및 대명과의 연계</p>', unsafe_allow_html=True)
    
    st.write("""
    2024년 저축은행 업계는 PF 대출과 관련하여 일정 부분 도전적인 상황에 직면해 있는 것으로 보입니다. 
    부동산 경기 조정과 금리 변동으로 PF 대출 연체율이 상승하는 추세이며, 일부 저축은행은 자본 건전성 관리에 
    각별한 주의를 기울이고 있습니다. 대명상호저축은행의 PF 대출 비중은 31.9%로, 동종업권 평균(약 15-20%)을 
    다소 상회하며, 연체비율 총합계가 23.11%에 이르러 선제적인 리스크 관리가 필요한 것으로 분석됩니다.
    
    이는 충북 지역의 중소기업 및 부동산 관련 대출 의존도가 상대적으로 높은 포트폴리오 구조와 연관이 있을 것으로 
    추정되며, 지역 경제의 변화와 연계되어 있을 가능성이 있습니다. 따라서 PF 대출 비중의 점진적 조정과 
    자산 건전성 강화가 주요 과제로 대두되고 있습니다.
    """)
    
    # 주요 과제
    st.markdown('<p class="subsection-header">1.3 주요 과제</p>', unsafe_allow_html=True)
    
    # STAR 방식 적용 - 행동(Action)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">행동(Action)</p>', unsafe_allow_html=True)
    st.write("""
    본 보고서에서는 대명상호저축은행의 현황을 심층 분석하고, 동종업권 비교를 통해 벤치마킹 요소를 도출했습니다. 
    재무 지표, 대출 포트폴리오, 예수금 구조 등을 다각도로 검토하여 수익성 개선을 위한 전략적 방안을 수립했으며, 
    특히 PF 대출 리스크 관리와 비이자수익 확대 방안에 중점을 두었습니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("""
    대명상호저축은행이 직면한 주요 과제는 다음과 같이 정리될 수 있습니다:
    
    1. **PF 대출 리스크 관리**
       - PF 대출 비중 31.9%로 부동산 시장 변동에 일정 부분 노출되어 있는 것으로 보입니다
       - 연체비율 총합계 23.11%로 자산 건전성 관리가 필요한 상황입니다
    
    2. **수익성 개선 기회**
       - ROA -0.75%, NIM 1.69%로 업계 평균과 비교하여 개선의 여지가 있습니다
       - 예수금 감소(6.9%)로 인한 조달 비용 최적화 필요성이 제기됩니다
    
    3. **자산 포트폴리오 다각화 가능성**
       - 기업자금대출 비중 56.55%, 부동산 의존도가 상대적으로 높은 편입니다
       - 담보 및 신용대출 균형 조정을 통한 리스크 분산이 검토될 수 있습니다
    
    4. **디지털 및 지역 경쟁력 강화 기회**
       - 디지털 뱅킹 서비스 고도화를 통한 고객 경험 개선 가능성이 있습니다
       - 충북 지역 특화 전략 수립을 통한 차별화 기회가 존재합니다
    """)

# 2. 재무 현황 분석
elif menu == "2. 재무 현황 분석":
    st.markdown('<p class="main-header">2. 재무 현황 분석</p>', unsafe_allow_html=True)
    
    # STAR 방식 적용 - 상황(Situation)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">상황(Situation)</p>', unsafe_allow_html=True)
    st.write("""
    대명상호저축은행의 2024년 3분기 재무제표 및 경영지표를 분석한 결과, 자본건전성은 양호한 수준을 유지하고 있으나 
    수익성 측면에서는 개선의 여지가 있는 것으로 확인되었습니다. 총자산 2,365억 원, 예수금 2,008억 원 규모로 
    지역 저축은행으로서 안정적인 기반을 갖추고 있으나, 최근 금융시장 변화와 부동산 경기 조정으로 인한 영향이 
    일부 지표에 반영되고 있는 것으로 보입니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
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
                '2023년 3분기': [2575, 2245, 330],
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
                '지표': ['ROA'],
                '2023년 3분기': [-0.13],
                '2024년 3분기': [-0.75]
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
                '2023년 3분기': [3.05, 4.26, 1.21],
                '2024년 3분기': [2.60, 4.29, 1.69]
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
    
    # STAR 방식 적용 - 과제(Task)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">과제(Task)</p>', unsafe_allow_html=True)
    st.write("""
    재무 현황 분석을 통해 도출된 주요 과제는 다음과 같습니다:
    
    1. 수익성 지표 개선 방안 도출 (ROA -0.75% → 양(+)의 수익률로 전환)
    2. 이자마진 확대 전략 수립 (현 1.69%에서 업계 평균 수준으로 개선)
    3. 대출 포트폴리오 최적화를 통한 리스크 관리 (부동산 및 PF 대출 비중 조정)
    4. 예수금 구조 개선을 통한 조달 비용 절감 (저원가성 예금 비중 확대)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 대출 포트폴리오 분석
    st.markdown('<p class="subsection-header"> 대출 포트폴리오 분석</p>', unsafe_allow_html=True)
    
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
    
    # STAR 방식 적용 - 행동(Action)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">행동(Action)</p>', unsafe_allow_html=True)
    st.write("""
    대출 포트폴리오 분석을 위해 용도별, 담보별 대출 구성을 심층적으로 검토했습니다. 또한 업계 평균과의 비교 분석을 
    통해 대명상호저축은행의 포트폴리오 특성과 리스크 요인을 식별했습니다. 이를 바탕으로 포트폴리오 최적화 방안과 
    리스크 관리 전략을 수립했습니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("""
    대명상호저축은행의 대출 포트폴리오를 분석한 결과, 용도별로는 기업자금대출이 1,015억 원(56.55%)으로
    가장 높은 비중을 차지하고 있으며, 가계자금대출은 689억 원(38.38%), 공공 및 기타자금 대출은
    91억 원(5.07%)입니다.
    
    담보별로는 부동산담보대출이 959억 원(53.43%)으로 상당한 비중을 차지하고 있으며,
    신용대출은 823억 원(45.85%)입니다. 이는 업계 평균과 비교할 때 신용대출 비중이 다소 높은 편으로,
    리스크 관리 측면에서 세심한 접근이 필요할 것으로 보입니다.
    
    중소기업 대출 비중은 50.37%로, 지역 기반 저축은행으로서 지역 내 중소기업 지원에 주력하고 있음을
    확인할 수 있습니다. 다만, 부동산 업종에 대한 신용공여 비중이 상대적으로 높아 부동산 경기 변동에
    따른 리스크 관리가 중요한 요소로 판단됩니다.
    """)

    # 예수금 현황
    st.markdown('<p class="subsection-header"> 예수금 현황 분석</p>', unsafe_allow_html=True)
    
    # 예수금 구성 데이터
    deposit_data = pd.DataFrame({
        '구분': ['거치식예금', '적립식예금', '요구불예금'],
        '금액(억원)': [1972, 26, 10],
        '비율(%)': [98.21, 1.29, 0.5]
    })

    # 예수금 추이 데이터
    deposit_trend = pd.DataFrame({
        '구분': ['2023년 3분기', '2024년 3분기'],
        '예수금(억원)': [2157, 2008]
    })

    # 퍼센트 감소 계산
    percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
    percent_change_text = f"{percent_change:.1f}%"

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
        # Bar Chart with Enhanced Visualization
        fig = px.bar(
            deposit_trend,
            x='구분',
            y='예수금(억원)',
            title='예수금 추이 (단위: 억원)',
            height=400,
            text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"),  # Add comma to values
        )
        
        # Customize bars and add percentage change annotation
        fig.update_traces(
            marker_color=['rgb(55, 83, 109)', 'rgb(255, 99, 71)'],  # Blue for 2023, Red for 2024 to highlight decrease
            textposition='auto'  # Place text inside bars
        )
        
        # Add percentage change as an annotation
        fig.add_annotation(
            x='2024년 3분기',
            y=deposit_trend['예수금(억원)'][1],
            text=f"변화율: {percent_change_text}",
            showarrow=True,
            arrowhead=1,
            yshift=20,  # Move text above the bar
            font=dict(color="red")
        )
        
        # Adjust Y-axis to zoom in on the change
        fig.update_layout(
            yaxis_range=[1900, 2200],  # Narrow range to emphasize difference
            yaxis_title="예수금 (억원)",
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

    # STAR 방식 적용 - 결과(Result)

    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">결과(Result)</p>', unsafe_allow_html=True)
    st.write("""
    예수금 분석 결과, 거치식예금 의존도가 98.21%로 매우 높은 것으로 확인되었습니다. 이는 조달 비용 측면에서 
    개선의 여지가 있음을 시사합니다. 또한 예수금이 전년 대비 6.9% 감소한 것은 시장 금리 변동과 경쟁 심화에 
    따른 영향으로 추정됩니다. 이러한 분석 결과를 바탕으로 저원가성 예금 비중 확대 및 예금 상품 다각화 전략을 
    수립하여 조달 비용 최적화를 도모할 수 있을 것으로 판단됩니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("""
    예수금 구성을 분석한 결과, 2024년 3분기 기준 총 예수금 2,008억 원 중 거치식예금이 1,972억 원으로
    98.21%의 상당히 높은 비중을 차지하고 있습니다. 적립식예금은 26억 원(1.29%), 요구불예금은 10억 원(0.5%)으로
    상대적으로 낮은 수준입니다.
    
    이러한 구조는 고객 기반이 주로 고금리 정기예금 중심으로 형성되어 있음을 시사하며, 저원가성 예금 비중이
    다소 낮아 조달 비용 측면에서 최적화의 여지가 있는 것으로 보입니다.
    
    예수금은 전년 동기 대비 6.9% 감소한 2,008억 원을 기록하였으며, 예대율은 83.2%로
    업계 평균과 비교했을 때 조정의 여지가 있는 것으로 판단됩니다. 이는 대출 자산의 효율적 운용 측면에서
    검토가 필요함을 시사하며, 수익성 개선을 위해 적정 예대율 관리와 함께 대출 자산의 질적 성장이 
    중요할 것으로 사료됩니다.
    """)
    
    # 건전성 및 리스크 현황
    st.markdown('<p class="subsection-header"> 자산건전성 및 리스크 현황</p>', unsafe_allow_html=True)
    
    # 자산건전성 데이터
    asset_quality_data = pd.DataFrame({
        '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
        '2023년 3분기': [91, 3, 60],
        '2024년 3분기': [271, 29, 125],
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
            '2023년 3분기': [2.30, 3.62],
            '2024년 3분기': [10.00, 10.46]
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
    자산건전성 측면에서는 고정이하분류여신이 271억 원으로 전년 동기(91억 원) 대비 증가하였으며,
    부실여신도 29억 원으로 전년 동기(3억 원) 대비 상승한 것으로 나타났습니다. 이는 전반적인 금융환경 변화와
    부동산 시장 조정의 영향이 일부 반영된 것으로 추정됩니다.
    
    연체대출비율은 10.00%로 전년 동기(2.30%) 대비 상승하였으며, 순고정이하여신비율 역시
    10.46%로 전년 동기(3.62%) 대비 증가한 것으로 확인되었습니다. 이는 자산 건전성 관리에 있어
    보다 세심한 접근이 필요함을 시사합니다.
    
    다만, 대손충당금은 125억 원으로 전년 동기(60억 원) 대비 증가하여, 
    잠재적 손실 흡수를 위한 선제적 대응이 이루어지고 있는 것으로 판단됩니다. 충당금적립률은 
    적정 수준을 유지하고 있어 리스크 관리 측면에서 긍정적인 요소로 볼 수 있습니다.
    """)

# 3. 수익성 강화 전략
elif menu == "3. 수익성 강화 전략":
    st.markdown('<p class="main-header">3. 수익성 강화 전략</p>', unsafe_allow_html=True)
    
    # STAR 방식 적용 - 상황(Situation)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">상황(Situation)</p>', unsafe_allow_html=True)
    st.write("""
    대명상호저축은행은 2024년 3분기 기준 ROA -0.75%, NIM 1.69%로 수익성 측면에서 개선의 여지가 있는 상황입니다.
    또한 예수금 감소(6.9%)와 연체대출비율 상승(10.00%)이 수익성에 부정적 영향을 미치고 있는 것으로 판단됩니다.
    이러한 상황에서 수익성 강화를 위한 체계적이고 실행 가능한 전략 수립이 필요한 시점입니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 수익성 강화 전략 개요
    st.markdown('<p class="subsection-header">3.1 전략 개요</p>', unsafe_allow_html=True)
    
    # STAR 방식 적용 - 과제(Task)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">과제(Task)</p>', unsafe_allow_html=True)
    st.write("""
    본 섹션의 주요 과제는 대명상호저축은행의 수익성을 개선하기 위한 실행 가능한 전략을 수립하는 것입니다.
    구체적으로는 ROA를 현재 -0.75%에서 양(+)의 수익률로 전환하고, NIM을 1.69%에서 업계 평균 수준으로 
    개선하며, 비이자수익 비중을 확대하는 방안을 도출하는 것이 핵심 과제입니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.write("""
        대명상호저축은행의 수익성을 개선하기 위해 다음과 같은 4가지 핵심 전략을 제안해 드리고자 합니다.
        이 전략들은 은행의 현재 재무상태와 경쟁 환경, 그리고 지역적 특성을 종합적으로 고려하여 설계되었습니다.
        
        1. **대출 포트폴리오 최적화**
           - 기업대출과 개인대출의 비중 조정을 통한 리스크 분산
           - 지역 중소기업 특화 대출 상품 개발로 차별화
           - 부동산 담보대출 다각화를 통한 안정성 강화
        
        2. **예대금리차 개선**
           - 예금 상품 재설계를 통한 조달비용 최적화
           - 특정 고객층 타겟팅을 통한 저원가성 예금 확대
           - 대출 상품별 금리 체계 최적화로 수익성 제고
        
        3. **비이자수익 확대**
           - 수수료 수입 확대를 위한 혁신적 서비스 도입
           - 자산관리 서비스 강화로 고객 가치 제고
           - 지역 기반 특화 부가서비스 개발을 통한 차별화
        
        4. **디지털 전환을 통한 효율성 제고**
           - 모바일뱅킹 서비스 고도화로 고객 경험 향상
           - 업무 프로세스의 자동화를 통한 운영 효율성 증대
           - 데이터 기반 의사결정 체계 구축으로 경영 효율성 제고
        """)
        
    with col2:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 기대 효과
        
        - ROA: -0.75% → 0.3% 개선
        - NIM: 1.69% → 3.0% 확대
        - 비이자수익 비중: 5% → 15% 확대
        - 고정이하여신비율: 10.46% → 7.0% 개선
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # STAR 방식 적용 - 행동(Action)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">행동(Action)</p>', unsafe_allow_html=True)
    st.write("""
    수익성 강화를 위해 비이자수익 확대 방안과 디지털 전환 전략을 중점적으로 분석했습니다. 
    현재 비이자수익 현황을 파악하고, 업계 선진 사례를 벤치마킹하여 대명상호저축은행에 적합한 
    비이자수익 확대 방안을 도출했습니다. 또한 디지털 전환을 위한 단계별 실행 계획과 투자 방안을 수립했습니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
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
       - 충북 소상공인 대상 '사업자 종합금융 패키지' 출시를 검토해 볼 수 있을 것으로 보입니다
         (결제계좌, POS 연동, 매출관리, 세무지원 등 통합 서비스)
       - 지역 자영업자 대상 '상권분석 보고서' 유료 서비스 도입을 고려해 볼 수 있습니다
       - 지역 내 부동산 중개업체와 연계한 '원스톱 부동산 금융 서비스' 제공 방안을 모색해 볼 수 있습니다
    
    2. **자산관리 서비스 도입**
       - 자산 5억 이상 고객 대상 '프리미엄 자산관리 서비스' 도입을 검토할 수 있습니다
       - 은퇴설계 상담 및 절세 컨설팅 서비스 유료화 방안을 고려해 볼 수 있습니다
       - 지역 내 전문가 네트워크 구축 (세무사, 변호사, 부동산 전문가 등)을 통한 차별화된 서비스 제공이 가능할 것으로 보입니다
       - 자산관리 전문인력 양성을 위한 교육 프로그램 도입을 검토할 수 있습니다
    
    3. **펀드/보험 판매 확대**
       - 증권사, 보험사와의 전략적 제휴를 통한 판매 채널 다변화를 모색해 볼 수 있습니다
       - 고객 맞춤형 포트폴리오 추천 서비스 도입을 통한 고객 경험 향상이 가능할 것으로 판단됩니다
       - 저축은행 특화 ELS, DLS 상품 개발 및 판매 방안을 검토할 수 있습니다
       - 지역 특화 투자상품 개발 (충북 개발 프로젝트 연계 상품 등)을 통한 차별화가 가능할 것으로 보입니다
    
    4. **디지털 기반 부가서비스**
       - 모바일뱅킹 내 유료 부가서비스 도입을 고려해 볼 수 있습니다
         (계좌 통합관리, 자산현황 분석, 예산관리 등)
       - 비대면 상담 서비스 유료화를 통한 새로운 수익원 창출이 가능할 것으로 판단됩니다
       - 금융교육 프로그램 운영 (청소년, 은퇴자 등 대상)을 통한 사회적 가치 창출과 브랜드 이미지 제고를 도모할 수 있습니다
    """)
    st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석 기반")
    
    # 디지털 전환
    st.markdown('<p class="subsection-header">3.5 디지털 전환을 통한 효율성 제고</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([7, 3])
    
    with col1:
        st.write("""
        대명상호저축은행의 디지털 역량 강화를 통해 고객 경험을 개선하고 운영 효율성을 높이는 전략을 제안해 드리고자 합니다.
        특히 지역 기반 저축은행의 특성을 살려, 디지털과 대면 서비스의 조화를 통해 차별화된 서비스를
        제공하는 데 중점을 두는 것이 효과적일 것으로 판단됩니다.
        
        **세부 실행 방안:**
        
        1. **모바일뱅킹 서비스 고도화**
           - 현재 기초 수준에서 종합 금융 플랫폼으로 점진적 확장을 고려해 볼 수 있습니다
           - 직관적인 UI/UX로 고령층도 편리하게 이용 가능한 앱 설계를 검토할 수 있습니다
           - 계좌 개설부터 대출 실행까지 비대면 프로세스 완성을 통한 고객 편의성 제고가 가능할 것으로 보입니다
           - 지역 생활정보 및 혜택 연계 서비스 도입을 통한 차별화를 모색해 볼 수 있습니다
        
        2. **업무 프로세스 자동화**
           - RPA(Robotic Process Automation) 도입을 통한 반복 업무 자동화를 검토할 수 있습니다
           - 대출 심사 프로세스 일부 자동화 (서류 검토, 신용평가 등)를 통한 효율성 제고가 가능할 것으로 판단됩니다
           - AI 기반 고객 응대 시스템 구축 (챗봇, 음성 상담 등)을 단계적으로 도입해 볼 수 있습니다
           - 내부 업무 시스템 클라우드 전환을 통한 운영비용 최적화를 고려할 수 있습니다
        
        3. **데이터 기반 의사결정 체계 구축**
           - 고객 데이터 통합 관리 시스템 구축을 통한 고객 이해도 제고가 가능할 것으로 보입니다
           - AI 기반 신용평가 모델 도입을 통한 리스크 관리 고도화를 검토할 수 있습니다
           - 고객 세그먼테이션을 통한 타겟 마케팅 강화로 마케팅 효율성을 제고할 수 있을 것으로 판단됩니다
           - 데이터 분석 역량 강화를 위한 전문인력 확보 및 교육 프로그램 도입을 고려해 볼 수 있습니다
        """)
        
    with col2:
        st.markdown('<div class="insight-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 디지털 전환 기대 효과
        
        **효율성 제고**
        - 업무처리 시간: 약 30% 단축
        - 운영비용: 약 15% 절감
        - 직원당 생산성: 약 20% 향상
        
        **고객 경험 개선**
        - 대출 처리 시간: 3일→1일
        - 고객만족도: 약 20% 향상
        - 모바일뱅킹 이용률: 약 30% 증가
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # STAR 방식 적용 - 결과(Result)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">결과(Result)</p>', unsafe_allow_html=True)
    st.write("""
    제안된 수익성 강화 전략을 단계적으로 실행할 경우, ROA -0.75%에서 0.3%로 개선, NIM 1.69%에서 3.0%로 확대, 
    비이자수익 비중 5%에서 15%로 확대, 고정이하여신비율 10.46%에서 7.0%로 개선이 가능할 것으로 예상됩니다. 
    특히 비이자수익 확대와 디지털 전환을 통한 효율성 제고는 장기적인 경쟁력 강화에 기여할 것으로 판단됩니다.
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

# 7. 동종업권 비교분석 및 전략 제언
elif menu == "7. 동종업권 비교분석 및 전략 제언":
    st.markdown('<p class="main-header">7. 동종업권 비교분석 및 전략 제언</p>', unsafe_allow_html=True)
    
    # STAR 방식 적용 - 상황(Situation)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">상황(Situation)</p>', unsafe_allow_html=True)
    st.write("""
    충청·강원권 저축은행 업계의 2024년 데이터를 분석한 결과, 대명상호저축은행은 ROA -0.75%, 연체대출비율 10%, 
    PF대출 비중 31.9%, 연체비율 총합계 23.11%로 수익성과 자산 건전성 측면에서 개선의 여지가 있는 것으로 
    확인되었습니다. BIS 자기자본비율 16.81%는 양호한 수준이나, 동종업권 내 경쟁력 강화를 위한 전략적 접근이 
    필요한 상황입니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 충청·강원권 저축은행 업계 현황
    st.markdown('<p class="subsection-header">7.1 충청·강원권 저축은행 업계 현황</p>', unsafe_allow_html=True)
    
    # 비교 데이터 (5번 항목 수정)
    comparison_data = pd.DataFrame({
        '은행명': ['대명', 'CK', '오투', '청주', '한성'],
        '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '충북 - 청주, 천안', '충남 - 대전, 청주, 옥천'],
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

    # STAR 방식 적용 - 과제(Task)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">과제(Task)</p>', unsafe_allow_html=True)
    st.write("""
    동종업권 비교분석을 통해 대명상호저축은행의 상대적 위치를 파악하고, 경쟁사의 성공 사례와 실패 요인을 
    분석하여 대명상호저축은행에 적용 가능한 전략적 시사점을 도출하는 것이 본 섹션의 핵심 과제입니다.
    특히 ROA 개선, 연체율 관리, PF대출 비중 최적화를 위한 구체적인 전략 방안을 수립하고자 합니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("""
    충청·강원권 저축은행의 2024년 데이터를 분석한 결과, 대명상호저축은행은 ROA -0.75%, 연체대출비율 10%, 
    PF대출 비중 31.9%, 연체비율 총합계 23.11%로 수익성과 자산 건전성 측면에서 개선의 여지가 있는 것으로 
    확인되었습니다. BIS 자기자본비율 16.81%는 양호한 수준이나, 경쟁력 강화를 위한 전략적 접근이 
    필요한 것으로 판단됩니다.
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

    # STAR 방식 적용 - 행동(Action)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">행동(Action)</p>', unsafe_allow_html=True)
    st.write("""
    충청·강원권 내 주요 저축은행 5개사의 핵심 지표를 비교 분석하여 각 은행의 강점과 약점을 파악했습니다.
    특히 수익성(ROA), 자본적정성(BIS 비율), 자산건전성(연체율), 대출 포트폴리오(부동산 및 PF 대출 비중) 등을
    다각도로 검토하여 대명상호저축은행에 적용 가능한 전략적 시사점을 도출했습니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # 경쟁사 분석
    st.markdown('<p class="subsection-header">7.2 경쟁사 분석</p>', unsafe_allow_html=True)
    
    st.write("""
    동종업권 내 주요 은행들의 데이터를 바탕으로 대명상호저축은행의 상대적 위치를 분석해 보았습니다.
    """)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### CK저축은행 (강원도 - 강릉, 춘천)
        - **현황**: ROA 1.64% (2024), 부동산 대출 43.35%, PF대출 0%, 연체비율 총합계 3.12%.
        - **분석**: PF대출을 전략적으로 배제하고, 부동산 대출 비중을 93.28%에서 43.35%로 조정하여 자산 건전성을 효과적으로 관리하고 있는 것으로 판단됩니다. 이러한 포트폴리오 전략이 양호한 ROA 수준 유지에 기여하고 있는 것으로 보입니다.
        """)
        
    with col2:
        st.markdown("""
        ### 오투저축은행 (충청남도 - 대전, 천안)
        - **현황**: ROA -1.53% (2024), 연체대출비율 12.92%, PF대출 10.46%, 연체비율 총합계 24.59%.
        - **분석**: 높은 부동산 대출 비중(73.3%)과 연체비율 총합계로 인해 자산 건전성과 수익성 측면에서 일정한 도전에 직면해 있는 것으로 보입니다. 이는 포트폴리오 다각화와 리스크 관리의 중요성을 시사합니다.
        """)

    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        ### 청주저축은행 (청주, 천안)
        - **현황**: ROA -0.22% (2024), 부동산 대출 20.24%, PF대출 7.38%, 연체비율 총합계 12.32%.
        - **분석**: 상대적으로 낮은 부동산 및 PF대출 비중을 통해 자산 건전성을 효과적으로 관리하고 있는 것으로 판단됩니다. 이러한 포트폴리오 전략이 리스크 관리에 긍정적으로 기여하고 있는 것으로 보입니다.
        """)
        
    with col4:
        st.markdown("""
        ### 한성저축은행 (대전, 청주, 옥천)
        - **현황**: ROA -0.24% (2024), BIS 22.49%, PF대출 10.6%, 연체비율 총합계 16.7%.
        - **분석**: 높은 자기자본비율(22.49%)과 적정 수준의 PF대출 비중을 통해 안정적인 재무구조를 유지하고 있는 것으로 판단됩니다. 이는 리스크 관리와 자본 건전성 측면에서 참고할 만한 사례로 볼 수 있습니다.
        """)

    # 대명저축은행 전략적 제언
    st.markdown('<p class="subsection-header">7.3 대명저축은행 전략적 제언</p>', unsafe_allow_html=True)
    
    # STAR 방식 적용 - 결과(Result)
    st.markdown('<div class="star-box">', unsafe_allow_html=True)
    st.markdown('<p class="star-header">결과(Result)</p>', unsafe_allow_html=True)
    st.write("""
    동종업권 비교분석을 통해 대명상호저축은행에 적합한 전략적 방향성을 도출했습니다. CK저축은행의 PF대출 관리 전략,
    청주저축은행의 포트폴리오 다각화 접근, 한성저축은행의 자본 건전성 관리 방식 등은 벤치마킹 요소로 활용 가능합니다.
    이를 바탕으로 수익성 개선, 리스크 관리 강화, 자산 포트폴리오 최적화를 위한 구체적인 실행 방안을 제시했습니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("""
    대명상호저축은행의 현재 지표(ROA -0.75%, 연체대출비율 10%, PF대출 31.9%, 연체비율 총합계 23.11%)를 
    고려할 때, 수익성과 자산 건전성 개선을 위한 전략적 접근이 필요한 것으로 판단됩니다. 
    동종업권 분석을 바탕으로 다음과 같은 전략을 제안해 드리고자 합니다.
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
    - **제안 방안**:
      1. CK저축은행의 사례를 참고하여 부동산 대출 비중(45.85%)을 점진적으로 조정하여 리스크를 분산하는 방안을 검토해 볼 수 있을 것으로 보입니다.
      2. 청주저축은행의 낮은 PF대출 비중(7.38%)을 벤치마킹하여 현재 PF대출 비중(31.9%)을 단계적으로 조정하는 전략을 고려해 볼 수 있습니다.
    """)

    # B. 리스크 관리 및 자산 건전성 강화
    st.markdown("#### B. 리스크 관리 및 자산 건전성 강화")
    
    risk_roadmap = pd.DataFrame({
        '단계': ['1Q 2025', '2Q 2025', '3Q 2025', '4Q 2025'],
        '주요과제': [
            '연체대출비율 10%에서 9%로 관리',
            'PF대출 비중 31.9%에서 25%로 점진적 조정',
            '연체비율 총합계 23.11%에서 18%로 개선',
            '부동산 대출 비중 최적화'
        ]
    })
    
    st.table(risk_roadmap)
    
    st.write("""
    - **제안 방안**:
      1. 오투저축은행의 사례를 참고하여 연체율(12.92%)과 연체비율 총합계(24.59%)가 수익성에 미치는 영향을 고려한 선제적 리스크 관리 방안을 검토해 볼 수 있습니다.
      2. CK저축은행의 PF대출 관리 전략을 참고하여 PF대출 관련 리스크를 체계적으로 관리하는 방안을 고려해 볼 수 있습니다.
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
    - **제안 방안**:
      1. 청주저축은행(부동산 20.24%, PF대출 7.38%)의 포트폴리오 전략을 참고하여 부동산 및 PF대출 비중을 점진적으로 조정하는 방안을 검토해 볼 수 있습니다.
      2. 한성저축은행의 연체비율 관리 사례를 벤치마킹하여 자산 건전성 개선 방안을 모색해 볼 수 있습니다.
    """)



