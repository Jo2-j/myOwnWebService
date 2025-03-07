# # # # # # # # # import pandas as pd
# # # # # # # # # import plotly.express as px
# # # # # # # # # import plotly.graph_objects as go
# # # # # # # # # import streamlit as st

# # # # # # # # # # 페이지 설정
# # # # # # # # # st.set_page_config(
# # # # # # # # #     page_title="대명상호저축은행 수익성 강화 전략 보고서",
# # # # # # # # #     page_icon="💰",
# # # # # # # # #     layout="wide",
# # # # # # # # #     initial_sidebar_state="expanded"
# # # # # # # # # )

# # # # # # # # # # 기본 스타일 설정
# # # # # # # # # st.markdown("""
# # # # # # # # # <style>
# # # # # # # # #     .main-header {font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem;}
# # # # # # # # #     .section-header {font-size: 1.8rem; font-weight: bold; margin-top: 2rem; margin-bottom: 1rem; color: #1E3A8A;}
# # # # # # # # #     .subsection-header {font-size: 1.4rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.8rem; color: #2563EB;}
# # # # # # # # #     .caption {font-size: 0.8rem; font-style: italic; color: #6B7280;}
# # # # # # # # #     .star-box {background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #3B82F6;}
# # # # # # # # #     .star-header {font-weight: bold; color: #1E3A8A; margin-bottom: 0.5rem;}
# # # # # # # # # </style>
# # # # # # # # # """, unsafe_allow_html=True)

# # # # # # # # # # 데이터 정의
# # # # # # # # # financial_data = pd.DataFrame({
# # # # # # # # #     'Year': ['2023년 3분기', '2024년 3분기'],
# # # # # # # # #     'Total_Assets': [2575, 2365],
# # # # # # # # #     'Loans': [2078, 2245],
# # # # # # # # #     'Deposits': [2157, 2008],
# # # # # # # # #     'Capital': [330, 287],
# # # # # # # # #     'ROA': [-0.13, -0.75],
# # # # # # # # #     'NIM': [1.21, 1.69]
# # # # # # # # # })

# # # # # # # # # loan_portfolio_data = pd.DataFrame({
# # # # # # # # #     '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
# # # # # # # # #     '금액(억원)': [1015, 689, 91],
# # # # # # # # #     '비율(%)': [56.55, 38.38, 5.07]
# # # # # # # # # })

# # # # # # # # # collateral_data = pd.DataFrame({
# # # # # # # # #     '담보유형': ['부동산', '예수금', '기타'],
# # # # # # # # #     '금액(억원)': [823, 7, 959],
# # # # # # # # #     '비율(%)': [45.85, 0.39, 53.43]
# # # # # # # # # })

# # # # # # # # # management_metrics = pd.DataFrame({
# # # # # # # # #     '지표': ['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율', '순고정이하여신비율', '총자산순수익률'],
# # # # # # # # #     '2024년 3분기': [16.81, 12.13, 15.52, 10.46, -0.75],
# # # # # # # # #     '2023년 3분기': [17.86, 12.81, 16.61, 3.62, -0.13]
# # # # # # # # # })

# # # # # # # # # deposit_data = pd.DataFrame({
# # # # # # # # #     '구분': ['거치식예금', '적립식예금', '요구불예금'],
# # # # # # # # #     '금액(억원)': [1972, 26, 10],
# # # # # # # # #     '비율(%)': [98.21, 1.29, 0.5]
# # # # # # # # # })

# # # # # # # # # deposit_trend = pd.DataFrame({
# # # # # # # # #     '구분': ['2023년 3분기', '2024년 3분기'],
# # # # # # # # #     '예수금(억원)': [2157, 2008]
# # # # # # # # # })

# # # # # # # # # asset_quality_data = pd.DataFrame({
# # # # # # # # #     '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
# # # # # # # # #     '2023년 3분기': [91, 3, 60],
# # # # # # # # #     '2024년 3분기': [271, 29, 125],
# # # # # # # # # })

# # # # # # # # # delinquency_data = pd.DataFrame({
# # # # # # # # #     '구분': ['연체대출비율', '순고정이하여신비율'],
# # # # # # # # #     '2023년 3분기': [2.30, 3.62],
# # # # # # # # #     '2024년 3분기': [10.00, 10.46]
# # # # # # # # # })

# # # # # # # # # non_interest_income = pd.DataFrame({
# # # # # # # # #     '수익원': ['송금 및 결제 수수료', '펀드/보험 판매', '자산관리 서비스', 'PB 서비스', '기타 부가서비스'],
# # # # # # # # #     '현재(억원)': [3, 2, 0, 0, 1],
# # # # # # # # #     '목표(억원)': [5, 8, 4, 3, 5]
# # # # # # # # # })

# # # # # # # # # # 수정된 comparison_data: "BIS 자기자본비율(%) 2023"과 "카드" 데이터 추가
# # # # # # # # # comparison_data = pd.DataFrame({
# # # # # # # # #     '은행명': ['대명', 'CK', '오투', '청주', '한성'],
# # # # # # # # #     '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '충북 - 청주, 천안', '충남 - 대전, 청주, 옥천'],
# # # # # # # # #     'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
# # # # # # # # #     'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
# # # # # # # # #     'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
# # # # # # # # #     'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],  # 2023년 BIS 데이터 추가
# # # # # # # # #     '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
# # # # # # # # #     '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
# # # # # # # # #     'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
# # # # # # # # #     '연체비율 총합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70],
# # # # # # # # #     '카드(2024)': [0, 17, 6, 1547, 0],  # 2024년 카드 데이터
# # # # # # # # #     '카드(2023)': [0, 0, 4, 11178, 0]  # 2023년 카드 데이터 (청주의 1,1178은 오타로 간주하고 11178로 수정)
# # # # # # # # # })

# # # # # # # # # # 사이드바 메뉴
# # # # # # # # # st.sidebar.title("대명상호저축은행")
# # # # # # # # # st.sidebar.subheader("수익성 강화 전략 보고서")
# # # # # # # # # menu = st.sidebar.radio("목차", [
# # # # # # # # #     "1. 은행 현황 및 PF 대출 연계 과제",
# # # # # # # # #     "2. 재무 현황 분석",
# # # # # # # # #     "3. 동종업권 비교분석 및 전략 제언",
# # # # # # # # #     "4. 수익성 강화 전략"
# # # # # # # # # ])

# # # # # # # # # st.sidebar.divider()
# # # # # # # # # st.sidebar.info("""
# # # # # # # # # **2024년 9월말 주요 지표**
# # # # # # # # # - 총자산: 2,365억 원
# # # # # # # # # - 대출금: 2,245억 원
# # # # # # # # # - 예수금: 2,008억 원
# # # # # # # # # - BIS 자기자본비율: 16.81%
# # # # # # # # # """)
# # # # # # # # # st.sidebar.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# # # # # # # # # # 1. 은행 현황 및 PF 대출 연계 과제
# # # # # # # # # if menu == "1. 은행 현황 및 PF 대출 연계 과제":
# # # # # # # # #     st.markdown('<p class="main-header">1. 대명상호저축은행 현황 및 PF 대출 연계 과제</p>', unsafe_allow_html=True)
# # # # # # # # #     st.write("""
# # # # # # # # #     대명상호저축은행은 충북 제천을 기반으로 본점과 충주지점 2개 영업점을 운영하며, 총자산 2,365억 원(2024년 9월말 기준) 규모를 보유하고 있습니다. 
# # # # # # # # #     2024년 3분기 기준 ROA -0.75%, 연체대출비율 10%, PF대출 비중 31.9%로 수익성과 자산 건전성 측면에서 개선의 여지가 있습니다.
# # # # # # # # #     """)
    
# # # # # # # # #     st.markdown('<p class="subsection-header">1.1 저축은행 PF 대출 현황 및 대명과의 연계</p>', unsafe_allow_html=True)
# # # # # # # # #     st.write("""
# # # # # # # # #     저축은행 업계는 부동산 경기 조정과 금리 변동으로 PF 대출 연체율이 상승 중이며, 대명상호저축은행의 PF 대출 비중(31.9%)은 동종업권 평균(15-20%)을 상회합니다.
# # # # # # # # #     연체비율 총합계 23.11%로 선제적 리스크 관리가 필요합니다.
# # # # # # # # #     """)

# # # # # # # # # # 2. 재무 현황 분석 (도표만 표시)
# # # # # # # # # elif menu == "2. 재무 현황 분석":
# # # # # # # # #     st.markdown('<p class="main-header">2. 재무 현황 분석</p>', unsafe_allow_html=True)
    
# # # # # # # # #     st.markdown("### 주요 재무지표 추이")
# # # # # # # # #     tab1, tab2 = st.tabs(["자본적정성", "수익성"])
    
# # # # # # # # #     with tab1:
# # # # # # # # #         col1, col2 = st.columns(2)
# # # # # # # # #         with col1:
# # # # # # # # #             fig = px.bar(management_metrics[management_metrics['지표'].isin(['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율'])],
# # # # # # # # #                          x='지표', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자본적정성 지표 변화', height=400)
# # # # # # # # #             st.plotly_chart(fig, use_container_width=True)
# # # # # # # # #         with col2:
# # # # # # # # #             asset_liability_data = pd.DataFrame({'구분': ['자산', '부채', '자본'], '2023년 3분기': [2575, 2245, 330], '2024년 3분기': [2365, 2078, 287]})
# # # # # # # # #             fig = px.bar(asset_liability_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산/부채/자본 변화 (단위: 억원)', height=400)
# # # # # # # # #             st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # # #     with tab2:
# # # # # # # # #         col1, col2 = st.columns(2)
# # # # # # # # #         with col1:
# # # # # # # # #             profitability_data = pd.DataFrame({'지표': ['ROA'], '2023년 3분기': [-0.13], '2024년 3분기': [-0.75]})
# # # # # # # # #             fig = px.bar(profitability_data, x='지표', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='수익성 지표 변화', height=400)
# # # # # # # # #             st.plotly_chart(fig, use_container_width=True)
# # # # # # # # #         with col2:
# # # # # # # # #             interest_rate_data = pd.DataFrame({'구분': ['조달 평균이자율', '운용 평균이자율', '이자마진'], '2023년 3분기': [3.05, 4.26, 1.21], '2024년 3분기': [2.60, 4.29, 1.69]})
# # # # # # # # #             fig = px.bar(interest_rate_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='이자율 추이 (%)', height=400)
# # # # # # # # #             st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # # #     st.markdown('<p class="subsection-header"> 대출 포트폴리오 분석</p>', unsafe_allow_html=True)
# # # # # # # # #     col1, col2 = st.columns(2)
# # # # # # # # #     with col1:
# # # # # # # # #         fig = px.pie(loan_portfolio_data, values='금액(억원)', names='구분', title='용도별 대출 구성 (2024년 3분기)', height=400)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # # #     with col2:
# # # # # # # # #         fig = px.pie(collateral_data, values='금액(억원)', names='담보유형', title='담보별 대출 구성 (2024년 3분기)', height=400)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # # #     st.markdown('<p class="subsection-header"> 예수금 현황 분석</p>', unsafe_allow_html=True)
# # # # # # # # #     col1, col2 = st.columns(2)
# # # # # # # # #     with col1:
# # # # # # # # #         fig = px.pie(deposit_data, values='금액(억원)', names='구분', title='예수금 구성 (2024년 3분기)', height=400)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # # #     with col2:
# # # # # # # # #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400, text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"))
# # # # # # # # #         fig.update_traces(marker_color=['rgb(55, 83, 109)', 'rgb(255, 99, 71)'], textposition='auto')
# # # # # # # # #         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
# # # # # # # # #         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
# # # # # # # # #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # # #     st.markdown('<p class="subsection-header"> 자산건전성 및 리스크 현황</p>', unsafe_allow_html=True)
# # # # # # # # #     col1, col2 = st.columns(2)
# # # # # # # # #     with col1:
# # # # # # # # #         fig = px.bar(asset_quality_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산건전성 지표 (단위: 억원)', height=400)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # # #     with col2:
# # # # # # # # #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # # #     st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# # # # # # # # # # 3. 동종업권 비교분석 및 전략 제언
# # # # # # # # # elif menu == "3. 동종업권 비교분석 및 전략 제언":
# # # # # # # # #     st.markdown('<p class="main-header">3. 동종업권 비교분석 및 전략 제언</p>', unsafe_allow_html=True)
    
# # # # # # # # #     st.markdown('<p class="subsection-header">3.1 충청·강원권 저축은행 비교</p>', unsafe_allow_html=True)
# # # # # # # # #     col1, col2 = st.columns(2)
# # # # # # # # #     with col1:
# # # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='총자산순수익률(ROA) 비교', height=400)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # # #     with col2:
# # # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['연체대출비율(%) 2024'], barmode='group', title='연체대출비율 비교 (2024)', height=400)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # # #     col3, col4 = st.columns(2)
# # # # # # # # #     with col3:
# # # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['부동산 대출금(%) 2024'], barmode='group', title='부동산 대출금 비율 비교 (2024)', height=400)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # # #     with col4:
# # # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024', '연체비율 총합계(%) 2024'], barmode='group', title='PF대출 및 연체비율 총합계 비교 (2024)', height=400)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # # #     # 추가된 BIS 자기자본비율 및 카드 비교
# # # # # # # # #     col5, col6 = st.columns(2)
# # # # # # # # #     with col5:
# # # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # # #     with col6:
# # # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='카드 비교', height=400)
# # # # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # # #     st.caption("출처: 사용자 제공 데이터 (2024년 3월 7일 기준)")
    
# # # # # # # # #     st.markdown('<p class="subsection-header">3.2 전략 제언 (STAR 방식)</p>', unsafe_allow_html=True)
    
# # # # # # # # #     st.markdown('<div class="star-box">', unsafe_allow_html=True)
# # # # # # # # #     st.markdown('<p class="star-header">상황(Situation)</p>', unsafe_allow_html=True)
# # # # # # # # #     st.write("""
# # # # # # # # #     - 대명상호저축은행은 ROA -0.75%, NIM 1.69%, 연체대출비율 10%, PF대출 비중 31.9%로 수익성과 자산 건전성 개선이 필요합니다.
# # # # # # # # #     - 예수금은 6.9% 감소(2,157억 원 → 2,008억 원), 거치식예금 의존도 98.21%로 조달 비용 최적화 여지가 있습니다.
# # # # # # # # #     - 동종업권 대비 PF대출 비중(평균 15-20%)과 연체비율 총합계(23.11%)가 높아 리스크 관리가 시급합니다.
# # # # # # # # #     """)
# # # # # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # # # # #     st.markdown('<div class="star-box">', unsafe_allow_html=True)
# # # # # # # # #     st.markdown('<p class="star-header">과제(Task)</p>', unsafe_allow_html=True)
# # # # # # # # #     st.write("""
# # # # # # # # #     - ROA를 양(+)으로 전환하고, NIM을 업계 평균(약 3%) 수준으로 개선합니다.
# # # # # # # # #     - PF대출 비중을 최적화하고, 연체비율을 7% 이하로 관리합니다.
# # # # # # # # #     - 비이자수익 비중을 5%에서 15%로 확대하며, 디지털 전환으로 운영 효율성을 높입니다.
# # # # # # # # #     """)
# # # # # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # # # # #     st.markdown('<div class="star-box">', unsafe_allow_html=True)
# # # # # # # # #     st.markdown('<p class="star-header">행동(Action)</p>', unsafe_allow_html=True)
# # # # # # # # #     st.write("""
# # # # # # # # #     1. **대출 포트폴리오 최적화**: PF대출 비중을 31.9%에서 20%로 조정하고, 지역 중소기업 특화 대출 상품 개발.
# # # # # # # # #     2. **예대금리차 개선**: 저원가성 예금 비중 확대 및 대출 금리 체계 최적화.
# # # # # # # # #     3. **비이자수익 확대**: 송금·결제, 자산관리 등 서비스 도입으로 연간 25억 원 목표.
# # # # # # # # #     4. **디지털 전환**: 모바일뱅킹 고도화 및 RPA 도입으로 업무 효율성 30% 향상.
# # # # # # # # #     5. **리스크 관리**: CK저축은행(PF대출 0%) 및 청주저축은행(부동산 20.24%) 벤치마킹.
# # # # # # # # #     """)
# # # # # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # # # # #     st.markdown('<div class="star-box">', unsafe_allow_html=True)
# # # # # # # # #     st.markdown('<p class="star-header">결과(Result)</p>', unsafe_allow_html=True)
# # # # # # # # #     st.write("""
# # # # # # # # #     - ROA: -0.75% → 0.3%, NIM: 1.69% → 3.0%, 고정이하여신비율: 10.46% → 7.0%.
# # # # # # # # #     - 운영비용 15% 절감, 고객만족도 20% 향상, 모바일뱅킹 이용률 30% 증가.
# # # # # # # # #     - 자산 건전성 및 경쟁력 강화로 지속 가능한 성장 기반 마련.
# # # # # # # # #     """)
# # # # # # # # #     st.markdown('</div>', unsafe_allow_html=True)

