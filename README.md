## 박민성 Minsung Park

UNIST 산업공학과에서 금융공학과 데이터를 공부하고 있습니다.
시장 데이터와 뉴스 같은 텍스트를 함께 보는 문제, 그리고 LLM을 추천과 검색에 붙이는 문제에 관심이 많습니다.

<br>

### Paper

**Comparing the Dot-com Bubble and the Current Semiconductor/AI Bubble: Diagnosing Bubble Stages via LLM Sentiment Analysis and Quantitative Indicators**
<br>박민성, UNIST IE412 Term Project, 2026.06
<br>[PDF](https://github.com/parkminsung45/dotcom-vs-ai-bubble/blob/main/paper/IE412_Report_MinsungPark.pdf) &nbsp;|&nbsp; [Code](https://github.com/parkminsung45/dotcom-vs-ai-bubble)

닷컴버블(1997–2000)과 지금의 반도체·AI 장세(2023–2026)를 같은 잣대로 비교했습니다.
버핏지수, Shiller CAPE, VIX, NASDAQ 네 가지 지표에 Qwen2.5-1.5B로 분류한 뉴스 100건의 감성을 더해 종합 점수를 만들고, 민스키 5단계 모델 위에서 현재 위치를 판단했습니다.
지금 시장은 버핏지수(249% vs 144%)와 뉴스 낙관도에서는 닷컴 정점을 넘었지만 가격 상승폭과 CAPE는 아직 못 미치고, 종합 점수로는 닷컴 정점의 92% 수준인 Euphoria 단계로 봤습니다.

<br>

### Projects

**금융 · 퀀트**

- [**upbit-spread-rl**](https://github.com/parkminsung45/Minsung-Crypto_Currency-Pair-Trading-Investment-Model-)
  <br>업비트 Open API로 페어 스프레드와 호가 스프레드 전략을 PPO로 학습하는 자동매매. [대시보드](https://upbit-spread-rl-dashboard.vercel.app)
- [**AI Investment Journal**](https://github.com/parkminsung45/ai-investment-journal)
  <br>투자 판단 과정을 기록하고 그 안의 편향과 패턴을 분석하는 다이어리 MVP

**LLM · NLP** <sub>멋쟁이사자처럼 AI Plus NLP 5기 팀 프로젝트</sub>

- [**αlpha Pick**](https://github.com/parkminsung45/Alphapick_-LLM-based-purchase-)
  <br>LLM(HCX)으로 검색어를 정제하고 실제 쇼핑몰 순위를 반영해 상품을 추천. Google ADK SequentialAgent 파이프라인
  <br><sub>맡은 일: 파이프라인 구조별 비용·성능 벤치마크, 토큰 사용량 트래킹 버그와 상세검색 facet 오분류 수정, 문서화</sub>
- [**Multimodal RAG**](https://github.com/parkminsung45/multimodality_RAG)
  <br>애널리스트 리포트 PDF를 페이지 유형별로 나눠 YOLOv11n, MinerU, Table Transformer, VLM으로 추출하고 하나의 DB로 합친 RAG
  <br><sub>맡은 일: KOSPI200 종목 스코어링 파이프라인(재무·뉴스·기술적 지표 결합, 최종 리포트 생성), [발표자료](https://www.figma.com/deck/rJKbTwLwK0yrvTLN2Ysl0G/%EB%A9%8B%EC%82%AC-2%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8?node-id=1-341)</sub>
- [**Keyphrase Extraction**](https://github.com/parkminsung45/keyphrase-extraction)
  <br>어휘 불일치 문제를 겨냥해 present/absent 키프레이즈를 함께 생성. TF-IDF, KeyBERT, KeyBART 비교
  <br><sub>맡은 일: Baseline과 Proposed 모델 설계, [발표자료](https://www.figma.com/deck/PnqYsZDIRUekmdCaOqXSyQ/%EB%A9%8B%EC%82%AC-1%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8?node-id=1-97)</sub>

**대회 · 해커톤**

- [**OIBC 2026 Solar Forecast**](https://github.com/parkminsung45/oibc-2026-solar-forecast)
  <br>태양광 발전소를 두 개의 집합자원(VPP)으로 묶고 하루 전 발전량을 예측
- [**GLIP**](https://github.com/parkminsung45/GLIP-Yonsei_Nur-Ulsan_Med-UNIST_Digital_Healthcare_Hackathon)
  <br>GLP-1 약물 사용자를 위한 아바타 기반 셀프케어 서비스 기획. 4th UU Digital Healthcare Hackathon 2026

<br>

### Experience

- **Data Intelligence Lab**, UNIST AIGS &nbsp;<sub>2026.09 – 현재</sub>
  <br>학부연구생. 논문 리뷰와 랩미팅 발표. [기록](https://github.com/parkminsung45/UNIST_Data-Intelligence-Lab-AIGS-)
- **멋쟁이사자처럼 AI Plus NLP 5기** &nbsp;<sub>수료</sub>
  <br>NLP 기초부터 임베딩, RAG, LLM 에이전트까지. 팀 프로젝트 3건
- **Financial Data Science Lab** &nbsp;<sub>2023.03 – 2023.06</sub>
  <br>학부연구생. 금융 시계열 클러스터링, 통계적 차익거래 전략, 백테스팅 파이프라인

<br>

### Education

**UNIST** AI융합대학 산업공학과 학사과정

<br>

### Tools

Python, SQL &nbsp;/&nbsp; pandas, NumPy, scikit-learn, PyTorch, TensorFlow, Hugging Face &nbsp;/&nbsp; Supabase, Streamlit &nbsp;/&nbsp; Tableau &nbsp;/&nbsp; Figma, Illustrator, After Effects, Premiere Pro
