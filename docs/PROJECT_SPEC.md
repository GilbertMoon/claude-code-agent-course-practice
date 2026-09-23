# AX Job Agent Pipeline

## 1. 프로젝트 목적

이 프로젝트는 잡코리아 등 채용정보 사이트에서 아래와 같은 키워드와 관련된 채용 공고를 수집하는 자동화 파이프라인을 만드는 것이 목표입니다.

- AX (AI Transformation)
- AI / 인공지능
- 데이터 분석
- 생성형 AI
- LLM
- Machine Learning
- Data Scientist
- AI Engineer

수집한 공고는 다음 과정을 거칩니다.

- pandas로 정리 및 분석
- 기존에 이미 수집했던 공고와 새로 나온 공고 구분
- 회사별 / 지역별 / 검색어별 기본 통계 계산
- 위 키워드와 관련성이 높은 공고만 추출
- Gemini API로 공고 내용 요약 및 필요 기술 추출
- 한 주간의 동향을 Markdown 보고서로 작성
- Slack 및 Gmail로 보고서 전송
- GitHub Actions를 이용해 주 1회 자동 실행

### 이 프로젝트의 진짜 목적 (교육 목적)

이 프로젝트의 핵심은 **크롤링 자체가 아닙니다.**

핵심은 아래 전체 파이프라인을 처음부터 끝까지 직접 경험하고 이해하는 것입니다.

```
수집 → 정제 → 분석 → AI 해석 → 검증 → 보고 → 자동화
```

각 단계를 건너뛰지 않고, 사람이 눈으로 직접 확인하면서 하나씩 쌓아 올리는 것이 이 프로젝트의 진짜 목표입니다.

## 2. 사용자 수준

- 이 프로젝트의 대상 사용자는 **Python 데이터 분석 초보자**입니다.
- pandas 사용 경험이 거의 없다고 가정하고 진행합니다.
- 한 번에 큰 코드를 작성하지 않고, 작은 단위(STEP)로 나누어 진행합니다.
- 모든 실습은 Jupyter Notebook에서 **셀 단위로** 작성하고 실행하며 검증합니다.
- 코드가 만든 결과는 반드시 **사람이 직접 눈으로 확인**합니다.
- 결과가 이상하거나 예상과 다르면, 원인을 이해하기 전까지 **다음 STEP으로 넘어가지 않습니다.**

## 3. 개발 도구와 역할

| 도구 | 역할 |
|------|------|
| GPT Web / Gemini Web / Claude Web | **Orchestrator.** 전체 계획 수립, 단계 분해, 각 STEP의 완료 조건 작성, Coding Agent에게 전달할 프롬프트 생성을 담당 |
| Claude Code / Codex / Copilot | **Local Coding Agent.** 실제 파일을 읽고, 코드를 작성/수정하고, 명령을 실행하고, 오류를 수정 |
| VS Code | 주 개발 환경 |
| Jupyter Notebook | 셀 단위 실험과 검증 환경 |
| pandas | 계산 가능한 사실(수치, 통계, 판별)을 계산하는 도구 |
| Gemini API | 채용공고 요약, 기술 추출, 직무 분류, 추천 이유 생성 |
| GitHub Actions | main.py를 주기적으로 실행하는 Scheduler |
| Human (사용자) | 실행 결과 검증, 데이터 해석 검증, 다음 단계 진행 승인 |

## 4. 개발 단계 구조 (사람이 코드를 만들어가는 흐름)

```
GPT Web (Orchestrator)
    ↓
Claude Code / Codex / Copilot (Local Coding Agent)
    ↓
VS Code
    ↓
Jupyter Notebook
    ↓
셀 단위 실행
    ↓
결과 확인
    ↓
Markdown 해석
    ↓
다음 STEP
```

## 5. 운영 단계 구조 (완성 후 매주 자동으로 도는 흐름)

```
GitHub Actions
    ↓
main.py
    ↓
Crawler
    ↓
pandas
    ↓
신규 공고 판별
    ↓
관련 공고 필터링
    ↓
Gemini API
    ↓
Markdown Report
    ↓
Slack / Gmail
```

개발 단계(4번)와 운영 단계(5번)는 서로 다른 흐름입니다. 개발 단계는 사람이 한 STEP씩 검증하며 만드는 과정이고, 운영 단계는 완성된 파이프라인이 매주 자동으로 반복 실행되는 과정입니다.

## 6. 최종 예상 폴더 구조

```
chapter11/
└── ax-job-agent/
    ├── docs/
    │   ├── PROJECT_SPEC.md            [완료]
    │   ├── PROGRESS.md                [완료]
    │   └── STEP_BY_STEP_GUIDE.md      [완료]
    │
    ├── notebooks/                     [예정]
    │   └── ax_job_pipeline.ipynb      [예정]
    │
    ├── src/                           [예정]
    │   ├── crawler.py                 [예정]
    │   ├── preprocess.py              [예정]
    │   ├── analyzer.py                [예정]
    │   ├── gemini_client.py           [예정]
    │   ├── reporter.py                [예정]
    │   └── notifier.py                [예정]
    │
    ├── data/                          [예정]
    │   ├── raw/                       [예정]
    │   └── processed/                 [예정]
    │
    ├── reports/                       [예정]
    │
    ├── .env.example                   [예정]
    ├── .gitignore                     [예정]
    ├── requirements.txt                [예정]
    ├── main.py                        [예정]
    └── README.md                      [완료]
```