# # # # # # # # # # 4. 수익성 강화 전략 (도표만 표시)
# # # # # # # # # elif menu == "4. 수익성 강화 전략":
# # # # # # # # #     st.markdown('<p class="main-header">4. 수익성 강화 전략</p>', unsafe_allow_html=True)
    
# # # # # # # # #     st.markdown('<p class="subsection-header">4.1 비이자수익 확대</p>', unsafe_allow_html=True)
# # # # # # # # #     fig = px.bar(non_interest_income, x='수익원', y=['현재(억원)', '목표(억원)'], barmode='group', title='비이자수익 확대 계획', height=400)
# # # # # # # # #     st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # # #     st.markdown('<p class="subsection-header">4.2 디지털 전환 로드맵</p>', unsafe_allow_html=True)
# # # # # # # # #     digital_roadmap = pd.DataFrame({
# # # # # # # # #         '단계': ['1단계(2025 Q1-Q2)', '2단계(2025 Q3-Q4)', '3단계(2026 Q1-Q2)'],
# # # # # # # # #         '주요과제': ['모바일앱 리뉴얼, RPA 일부 도입', '비대면 대출 프로세스 완성, 데이터 분석 기반 구축', 'AI 기반 신용평가, 종합 금융 플랫폼화'],
# # # # # # # # #         '투자비용(억원)': [3, 5, 7]
# # # # # # # # #     })
# # # # # # # # #     st.table(digital_roadmap)
# # # # # # # # #     st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석 기반")

# # # # # # # # import pandas as pd
# # # # # # # # import plotly.express as px
# # # # # # # # import plotly.graph_objects as go
# # # # # # # # import streamlit as st

# # # # # # # # # 페이지 설정
# # # # # # # # st.set_page_config(
# # # # # # # #     page_title="대명상호저축은행 수익성 강화 전략 보고서",
# # # # # # # #     page_icon="💰",
# # # # # # # #     layout="wide",
# # # # # # # #     initial_sidebar_state="expanded"
# # # # # # # # )

# # # # # # # # # 기본 스타일 설정
# # # # # # # # st.markdown("""
# # # # # # # # <style>
# # # # # # # #     .main-header {font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem;}
# # # # # # # #     .section-header {font-size: 1.8rem; font-weight: bold; margin-top: 2rem; margin-bottom: 1rem; color: #1E3A8A;}
# # # # # # # #     .subsection-header {font-size: 1.4rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.8rem; color: #2563EB;}
# # # # # # # #     .caption {font-size: 0.8rem; font-style: italic; color: #6B7280;}
# # # # # # # #     .star-box {background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #3B82F6;}
# # # # # # # #     .star-header {font-weight: bold; color: #1E3A8A; margin-bottom: 0.5rem;}
# # # # # # # # </style>
# # # # # # # # """, unsafe_allow_html=True)

# # # # # # # # # 데이터 정의
# # # # # # # # financial_data = pd.DataFrame({
# # # # # # # #     'Year': ['2023년 3분기', '2024년 3분기'],
# # # # # # # #     'Total_Assets': [2575, 2365],
# # # # # # # #     'Loans': [2078, 2245],
# # # # # # # #     'Deposits': [2157, 2008],
# # # # # # # #     'Capital': [330, 287],
# # # # # # # #     'ROA': [-0.13, -0.75],
# # # # # # # #     'NIM': [1.21, 1.69]
# # # # # # # # })

# # # # # # # # loan_portfolio_data = pd.DataFrame({
# # # # # # # #     '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
# # # # # # # #     '금액(억원)': [1015, 689, 91],
# # # # # # # #     '비율(%)': [56.55, 38.38, 5.07]
# # # # # # # # })

# # # # # # # # collateral_data = pd.DataFrame({
# # # # # # # #     '담보유형': ['부동산', '예수금', '기타'],
# # # # # # # #     '금액(억원)': [823, 7, 959],
# # # # # # # #     '비율(%)': [45.85, 0.39, 53.43]
# # # # # # # # })

# # # # # # # # management_metrics = pd.DataFrame({
# # # # # # # #     '지표': ['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율', '순고정이하여신비율', '총자산순수익률'],
# # # # # # # #     '2024년 3분기': [16.81, 12.13, 15.52, 10.46, -0.75],
# # # # # # # #     '2023년 3분기': [17.86, 12.81, 16.61, 3.62, -0.13]
# # # # # # # # })

# # # # # # # # deposit_data = pd.DataFrame({
# # # # # # # #     '구분': ['거치식예금', '적립식예금', '요구불예금'],
# # # # # # # #     '금액(억원)': [1972, 26, 10],
# # # # # # # #     '비율(%)': [98.21, 1.29, 0.5]
# # # # # # # # })

# # # # # # # # deposit_trend = pd.DataFrame({
# # # # # # # #     '구분': ['2023년 3분기', '2024년 3분기'],
# # # # # # # #     '예수금(억원)': [2157, 2008]
# # # # # # # # })

# # # # # # # # asset_quality_data = pd.DataFrame({
# # # # # # # #     '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
# # # # # # # #     '2023년 3분기': [91, 3, 60],
# # # # # # # #     '2024년 3분기': [271, 29, 125],
# # # # # # # # })

# # # # # # # # delinquency_data = pd.DataFrame({
# # # # # # # #     '구분': ['연체대출비율', '순고정이하여신비율'],
# # # # # # # #     '2023년 3분기': [2.30, 3.62],
# # # # # # # #     '2024년 3분기': [10.00, 10.46]
# # # # # # # # })

# # # # # # # # non_interest_income = pd.DataFrame({
# # # # # # # #     '수익원': ['송금 및 결제 수수료', '펀드/보험 판매', '자산관리 서비스', 'PB 서비스', '기타 부가서비스'],
# # # # # # # #     '현재(억원)': [3, 2, 0, 0, 1],
# # # # # # # #     '목표(억원)': [5, 8, 4, 3, 5]
# # # # # # # # })

# # # # # # # # comparison_data = pd.DataFrame({
# # # # # # # #     '은행명': ['대명', 'CK', '오투', '청주', '한성'],
# # # # # # # #     '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '충북 - 청주, 천안', '충남 - 대전, 청주, 옥천'],
# # # # # # # #     'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
# # # # # # # #     'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
# # # # # # # #     'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
# # # # # # # #     'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
# # # # # # # #     '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
# # # # # # # #     '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
# # # # # # # #     'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
# # # # # # # #     '연체비율 총합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70],
# # # # # # # #     '카드(2024)': [0, 17, 6, 1547, 0],
# # # # # # # #     '카드(2023)': [0, 0, 4, 11178, 0]
# # # # # # # # })

# # # # # # # # # 사이드바 메뉴
# # # # # # # # st.sidebar.title("대명상호저축은행")
# # # # # # # # st.sidebar.subheader("수익성 강화 전략 보고서")
# # # # # # # # menu = st.sidebar.radio("목차", [
# # # # # # # #     "1. 은행 현황 및 PF 대출 연계 과제",
# # # # # # # #     "2. 재무 현황 분석",
# # # # # # # #     "3. 동종업권 비교분석",
# # # # # # # #     "4. 수익성 강화 전략"
# # # # # # # # ])

# # # # # # # # st.sidebar.divider()
# # # # # # # # st.sidebar.info("""
# # # # # # # # **2024년 9월말 주요 지표**
# # # # # # # # - 총자산: 2,365억 원
# # # # # # # # - 대출금: 2,245억 원
# # # # # # # # - 예수금: 2,008억 원
# # # # # # # # - BIS 자기자본비율: 16.81%
# # # # # # # # """)
# # # # # # # # st.sidebar.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# # # # # # # # # 1. 은행 현황 및 PF 대출 연계 과제
# # # # # # # # if menu == "1. 은행 현황 및 PF 대출 연계 과제":
# # # # # # # #     st.markdown('<p class="main-header">1. 대명상호저축은행 현황 및 PF 대출 연계 과제</p>', unsafe_allow_html=True)
# # # # # # # #     st.write("""
# # # # # # # #     대명상호저축은행은 충북 제천을 기반으로 본점과 충주지점 2개 영업점을 운영하며, 총자산 2,365억 원(2024년 9월말 기준) 규모를 보유하고 있습니다. 
# # # # # # # #     2024년 3분기 기준 ROA -0.75%, 연체대출비율 10%, PF대출 비중 31.9%로 수익성과 자산 건전성 측면에서 개선의 여지가 있습니다.
# # # # # # # #     """)
    
# # # # # # # #     st.markdown('<p class="subsection-header">1.1 저축은행 PF 대출 현황 및 대명과의 연계</p>', unsafe_allow_html=True)
# # # # # # # #     st.write("""
# # # # # # # #     저축은행 업계는 부동산 경기 조정과 금리 변동으로 PF 대출 연체율이 상승 중이며, 대명상호저축은행의 PF 대출 비중(31.9%)은 동종업권 평균(15-20%)을 상회합니다.
# # # # # # # #     연체비율 총합계 23.11%로 선제적 리스크 관리가 필요합니다.
# # # # # # # #     """)

# # # # # # # # # 2. 재무 현황 분석 (소제목 재분류 및 탭 제거)
# # # # # # # # elif menu == "2. 재무 현황 분석":
# # # # # # # #     st.markdown('<p class="main-header">2. 재무 현황 분석</p>', unsafe_allow_html=True)
    
# # # # # # # #     st.markdown('<p class="subsection-header">2.1 주요 재무지표</p>', unsafe_allow_html=True)
# # # # # # # #     col1, col2 = st.columns(2)
# # # # # # # #     with col1:
# # # # # # # #         fig = px.bar(management_metrics[management_metrics['지표'].isin(['BIS 자기자본비율', '총자산순수익률'])],
# # # # # # # #                      x='지표', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='BIS 자기자본비율 및 ROA 추이', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # #     with col2:
# # # # # # # #         asset_liability_data = pd.DataFrame({'구분': ['자산', '부채', '자본'], '2023년 3분기': [2575, 2245, 330], '2024년 3분기': [2365, 2078, 287]})
# # # # # # # #         fig = px.bar(asset_liability_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산/부채/자본 변화 (단위: 억원)', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # #     st.markdown('<p class="subsection-header">2.2 대출 포트폴리오</p>', unsafe_allow_html=True)
# # # # # # # #     col1, col2 = st.columns(2)
# # # # # # # #     with col1:
# # # # # # # #         fig = px.pie(loan_portfolio_data, values='금액(억원)', names='구분', title='용도별 대출 구성 (2024년 3분기)', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # #     with col2:
# # # # # # # #         fig = px.pie(collateral_data, values='금액(억원)', names='담보유형', title='담보별 대출 구성 (2024년 3분기)', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # #     st.markdown('<p class="subsection-header">2.3 예수금 현황</p>', unsafe_allow_html=True)
# # # # # # # #     col1, col2 = st.columns(2)
# # # # # # # #     with col1:
# # # # # # # #         fig = px.pie(deposit_data, values='금액(억원)', names='구분', title='예수금 구성 (2024년 3분기)', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # #     with col2:
# # # # # # # #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400, text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"))
# # # # # # # #         fig.update_traces(marker_color=['rgb(55, 83, 109)', 'rgb(255, 99, 71)'], textposition='auto')
# # # # # # # #         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
# # # # # # # #         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
# # # # # # # #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # #     st.markdown('<p class="subsection-header">2.4 자산 건전성</p>', unsafe_allow_html=True)
# # # # # # # #     col1, col2 = st.columns(2)
# # # # # # # #     with col1:
# # # # # # # #         fig = px.bar(asset_quality_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산건전성 지표 (단위: 억원)', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # #     with col2:
# # # # # # # #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # #     st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# # # # # # # # # 3. 동종업권 비교분석 (도표만 표시)
# # # # # # # # elif menu == "3. 동종업권 비교분석":
# # # # # # # #     st.markdown('<p class="main-header">3. 동종업권 비교분석</p>', unsafe_allow_html=True)
    
# # # # # # # #     col1, col2 = st.columns(2)
# # # # # # # #     with col1:
# # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='총자산순수익률(ROA) 비교', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # #     with col2:
# # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['연체대출비율(%) 2024'], barmode='group', title='연체대출비율 비교 (2024)', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # #     col3, col4 = st.columns(2)
# # # # # # # #     with col3:
# # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['부동산 대출금(%) 2024'], barmode='group', title='부동산 대출금 비율 비교 (2024)', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # #     with col4:
# # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024', '연체비율 총합계(%) 2024'], barmode='group', title='PF대출 및 연체비율 총합계 비교 (2024)', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # #     col5, col6 = st.columns(2)
# # # # # # # #     with col5:
# # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # # #     with col6:
# # # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='카드 비교', height=400)
# # # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # #     st.caption("출처: 사용자 제공 데이터 (2024년 3월 7일 기준)")

# # # # # # # # # 4. 수익성 강화 전략 (전략 제언 통합)
# # # # # # # # elif menu == "4. 수익성 강화 전략":
# # # # # # # #     st.markdown('<p class="main-header">4. 수익성 강화 전략</p>', unsafe_allow_html=True)
    
# # # # # # # #     st.markdown('<p class="subsection-header">4.1 비이자수익 확대</p>', unsafe_allow_html=True)
# # # # # # # #     fig = px.bar(non_interest_income, x='수익원', y=['현재(억원)', '목표(억원)'], barmode='group', title='비이자수익 확대 계획', height=400)
# # # # # # # #     st.plotly_chart(fig, use_container_width=True)
    
# # # # # # # #     st.markdown('<p class="subsection-header">4.2 디지털 전환 로드맵</p>', unsafe_allow_html=True)
# # # # # # # #     digital_roadmap = pd.DataFrame({
# # # # # # # #         '단계': ['1단계(2025 Q1-Q2)', '2단계(2025 Q3-Q4)', '3단계(2026 Q1-Q2)'],
# # # # # # # #         '주요과제': ['모바일앱 리뉴얼, RPA 일부 도입', '비대면 대출 프로세스 완성, 데이터 분석 기반 구축', 'AI 기반 신용평가, 종합 금융 플랫폼화'],
# # # # # # # #         '투자비용(억원)': [3, 5, 7]
# # # # # # # #     })
# # # # # # # #     st.table(digital_roadmap)
    
# # # # # # # #     st.markdown('<p class="subsection-header">4.3 전략 제언 (STAR 방식)</p>', unsafe_allow_html=True)
    
# # # # # # # #     st.markdown('<div class="star-box">', unsafe_allow_html=True)
# # # # # # # #     st.markdown('<p class="star-header">상황(Situation)</p>', unsafe_allow_html=True)
# # # # # # # #     st.write("""
# # # # # # # #     - 대명상호저축은행은 ROA -0.75%, NIM 1.69%, 연체대출비율 10%, PF대출 비중 31.9%로 수익성과 자산 건전성 개선이 필요합니다.
# # # # # # # #     - 예수금은 6.9% 감소(2,157억 원 → 2,008억 원), 거치식예금 의존도 98.21%로 조달 비용 최적화 여지가 있습니다.
# # # # # # # #     - 동종업권 대비 PF대출 비중(평균 15-20%)과 연체비율 총합계(23.11%)가 높아 리스크 관리가 시급합니다.
# # # # # # # #     """)
# # # # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # # # #     st.markdown('<div class="star-box">', unsafe_allow_html=True)
# # # # # # # #     st.markdown('<p class="star-header">과제(Task)</p>', unsafe_allow_html=True)
# # # # # # # #     st.write("""
# # # # # # # #     - ROA를 양(+)으로 전환하고, NIM을 업계 평균(약 3%) 수준으로 개선합니다.
# # # # # # # #     - PF대출 비중을 최적화하고, 연체비율을 7% 이하로 관리합니다.
# # # # # # # #     - 비이자수익 비중을 5%에서 15%로 확대하며, 디지털 전환으로 운영 효율성을 높입니다.
# # # # # # # #     """)
# # # # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # # # #     st.markdown('<div class="star-box">', unsafe_allow_html=True)
# # # # # # # #     st.markdown('<p class="star-header">행동(Action)</p>', unsafe_allow_html=True)
# # # # # # # #     st.write("""
# # # # # # # #     1. **대출 포트폴리오 최적화**: PF대출 비중을 31.9%에서 20%로 조정하고, 지역 중소기업 특화 대출 상품 개발.
# # # # # # # #     2. **예대금리차 개선**: 저원가성 예금 비중 확대 및 대출 금리 체계 최적화.
# # # # # # # #     3. **비이자수익 확대**: 송금·결제, 자산관리 등 서비스 도입으로 연간 25억 원 목표.
# # # # # # # #     4. **디지털 전환**: 모바일뱅킹 고도화 및 RPA 도입으로 업무 효율성 30% 향상.
# # # # # # # #     5. **리스크 관리**: CK저축은행(PF대출 0%) 및 청주저축은행(부동산 20.24%) 벤치마킹.
# # # # # # # #     """)
# # # # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # # # #     st.markdown('<div class="star-box">', unsafe_allow_html=True)
# # # # # # # #     st.markdown('<p class="star-header">결과(Result)</p>', unsafe_allow_html=True)
# # # # # # # #     st.write("""
# # # # # # # #     - ROA: -0.75% → 0.3%, NIM: 1.69% → 3.0%, 고정이하여신비율: 10.46% → 7.0%.
# # # # # # # #     - 운영비용 15% 절감, 고객만족도 20% 향상, 모바일뱅킹 이용률 30% 증가.
# # # # # # # #     - 자산 건전성 및 경쟁력 강화로 지속 가능한 성장 기반 마련.
# # # # # # # #     """)
# # # # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # # # #     st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 분석 기반")

# # # # # # # import pandas as pd
# # # # # # # import plotly.express as px
# # # # # # # import plotly.graph_objects as go
# # # # # # # import streamlit as st

# # # # # # # # 페이지 설정
# # # # # # # st.set_page_config(
# # # # # # #     page_title="대명상호저축은행 수익성 강화 전략 보고서",
# # # # # # #     page_icon="💰",
# # # # # # #     layout="wide",
# # # # # # #     initial_sidebar_state="expanded"
# # # # # # # )

# # # # # # # # 기본 스타일 설정
# # # # # # # st.markdown("""
# # # # # # # <style>
# # # # # # #     .main-header {font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem;}
# # # # # # #     .section-header {font-size: 1.8rem; font-weight: bold; margin-top: 2rem; margin-bottom: 1rem; color: #1E3A8A;}
# # # # # # #     .subsection-header {font-size: 1.4rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.8rem; color: #2563EB;}
# # # # # # #     .caption {font-size: 0.8rem; font-style: italic; color: #6B7280;}
# # # # # # #     .insight-box {background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #3B82F6;}
# # # # # # #     .insight-header {font-weight: bold; color: #1E3A8A; margin-bottom: 0.5rem;}
# # # # # # # </style>
# # # # # # # """, unsafe_allow_html=True)

# # # # # # # # 데이터 정의 (이전과 동일, 생략)
# # # # # # # financial_data = pd.DataFrame({
# # # # # # #     'Year': ['2023년 3분기', '2024년 3분기'],
# # # # # # #     'Total_Assets': [2575, 2365],
# # # # # # #     'Loans': [2078, 2245],
# # # # # # #     'Deposits': [2157, 2008],
# # # # # # #     'Capital': [330, 287],
# # # # # # #     'ROA': [-0.13, -0.75],
# # # # # # #     'NIM': [1.21, 1.69]
# # # # # # # })

# # # # # # # loan_portfolio_data = pd.DataFrame({
# # # # # # #     '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
# # # # # # #     '금액(억원)': [1015, 689, 91],
# # # # # # #     '비율(%)': [56.55, 38.38, 5.07]
# # # # # # # })

# # # # # # # collateral_data = pd.DataFrame({
# # # # # # #     '담보유형': ['부동산', '예수금', '기타'],
# # # # # # #     '금액(억원)': [823, 7, 959],
# # # # # # #     '비율(%)': [45.85, 0.39, 53.43]
# # # # # # # })

# # # # # # # management_metrics = pd.DataFrame({
# # # # # # #     '지표': ['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율', '순고정이하여신비율', '총자산순수익률'],
# # # # # # #     '2024년 3분기': [16.81, 12.13, 15.52, 10.46, -0.75],
# # # # # # #     '2023년 3분기': [17.86, 12.81, 16.61, 3.62, -0.13]
# # # # # # # })

# # # # # # # deposit_data = pd.DataFrame({
# # # # # # #     '구분': ['거치식예금', '적립식예금', '요구불예금'],
# # # # # # #     '금액(억원)': [1972, 26, 10],
# # # # # # #     '비율(%)': [98.21, 1.29, 0.5]
# # # # # # # })

# # # # # # # deposit_trend = pd.DataFrame({
# # # # # # #     '구분': ['2023년 3분기', '2024년 3분기'],
# # # # # # #     '예수금(억원)': [2157, 2008]
# # # # # # # })

# # # # # # # asset_quality_data = pd.DataFrame({
# # # # # # #     '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
# # # # # # #     '2023년 3분기': [91, 3, 60],
# # # # # # #     '2024년 3분기': [271, 29, 125],
# # # # # # # })

# # # # # # # delinquency_data = pd.DataFrame({
# # # # # # #     '구분': ['연체대출비율', '순고정이하여신비율'],
# # # # # # #     '2023년 3분기': [2.30, 3.62],
# # # # # # #     '2024년 3분기': [10.00, 10.46]
# # # # # # # })

# # # # # # # non_interest_income = pd.DataFrame({
# # # # # # #     '수익원': ['송금 및 결제 수수료', '펀드/보험 판매', '자산관리 서비스', 'PB 서비스', '기타 부가서비스'],
# # # # # # #     '현재(억원)': [3, 2, 0, 0, 1],
# # # # # # #     '목표(억원)': [5, 8, 4, 3, 5]
# # # # # # # })

# # # # # # # comparison_data = pd.DataFrame({
# # # # # # #     '은행명': ['대명', 'CK', '오투', '청주', '한성'],
# # # # # # #     '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '충북 - 청주, 천안', '충남 - 대전, 청주, 옥천'],
# # # # # # #     'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
# # # # # # #     'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
# # # # # # #     'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
# # # # # # #     'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
# # # # # # #     '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
# # # # # # #     '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
# # # # # # #     'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
# # # # # # #     '연체비율 총합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70],
# # # # # # #     '카드(2024)': [0, 17, 6, 1547, 0],
# # # # # # #     '카드(2023)': [0, 0, 4, 11178, 0]
# # # # # # # })

# # # # # # # # 사이드바 메뉴 (이전과 동일, 생략)
# # # # # # # st.sidebar.title("대명상호저축은행")
# # # # # # # st.sidebar.subheader("수익성 강화 전략 보고서")
# # # # # # # menu = st.sidebar.radio("목차", [
# # # # # # #     "1. 은행 현황 및 PF 대출 연계 과제",
# # # # # # #     "2. 재무 현황 분석",
# # # # # # #     "3. 동종업권 비교분석",
# # # # # # #     "4. 수익성 강화 전략"
# # # # # # # ])

# # # # # # # st.sidebar.divider()
# # # # # # # st.sidebar.info("""
# # # # # # # **2024년 9월말 주요 지표**
# # # # # # # - 총자산: 2,365억 원
# # # # # # # - 대출금: 2,245억 원
# # # # # # # - 예수금: 2,008억 원
# # # # # # # - BIS 자기자본비율: 16.81%
# # # # # # # """)
# # # # # # # st.sidebar.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# # # # # # # # 1, 2, 3번 섹션 (이전과 동일, 생략)
# # # # # # # if menu == "1. 은행 현황 및 PF 대출 연계 과제":
# # # # # # #     st.markdown('<p class="main-header">1. 대명상호저축은행 현황 및 PF 대출 연계 과제</p>', unsafe_allow_html=True)
# # # # # # #     st.write("""
# # # # # # #     대명상호저축은행은 충북 제천을 기반으로 본점과 충주지점 2개 영업점을 운영하며, 총자산 2,365억 원(2024년 9월말 기준) 규모를 보유하고 있습니다. 
# # # # # # #     2024년 3분기 기준 ROA -0.75%, 연체대출비율 10%, PF대출 비중 31.9%로 수익성과 자산 건전성 측면에서 개선의 여지가 있습니다.
# # # # # # #     """)
    
# # # # # # #     st.markdown('<p class="subsection-header">1.1 저축은행 PF 대출 현황 및 대명과의 연계</p>', unsafe_allow_html=True)
# # # # # # #     st.write("""
# # # # # # #     저축은행 업계는 부동산 경기 조정과 금리 변동으로 PF 대출 연체율이 상승 중이며, 대명상호저축은행의 PF 대출 비중(31.9%)은 동종업권 평균(15-20%)을 상회합니다.
# # # # # # #     연체비율 총합계 23.11%로 선제적 리스크 관리가 필요합니다.
# # # # # # #     """)

# # # # # # # elif menu == "2. 재무 현황 분석":
# # # # # # #     st.markdown('<p class="main-header">2. 재무 현황 분석</p>', unsafe_allow_html=True)
    
# # # # # # #     st.markdown('<p class="subsection-header">2.1 주요 재무지표</p>', unsafe_allow_html=True)
# # # # # # #     col1, col2 = st.columns(2)
# # # # # # #     with col1:
# # # # # # #         fig = px.bar(management_metrics[management_metrics['지표'].isin(['BIS 자기자본비율', '총자산순수익률'])],
# # # # # # #                      x='지표', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='BIS 자기자본비율 및 ROA 추이', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # #     with col2:
# # # # # # #         asset_liability_data = pd.DataFrame({'구분': ['자산', '부채', '자본'], '2023년 3분기': [2575, 2245, 330], '2024년 3분기': [2365, 2078, 287]})
# # # # # # #         fig = px.bar(asset_liability_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산/부채/자본 변화 (단위: 억원)', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # #     st.markdown('<p class="subsection-header">2.2 대출 포트폴리오</p>', unsafe_allow_html=True)
# # # # # # #     col1, col2 = st.columns(2)
# # # # # # #     with col1:
# # # # # # #         fig = px.pie(loan_portfolio_data, values='금액(억원)', names='구분', title='용도별 대출 구성 (2024년 3분기)', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # #     with col2:
# # # # # # #         fig = px.pie(collateral_data, values='금액(억원)', names='담보유형', title='담보별 대출 구성 (2024년 3분기)', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # #     st.markdown('<p class="subsection-header">2.3 예수금 현황</p>', unsafe_allow_html=True)
# # # # # # #     col1, col2 = st.columns(2)
# # # # # # #     with col1:
# # # # # # #         fig = px.pie(deposit_data, values='금액(억원)', names='구분', title='예수금 구성 (2024년 3분기)', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # #     with col2:
# # # # # # #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400, text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"))
# # # # # # #         fig.update_traces(marker_color=['rgb(55, 83, 109)', 'rgb(255, 99, 71)'], textposition='auto')
# # # # # # #         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
# # # # # # #         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
# # # # # # #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # #     st.markdown('<p class="subsection-header">2.4 자산 건전성</p>', unsafe_allow_html=True)
# # # # # # #     col1, col2 = st.columns(2)
# # # # # # #     with col1:
# # # # # # #         fig = px.bar(asset_quality_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산건전성 지표 (단위: 억원)', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # #     with col2:
# # # # # # #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # #     st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# # # # # # # elif menu == "3. 동종업권 비교분석":
# # # # # # #     st.markdown('<p class="main-header">3. 동종업권 비교분석</p>', unsafe_allow_html=True)
    
# # # # # # #     col1, col2 = st.columns(2)
# # # # # # #     with col1:
# # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='총자산순수익률(ROA) 비교', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # #     with col2:
# # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['연체대출비율(%) 2024'], barmode='group', title='연체대출비율 비교 (2024)', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # #     col3, col4 = st.columns(2)
# # # # # # #     with col3:
# # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['부동산 대출금(%) 2024'], barmode='group', title='부동산 대출금 비율 비교 (2024)', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # #     with col4:
# # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024', '연체비율 총합계(%) 2024'], barmode='group', title='PF대출 및 연체비율 총합계 비교 (2024)', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # #     col5, col6 = st.columns(2)
# # # # # # #     with col5:
# # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # #     with col6:
# # # # # # #         fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='카드 비교', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # # #     st.caption("출처: 사용자 제공 데이터 (2024년 3월 7일 기준)")

# # # # # # # # 4. 수익성 강화 전략 (통합 인사이트로 재구성)
# # # # # # # elif menu == "4. 수익성 강화 전략":
# # # # # # #     st.markdown('<p class="main-header">4. 수익성 강화 전략</p>', unsafe_allow_html=True)
    
# # # # # # #     st.markdown('<p class="subsection-header">4.1 비이자수익 및 디지털 전환 현황</p>', unsafe_allow_html=True)
# # # # # # #     col1, col2 = st.columns(2)
# # # # # # #     with col1:
# # # # # # #         fig = px.bar(non_interest_income, x='수익원', y=['현재(억원)', '목표(억원)'], barmode='group', title='비이자수익 현황 및 목표', height=400)
# # # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # # #     with col2:
# # # # # # #         digital_roadmap = pd.DataFrame({
# # # # # # #             '단계': ['1단계(2025 Q1-Q2)', '2단계(2025 Q3-Q4)', '3단계(2026 Q1-Q2)'],
# # # # # # #             '주요과제': ['모바일앱 리뉴얼, RPA 일부 도입', '비대면 대출 프로세스 완성, 데이터 분석 기반 구축', 'AI 기반 신용평가, 종합 금융 플랫폼화'],
# # # # # # #             '투자비용(억원)': [3, 5, 7]
# # # # # # #         })
# # # # # # #         st.table(digital_roadmap)
    
# # # # # # #     st.markdown('<p class="subsection-header">4.2 수익성 강화를 위한 인사이트</p>', unsafe_allow_html=True)
    
# # # # # # #     st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # # # # #     st.markdown('<p class="insight-header">리스크 관리 개선</p>', unsafe_allow_html=True)
# # # # # # #     st.write("""
# # # # # # #     - PF대출 비중(31.9%)과 연체비율 총합계(23.11%)가 동종업권 평균(15-20%, 12-16%) 대비 높아 리스크 관리가 필요해 보입니다.
# # # # # # #     - CK저축은행(PF대출 0%)과 청주저축은행(부동산 대출 20.24%) 사례를 참고하여 PF대출 비중을 20% 수준으로 조정하는 방안이 유효할 수 있습니다.
# # # # # # #     - 연체대출비율(10%)을 동종업권 평균(7% 이하)으로 낮추기 위해 지역 중소기업 특화 대출 등 안정적 포트폴리오로의 전환이 고려될 수 있습니다.
# # # # # # #     """)
# # # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # # #     st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # # # # #     st.markdown('<p class="insight-header">이자수익 구조 개선</p>', unsafe_allow_html=True)
# # # # # # #     st.write("""
# # # # # # #     - NIM(1.69%)이 업계 평균(약 3%)에 미치지 못하며, 예수금 감소(6.9%)와 거치식 예금 의존도(98.21%)가 조달 비용에 영향을 줄 가능성이 있습니다.
# # # # # # #     - 저원가성 예금(요구불/적립식) 비중 확대와 대출 금리 체계 최적화로 예대금리차를 개선하는 방향이 적절해 보입니다.
# # # # # # #     - 동종업권 내 CK저축은행(ROA 1.64%)의 안정적 수익 구조를 벤치마킹할 수 있습니다.
# # # # # # #     """)
# # # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # # #     st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # # # # #     st.markdown('<p class="insight-header">비이자수익 및 디지털 전환 강화</p>', unsafe_allow_html=True)
# # # # # # #     st.write("""
# # # # # # #     - 비이자수익(현재 6억 원)이 전체 수익에서 차지하는 비중이 낮아 송금·결제, 자산관리 서비스 도입으로 연간 25억 원 수준으로 확대하는 방안이 효과적일 수 있습니다.
# # # # # # #     - 디지털 전환(모바일뱅킹 고도화, RPA 도입)을 통해 운영 효율성을 약 30% 향상시키고, 고객 접근성을 높이는 것이 경쟁력 강화에 기여할 가능성이 있습니다.
# # # # # # #     - 청주저축은행(카드 1,547건)의 비이자수익 모델을 참고하여 지역 특화 금융 상품 개발이 유망해 보입니다.
# # # # # # #     """)
# # # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # # #     st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # # # # #     st.markdown('<p class="insight-header">기대 효과</p>', unsafe_allow_html=True)
# # # # # # #     st.write("""
# # # # # # #     - 리스크 관리와 수익 구조 개선을 통해 ROA(-0.75% → 0.3%), NIM(1.69% → 3.0%), 연체비율(10% → 7%) 달성이 가능해 보입니다.
# # # # # # #     - 디지털 전환으로 운영비용 15% 절감, 고객만족도 20% 향상, 모바일뱅킹 이용률 30% 증가 등이 예상됩니다.
# # # # # # #     - 지속 가능한 성장 기반을 마련하기 위해 동종업권 우수 사례와 데이터 기반 접근이 중요할 수 있습니다.
# # # # # # #     """)
# # # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # # #     st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 및 사용자 제공 데이터 분석 기반")

# # # # # # import pandas as pd
# # # # # # import plotly.express as px
# # # # # # import plotly.graph_objects as go
# # # # # # import streamlit as st

# # # # # # # 페이지 설정
# # # # # # st.set_page_config(
# # # # # #     page_title="대명상호저축은행 수익성 강화 전략 보고서",
# # # # # #     page_icon="💰",
# # # # # #     layout="wide",
# # # # # #     initial_sidebar_state="expanded"
# # # # # # )