> 위 구조 중 현재 실제로 존재하는 것은 `docs/`, `README.md`, 그리고 Python 환경(`.venv/`)뿐입니다. 나머지는 모두 앞으로 STEP을 진행하며 만들어질 예정 항목입니다. 실제 존재 여부는 `docs/PROGRESS.md`를 기준으로 확인하세요.

## 7. 데이터 명세

수집 결과는 pandas `DataFrame`으로 관리하며, **DataFrame의 한 행(row)은 채용 공고 한 건**을 의미합니다.

### 초기 컬럼 정의

| 컬럼명 | 설명 |
|--------|------|
| `company_name` | 채용 공고를 올린 회사명 |
| `job_title` | 채용 공고 제목(직무명) |
| `career` | 요구 경력 수준 (예: 신입, 경력 3년 이상, 경력무관 등) |
| `location` | 근무 지역 |
| `posted_date` | 공고 등록일 |
| `closing_date` | 공고 마감일 |
| `job_url` | 공고 상세 페이지 URL. 중복 제거 및 신규 공고 판별의 기준 키로 사용 |
| `search_keyword` | 이 공고를 수집할 때 사용한 검색어 (예: "AI Engineer", "데이터 분석") |
| `collected_at` | 이 공고를 실제로 수집한 시각(타임스탬프) |

이 컬럼 구조는 STEP 03에서 다시 검토하고 확정하며, 필요 시 STEP_BY_STEP_GUIDE.md의 STEP 03 내용에 변경 이력을 기록합니다.

## 8. pandas 역할

아래 작업은 모두 **pandas가 담당**합니다.

- `shape` 확인 (행/열 개수)
- `head()` 확인 (데이터 미리보기)
- 결측값 확인
- 중복 확인 및 제거
- 날짜 컬럼 변환 (문자열 → datetime)
- 여러 검색어로 수집한 결과 통합
- 기존 공고 / 신규 공고 판별
- 기본 통계 계산 (신규 공고 수, 회사별/지역별/경력별/검색어별 집계)
- 관련성 1차 필터링 (키워드 기반)

### 핵심 원칙

> **Python(pandas)이 계산할 수 있는 사실은 반드시 Python으로 계산한다.**

즉, "숫자로 셀 수 있는 것"과 "표로 정리할 수 있는 것"은 절대 Gemini에게 맡기지 않습니다.

## 9. Gemini 역할

Gemini API는 아래 항목만 담당합니다.

- 공고 핵심 내용 요약
- 요구 기술 추출
- 직무 유형 분류
- AX 관련성 설명 (왜 이 공고가 AX/AI 관련성이 높은지 서술)
- 추천 이유 생성

### Gemini가 담당하면 안 되는 항목

- 신규 공고 수
- 회사별 공고 수
- 지역별 공고 수
- 검색어별 공고 수

이런 값은 반드시 pandas에서 계산합니다 (8번 항목 참고). Gemini는 "사실 계산"이 아니라 "언어 이해와 요약"에만 사용합니다.

## 10. 보안 원칙

- `.env` 파일은 절대 Git에 커밋하지 않습니다. (`.gitignore`에 반드시 포함 — STEP 12/17에서 생성 예정)
- 실제 값이 없는 `.env.example` 파일만 저장소에 포함합니다.

### 예정 환경변수

| 변수명 | 용도 |
|--------|------|
| `GEMINI_API_KEY` | Gemini API 인증 키 |
| `SLACK_WEBHOOK_URL` | Slack 메시지 전송용 Webhook URL |
| `GMAIL_USER` | Gmail 발신 계정 |
| `GMAIL_APP_PASSWORD` | Gmail 앱 비밀번호 (일반 로그인 비밀번호 아님) |

GitHub Actions에서 자동 실행할 때는 위 값들을 로컬 `.env` 대신 **GitHub Secrets**에 등록하여 사용합니다.

## 11. 핵심 작업 원칙

1. 한 번에 전체 프로그램을 만들지 않는다.
2. 현재 STEP 하나만 Coding Agent에게 맡긴다.
3. 코드를 작성하면 반드시 직접 실행한다.
4. 실행 결과를 사람이 눈으로 직접 확인한다.
5. 결과를 Markdown Cell에 해석하여 기록한다.
6. 결과가 이상하면 다음 STEP으로 넘어가지 않는다.
7. 계산 가능한 사실(숫자, 통계, 판별)은 pandas가 계산한다.
8. Gemini는 요약과 설명 중심으로만 사용한다.
9. API Key와 비밀번호는 어떤 경우에도 Git에 올리지 않는다.
10. 로컬에서 전체 파이프라인 검증을 마친 후에만 GitHub Actions를 추가한다.

## 12. 관련 문서

- 진행 상태 추적: [`PROGRESS.md`](./PROGRESS.md)
- 전체 실행 가이드: [`STEP_BY_STEP_GUIDE.md`](./STEP_BY_STEP_GUIDE.md)