# # # # # # # 기본 스타일 설정
# # # # # # st.markdown("""
# # # # # # <style>
# # # # # #     .main-header {font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem;}
# # # # # #     .section-header {font-size: 1.8rem; font-weight: bold; margin-top: 2rem; margin-bottom: 1rem; color: #1E3A8A;}
# # # # # #     .subsection-header {font-size: 1.4rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.8rem; color: #2563EB;}
# # # # # #     .caption {font-size: 0.8rem; font-style: italic; color: #6B7280;}
# # # # # #     .recap-box {background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #3B82F6;}
# # # # # #     .recap-header {font-weight: bold; color: #1E3A8A; margin-bottom: 0.5rem;}
# # # # # # </style>
# # # # # # """, unsafe_allow_html=True)

# # # # # # # 데이터 정의 (이전과 동일, 생략)
# # # # # # financial_data = pd.DataFrame({
# # # # # #     'Year': ['2023년 3분기', '2024년 3분기'],
# # # # # #     'Total_Assets': [2575, 2365],
# # # # # #     'Loans': [2078, 2245],
# # # # # #     'Deposits': [2157, 2008],
# # # # # #     'Capital': [330, 287],
# # # # # #     'ROA': [-0.13, -0.75],
# # # # # #     'NIM': [1.21, 1.69]
# # # # # # })

# # # # # # loan_portfolio_data = pd.DataFrame({
# # # # # #     '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
# # # # # #     '금액(억원)': [1015, 689, 91],
# # # # # #     '비율(%)': [56.55, 38.38, 5.07]
# # # # # # })

# # # # # # collateral_data = pd.DataFrame({
# # # # # #     '담보유형': ['부동산', '예수금', '기타'],
# # # # # #     '금액(억원)': [823, 7, 959],
# # # # # #     '비율(%)': [45.85, 0.39, 53.43]
# # # # # # })

# # # # # # management_metrics = pd.DataFrame({
# # # # # #     '지표': ['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율', '순고정이하여신비율', '총자산순수익률'],
# # # # # #     '2024년 3분기': [16.81, 12.13, 15.52, 10.46, -0.75],
# # # # # #     '2023년 3분기': [17.86, 12.81, 16.61, 3.62, -0.13]
# # # # # # })

# # # # # # deposit_data = pd.DataFrame({
# # # # # #     '구분': ['거치식예금', '적립식예금', '요구불예금'],
# # # # # #     '금액(억원)': [1972, 26, 10],
# # # # # #     '비율(%)': [98.21, 1.29, 0.5]
# # # # # # })

# # # # # # deposit_trend = pd.DataFrame({
# # # # # #     '구분': ['2023년 3분기', '2024년 3분기'],
# # # # # #     '예수금(억원)': [2157, 2008]
# # # # # # })

# # # # # # asset_quality_data = pd.DataFrame({
# # # # # #     '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
# # # # # #     '2023년 3분기': [91, 3, 60],
# # # # # #     '2024년 3분기': [271, 29, 125],
# # # # # # })

# # # # # # delinquency_data = pd.DataFrame({
# # # # # #     '구분': ['연체대출비율', '순고정이하여신비율'],
# # # # # #     '2023년 3분기': [2.30, 3.62],
# # # # # #     '2024년 3분기': [10.00, 10.46]
# # # # # # })

# # # # # # comparison_data = pd.DataFrame({
# # # # # #     '은행명': ['대명', 'CK', '오투', '청주', '한성'],
# # # # # #     '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '충북 - 청주, 천안', '충남 - 대전, 청주, 옥천'],
# # # # # #     'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
# # # # # #     'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
# # # # # #     'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
# # # # # #     'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
# # # # # #     '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
# # # # # #     '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
# # # # # #     'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
# # # # # #     '연체비율 총합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70],
# # # # # #     '카드(2024)': [0, 17, 6, 1547, 0],
# # # # # #     '카드(2023)': [0, 0, 4, 11178, 0]
# # # # # # })

# # # # # # # 사이드바 메뉴 (이전과 동일, 생략)
# # # # # # st.sidebar.title("대명상호저축은행")
# # # # # # st.sidebar.subheader("수익성 강화 전략 보고서")
# # # # # # menu = st.sidebar.radio("목차", [
# # # # # #     "1. 은행 현황 및 PF 대출 연계 과제",
# # # # # #     "2. 재무 현황 분석",
# # # # # #     "3. 동종업권 비교분석",
# # # # # #     "4. 수익성 강화 전략"
# # # # # # ])

# # # # # # st.sidebar.divider()
# # # # # # st.sidebar.info("""
# # # # # # **2024년 9월말 주요 지표**
# # # # # # - 총자산: 2,365억 원
# # # # # # - 대출금: 2,245억 원
# # # # # # - 예수금: 2,008억 원
# # # # # # - BIS 자기자본비율: 16.81%
# # # # # # """)
# # # # # # st.sidebar.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# # # # # # # 1, 2, 3번 섹션 (이전과 동일, 생략)
# # # # # # if menu == "1. 은행 현황 및 PF 대출 연계 과제":
# # # # # #     st.markdown('<p class="main-header">1. 대명상호저축은행 현황 및 PF 대출 연계 과제</p>', unsafe_allow_html=True)
# # # # # #     st.write("""
# # # # # #     대명상호저축은행은 충북 제천을 기반으로 본점과 충주지점 2개 영업점을 운영하며, 총자산 2,365억 원(2024년 9월말 기준) 규모를 보유하고 있습니다. 
# # # # # #     2024년 3분기 기준 ROA -0.75%, 연체대출비율 10%, PF대출 비중 31.9%로 수익성과 자산 건전성 측면에서 개선의 여지가 있습니다.
# # # # # #     """)
    
# # # # # #     st.markdown('<p class="subsection-header">1.1 저축은행 PF 대출 현황 및 대명과의 연계</p>', unsafe_allow_html=True)
# # # # # #     st.write("""
# # # # # #     저축은행 업계는 부동산 경기 조정과 금리 변동으로 PF 대출 연체율이 상승 중이며, 대명상호저축은행의 PF 대출 비중(31.9%)은 동종업권 평균(15-20%)을 상회합니다.
# # # # # #     연체비율 총합계 23.11%로 선제적 리스크 관리가 필요합니다.
# # # # # #     """)

# # # # # # elif menu == "2. 재무 현황 분석":
# # # # # #     st.markdown('<p class="main-header">2. 재무 현황 분석</p>', unsafe_allow_html=True)
    
# # # # # #     st.markdown('<p class="subsection-header">2.1 주요 재무지표</p>', unsafe_allow_html=True)
# # # # # #     col1, col2 = st.columns(2)
# # # # # #     with col1:
# # # # # #         fig = px.bar(management_metrics[management_metrics['지표'].isin(['BIS 자기자본비율', '총자산순수익률'])],
# # # # # #                      x='지표', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='BIS 자기자본비율 및 ROA 추이', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # #     with col2:
# # # # # #         asset_liability_data = pd.DataFrame({'구분': ['자산', '부채', '자본'], '2023년 3분기': [2575, 2245, 330], '2024년 3분기': [2365, 2078, 287]})
# # # # # #         fig = px.bar(asset_liability_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산/부채/자본 변화 (단위: 억원)', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # #     st.markdown('<p class="subsection-header">2.2 대출 포트폴리오</p>', unsafe_allow_html=True)
# # # # # #     col1, col2 = st.columns(2)
# # # # # #     with col1:
# # # # # #         fig = px.pie(loan_portfolio_data, values='금액(억원)', names='구분', title='용도별 대출 구성 (2024년 3분기)', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # #     with col2:
# # # # # #         fig = px.pie(collateral_data, values='금액(억원)', names='담보유형', title='담보별 대출 구성 (2024년 3분기)', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # #     st.markdown('<p class="subsection-header">2.3 예수금 현황</p>', unsafe_allow_html=True)
# # # # # #     col1, col2 = st.columns(2)
# # # # # #     with col1:
# # # # # #         fig = px.pie(deposit_data, values='금액(억원)', names='구분', title='예수금 구성 (2024년 3분기)', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # #     with col2:
# # # # # #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400, text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"))
# # # # # #         fig.update_traces(marker_color=['rgb(55, 83, 109)', 'rgb(255, 99, 71)'], textposition='auto')
# # # # # #         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
# # # # # #         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
# # # # # #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # #     st.markdown('<p class="subsection-header">2.4 자산 건전성</p>', unsafe_allow_html=True)
# # # # # #     col1, col2 = st.columns(2)
# # # # # #     with col1:
# # # # # #         fig = px.bar(asset_quality_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산건전성 지표 (단위: 억원)', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # #     with col2:
# # # # # #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # #     st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# # # # # # elif menu == "3. 동종업권 비교분석":
# # # # # #     st.markdown('<p class="main-header">3. 동종업권 비교분석</p>', unsafe_allow_html=True)
    
# # # # # #     col1, col2 = st.columns(2)
# # # # # #     with col1:
# # # # # #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='총자산순수익률(ROA) 비교', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # #     with col2:
# # # # # #         fig = px.bar(comparison_data, x='은행명', y=['연체대출비율(%) 2024'], barmode='group', title='연체대출비율 비교 (2024)', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # #     col3, col4 = st.columns(2)
# # # # # #     with col3:
# # # # # #         fig = px.bar(comparison_data, x='은행명', y=['부동산 대출금(%) 2024'], barmode='group', title='부동산 대출금 비율 비교 (2024)', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # #     with col4:
# # # # # #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024', '연체비율 총합계(%) 2024'], barmode='group', title='PF대출 및 연체비율 총합계 비교 (2024)', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # #     col5, col6 = st.columns(2)
# # # # # #     with col5:
# # # # # #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # # #     with col6:
# # # # # #         fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='카드 비교', height=400)
# # # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # # #     st.caption("출처: 사용자 제공 데이터 (2024년 3월 7일 기준)")

# # # # # # # 4. 수익성 강화 전략 (숫자 기반 Recap)
# # # # # # elif menu == "4. 수익성 강화 전략":
# # # # # #     st.markdown('<p class="main-header">4. 수익성 강화 전략</p>', unsafe_allow_html=True)
    
# # # # # #     st.markdown('<p class="subsection-header">4.1 주요 데이터 Recap</p>', unsafe_allow_html=True)
    
# # # # # #     st.markdown('<div class="recap-box">', unsafe_allow_html=True)
# # # # # #     st.markdown('<p class="recap-header">수익성 지표</p>', unsafe_allow_html=True)
# # # # # #     st.write("""
# # # # # #     - ROA: 2023년 -0.13% → 2024년 -0.75% (변화: -0.62%p, 동종업권 평균: -0.22% ~ 1.64%)
# # # # # #     - NIM: 2023년 1.21% → 2024년 1.69% (변화: +0.48%p, 업계 평균 약 3%)
# # # # # #     - CK저축은행 ROA: 4.01% → 1.64% (변화: -2.37%p), 오투저축은행: 1.21% → -1.53% (변화: -2.74%p)
# # # # # #     """)
# # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # #     st.markdown('<div class="recap-box">', unsafe_allow_html=True)
# # # # # #     st.markdown('<p class="recap-header">자산 건전성</p>', unsafe_allow_html=True)
# # # # # #     st.write("""
# # # # # #     - 연체대출비율: 2023년 2.30% → 2024년 10.00% (변화: +7.70%p, 동종업권 평균: 3.61% ~ 12.92%)
# # # # # #     - PF대출 비중: 2024년 31.90% (동종업권 평균: 0% ~ 10.60%)
# # # # # #     - 연체비율 총합계: 2024년 23.11% (동종업권: 3.12% ~ 24.59%)
# # # # # #     - 고정이하분류여신: 2023년 91억 원 → 2024년 271억 원 (변화: +180억 원)
# # # # # #     """)
# # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # #     st.markdown('<div class="recap-box">', unsafe_allow_html=True)
# # # # # #     st.markdown('<p class="recap-header">대출 및 예수금 구조</p>', unsafe_allow_html=True)
# # # # # #     st.write("""
# # # # # #     - 대출금: 2023년 2,078억 원 → 2024년 2,245억 원 (변화: +167억 원)
# # # # # #     - 부동산 담보 대출: 2024년 45.85% (동종업권: 20.24% ~ 73.30%)
# # # # # #     - 예수금: 2023년 2,157억 원 → 2024년 2,008억 원 (변화: -149억 원, -6.9%)
# # # # # #     - 거치식 예금 비중: 2024년 98.21% (1,972억 원)
# # # # # #     """)
# # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # #     st.markdown('<div class="recap-box">', unsafe_allow_html=True)
# # # # # #     st.markdown('<p class="recap-header">자본 및 기타</p>', unsafe_allow_html=True)
# # # # # #     st.write("""
# # # # # #     - BIS 자기자본비율: 2023년 17.86% → 2024년 16.81% (변화: -1.05%p, 동종업권: 10.69% ~ 22.49%)
# # # # # #     - 자본: 2023년 330억 원 → 2024년 287억 원 (변화: -43억 원)
# # # # # #     - 카드 건수: 2023년 0건 → 2024년 0건 (동종업권: 0 ~ 1,547건, 청주 1,547건)
# # # # # #     """)
# # # # # #     st.markdown('</div>', unsafe_allow_html=True)
    
# # # # # #     st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 및 사용자 제공 데이터 (2024년 3월 7일 기준)")

# # # # # import pandas as pd
# # # # # import plotly.express as px
# # # # # import plotly.graph_objects as go
# # # # # import streamlit as st

# # # # # # 페이지 설정
# # # # # st.set_page_config(
# # # # #     page_title="대명상호저축은행 수익성 강화 전략 보고서",
# # # # #     page_icon="💰",
# # # # #     layout="wide",
# # # # #     initial_sidebar_state="expanded"
# # # # # )

# # # # # # 기본 스타일 설정
# # # # # st.markdown("""
# # # # # <style>
# # # # #     .main-header {font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem;}
# # # # #     .section-header {font-size: 1.8rem; font-weight: bold; margin-top: 2rem; margin-bottom: 1rem; color: #1E3A8A;}
# # # # #     .subsection-header {font-size: 1.4rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.8rem; color: #2563EB;}
# # # # #     .caption {font-size: 0.8rem; font-style: italic; color: #6B7280;}
# # # # #     .insight-box {background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #3B82F6;}
# # # # #     .insight-header {font-weight: bold; color: #1E3A8A; margin-bottom: 0.5rem;}
# # # # # </style>
# # # # # """, unsafe_allow_html=True)

# # # # # # 데이터 정의 (이전과 동일)
# # # # # financial_data = pd.DataFrame({
# # # # #     'Year': ['2023년 3분기', '2024년 3분기'],
# # # # #     'Total_Assets': [2575, 2365],
# # # # #     'Loans': [2078, 2245],
# # # # #     'Deposits': [2157, 2008],
# # # # #     'Capital': [330, 287],
# # # # #     'ROA': [-0.13, -0.75],
# # # # #     'NIM': [1.21, 1.69]
# # # # # })

# # # # # loan_portfolio_data = pd.DataFrame({
# # # # #     '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
# # # # #     '금액(억원)': [1015, 689, 91],
# # # # #     '비율(%)': [56.55, 38.38, 5.07]
# # # # # })

# # # # # collateral_data = pd.DataFrame({
# # # # #     '담보유형': ['부동산', '예수금', '기타'],
# # # # #     '금액(억원)': [823, 7, 959],
# # # # #     '비율(%)': [45.85, 0.39, 53.43]
# # # # # })

# # # # # management_metrics = pd.DataFrame({
# # # # #     '지표': ['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율', '순고정이하여신비율', '총자산순수익률'],
# # # # #     '2024년 3분기': [16.81, 12.13, 15.52, 10.46, -0.75],
# # # # #     '2023년 3분기': [17.86, 12.81, 16.61, 3.62, -0.13]
# # # # # })

# # # # # deposit_data = pd.DataFrame({
# # # # #     '구분': ['거치식예금', '적립식예금', '요구불예금'],
# # # # #     '금액(억원)': [1972, 26, 10],
# # # # #     '비율(%)': [98.21, 1.29, 0.5]
# # # # # })

# # # # # deposit_trend = pd.DataFrame({
# # # # #     '구분': ['2023년 3분기', '2024년 3분기'],
# # # # #     '예수금(억원)': [2157, 2008]
# # # # # })

# # # # # asset_quality_data = pd.DataFrame({
# # # # #     '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
# # # # #     '2023년 3분기': [91, 3, 60],
# # # # #     '2024년 3분기': [271, 29, 125],
# # # # # })

# # # # # delinquency_data = pd.DataFrame({
# # # # #     '구분': ['연체대출비율', '순고정이하여신비율'],
# # # # #     '2023년 3분기': [2.30, 3.62],
# # # # #     '2024년 3분기': [10.00, 10.46]
# # # # # })

# # # # # comparison_data = pd.DataFrame({
# # # # #     '은행명': ['대명', 'CK', '오투', '청주', '한성'],
# # # # #     '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '충북 - 청주, 천안', '충남 - 대전, 청주, 옥천'],
# # # # #     'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
# # # # #     'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
# # # # #     'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
# # # # #     'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
# # # # #     '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
# # # # #     '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
# # # # #     'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
# # # # #     '연체비율 총합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70],
# # # # #     '카드(2024)': [0, 17, 6, 1547, 0],
# # # # #     '카드(2023)': [0, 0, 4, 11178, 0]
# # # # # })

# # # # # # 사이드바 메뉴 (이전과 동일, 생략)
# # # # # st.sidebar.title("대명상호저축은행")
# # # # # st.sidebar.subheader("수익성 강화 전략 보고서")
# # # # # menu = st.sidebar.radio("목차", [
# # # # #     "1. 은행 현황 및 PF 대출 연계 과제",
# # # # #     "2. 재무 현황 분석",
# # # # #     "3. 동종업권 비교분석",
# # # # #     "4. 수익성 강화 전략"
# # # # # ])

# # # # # st.sidebar.divider()
# # # # # st.sidebar.info("""
# # # # # **2024년 9월말 주요 지표**
# # # # # - 총자산: 2,365억 원
# # # # # - 대출금: 2,245억 원
# # # # # - 예수금: 2,008억 원
# # # # # - BIS 자기자본비율: 16.81%
# # # # # """)
# # # # # st.sidebar.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# # # # # # 1, 2, 3번 섹션 (이전과 동일, 생략)
# # # # # if menu == "1. 은행 현황 및 PF 대출 연계 과제":
# # # # #     st.markdown('<p class="main-header">1. 대명상호저축은행 현황 및 PF 대출 연계 과제</p>', unsafe_allow_html=True)
# # # # #     st.write("""
# # # # #     대명상호저축은행은 충북 제천을 기반으로 본점과 충주지점 2개 영업점을 운영하며, 총자산 2,365억 원(2024년 9월말 기준) 규모를 보유하고 있습니다. 
# # # # #     2024년 3분기 기준 ROA -0.75%, 연체대출비율 10%, PF대출 비중 31.9%로 수익성과 자산 건전성 측면에서 개선의 여지가 있습니다.
# # # # #     """)
    
# # # # #     st.markdown('<p class="subsection-header">1.1 저축은행 PF 대출 현황 및 대명과의 연계</p>', unsafe_allow_html=True)
# # # # #     st.write("""
# # # # #     저축은행 업계는 부동산 경기 조정과 금리 변동으로 PF 대출 연체율이 상승 중이며, 대명상호저축은행의 PF 대출 비중(31.9%)은 동종업권 평균(15-20%)을 상회합니다.
# # # # #     연체비율 총합계 23.11%로 선제적 리스크 관리가 필요합니다.
# # # # #     """)

# # # # # elif menu == "2. 재무 현황 분석":
# # # # #     st.markdown('<p class="main-header">2. 재무 현황 분석</p>', unsafe_allow_html=True)
    
# # # # #     st.markdown('<p class="subsection-header">2.1 주요 재무지표</p>', unsafe_allow_html=True)
# # # # #     col1, col2 = st.columns(2)
# # # # #     with col1:
# # # # #         fig = px.bar(management_metrics[management_metrics['지표'].isin(['BIS 자기자본비율', '총자산순수익률'])],
# # # # #                      x='지표', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='BIS 자기자본비율 및 ROA 추이', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # #     with col2:
# # # # #         asset_liability_data = pd.DataFrame({'구분': ['자산', '부채', '자본'], '2023년 3분기': [2575, 2245, 330], '2024년 3분기': [2365, 2078, 287]})
# # # # #         fig = px.bar(asset_liability_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산/부채/자본 변화 (단위: 억원)', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # #     st.markdown('<p class="subsection-header">2.2 대출 포트폴리오</p>', unsafe_allow_html=True)
# # # # #     col1, col2 = st.columns(2)
# # # # #     with col1:
# # # # #         fig = px.pie(loan_portfolio_data, values='금액(억원)', names='구분', title='용도별 대출 구성 (2024년 3분기)', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # #     with col2:
# # # # #         fig = px.pie(collateral_data, values='금액(억원)', names='담보유형', title='담보별 대출 구성 (2024년 3분기)', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # #     st.markdown('<p class="subsection-header">2.3 예수금 현황</p>', unsafe_allow_html=True)
# # # # #     col1, col2 = st.columns(2)
# # # # #     with col1:
# # # # #         fig = px.pie(deposit_data, values='금액(억원)', names='구분', title='예수금 구성 (2024년 3분기)', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # #     with col2:
# # # # #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400, text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"))
# # # # #         fig.update_traces(marker_color=['rgb(55, 83, 109)', 'rgb(255, 99, 71)'], textposition='auto')
# # # # #         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
# # # # #         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
# # # # #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # #     st.markdown('<p class="subsection-header">2.4 자산 건전성</p>', unsafe_allow_html=True)
# # # # #     col1, col2 = st.columns(2)
# # # # #     with col1:
# # # # #         fig = px.bar(asset_quality_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산건전성 지표 (단위: 억원)', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # #     with col2:
# # # # #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # #     st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료")

# # # # # elif menu == "3. 동종업권 비교분석":
# # # # #     st.markdown('<p class="main-header">3. 동종업권 비교분석</p>', unsafe_allow_html=True)
    
# # # # #     col1, col2 = st.columns(2)
# # # # #     with col1:
# # # # #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='총자산순수익률(ROA) 비교', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # #     with col2:
# # # # #         fig = px.bar(comparison_data, x='은행명', y=['연체대출비율(%) 2024'], barmode='group', title='연체대출비율 비교 (2024)', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # #     col3, col4 = st.columns(2)
# # # # #     with col3:
# # # # #         fig = px.bar(comparison_data, x='은행명', y=['부동산 대출금(%) 2024'], barmode='group', title='부동산 대출금 비율 비교 (2024)', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # #     with col4:
# # # # #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024', '연체비율 총합계(%) 2024'], barmode='group', title='PF대출 및 연체비율 총합계 비교 (2024)', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # #     col5, col6 = st.columns(2)
# # # # #     with col5:
# # # # #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
# # # # #     with col6:
# # # # #         fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='카드 비교', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # #     st.caption("출처: 사용자 제공 데이터 (2024년 3월 7일 기준)")

# # # # # # 4. 수익성 강화 전략 (주요 지표별 인사이트와 도표)
# # # # # elif menu == "4. 수익성 강화 전략":
# # # # #     st.markdown('<p class="main-header">4. 수익성 강화 전략</p>', unsafe_allow_html=True)
    
# # # # #     st.markdown('<p class="subsection-header">4.1 주요 지표 분석</p>', unsafe_allow_html=True)
    
# # # # #     col1, col2 = st.columns(2)
# # # # #     with col1:
# # # # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # # #         st.markdown('<p class="insight-header">ROA (총자산순수익률)</p>', unsafe_allow_html=True)
# # # # #         st.write("""
# # # # #         - 2023년 -0.13% → 2024년 -0.75% (변화: -0.62%p)
# # # # #         - 자산 대비 수익성을 나타내며, 은행의 전반적인 경영 효율성을 보여줍니다.
# # # # #         - 권역 평균(-0.22% ~ 1.64%) 대비 하락폭이 크며, CK(1.64%)나 청주(-0.22%)와 비교해 수익성 악화가 두드러집니다.
# # # # #         """)
# # # # #         st.markdown('</div>', unsafe_allow_html=True)
# # # # #     with col2:
# # # # #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='ROA 비교', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
    
    
# # # # #     col1, col2 = st.columns(2)
# # # # #     with col1:
# # # # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # # #         st.markdown('<p class="insight-header">연체대출비율</p>', unsafe_allow_html=True)
# # # # #         st.write("""
# # # # #         - 2023년 2.30% → 2024년 10.00% (변화: +7.70%p)
# # # # #         - 대출 자산의 건전성을 나타내며, 리스크 관리 수준을 반영합니다.
# # # # #         - 비교군 (3.61% ~ 12.92%) 중 높은 편에 속하며, PF대출 비중(31.90%)과 연계된 자산 질 하락이 주요 원인으로 보입니다.
# # # # #         """)
# # # # #         st.markdown('</div>', unsafe_allow_html=True)
# # # # #     with col2:
# # # # #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # #     col1, col2 = st.columns(2)
# # # # #     with col1:
# # # # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # # #         st.markdown('<p class="insight-header">PF대출 비중</p>', unsafe_allow_html=True)
# # # # #         st.write("""
# # # # #         - 2024년 31.90% (동종업권: 0% ~ 10.60%)
# # # # #         - 부동산 프로젝트 파이낸싱 의존도를 보여주며, 연체율(23.11%)과 직결됩니다.
# # # # #         - CK(0%)나 청주(7.38%) 대비 월등히 높아, 연체비율 총합계(23.11%) 상승의 주요 요인으로 나타납니다.
# # # # #         """)
# # # # #         st.markdown('</div>', unsafe_allow_html=True)
# # # # #     with col2:
# # # # #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024'], title='PF대출 비중 비교 (2024)', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # #     col1, col2 = st.columns(2)
# # # # #     with col1:
# # # # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # # #         st.markdown('<p class="insight-header">예수금</p>', unsafe_allow_html=True)
# # # # #         st.write("""
# # # # #         - 2023년 2,157억 원 → 2024년 2,008억 원 (변화: -149억 원, -6.9%)
# # # # #         - 자금 조달의 안정성을 나타내며, NIM과 수익성에 영향을 미칩니다.
# # # # #         - 거치식 예금 비중(98.21%)이 높아 조달 구조의 유연성이 낮고, 감소폭(-6.9%)이 수익성에 부담을 줄 수 있습니다.
# # # # #         """)
# # # # #         st.markdown('</div>', unsafe_allow_html=True)
# # # # #     with col2:
# # # # #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400, text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"))
# # # # #         fig.update_traces(marker_color=['rgb(55, 83, 109)', 'rgb(255, 99, 71)'], textposition='auto')
# # # # #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # #     col1, col2 = st.columns(2)
# # # # #     with col1:
# # # # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # # #         st.markdown('<p class="insight-header">BIS 자기자본비율</p>', unsafe_allow_html=True)
# # # # #         st.write("""
# # # # #         - 2023년 17.86% → 2024년 16.81% (변화: -1.05%p)
# # # # #         - 자본 건전성을 나타내며, 리스크 대응 능력을 보여줍니다.
# # # # #         - 비교군(10.69% ~ 22.49%) 내 중간 수준이나, 자본 감소(-43억 원)와 함께 하락해 안정성에 주의가 필요합니다.
# # # # #         """)
# # # # #         st.markdown('</div>', unsafe_allow_html=True)
# # # # #     with col2:
# # # # #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400)
# # # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # # #     st.caption("출처: 대명상호저축은행 제28기 3분기 경영공시자료 및 사용자 제공 데이터 (2024년 3월 7일 기준)")

# # # # import pandas as pd
# # # # import plotly.express as px
# # # # import plotly.graph_objects as go
# # # # import streamlit as st

# # # # # 페이지 설정
# # # # st.set_page_config(
# # # #     page_title="대명상호저축은행 수익성 강화 전략 보고서",
# # # #     page_icon="💰",
# # # #     layout="wide",
# # # #     initial_sidebar_state="expanded"
# # # # )

# # # # # 기본 스타일 설정
# # # # st.markdown("""
# # # # <style>
# # # #     .main-header {font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem;}
# # # #     .section-header {font-size: 1.8rem; font-weight: bold; margin-top: 2rem; margin-bottom: 1rem; color: #1E3A8A;}
# # # #     .subsection-header {font-size: 1.4rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.8rem; color: #2563EB;}
# # # #     .caption {font-size: 0.8rem; font-style: italic; color: #6B7280;}
# # # #     .insight-box {background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #3B82F6;}
# # # #     .insight-header {font-weight: bold; color: #1E3A8A; margin-bottom: 0.5rem;}
# # # # </style>
# # # # """, unsafe_allow_html=True)

# # # # # 데이터 정의
# # # # financial_data = pd.DataFrame({
# # # #     'Year': ['2023년 3분기', '2024년 3분기'],
# # # #     'Total_Assets': [2575, 2365],
# # # #     'Loans': [2078, 2245],
# # # #     'Deposits': [2157, 2008],
# # # #     'Capital': [330, 287],
# # # #     'ROA': [-0.13, -0.75],
# # # #     'NIM': [1.21, 1.69]
# # # # })

# # # # loan_portfolio_data = pd.DataFrame({
# # # #     '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
# # # #     '금액(억원)': [1015, 689, 91],
# # # #     '비율(%)': [56.55, 38.38, 5.07]
# # # # })

# # # # collateral_data = pd.DataFrame({
# # # #     '담보유형': ['부동산', '예수금', '기타'],
# # # #     '금액(억원)': [823, 7, 959],
# # # #     '비율(%)': [45.85, 0.39, 53.43]
# # # # })

# # # # management_metrics = pd.DataFrame({
# # # #     '지표': ['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율', '순고정이하여신비율', '총자산순수익률'],
# # # #     '2024년 3분기': [16.81, 12.13, 15.52, 10.46, -0.75],
# # # #     '2023년 3분기': [17.86, 12.81, 16.61, 3.62, -0.13]
# # # # })

# # # # deposit_data = pd.DataFrame({
# # # #     '구분': ['거치식예금', '적립식예금', '요구불예금'],
# # # #     '금액(억원)': [1972, 26, 10],
# # # #     '비율(%)': [98.21, 1.29, 0.5]
# # # # })

# # # # deposit_trend = pd.DataFrame({
# # # #     '구분': ['2023년 3분기', '2024년 3분기'],
# # # #     '예수금(억원)': [2157, 2008]
# # # # })

# # # # asset_quality_data = pd.DataFrame({
# # # #     '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
# # # #     '2023년 3분기': [91, 3, 60],
# # # #     '2024년 3분기': [271, 29, 125],
# # # # })

# # # # delinquency_data = pd.DataFrame({
# # # #     '구분': ['연체대출비율', '순고정이하여신비율'],
# # # #     '2023년 3분기': [2.30, 3.62],
# # # #     '2024년 3분기': [10.00, 10.46]
# # # # })

# # # # comparison_data = pd.DataFrame({
# # # #     '은행명': ['대명', 'CK', '오투', '청주', '한성'],
# # # #     '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '충북 - 청주, 천안', '충남 - 대전, 청주, 옥천'],
# # # #     'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
# # # #     'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
# # # #     'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
# # # #     'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
# # # #     '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
# # # #     '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
# # # #     'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
# # # #     '연체비율 총합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70],
# # # #     '카드(2024)': [0, 17, 6, 1547, 0],
# # # #     '카드(2023)': [0, 0, 4, 11178, 0]
# # # # })

# # # # # 색상 테마 정의
# # # # COLOR_2023 = '#1E3A8A'  # 진한 파란색 (2023년 데이터)
# # # # COLOR_2024 = '#2563EB'  # 밝은 파란색 (2024년 데이터)
# # # # COLOR_PIE = ['#1E3A8A', '#2563EB', '#3B82F6']  # 파이 차트 색상

# # # # # 사이드바 메뉴
# # # # st.sidebar.title("대명상호저축은행")
# # # # st.sidebar.subheader("수익성 강화 전략 보고서")
# # # # menu = st.sidebar.radio("목차", [
# # # #     "1. 은행 현황 및 PF 대출 연계 과제",
# # # #     "2. 재무 현황 분석",
# # # #     "3. 동종업권 비교분석",
# # # #     "4. 수익성 강화 전략"
# # # # ])

# # # # st.sidebar.divider()
# # # # st.sidebar.info("""
# # # # **2024년 9월말 주요 지표**
# # # # - 총자산: 2,365억 원
# # # # - 대출금: 2,245억 원
# # # # - 예수금: 2,008억 원
# # # # - BIS 자기자본비율: 16.81%
# # # # """)
# # # # st.sidebar.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # # # # 1. 은행 현황 및 PF 대출 연계 과제
# # # # if menu == "1. 은행 현황 및 PF 대출 연계 과제":
# # # #     st.markdown('<p class="main-header">1. 대명상호저축은행 현황 및 PF 대출 연계 과제</p>', unsafe_allow_html=True)
# # # #     st.write("""
# # # #     대명상호저축은행은 충북 제천을 기반으로 본점과 충주지점 2개 영업점을 운영하며, 총자산 2,365억 원(2024년 9월말 기준) 규모를 보유하고 있습니다. 
# # # #     2024년 3분기 기준 ROA -0.75%, 연체대출비율 10%, PF대출 비중 31.9%로 수익성과 자산 건전성 측면에서 개선의 여지가 있습니다.
# # # #     """)
    
# # # #     st.markdown('<p class="subsection-header">1.1 저축은행 PF 대출 현황 및 대명과의 연계</p>', unsafe_allow_html=True)
# # # #     st.write("""
# # # #     저축은행 업계는 부동산 경기 조정과 금리 변동으로 PF 대출 연체율이 상승 중이며, 대명상호저축은행의 PF 대출 비중(31.9%)은 동종업권 평균(15-20%)을 상회합니다.
# # # #     연체비율 총합계 23.11%로 선제적 리스크 관리가 필요합니다.
# # # #     """)

# # # # # 2. 재무 현황 분석
# # # # elif menu == "2. 재무 현황 분석":
# # # #     st.markdown('<p class="main-header">2. 재무 현황 분석</p>', unsafe_allow_html=True)
    
# # # #     st.markdown('<p class="subsection-header">2.1 주요 재무지표</p>', unsafe_allow_html=True)
# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         fig = px.bar(management_metrics[management_metrics['지표'].isin(['BIS 자기자본비율', '총자산순수익률'])],
# # # #                      x='지표', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='BIS 자기자본비율 및 ROA 추이', height=400,
# # # #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# # # #         st.plotly_chart(fig, use_container_width=True)
# # # #     with col2:
# # # #         asset_liability_data = pd.DataFrame({'구분': ['자산', '부채', '자본'], '2023년 3분기': [2575, 2245, 330], '2024년 3분기': [2365, 2078, 287]})
# # # #         fig = px.bar(asset_liability_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산/부채/자본 변화 (단위: 억원)', height=400,
# # # #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # #     st.markdown('<p class="subsection-header">2.2 대출 포트폴리오</p>', unsafe_allow_html=True)
# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         fig = px.pie(loan_portfolio_data, values='금액(억원)', names='구분', title='용도별 대출 구성 (2024년 3분기)', height=400,
# # # #                      color_discrete_sequence=COLOR_PIE)
# # # #         st.plotly_chart(fig, use_container_width=True)
# # # #     with col2:
# # # #         fig = px.pie(collateral_data, values='금액(억원)', names='담보유형', title='담보별 대출 구성 (2024년 3분기)', height=400,
# # # #                      color_discrete_sequence=COLOR_PIE)
# # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # #     st.markdown('<p class="subsection-header">2.3 예수금 현황</p>', unsafe_allow_html=True)
# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         fig = px.pie(deposit_data, values='금액(억원)', names='구분', title='예수금 구성 (2024년 3분기)', height=400,
# # # #                      color_discrete_sequence=COLOR_PIE)
# # # #         st.plotly_chart(fig, use_container_width=True)
# # # #     with col2:
# # # #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400,
# # # #                      text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"),
# # # #                      color_discrete_sequence=[COLOR_2023, COLOR_2024])
# # # #         fig.update_traces(textposition='auto')
# # # #         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
# # # #         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
# # # #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # #     st.markdown('<p class="subsection-header">2.4 자산 건전성</p>', unsafe_allow_html=True)
# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         fig = px.bar(asset_quality_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산건전성 지표 (단위: 억원)', height=400,
# # # #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# # # #         st.plotly_chart(fig, use_container_width=True)
# # # #     with col2:
# # # #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400,
# # # #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# # # #         st.plotly_chart(fig, use_container_width=True)
# # # #     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # # # # 3. 동종업권 비교분석
# # # # elif menu == "3. 동종업권 비교분석":
# # # #     st.markdown('<p class="main-header">3. 동종업권 비교분석</p>', unsafe_allow_html=True)
    
# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='총자산순수익률(ROA) 비교', height=400,
# # # #                      color_discrete_map={'ROA(%) 2023': COLOR_2023, 'ROA(%) 2024': COLOR_2024})
# # # #         st.plotly_chart(fig, use_container_width=True)
# # # #     with col2:
# # # #         fig = px.bar(comparison_data, x='은행명', y=['연체대출비율(%) 2024'], barmode='group', title='연체대출비율 비교 (2024)', height=400,
# # # #                      color_discrete_sequence=[COLOR_2024])
# # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # #     col3, col4 = st.columns(2)
# # # #     with col3:
# # # #         fig = px.bar(comparison_data, x='은행명', y=['부동산 대출금(%) 2024'], barmode='group', title='부동산 대출금 비율 비교 (2024)', height=400,
# # # #                      color_discrete_sequence=[COLOR_2024])
# # # #         st.plotly_chart(fig, use_container_width=True)
# # # #     with col4:
# # # #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024', '연체비율 총합계(%) 2024'], barmode='group', title='PF대출 및 연체비율 총합계 비교 (2024)', height=400,
# # # #                      color_discrete_map={'PF대출(%) 2024': COLOR_2023, '연체비율 총합계(%) 2024': COLOR_2024})
# # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # #     col5, col6 = st.columns(2)
# # # #     with col5:
# # # #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400,
# # # #                      color_discrete_map={'BIS 자기자본비율(%) 2023': COLOR_2023, 'BIS 자기자본비율(%) 2024': COLOR_2024})
# # # #         st.plotly_chart(fig, use_container_width=True)
# # # #     with col6:
# # # #         fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='카드 비교', height=400,
# # # #                      color_discrete_map={'카드(2023)': COLOR_2023, '카드(2024)': COLOR_2024})
# # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # #     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # # # # 4. 수익성 강화 전략
# # # # elif menu == "4. 수익성 강화 전략":
# # # #     st.markdown('<p class="main-header">4. 수익성 강화 전략</p>', unsafe_allow_html=True)
    
# # # #     st.markdown('<p class="subsection-header">4.1 주요 지표 분석</p>', unsafe_allow_html=True)
    
# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # #         st.markdown('<p class="insight-header">ROA (총자산순수익률)</p>', unsafe_allow_html=True)
# # # #         st.write("""
# # # #         - 2023년 -0.13% → 2024년 -0.75% (변화: -0.62%p)
# # # #         - 자산 대비 수익성을 나타내며, 은행의 전반적인 경영 효율성을 보여줍니다.
# # # #         - 권역 평균(-0.22% ~ 1.64%) 대비 하락폭이 크며, CK(1.64%)나 청주(-0.22%)와 비교해 수익성 악화가 두드러집니다.
# # # #         """)
# # # #         st.markdown('</div>', unsafe_allow_html=True)
# # # #     with col2:
# # # #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='ROA 비교', height=400,
# # # #                      color_discrete_map={'ROA(%) 2023': COLOR_2023, 'ROA(%) 2024': COLOR_2024})
# # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # #         st.markdown('<p class="insight-header">연체대출비율</p>', unsafe_allow_html=True)
# # # #         st.write("""
# # # #         - 2023년 2.30% → 2024년 10.00% (변화: +7.70%p)
# # # #         - 대출 자산의 건전성을 나타내며, 리스크 관리 수준을 반영합니다.
# # # #         - 비교군 (3.61% ~ 12.92%) 중 높은 편에 속하며, PF대출 비중(31.90%)과 연계된 자산 질 하락이 주요 원인으로 보입니다.
# # # #         """)
# # # #         st.markdown('</div>', unsafe_allow_html=True)
# # # #     with col2:
# # # #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400,
# # # #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # #         st.markdown('<p class="insight-header">PF대출 비중</p>', unsafe_allow_html=True)
# # # #         st.write("""
# # # #         - 2024년 31.90% (동종업권: 0% ~ 10.60%)
# # # #         - 부동산 프로젝트 파이낸싱 의존도를 보여주며, 연체율(23.11%)과 직결됩니다.
# # # #         - CK(0%)나 청주(7.38%) 대비 월등히 높아, 연체비율 총합계(23.11%) 상승의 주요 요인으로 나타납니다.
# # # #         """)
# # # #         st.markdown('</div>', unsafe_allow_html=True)
# # # #     with col2:
# # # #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024'], title='PF대출 비중 비교 (2024)', height=400,
# # # #                      color_discrete_sequence=[COLOR_2024])
# # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # #         st.markdown('<p class="insight-header">예수금</p>', unsafe_allow_html=True)
# # # #         st.write("""
# # # #         - 2023년 2,157억 원 → 2024년 2,008억 원 (변화: -149억 원, -6.9%)
# # # #         - 자금 조달의 안정성을 나타내며, NIM과 수익성에 영향을 미칩니다.
# # # #         - 거치식 예금 비중(98.21%)이 높아 조달 구조의 유연성이 낮고, 감소폭(-6.9%)이 수익성에 부담을 줄 수 있습니다.
# # # #         """)
# # # #         st.markdown('</div>', unsafe_allow_html=True)
# # # #     with col2:
# # # #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400,
# # # #                      text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"),
# # # #                      color_discrete_sequence=[COLOR_2023, COLOR_2024])
# # # #         fig.update_traces(textposition='auto')
# # # #         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
# # # #         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
# # # #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # #     col1, col2 = st.columns(2)
# # # #     with col1:
# # # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # # #         st.markdown('<p class="insight-header">BIS 자기자본비율</p>', unsafe_allow_html=True)
# # # #         st.write("""
# # # #         - 2023년 17.86% → 2024년 16.81% (변화: -1.05%p)
# # # #         - 자본 건전성을 나타내며, 리스크 대응 능력을 보여줍니다.
# # # #         - 비교군(10.69% ~ 22.49%) 내 중간 수준이나, 자본 감소(-43억 원)와 함께 하락해 안정성에 주의가 필요합니다.
# # # #         """)
# # # #         st.markdown('</div>', unsafe_allow_html=True)
# # # #     with col2:
# # # #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400,
# # # #                      color_discrete_map={'BIS 자기자본비율(%) 2023': COLOR_2023, 'BIS 자기자본비율(%) 2024': COLOR_2024})
# # # #         st.plotly_chart(fig, use_container_width=True)
    
# # # #     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # # import pandas as pd
# # # import plotly.express as px
# # # import plotly.graph_objects as go
# # # import streamlit as st

# # # # 페이지 설정
# # # st.set_page_config(
# # #     page_title="대명상호저축은행 수익성 강화 전략 보고서",
# # #     page_icon="💰",
# # #     layout="wide",
# # #     initial_sidebar_state="expanded"
# # # )

# # # # 기본 스타일 설정
# # # st.markdown("""
# # # <style>
# # #     .main-header {font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem;}
# # #     .section-header {font-size: 1.8rem; font-weight: bold; margin-top: 2rem; margin-bottom: 1rem; color: #1E3A8A;}
# # #     .subsection-header {font-size: 1.4rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.8rem; color: #2563EB;}
# # #     .caption {font-size: 0.8rem; font-style: italic; color: #6B7280;}
# # #     .insight-box {background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #3B82F6;}
# # #     .insight-header {font-weight: bold; color: #1E3A8A; margin-bottom: 0.5rem;}
# # # </style>
# # # """, unsafe_allow_html=True)

# # # # 데이터 정의
# # # financial_data = pd.DataFrame({
# # #     'Year': ['2023년 3분기', '2024년 3분기'],
# # #     'Total_Assets': [2575, 2365],
# # #     'Loans': [2078, 2245],
# # #     'Deposits': [2157, 2008],
# # #     'Capital': [330, 287],
# # #     'ROA': [-0.13, -0.75],
# # #     'NIM': [1.21, 1.69]
# # # })

# # # loan_portfolio_data = pd.DataFrame({
# # #     '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
# # #     '금액(억원)': [1015, 689, 91],
# # #     '비율(%)': [56.55, 38.38, 5.07]
# # # })

# # # collateral_data = pd.DataFrame({
# # #     '담보유형': ['부동산', '예수금', '기타'],
# # #     '금액(억원)': [823, 7, 959],
# # #     '비율(%)': [45.85, 0.39, 53.43]
# # # })

# # # management_metrics = pd.DataFrame({
# # #     '지표': ['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율', '순고정이하여신비율', '총자산순수익률'],
# # #     '2024년 3분기': [16.81, 12.13, 15.52, 10.46, -0.75],
# # #     '2023년 3분기': [17.86, 12.81, 16.61, 3.62, -0.13]
# # # })

# # # deposit_data = pd.DataFrame({
# # #     '구분': ['거치식예금', '적립식예금', '요구불예금'],
# # #     '금액(억원)': [1972, 26, 10],
# # #     '비율(%)': [98.21, 1.29, 0.5]
# # # })

# # # deposit_trend = pd.DataFrame({
# # #     '구분': ['2023년 3분기', '2024년 3분기'],
# # #     '예수금(억원)': [2157, 2008]
# # # })

# # # asset_quality_data = pd.DataFrame({
# # #     '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
# # #     '2023년 3분기': [91, 3, 60],
# # #     '2024년 3분기': [271, 29, 125],
# # # })

# # # delinquency_data = pd.DataFrame({
# # #     '구분': ['연체대출비율', '순고정이하여신비율'],
# # #     '2023년 3분기': [2.30, 3.62],
# # #     '2024년 3분기': [10.00, 10.46]
# # # })

# # # comparison_data = pd.DataFrame({
# # #     '은행명': ['대명', 'CK', '오투', '청주', '한성'],
# # #     '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '충북 - 청주, 천안', '충남 - 대전, 청주, 옥천'],
# # #     'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
# # #     'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
# # #     'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
# # #     'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
# # #     '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
# # #     '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
# # #     'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
# # #     '연체비율 총합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70],
# # #     '카드(2024)': [0, 17, 6, 1547, 0],
# # #     '카드(2023)': [0, 0, 4, 11178, 0]
# # # })

# # # # 색상 테마 정의
# # # COLOR_2023 = '#1E3A8A'  # 진한 파란색 (2023년 데이터)
# # # COLOR_2024 = '#2563EB'  # 밝은 파란색 (2024년 데이터)
# # # COLOR_PIE = ['#1E3A8A', '#2563EB', '#3B82F6']  # 파이 차트 색상

# # # # 사이드바 메뉴
# # # st.sidebar.title("대명상호저축은행")
# # # st.sidebar.subheader("수익성 강화 전략 보고서")
# # # menu = st.sidebar.radio("목차", [
# # #     "재무 현황 분석",
# # #     "동종업권 비교분석",
# # #     "수익성 강화 전략"
# # # ])

# # # st.sidebar.divider()
# # # st.sidebar.info("""
# # # **2024년 9월말 주요 지표**
# # # - 총자산: 2,365억 원
# # # - 대출금: 2,245억 원
# # # - 예수금: 2,008억 원
# # # - BIS 자기자본비율: 16.81%
# # # """)
# # # st.sidebar.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # # # 재무 현황 분석
# # # if menu == "재무 현황 분석":
# # #     st.markdown('<p class="main-header">재무 현황 분석</p>', unsafe_allow_html=True)
    
# # #     st.markdown('<p class="subsection-header">주요 재무지표</p>', unsafe_allow_html=True)
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         fig = px.bar(management_metrics[management_metrics['지표'].isin(['BIS 자기자본비율', '총자산순수익률'])],
# # #                      x='지표', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='BIS 자기자본비율 및 ROA 추이', height=400,
# # #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# # #         st.plotly_chart(fig, use_container_width=True)
# # #     with col2:
# # #         asset_liability_data = pd.DataFrame({'구분': ['자산', '부채', '자본'], '2023년 3분기': [2575, 2245, 330], '2024년 3분기': [2365, 2078, 287]})
# # #         fig = px.bar(asset_liability_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산/부채/자본 변화 (단위: 억원)', height=400,
# # #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# # #         st.plotly_chart(fig, use_container_width=True)
    
# # #     st.markdown('<p class="subsection-header">대출 포트폴리오</p>', unsafe_allow_html=True)
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         fig = px.pie(loan_portfolio_data, values='금액(억원)', names='구분', title='용도별 대출 구성 (2024년 3분기)', height=400,
# # #                      color_discrete_sequence=COLOR_PIE)
# # #         st.plotly_chart(fig, use_container_width=True)
# # #     with col2:
# # #         fig = px.pie(collateral_data, values='금액(억원)', names='담보유형', title='담보별 대출 구성 (2024년 3분기)', height=400,
# # #                      color_discrete_sequence=COLOR_PIE)
# # #         st.plotly_chart(fig, use_container_width=True)
    
# # #     st.markdown('<p class="subsection-header">예수금 현황</p>', unsafe_allow_html=True)
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         fig = px.pie(deposit_data, values='금액(억원)', names='구분', title='예수금 구성 (2024년 3분기)', height=400,
# # #                      color_discrete_sequence=COLOR_PIE)
# # #         st.plotly_chart(fig, use_container_width=True)
# # #     with col2:
# # #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400,
# # #                      text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"),
# # #                      color_discrete_sequence=[COLOR_2023, COLOR_2024])
# # #         fig.update_traces(textposition='auto')
# # #         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
# # #         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
# # #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# # #         st.plotly_chart(fig, use_container_width=True)
    
# # #     st.markdown('<p class="subsection-header">자산 건전성</p>', unsafe_allow_html=True)
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         fig = px.bar(asset_quality_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산건전성 지표 (단위: 억원)', height=400,
# # #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# # #         st.plotly_chart(fig, use_container_width=True)
# # #     with col2:
# # #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400,
# # #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# # #         st.plotly_chart(fig, use_container_width=True)
# # #     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # # # 동종업권 비교분석
# # # elif menu == "동종업권 비교분석":
# # #     st.markdown('<p class="main-header">동종업권 비교분석</p>', unsafe_allow_html=True)
    
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='총자산순수익률(ROA) 비교', height=400,
# # #                      color_discrete_map={'ROA(%) 2023': COLOR_2023, 'ROA(%) 2024': COLOR_2024})
# # #         st.plotly_chart(fig, use_container_width=True)
# # #     with col2:
# # #         fig = px.bar(comparison_data, x='은행명', y=['연체대출비율(%) 2024'], barmode='group', title='연체대출비율 비교 (2024)', height=400,
# # #                      color_discrete_sequence=[COLOR_2024])
# # #         st.plotly_chart(fig, use_container_width=True)
    
# # #     col3, col4 = st.columns(2)
# # #     with col3:
# # #         fig = px.bar(comparison_data, x='은행명', y=['부동산 대출금(%) 2024'], barmode='group', title='부동산 대출금 비율 비교 (2024)', height=400,
# # #                      color_discrete_sequence=[COLOR_2024])
# # #         st.plotly_chart(fig, use_container_width=True)
# # #     with col4:
# # #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024', '연체비율 총합계(%) 2024'], barmode='group', title='PF대출 및 연체비율 총합계 비교 (2024)', height=400,
# # #                      color_discrete_map={'PF대출(%) 2024': COLOR_2023, '연체비율 총합계(%) 2024': COLOR_2024})
# # #         st.plotly_chart(fig, use_container_width=True)
    
# # #     col5, col6 = st.columns(2)
# # #     with col5:
# # #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400,
# # #                      color_discrete_map={'BIS 자기자본비율(%) 2023': COLOR_2023, 'BIS 자기자본비율(%) 2024': COLOR_2024})
# # #         st.plotly_chart(fig, use_container_width=True)
# # #     with col6:
# # #         fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='카드 비교', height=400,
# # #                      color_discrete_map={'카드(2023)': COLOR_2023, '카드(2024)': COLOR_2024})
# # #         st.plotly_chart(fig, use_container_width=True)
    
# # #     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # # # 수익성 강화 전략
# # # elif menu == "수익성 강화 전략":
# # #     st.markdown('<p class="main-header">수익성 강화 전략</p>', unsafe_allow_html=True)
    
# # #     st.markdown('<p class="subsection-header">주요 지표 분석</p>', unsafe_allow_html=True)
    
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # #         st.markdown('<p class="insight-header">ROA (총자산순수익률)</p>', unsafe_allow_html=True)
# # #         st.write("""
# # #         - 2023년 -0.13% → 2024년 -0.75% (변화: -0.62%p)
# # #         - 자산 대비 수익성을 나타내며, 은행의 전반적인 경영 효율성을 보여줍니다.
# # #         - 권역 평균(-0.22% ~ 1.64%) 대비 하락폭이 크며, CK(1.64%)나 청주(-0.22%)와 비교해 수익성 악화가 두드러집니다.
# # #         """)
# # #         st.markdown('</div>', unsafe_allow_html=True)
# # #     with col2:
# # #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='ROA 비교', height=400,
# # #                      color_discrete_map={'ROA(%) 2023': COLOR_2023, 'ROA(%) 2024': COLOR_2024})
# # #         st.plotly_chart(fig, use_container_width=True)
    
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # #         st.markdown('<p class="insight-header">연체대출비율</p>', unsafe_allow_html=True)
# # #         st.write("""
# # #         - 2023년 2.30% → 2024년 10.00% (변화: +7.70%p)
# # #         - 대출 자산의 건전성을 나타내며, 리스크 관리 수준을 반영합니다.
# # #         - 비교군 (3.61% ~ 12.92%) 중 높은 편에 속하며, PF대출 비중(31.90%)과 연계된 자산 질 하락이 주요 원인으로 보입니다.
# # #         """)
# # #         st.markdown('</div>', unsafe_allow_html=True)
# # #     with col2:
# # #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400,
# # #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# # #         st.plotly_chart(fig, use_container_width=True)
    
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # #         st.markdown('<p class="insight-header">PF대출 비중</p>', unsafe_allow_html=True)
# # #         st.write("""
# # #         - 2024년 31.90% (동종업권: 0% ~ 10.60%)
# # #         - 부동산 프로젝트 파이낸싱 의존도를 보여주며, 연체율(23.11%)과 직결됩니다.
# # #         - CK(0%)나 청주(7.38%) 대비 월등히 높아, 연체비율 총합계(23.11%) 상승의 주요 요인으로 나타납니다.
# # #         """)
# # #         st.markdown('</div>', unsafe_allow_html=True)
# # #     with col2:
# # #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024'], title='PF대출 비중 비교 (2024)', height=400,
# # #                      color_discrete_sequence=[COLOR_2024])
# # #         st.plotly_chart(fig, use_container_width=True)
    
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # #         st.markdown('<p class="insight-header">예수금</p>', unsafe_allow_html=True)
# # #         st.write("""
# # #         - 2023년 2,157억 원 → 2024년 2,008억 원 (변화: -149억 원, -6.9%)
# # #         - 자금 조달의 안정성을 나타내며, NIM과 수익성에 영향을 미칩니다.
# # #         - 거치식 예금 비중(98.21%)이 높아 조달 구조의 유연성이 낮고, 감소폭(-6.9%)이 수익성에 부담을 줄 수 있습니다.
# # #         """)
# # #         st.markdown('</div>', unsafe_allow_html=True)
# # #     with col2:
# # #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400,
# # #                      text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"),
# # #                      color_discrete_sequence=[COLOR_2023, COLOR_2024])
# # #         fig.update_traces(textposition='auto')
# # #         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
# # #         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
# # #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# # #         st.plotly_chart(fig, use_container_width=True)
    
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# # #         st.markdown('<p class="insight-header">BIS 자기자본비율</p>', unsafe_allow_html=True)
# # #         st.write("""
# # #         - 2023년 17.86% → 2024년 16.81% (변화: -1.05%p)
# # #         - 자본 건전성을 나타내며, 리스크 대응 능력을 보여줍니다.
# # #         - 비교군(10.69% ~ 22.49%) 내 중간 수준이나, 자본 감소(-43억 원)와 함께 하락해 안정성에 주의가 필요합니다.
# # #         """)
# # #         st.markdown('</div>', unsafe_allow_html=True)
# # #     with col2:
# # #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400,
# # #                      color_discrete_map={'BIS 자기자본비율(%) 2023': COLOR_2023, 'BIS 자기자본비율(%) 2024': COLOR_2024})
# # #         st.plotly_chart(fig, use_container_width=True)
    
# # #     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # import pandas as pd
# # import plotly.express as px
# # import plotly.graph_objects as go
# # import streamlit as st

# # # 페이지 설정
# # st.set_page_config(
# #     page_title="대명상호저축은행 수익성 강화 전략 보고서",
# #     page_icon="💰",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # 기본 스타일 설정
# # st.markdown("""
# # <style>
# #     .main-header {font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem;}
# #     .section-header {font-size: 1.8rem; font-weight: bold; margin-top: 2rem; margin-bottom: 1rem; color: #1E3A8A;}
# #     .subsection-header {font-size: 1.4rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.8rem; color: #2563EB;}
# #     .caption {font-size: 0.8rem; font-style: italic; color: #6B7280;}
# #     .insight-box {background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #3B82F6;}
# #     .insight-header {font-weight: bold; color: #1E3A8A; margin-bottom: 0.5rem;}
# #     .suggestion-box {background-color: #ECFDF5; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #10B981;}
# #     .suggestion-header {font-weight: bold; color: #065F46; margin-bottom: 0.5rem;}
# # </style>
# # """, unsafe_allow_html=True)

# # # 데이터 정의
# # financial_data = pd.DataFrame({
# #     'Year': ['2023년 3분기', '2024년 3분기'],
# #     'Total_Assets': [2575, 2365],
# #     'Loans': [2078, 2245],
# #     'Deposits': [2157, 2008],
# #     'Capital': [330, 287],
# #     'ROA': [-0.13, -0.75],
# #     'NIM': [1.21, 1.69]
# # })

# # loan_portfolio_data = pd.DataFrame({
# #     '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
# #     '금액(억원)': [1015, 689, 91],
# #     '비율(%)': [56.55, 38.38, 5.07]
# # })

# # collateral_data = pd.DataFrame({
# #     '담보유형': ['부동산', '예수금', '기타'],
# #     '금액(억원)': [823, 7, 959],
# #     '비율(%)': [45.85, 0.39, 53.43]
# # })

# # management_metrics = pd.DataFrame({
# #     '지표': ['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율', '순고정이하여신비율', '총자산순수익률'],
# #     '2024년 3분기': [16.81, 12.13, 15.52, 10.46, -0.75],
# #     '2023년 3분기': [17.86, 12.81, 16.61, 3.62, -0.13]
# # })

# # deposit_data = pd.DataFrame({
# #     '구분': ['거치식예금', '적립식예금', '요구불예금'],
# #     '금액(억원)': [1972, 26, 10],
# #     '비율(%)': [98.21, 1.29, 0.5]
# # })

# # deposit_trend = pd.DataFrame({
# #     '구분': ['2023년 3분기', '2024년 3분기'],
# #     '예수금(억원)': [2157, 2008]
# # })

# # asset_quality_data = pd.DataFrame({
# #     '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
# #     '2023년 3분기': [91, 3, 60],
# #     '2024년 3분기': [271, 29, 125],
# # })

# # delinquency_data = pd.DataFrame({
# #     '구분': ['연체대출비율', '순고정이하여신비율'],
# #     '2023년 3분기': [2.30, 3.62],
# #     '2024년 3분기': [10.00, 10.46]
# # })

# # comparison_data = pd.DataFrame({
# #     '은행명': ['대명', 'CK', '오투', '청주', '한성'],
# #     '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '충북 - 청주, 천안', '충남 - 대전, 청주, 옥천'],
# #     'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
# #     'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
# #     'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
# #     'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
# #     '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
# #     '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
# #     'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
# #     '연체비율 총합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70],
# #     '카드(2024)': [0, 17, 6, 1547, 0],
# #     '카드(2023)': [0, 0, 4, 11178, 0]
# # })

# # # 색상 테마 정의
# # COLOR_2023 = '#1E3A8A'  # 진한 파란색 (2023년 데이터)
# # COLOR_2024 = '#2563EB'  # 밝은 파란색 (2024년 데이터)
# # COLOR_PIE = ['#1E3A8A', '#2563EB', '#3B82F6']  # 파이 차트 색상

# # # 사이드바 메뉴
# # st.sidebar.title("대명상호저축은행")
# # st.sidebar.subheader("수익성 강화 전략 보고서")
# # menu = st.sidebar.radio("목차", [
# #     "현황 분석",
# #     "비교 분석",
# #     "제안"
# # ])

# # st.sidebar.divider()
# # st.sidebar.info("""
# # **2024년 9월말 주요 지표**
# # - 총자산: 2,365억 원
# # - 대출금: 2,245억 원
# # - 예수금: 2,008억 원
# # - BIS 자기자본비율: 16.81%
# # """)
# # st.sidebar.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # # 현황 분석
# # if menu == "현황 분석":
# #     st.markdown('<p class="main-header">현황 분석</p>', unsafe_allow_html=True)
    
# #     st.markdown('<p class="subsection-header">주요 재무지표</p>', unsafe_allow_html=True)
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         fig = px.bar(management_metrics[management_metrics['지표'].isin(['BIS 자기자본비율', '총자산순수익률'])],
# #                      x='지표', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='BIS 자기자본비율 및 ROA 추이', height=400,
# #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# #         st.plotly_chart(fig, use_container_width=True)
# #     with col2:
# #         asset_liability_data = pd.DataFrame({'구분': ['자산', '부채', '자본'], '2023년 3분기': [2575, 2245, 330], '2024년 3분기': [2365, 2078, 287]})
# #         fig = px.bar(asset_liability_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산/부채/자본 변화 (단위: 억원)', height=400,
# #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     st.markdown('<p class="subsection-header">대출 포트폴리오</p>', unsafe_allow_html=True)
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         fig = px.pie(loan_portfolio_data, values='금액(억원)', names='구분', title='용도별 대출 구성 (2024년 3분기)', height=400,
# #                      color_discrete_sequence=COLOR_PIE)
# #         st.plotly_chart(fig, use_container_width=True)
# #     with col2:
# #         fig = px.pie(collateral_data, values='금액(억원)', names='담보유형', title='담보별 대출 구성 (2024년 3분기)', height=400,
# #                      color_discrete_sequence=COLOR_PIE)
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     st.markdown('<p class="subsection-header">예수금 현황</p>', unsafe_allow_html=True)
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         fig = px.pie(deposit_data, values='금액(억원)', names='구분', title='예수금 구성 (2024년 3분기)', height=400,
# #                      color_discrete_sequence=COLOR_PIE)
# #         st.plotly_chart(fig, use_container_width=True)
# #     with col2:
# #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400,
# #                      text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"),
# #                      color_discrete_sequence=[COLOR_2023, COLOR_2024])
# #         fig.update_traces(textposition='auto')
# #         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
# #         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
# #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     st.markdown('<p class="subsection-header">자산 건전성</p>', unsafe_allow_html=True)
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         fig = px.bar(asset_quality_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산건전성 지표 (단위: 억원)', height=400,
# #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# #         st.plotly_chart(fig, use_container_width=True)
# #     with col2:
# #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400,
# #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# #         st.plotly_chart(fig, use_container_width=True)
# #     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # # 비교 분석
# # elif menu == "비교 분석":
# #     st.markdown('<p class="main-header">비교 분석</p>', unsafe_allow_html=True)
    
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='총자산순수익률(ROA) 비교', height=400,
# #                      color_discrete_map={'ROA(%) 2023': COLOR_2023, 'ROA(%) 2024': COLOR_2024})
# #         st.plotly_chart(fig, use_container_width=True)
# #     with col2:
# #         fig = px.bar(comparison_data, x='은행명', y=['연체대출비율(%) 2024'], barmode='group', title='연체대출비율 비교 (2024)', height=400,
# #                      color_discrete_sequence=[COLOR_2024])
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     col3, col4 = st.columns(2)
# #     with col3:
# #         fig = px.bar(comparison_data, x='은행명', y=['부동산 대출금(%) 2024'], barmode='group', title='부동산 대출금 비율 비교 (2024)', height=400,
# #                      color_discrete_sequence=[COLOR_2024])
# #         st.plotly_chart(fig, use_container_width=True)
# #     with col4:
# #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024', '연체비율 총합계(%) 2024'], barmode='group', title='PF대출 및 연체비율 총합계 비교 (2024)', height=400,
# #                      color_discrete_map={'PF대출(%) 2024': COLOR_2023, '연체비율 총합계(%) 2024': COLOR_2024})
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     col5, col6 = st.columns(2)
# #     with col5:
# #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400,
# #                      color_discrete_map={'BIS 자기자본비율(%) 2023': COLOR_2023, 'BIS 자기자본비율(%) 2024': COLOR_2024})
# #         st.plotly_chart(fig, use_container_width=True)
# #     with col6:
# #         fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='카드 비교', height=400,
# #                      color_discrete_map={'카드(2023)': COLOR_2023, '카드(2024)': COLOR_2024})
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # # 제안
# # elif menu == "제안":
# #     st.markdown('<p class="main-header">제안</p>', unsafe_allow_html=True)
    
# #     st.markdown('<p class="subsection-header">주요 지표 분석 및 개선 방향</p>', unsafe_allow_html=True)
    
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# #         st.markdown('<p class="insight-header">ROA (총자산순수익률)</p>', unsafe_allow_html=True)
# #         st.write("""
# #         - 2023년 -0.13% → 2024년 -0.75% (변화: -0.62%p)
# #         - 자산 대비 수익성을 나타내며, 은행의 전반적인 경영 효율성을 보여줍니다.
# #         - 권역 평균(-0.22% ~ 1.64%) 대비 하락폭이 크며, CK(1.64%)나 청주(-0.22%)와 비교해 수익성 악화가 두드러집니다.
# #         """)
# #         st.markdown('</div>', unsafe_allow_html=True)
# #     with col2:
# #         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='ROA 비교', height=400,
# #                      color_discrete_map={'ROA(%) 2023': COLOR_2023, 'ROA(%) 2024': COLOR_2024})
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# #         st.markdown('<p class="insight-header">연체대출비율</p>', unsafe_allow_html=True)
# #         st.write("""
# #         - 2023년 2.30% → 2024년 10.00% (변화: +7.70%p)
# #         - 대출 자산의 건전성을 나타내며, 리스크 관리 수준을 반영합니다.
# #         - 비교군 (3.61% ~ 12.92%) 중 높은 편에 속하며, PF대출 비중(31.90%)과 연계된 자산 질 하락이 주요 원인으로 보입니다.
# #         """)
# #         st.markdown('</div>', unsafe_allow_html=True)
# #     with col2:
# #         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400,
# #                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# #         st.markdown('<p class="insight-header">PF대출 비중</p>', unsafe_allow_html=True)
# #         st.write("""
# #         - 2024년 31.90% (동종업권: 0% ~ 10.60%)
# #         - 부동산 프로젝트 파이낸싱 의존도를 보여주며, 연체율(23.11%)과 직결됩니다.
# #         - CK(0%)나 청주(7.38%) 대비 월등히 높아, 연체비율 총합계(23.11%) 상승의 주요 요인으로 나타납니다.
# #         """)
# #         st.markdown('</div>', unsafe_allow_html=True)
# #     with col2:
# #         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024'], title='PF대출 비중 비교 (2024)', height=400,
# #                      color_discrete_sequence=[COLOR_2024])
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         st.markdown('<div class="insight-box">', unsafe_allow_html=True)
# #         st.markdown('<p class="insight-header">예수금</p>', unsafe_allow_html=True)
# #         st.write("""
# #         - 2023년 2,157억 원 → 2024년 2,008억 원 (변화: -149억 원, -6.9%)
# #         - 자금 조달의 안정성을 나타내며, NIM과 수익성에 영향을 미칩니다.
# #         - 거치식 예금 비중(98.21%)이 높아 조달 구조의 유연성이 낮고, 감소폭(-6.9%)이 수익성에 부담을 줄 수 있습니다.
# #         """)
# #         st.markdown('</div>', unsafe_allow_html=True)
# #     with col2:
# #         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400,
# #                      text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"),
# #                      color_discrete_sequence=[COLOR_2023, COLOR_2024])
# #         fig.update_traces(textposition='auto')
# #         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
# #         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
# #         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         st.markdown('<div class="suggestion-box">', unsafe_allow_html=True)
# #         st.markdown('<p class="suggestion-header">신입사원 제안</p>', unsafe_allow_html=True)
# #         st.write("""
# #         - 음... 선배님들, 제가 조심스럽게 제안드려볼게요. PF대출 비중(31.90%)이 동종업권 대비 높고 연체율(23.11%)도 큰 상황이라, 혹시 PF대출을 조금 줄이고 안정적인 가계자금대출이나 기업자금대출로 포트폴리오를 다각화하면 어떨까요?
# #         - 또 예수금이 줄어드는 부분(-6.9%)을 보면, 요구불예금(0.5%) 비중을 살짝 늘려서 유연성을 키우는 것도 괜찮을 것 같아요. 의견 부탁드립니다!
# #         """)
# #         st.markdown('</div>', unsafe_allow_html=True)
# #     with col2:
# #         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400,
# #                      color_discrete_map={'BIS 자기자본비율(%) 2023': COLOR_2023, 'BIS 자기자본비율(%) 2024': COLOR_2024})
# #         st.plotly_chart(fig, use_container_width=True)
    
# #     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# import streamlit as st

# # 페이지 설정
# st.set_page_config(
#     page_title="대명상호저축은행 수익성 강화 전략 보고서",
#     page_icon="💰",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # 기본 스타일 설정
# st.markdown("""
# <style>
#     .main-header {font-size: 2.5rem; font-weight: bold; margin-bottom: 1.5rem;}
#     .section-header {font-size: 1.8rem; font-weight: bold; margin-top: 2rem; margin-bottom: 1rem; color: #1E3A8A;}
#     .subsection-header {font-size: 1.4rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.8rem; color: #2563EB;}
#     .caption {font-size: 0.8rem; font-style: italic; color: #6B7280;}
#     .insight-box {background-color: #F3F4F6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #3B82F6;}
#     .insight-header {font-weight: bold; color: #1E3A8A; margin-bottom: 0.5rem;}
#     .suggestion-box {background-color: #ECFDF5; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; border-left: 4px solid #10B981;}
#     .suggestion-header {font-weight: bold; color: #065F46; margin-bottom: 0.5rem;}
# </style>
# """, unsafe_allow_html=True)

# # 데이터 정의
# financial_data = pd.DataFrame({
#     'Year': ['2023년 3분기', '2024년 3분기'],
#     'Total_Assets': [2575, 2365],
#     'Loans': [2078, 2245],
#     'Deposits': [2157, 2008],
#     'Capital': [330, 287],
#     'ROA': [-0.13, -0.75],
#     'NIM': [1.21, 1.69]
# })

# loan_portfolio_data = pd.DataFrame({
#     '구분': ['기업자금대출', '가계자금대출', '공공 및 기타자금 대출'],
#     '금액(억원)': [1015, 689, 91],
#     '비율(%)': [56.55, 38.38, 5.07]
# })

# collateral_data = pd.DataFrame({
#     '담보유형': ['부동산', '예수금', '기타'],
#     '금액(억원)': [823, 7, 959],
#     '비율(%)': [45.85, 0.39, 53.43]
# })

# management_metrics = pd.DataFrame({
#     '지표': ['BIS 자기자본비율', '단순자기자본비율', 'BIS 기준기본자본비율', '순고정이하여신비율', '총자산순수익률'],
#     '2024년 3분기': [16.81, 12.13, 15.52, 10.46, -0.75],
#     '2023년 3분기': [17.86, 12.81, 16.61, 3.62, -0.13]
# })

# deposit_data = pd.DataFrame({
#     '구분': ['거치식예금', '적립식예금', '요구불예금'],
#     '금액(억원)': [1972, 26, 10],
#     '비율(%)': [98.21, 1.29, 0.5]
# })

# deposit_trend = pd.DataFrame({
#     '구분': ['2023년 3분기', '2024년 3분기'],
#     '예수금(억원)': [2157, 2008]
# })

# asset_quality_data = pd.DataFrame({
#     '구분': ['고정이하분류여신', '부실여신', '대손충당금'],
#     '2023년 3분기': [91, 3, 60],
#     '2024년 3분기': [271, 29, 125],
# })

# delinquency_data = pd.DataFrame({
#     '구분': ['연체대출비율', '순고정이하여신비율'],
#     '2023년 3분기': [2.30, 3.62],
#     '2024년 3분기': [10.00, 10.46]
# })

# comparison_data = pd.DataFrame({
#     '은행명': ['대명', 'CK', '오투', '청주', '한성'],
#     '권역': ['충북 - 제천, 충주', '강원도 - 강릉, 춘천', '충청남도 - 대전, 천안', '충북 - 청주, 천안', '충남 - 대전, 청주, 옥천'],
#     'ROA(%) 2024': [-0.75, 1.64, -1.53, -0.22, -0.24],
#     'ROA(%) 2023': [-0.13, 4.01, 1.21, 0.77, 0.10],
#     'BIS 자기자본비율(%) 2024': [16.81, 10.69, 13.22, 17.49, 22.49],
#     'BIS 자기자본비율(%) 2023': [17.86, 9.76, 14.56, 16.41, 22.07],
#     '연체대출비율(%) 2024': [10.00, 3.61, 12.92, 8.54, 8.80],
#     '부동산 대출금(%) 2024': [45.85, 43.35, 73.30, 20.24, 50.90],
#     'PF대출(%) 2024': [31.90, 0.00, 10.46, 7.38, 10.60],
#     '연체비율 총합계(%) 2024': [23.11, 3.12, 24.59, 12.32, 16.70],
#     '카드(2024)': [0, 17, 6, 1547, 0],
#     '카드(2023)': [0, 0, 4, 11178, 0]
# })

# # 색상 테마 정의
# COLOR_2023 = '#1E3A8A'  # 진한 파란색 (2023년 데이터)
# COLOR_2024 = '#2563EB'  # 밝은 파란색 (2024년 데이터)
# COLOR_PIE = ['#1E3A8A', '#2563EB', '#3B82F6']  # 파이 차트 색상

# # 사이드바 메뉴
# st.sidebar.title("대명상호저축은행")
# st.sidebar.subheader("수익성 강화 전략 보고서")
# menu = st.sidebar.radio("목차", [
#     "현황 분석",
#     "비교 분석",
#     "제안"
# ])

# st.sidebar.divider()
# st.sidebar.info("""
# **2024년 9월말 주요 지표**
# - 총자산: 2,365억 원
# - 대출금: 2,245억 원
# - 예수금: 2,008억 원
# - BIS 자기자본비율: 16.81%
# """)
# st.sidebar.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # 현황 분석
# if menu == "현황 분석":
#     st.markdown('<p class="main-header">현황 분석</p>', unsafe_allow_html=True)
    
#     st.markdown('<p class="subsection-header">주요 재무지표</p>', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         fig = px.bar(management_metrics[management_metrics['지표'].isin(['BIS 자기자본비율', '총자산순수익률'])],
#                      x='지표', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='BIS 자기자본비율 및 ROA 추이', height=400,
#                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
#         st.plotly_chart(fig, use_container_width=True)
#     with col2:
#         asset_liability_data = pd.DataFrame({'구분': ['자산', '부채', '자본'], '2023년 3분기': [2575, 2245, 330], '2024년 3분기': [2365, 2078, 287]})
#         fig = px.bar(asset_liability_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산/부채/자본 변화 (단위: 억원)', height=400,
#                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
#         st.plotly_chart(fig, use_container_width=True)
    
#     st.markdown('<p class="subsection-header">대출 포트폴리오</p>', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         fig = px.pie(loan_portfolio_data, values='금액(억원)', names='구분', title='용도별 대출 구성 (2024년 3분기)', height=400,
#                      color_discrete_sequence=COLOR_PIE)
#         st.plotly_chart(fig, use_container_width=True)
#     with col2:
#         fig = px.pie(collateral_data, values='금액(억원)', names='담보유형', title='담보별 대출 구성 (2024년 3분기)', height=400,
#                      color_discrete_sequence=COLOR_PIE)
#         st.plotly_chart(fig, use_container_width=True)
    
#     st.markdown('<p class="subsection-header">예수금 현황</p>', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         fig = px.pie(deposit_data, values='금액(억원)', names='구분', title='예수금 구성 (2024년 3분기)', height=400,
#                      color_discrete_sequence=COLOR_PIE)
#         st.plotly_chart(fig, use_container_width=True)
#     with col2:
#         fig = px.bar(deposit_trend, x='구분', y='예수금(억원)', title='예수금 추이 (단위: 억원)', height=400,
#                      text=deposit_trend['예수금(억원)'].apply(lambda x: f"{x:,}"),
#                      color_discrete_sequence=[COLOR_2023, COLOR_2024])
#         fig.update_traces(textposition='auto')
#         percent_change = ((deposit_trend['예수금(억원)'][1] - deposit_trend['예수금(억원)'][0]) / deposit_trend['예수금(억원)'][0]) * 100
#         fig.add_annotation(x='2024년 3분기', y=deposit_trend['예수금(억원)'][1], text=f"변화율: {percent_change:.1f}%", showarrow=True, yshift=20, font=dict(color="red"))
#         fig.update_layout(yaxis_range=[1900, 2200], showlegend=False)
#         st.plotly_chart(fig, use_container_width=True)
    
#     st.markdown('<p class="subsection-header">자산 건전성</p>', unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         fig = px.bar(asset_quality_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='자산건전성 지표 (단위: 억원)', height=400,
#                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
#         st.plotly_chart(fig, use_container_width=True)
#     with col2:
#         fig = px.bar(delinquency_data, x='구분', y=['2023년 3분기', '2024년 3분기'], barmode='group', title='연체율 추이 (%)', height=400,
#                      color_discrete_map={'2023년 3분기': COLOR_2023, '2024년 3분기': COLOR_2024})
#         st.plotly_chart(fig, use_container_width=True)
#     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # 비교 분석
# elif menu == "비교 분석":
#     st.markdown('<p class="main-header">비교 분석</p>', unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
#     with col1:
#         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='총자산순수익률(ROA) 비교', height=400,
#                      color_discrete_map={'ROA(%) 2023': COLOR_2023, 'ROA(%) 2024': COLOR_2024})
#         st.plotly_chart(fig, use_container_width=True)
#     with col2:
#         fig = px.bar(comparison_data, x='은행명', y=['연체대출비율(%) 2024'], barmode='group', title='연체대출비율 비교 (2024)', height=400,
#                      color_discrete_sequence=[COLOR_2024])
#         st.plotly_chart(fig, use_container_width=True)
    
#     col3, col4 = st.columns(2)
#     with col3:
#         fig = px.bar(comparison_data, x='은행명', y=['부동산 대출금(%) 2024'], barmode='group', title='부동산 대출금 비율 비교 (2024)', height=400,
#                      color_discrete_sequence=[COLOR_2024])
#         st.plotly_chart(fig, use_container_width=True)
#     with col4:
#         fig = px.bar(comparison_data, x='은행명', y=['PF대출(%) 2024', '연체비율 총합계(%) 2024'], barmode='group', title='PF대출 및 연체비율 총합계 비교 (2024)', height=400,
#                      color_discrete_map={'PF대출(%) 2024': COLOR_2023, '연체비율 총합계(%) 2024': COLOR_2024})
#         st.plotly_chart(fig, use_container_width=True)
    
#     col5, col6 = st.columns(2)
#     with col5:
#         fig = px.bar(comparison_data, x='은행명', y=['BIS 자기자본비율(%) 2024', 'BIS 자기자본비율(%) 2023'], barmode='group', title='BIS 자기자본비율 비교', height=400,
#                      color_discrete_map={'BIS 자기자본비율(%) 2023': COLOR_2023, 'BIS 자기자본비율(%) 2024': COLOR_2024})
#         st.plotly_chart(fig, use_container_width=True)
#     with col6:
#         fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='카드 비교', height=400,
#                      color_discrete_map={'카드(2023)': COLOR_2023, '카드(2024)': COLOR_2024})
#         st.plotly_chart(fig, use_container_width=True)
    
#     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

# # 제안
# elif menu == "제안":
#     st.markdown('<p class="main-header">제안</p>', unsafe_allow_html=True)
    
#     st.markdown('<p class="subsection-header">대명상호저축은행의 지속 가능한 성장 전략</p>', unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown('<div class="suggestion-box">', unsafe_allow_html=True)
#         st.markdown('<p class="suggestion-header">신입사원 제안: 체크카드 활성화를 통한 지역 기반 강화</p>', unsafe_allow_html=True)
#         st.write("""
#         - 음... 선배님들, 조심스럽게 제안드려볼게요. 충청권 저축은행들의 경영공시를 보면, 대명상호저축은행과 경쟁사들 모두 체크카드 발급과 활용에 적극적이지 않은 상황이에요. 예를 들어, 대명은 2024년 카드 발급 건수가 0건이고, CK와 오투도 각각 17건, 6건에 불과하죠.
#         - 이 기회를 살려서, 대명에서 체크카드 서비스를 활성화하면 어떨까요? 대규모 광고가 제한된 환경에서도 고객들이 지역 내 가맹점에서 결제할 때마다 자연스럽게 저축은행의 인지도를 높일 수 있을 것 같아요.
#         - 특판을 통한 모객 대신, 초기에는 이율 경쟁보다 지역 내 차별화된 고객 경험을 제공하는 상품 개발에 집중하면 충성도 높은 고객 기반을 다질 수 있을 거예요. 온라인 금융상품 비교 사이트가 많아진 요즘, 특판은 운용 규모가 큰 금융기관에 더 적합한 전략 같아서요.
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
#     with col2:
#         fig = px.bar(comparison_data, x='은행명', y=['카드(2024)', '카드(2023)'], barmode='group', title='체크카드 발급 건수 비교', height=400,
#                      color_discrete_map={'카드(2023)': COLOR_2023, '카드(2024)': COLOR_2024})
#         st.plotly_chart(fig, use_container_width=True)
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown('<div class="suggestion-box">', unsafe_allow_html=True)
#         st.markdown('<p class="suggestion-header">지역 기반 전략과 단계적 확장</p>', unsafe_allow_html=True)
#         st.write("""
#         - 지역 기반을 다진 후에는, 상호저축은행법상 영업구역 내 개인 및 중소기업 대출 비율 요건을 철저히 고려하면서 수익성과 건전성에 기여할 수 있을 것 같아요. 지역별 산업 특성과 위험 요인을 분석해서 균형 잡힌 포트폴리오를 구성하는 데 힘쓰겠습니다.
#         - 탄탄한 기반이 마련되면, 강원도나 충청북도처럼 저축은행 밀집도가 낮은 지역(50만 명당 1개사 수준)으로 점진적으로 확장하면 어떨까요? 동시에 온라인 채널을 활용해 매력적인 상품을 제공하면 물리적 한계를 넘어 영업점을 확장하는 데도 도움이 될 거예요.
#         - 이런 단계적인 접근으로, 초기에는 지역 내 충성도를 높이고, 역량이 커진 후에는 더 다양한 영업 전략을 도입해 사세를 키워가면 좋을 것 같습니다. 의견 부탁드려요!
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)
#     with col2:
#         fig = px.bar(comparison_data, x='은행명', y=['ROA(%) 2024', 'ROA(%) 2023'], barmode='group', title='ROA 비교', height=400,
#                      color_discrete_map={'ROA(%) 2023': COLOR_2023, 'ROA(%) 2024': COLOR_2024})
#         st.plotly_chart(fig, use_container_width=True)
    
#     st.caption("출처: 대명상호저축은행 외 4개 저축은행 2024년 3분기 경영공시자료")

