# AX Job Agent — Step by Step Guide

이 문서는 아무것도 기억하지 못하는 상태에서도 처음부터 끝까지 이 프로젝트를 따라갈 수 있도록 작성된 전체 실행 가이드입니다.

관련 문서:
- 전체 사양: [`PROJECT_SPEC.md`](./PROJECT_SPEC.md)
- 현재 진행 상태: [`PROGRESS.md`](./PROGRESS.md)

---

# 작업을 다시 시작할 때 가장 먼저 할 것

며칠 또는 몇 주 만에 이 프로젝트로 돌아왔다면, 아래 순서를 **반드시** 그대로 따르세요. 기억에 의존하지 말고 항상 이 순서로 상태를 확인합니다.

1. 프로젝트 폴더로 이동한다.
   ```powershell
   cd C:\dev\claude-code-agent-course-practice
   ```
2. 가상환경을 활성화한다.
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
3. 현재 Git 브랜치를 확인한다. (practice 저장소에서는 `main`이어야 함. 이관 전 원본 저장소에서는 `ax-job-agent` 브랜치를 사용했음)
   ```powershell
   git branch --show-current
   ```
4. `git status`로 작업 중이던 파일이 남아있는지 확인한다.
   ```powershell
   git status
   ```
5. `docs/PROGRESS.md` 파일을 연다.
6. 파일 상단의 **"현재 STEP"** 을 확인한다.
7. **"다음 작업"** 과 **"다음 작업 완료 기준"** 을 확인한다.
8. 해당 STEP **하나만** 진행한다. (여러 STEP을 한 번에 진행하지 않는다)
9. 실행 결과를 사람이 직접 눈으로 확인한다.
10. 작업이 끝나면 `docs/PROGRESS.md`를 최신 상태로 업데이트한다. (아래 "진행 상태 관리 규칙" 참고)

---

# Notebook 운영 규칙

모든 Notebook STEP은 아래 4단계 패턴을 반복합니다.

1. **Markdown Cell** — STEP 제목과 작업 계획
2. **Code Cell** — 실행 코드
3. **Code Cell** — 결과 확인 (필요하면 여러 개)
4. **Markdown Cell** — 실행 결과 해석 (예상과 다른 부분, 다음 단계 진행 가능 여부)

### 예시

```markdown
# STEP 04. 페이지 접근 테스트

## 작업 계획
- 검색어 1개, 페이지 1개로 요청을 보낸다.
- 상태 코드와 응답 길이를 확인한다.
```

```python
# Code Cell: 실행 코드
response = requests.get(url, headers=headers, timeout=10)
print(response.status_code)
```

```python
# Code Cell: 결과 확인
print(response.headers.get("Content-Type"))
print(len(response.text))
```

```markdown
## 실행 결과 해석
- 요청 성공 여부:
- 확인한 데이터:
- 예상과 다른 부분:
- 다음 단계 진행 가능 여부:
- 추가 확인 사항:
```

이 4단계를 건너뛰지 마세요. 특히 마지막 "실행 결과 해석" Markdown Cell은 사람이 직접 채워야 하며, 여기서 이상 징후를 발견하면 다음 STEP으로 넘어가지 않습니다.

---

# 진행 상태 관리 규칙

- STEP을 **시작하기 전**: `docs/PROGRESS.md`의 상태를 `IN_PROGRESS`로 바꾼다.
- STEP을 **완료한 후**: 상태를 `DONE`으로 바꾼다.
- 다음 STEP으로 넘어갈 때: 다음 STEP의 상태를 `IN_PROGRESS` 또는 `NOT_STARTED`로 설정한다.

그리고 매번 아래 항목을 최신 상태로 갱신합니다.

- 마지막 작업일
- 마지막 완료 STEP
- 현재 STEP
- 다음 작업
- 다음 명령
- 완료 기준
- 특이사항

---

# STEP 상세 가이드

## STEP 00. 저장소 준비

### 목표
GitHub 저장소를 로컬로 가져오고, 이 프로젝트 전용 브랜치와 폴더를 준비한다.

### 왜 하는가
모든 작업은 별도 브랜치(`ax-job-agent`)에서 진행해야 `main` 브랜치와 다른 챕터에 영향을 주지 않습니다.

### 시작 전 확인
- Git이 설치되어 있어야 함
- GitHub 저장소 접근 권한이 있어야 함

### 실행 명령
```powershell
git clone https://github.com/GilbertMoon/claude-code-agent-course.git
cd claude-code-agent-course
git pull --ff-only
git checkout -b ax-job-agent
mkdir chapter11\ax-job-agent
```

### 예상 결과
- 로컬에 저장소 폴더가 생성됨
- `git branch --show-current` 실행 시 `ax-job-agent` 출력

### 사람이 확인할 것
- `chapter11/ax-job-agent` 폴더가 실제로 존재하는지

### 완료 조건
`git branch --show-current`가 `ax-job-agent`를 출력하고, `chapter11/ax-job-agent` 폴더가 존재함.

### 실패하면
- clone 실패 → 네트워크/권한 확인
- 브랜치 생성 오류 → 이미 브랜치가 있는지 `git branch -a`로 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 00 → `DONE`

**현재 상태: DONE (확인 완료)**

---

## STEP 01. Python 환경 준비

### 목표
이 프로젝트 전용 Python 가상환경을 만들고 기본 패키지를 설치한다.

### 왜 하는가
다른 프로젝트(chapter01~10, fast-track 등)의 패키지 버전과 충돌하지 않도록, 이 프로젝트만의 독립된 Python 환경이 필요합니다.

### 시작 전 확인
- STEP 00 완료 (프로젝트 폴더 존재)
- Python 3.12가 시스템에 설치되어 있어야 함

### 실행 명령
```powershell
cd C:\dev\claude-code-agent-course-practice
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
where.exe python
python -m pip install --upgrade pip
pip install pandas requests beautifulsoup4 jupyter python-dotenv
```

> (2026-09-23 저장소 이관 이후 경로. 이관 전에는 `C:\dev\claude-code-agent-course\chapter11\ax-job-agent`였습니다. 이관 후 `.venv`는 practice 저장소에 다시 생성해야 합니다.)

### 예상 결과
- `python --version` → `Python 3.12.10`
- `where.exe python` → `.venv\Scripts\python.exe` 경로가 최상단에 표시
- pip 설치 로그에 5개 패키지(및 의존성) 설치 완료 메시지

### 사람이 확인할 것
- 프롬프트 앞에 `(.venv)` 표시가 붙는지
- `python --version`이 정확히 3.12.10인지

### 완료 조건
가상환경이 활성화된 상태에서 `python --version`이 3.12.10을 출력하고, `pip list`에 pandas/requests/beautifulsoup4/jupyter/python-dotenv가 모두 보임.

### 실패하면
- 실행 정책 오류(스크립트 실행 차단) → PowerShell을 관리자 권한으로 열거나 `Set-ExecutionPolicy` 확인 필요 (임의로 보안 정책을 낮추지 말고 사용자에게 확인)
- `python`이 다른 버전을 가리킴 → `where.exe python` 결과 순서 확인, `.venv` 재활성화

### 완료 후 PROGRESS.md에 기록할 내용
STEP 01 → `DONE`

**현재 상태: DONE (확인 완료 — pandas 3.0.6, requests 2.34.2, beautifulsoup4 4.15.0, jupyter 1.1.1, python-dotenv 1.2.3, pip 26.2.1 설치 확인됨)**

---

## STEP 02. Jupyter 환경 준비

### 목표
이 프로젝트 전용 Jupyter 커널을 등록하고, 실습에 사용할 Notebook 파일을 만든다.

### 왜 하는가
VS Code에서 Notebook을 열 때 이 프로젝트의 `.venv` 환경을 커널로 선택할 수 있어야, 방금 설치한 pandas/requests 등을 Notebook에서 바로 사용할 수 있습니다.

### 시작 전 확인
- STEP 01 완료 (`.venv` 활성화 및 jupyter 설치 완료)

### 실행 명령
```powershell
cd C:\dev\claude-code-agent-course-practice
.\.venv\Scripts\Activate.ps1
python -m ipykernel install --user --name ax-job-agent --display-name "Python (ax-job-agent)"
mkdir notebooks
```
이후 VS Code에서 `notebooks/ax_job_pipeline.ipynb` 파일을 새로 생성합니다.

### 예상 결과
- ipykernel 등록 성공 메시지 (`Installed kernelspec ax-job-agent in ...`)
- `jupyter kernelspec list` 실행 시 `ax-job-agent` 항목이 표시됨
- `notebooks/ax_job_pipeline.ipynb` 파일이 생성됨

### 사람이 확인할 것
- VS Code Notebook 우측 상단 Kernel 선택 화면에 **"Python (ax-job-agent)"** 항목이 보이는지
- 실제로 그 커널을 선택하고 첫 셀(`import pandas`)이 오류 없이 실행되는지

### 완료 조건
VS Code에서 "Python (ax-job-agent)" 커널을 선택할 수 있고, 해당 커널로 `import pandas as pd` 셀이 오류 없이 실행됨.

### 실패하면
- 커널 목록에 안 보임 → VS Code 재시작, 또는 `python -m ipykernel install` 재실행
- import 오류 → 잘못된 커널(`python3` 기본 커널)을 선택한 것은 아닌지 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 02 → `DONE`

**현재 상태 (2026-09-23 확인): NOT_STARTED — `jupyter kernelspec list`에 `ax-job-agent` 커널 없음, `notebooks/` 폴더 없음. 다음에 진행할 STEP.**

---

## STEP 03. 수집 데이터 명세

### 목표
DataFrame의 컬럼 구조를 확정한다.

### 왜 하는가
크롤링 코드를 작성하기 전에 "어떤 데이터를 어떤 컬럼명으로 저장할지" 먼저 정해야, 이후 전처리/분석/필터링 코드가 흔들리지 않습니다.

### 시작 전 확인
- STEP 02 완료 (Notebook 사용 가능)

### 실행 명령
Notebook의 첫 Markdown Cell에 아래 명세를 그대로 기록합니다. (PROJECT_SPEC.md 7번 항목과 동일)

DataFrame 1행 = 채용 공고 1건

컬럼: `company_name`, `job_title`, `career`, `location`, `posted_date`, `closing_date`, `job_url`, `search_keyword`, `collected_at`

### 예상 결과
Notebook 상단에 데이터 명세가 Markdown으로 정리되어 있음.

### 사람이 확인할 것
- 컬럼명과 설명이 실제 웹사이트에서 확인 가능한 항목과 일치하는지

### 완료 조건
9개 컬럼 정의가 Notebook과 `PROJECT_SPEC.md`에 동일하게 기록되어 있음.

### 실패하면
- 사이트 구조상 특정 컬럼(예: `closing_date`)을 구하기 어려우면, 이 단계에서 컬럼을 조정하고 `PROJECT_SPEC.md`에도 반영

### 완료 후 PROGRESS.md에 기록할 내용
STEP 03 → `DONE`, 컬럼 확정 여부 기록

---

## STEP 04. 채용공고 페이지 접근 테스트

### 목표
크롤링 대상 사이트에 실제로 요청을 보내고 응답을 받아본다. 딱 1개 검색어, 1개 페이지만 시도한다.

### 왜 하는가
대량 수집 코드를 작성하기 전에, 사이트가 요청을 정상적으로 받아주는지 / 로그인이나 차단이 있는지 / HTML 구조가 어떤지 먼저 확인해야 합니다.

### 시작 전 확인
- STEP 03 완료 (데이터 명세 확정)

### 실행 명령
Notebook Code Cell에서:
```python
import requests

url = "..."  # 실제 검색 결과 URL 1개
headers = {"User-Agent": "..."}
response = requests.get(url, headers=headers, timeout=10)
print(response.status_code)
print(response.headers.get("Content-Type"))
print(len(response.text))
```

### 예상 결과
- `status_code`가 200
- HTML 텍스트가 정상적으로 반환됨 (길이가 0이 아님)

### 사람이 확인할 것
- 응답 HTML을 직접 열어보고 채용 공고 목록이 실제로 포함되어 있는지
- 로그인/캡차 요구 여부

### 완료 조건
상태 코드 200 확인, HTML 안에서 채용 공고로 보이는 태그(회사명/제목 등)를 육안으로 확인함.

### 실패하면
- 상태 코드가 200이 아님 → User-Agent 헤더 추가, URL 재확인
- HTML에 공고 내용이 없음 → JavaScript 렌더링 방식인지 확인 (이 경우 접근 방법을 다시 논의해야 함)

### 완료 후 PROGRESS.md에 기록할 내용
STEP 04 → `DONE`, 접근 가능 여부와 HTML 구조 특이사항 기록

---

## STEP 05. 소량 데이터 수집

### 목표
처음에는 1건만, 성공하면 5~10건만 수집해본다.

### 왜 하는가
대량 수집은 사이트에 부담을 주고 디버깅도 어렵습니다. 소량으로 먼저 성공시킨 뒤 점진적으로 늘립니다.

### 시작 전 확인
- STEP 04 완료 (페이지 접근 및 HTML 구조 확인)

### 실행 명령
BeautifulSoup으로 HTML을 파싱하여 공고 1건의 정보를 추출 → 성공하면 반복문으로 5~10건 추출.

### 예상 결과
공고 1건의 회사명/제목/URL 등이 출력됨. 이어서 5~10건의 리스트(dict 목록 등)가 출력됨.

### 사람이 확인할 것
- 추출된 값이 실제 웹페이지 내용과 정확히 일치하는지 (오타, 누락, 다른 공고와 섞임 없는지)

### 완료 조건
5~10건의 공고 정보가 올바르게 추출됨 (사람이 직접 원본과 대조 확인).

### 실패하면
- 특정 필드가 비어있음 → CSS 선택자/HTML 구조 재확인
- 값이 뒤섞임 → 반복문 인덱싱 오류 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 05 → `DONE`, 수집한 샘플 건수 기록

---

## STEP 06. DataFrame 생성

### 목표
수집한 리스트 데이터를 pandas DataFrame으로 변환한다.

### 왜 하는가
이후 모든 정제/분석/필터링 작업은 DataFrame 위에서 이루어지므로, 우선 데이터를 표 형태로 만들어야 합니다.

### 시작 전 확인
- STEP 05 완료 (5~10건의 공고 데이터 확보)

### 실행 명령
```python
import pandas as pd

df = pd.DataFrame(jobs)
print(df.shape)
df.head()
print(df.columns.tolist())
```

### 예상 결과
- `shape`가 (수집건수, 컬럼수)로 출력
- `head()`로 상위 5건 표 출력
- `columns`가 STEP 03에서 정의한 컬럼명과 일치

### 사람이 확인할 것
- 컬럼명이 명세와 정확히 일치하는지
- 각 셀 값이 올바른 컬럼에 들어갔는지

### 완료 조건
`df.shape`, `df.head()`, `df.columns`가 모두 예상과 일치함.

### 실패하면
- 컬럼명이 다름 → 리스트를 만들 때 사용한 dict의 key 확인
- 일부 값이 NaN → STEP 07에서 처리하되, 원인은 이 단계에서 미리 파악

### 완료 후 PROGRESS.md에 기록할 내용
STEP 06 → `DONE`

---

## STEP 07. 데이터 전처리

### 목표
결측값을 확인/처리하고, 문자열을 정리하고, 날짜 컬럼을 datetime으로 변환한다.

### 왜 하는가
정제되지 않은 데이터는 이후 통계 계산과 필터링에서 잘못된 결과를 만듭니다.

### 시작 전 확인
- STEP 06 완료 (DataFrame 생성)

### 실행 명령
```python
df.isna().sum()
df["company_name"] = df["company_name"].str.strip()
df["posted_date"] = pd.to_datetime(df["posted_date"], errors="coerce")
```

### 예상 결과
- 결측값 개수가 컬럼별로 출력됨
- 날짜 컬럼의 dtype이 `datetime64`로 변경됨

### 사람이 확인할 것
- 문자열 정리 후에도 의미가 바뀌지 않았는지
- 날짜 변환 후 `NaT`(변환 실패)가 많이 발생하지 않았는지

### 완료 조건
`df.dtypes`에서 날짜 컬럼이 datetime 타입이고, 주요 컬럼의 결측값 비율이 허용 범위 내임.

### 실패하면
- 날짜 변환 실패 다수 → 원본 날짜 형식 재확인 (예: "2026.09.23" vs "2026-09-23")

### 완료 후 PROGRESS.md에 기록할 내용
STEP 07 → `DONE`

---

## STEP 08. 중복 제거

### 목표
`job_url` 기준으로 중복된 공고를 제거한다.

### 왜 하는가
같은 공고가 여러 검색어에 걸려 중복 수집될 수 있습니다. `job_url`은 공고를 유일하게 식별하는 키입니다.

### 시작 전 확인
- STEP 07 완료 (전처리 완료)

### 실행 명령
```python
before = df.shape[0]
df = df.drop_duplicates(subset="job_url")
after = df.shape[0]
print(before, after)
```

### 예상 결과
제거 전/후 행 수가 출력되고, 중복이 있었다면 `after < before`.

### 사람이 확인할 것
- 실제로 같은 공고가 중복 제거되었는지 (다른 공고가 잘못 제거되지 않았는지)

### 완료 조건
`df["job_url"].duplicated().sum()`이 0.

### 실패하면
- 중복 제거 후에도 중복이 남음 → URL에 쿼리 파라미터 등 불필요한 값이 섞여있는지 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 08 → `DONE`

---

## STEP 09. 신규 공고 판별

### 목표
이전에 수집했던 공고 URL 목록과 이번에 수집한 URL을 비교하여 신규 공고를 판별한다.

### 왜 하는가
매주 같은 공고를 반복 보고하지 않고, "새로 올라온 공고"만 강조하기 위함입니다.

### 시작 전 확인
- STEP 08 완료 (중복 제거 완료)
- `data/processed/jobs_history.csv` 파일 (최초 실행 시에는 없을 수 있음 — 이 경우 전체를 신규로 간주)

### 실행 명령
```python
import os

history_path = "data/processed/jobs_history.csv"
if os.path.exists(history_path):
    history = pd.read_csv(history_path)
    known_urls = set(history["job_url"])
else:
    known_urls = set()

df["is_new"] = ~df["job_url"].isin(known_urls)
```

### 예상 결과
`is_new` 컬럼이 추가되고, True/False 값이 올바르게 채워짐.

### 사람이 확인할 것
- 이전 이력 파일이 없을 때 전체가 신규로 표시되는지
- 이전 이력 파일이 있을 때 실제로 새 URL만 True로 표시되는지

### 완료 조건
`df["is_new"].value_counts()` 결과가 실제 상황과 일치함.

### 실패하면
- 전부 신규로 표시됨(이력 파일이 있는데도) → 경로 확인, `job_url` 형식 일치 여부 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 09 → `DONE`, `data/processed/jobs_history.csv` 최초 저장 여부 기록

---

## STEP 10. 기본 분석

### 목표
pandas로 신규 공고 수, 회사별/지역별/경력별/검색어별 통계, 직무 키워드 빈도를 계산한다.

### 왜 하는가
"사실"에 해당하는 모든 숫자는 이 단계에서 pandas로 확정합니다. (Gemini에게 맡기지 않음 — PROJECT_SPEC.md 8~9번 참고)

### 시작 전 확인
- STEP 09 완료 (신규 공고 판별 완료)

### 실행 명령
```python
df["is_new"].sum()
df.groupby("company_name").size().sort_values(ascending=False)
df.groupby("location").size().sort_values(ascending=False)
df.groupby("career").size()
df.groupby("search_keyword").size()
```

### 예상 결과
각 집계가 표 또는 Series 형태로 출력됨.

### 사람이 확인할 것
- 집계 결과 합계가 전체 행 수와 맞는지

### 완료 조건
5가지 통계(신규 수, 회사별, 지역별, 경력별, 검색어별)가 모두 출력되고 합계가 검증됨.

### 실패하면
- 집계 합이 안 맞음 → 결측값이나 그룹핑 키의 공백/대소문자 차이 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 10 → `DONE`

---

## STEP 11. 관련 공고 필터링

### 목표
AX/AI/인공지능/데이터 분석/생성형 AI/LLM/Machine Learning/Data Scientist/AI Engineer 키워드와 관련성이 높은 공고만 1차로 걸러낸다.

### 왜 하는가
Gemini API 호출은 비용과 시간이 들기 때문에, 명백히 관련 없는 공고는 pandas 단계에서 미리 제외합니다.

### 시작 전 확인
- STEP 10 완료 (기본 분석 완료)

### 실행 명령
```python
keywords = ["AX", "AI", "인공지능", "데이터 분석", "생성형 AI", "LLM",
            "Machine Learning", "Data Scientist", "AI Engineer"]
pattern = "|".join(keywords)
mask = df["job_title"].str.contains(pattern, case=False, na=False)
filtered = df[mask]
```

### 예상 결과
`filtered`가 전체 대비 일부만 포함하는 DataFrame.

### 사람이 확인할 것
- 걸러진 공고들이 실제로 관련성이 있는지 (직접 몇 건 읽어보기)
- 관련 있는데 제외된 공고는 없는지 (키워드 목록 보완 필요 여부)

### 완료 조건
필터링된 결과를 사람이 눈으로 검토하여 관련성이 확인됨.

### 실패하면
- 관련 없는 공고가 다수 포함 → 키워드 재조정 또는 `job_title` 외 다른 컬럼도 검사

### 완료 후 PROGRESS.md에 기록할 내용
STEP 11 → `DONE`

---

## STEP 12. Gemini API 연동

### 목표
Gemini API를 호출할 수 있는 기본 연동 코드를 작성한다.

### 왜 하는가
이후 STEP에서 공고 요약/기술 추출을 하려면 먼저 API 키 관리와 호출 방식을 검증해야 합니다.

### 시작 전 확인
- STEP 11 완료 (필터링된 공고 확보)
- Gemini API 키 발급 완료 (사용자가 별도로 준비)

### 실행 명령
```powershell
# .env.example 및 .env 파일 생성 (실제 키는 .env에만)
```
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
```

### 예상 결과
`.env`에서 키를 정상적으로 읽어옴 (`api_key`가 `None`이 아님).

### 사람이 확인할 것
- `.env` 파일이 `.gitignore`에 의해 Git에 포함되지 않는지 (`git status`에 안 보여야 함)

### 완료 조건
`.env`의 키가 코드에서 정상적으로 로드되고, `git status`에 `.env`가 나타나지 않음.

### 실패하면
- 키가 `None` → `.env` 파일 위치 및 변수명 오타 확인
- `git status`에 `.env`가 보임 → `.gitignore` 확인 및 즉시 추가

### 완료 후 PROGRESS.md에 기록할 내용
STEP 12 → `DONE`

---

## STEP 13. Gemini 결과 검증

### 목표
Gemini가 반환한 요약/기술 추출 결과를 실제 공고 원문과 대조한다.

### 왜 하는가
AI 결과를 검증 없이 그대로 신뢰하면 잘못된 정보가 보고서에 그대로 실릴 수 있습니다.

### 시작 전 확인
- STEP 12 완료 (API 연동 성공)

### 실행 명령
최소 3~5개 공고에 대해 Gemini 응답과 원문을 나란히 출력하여 비교.

### 예상 결과
공고별 원문 요약과 Gemini 요약이 나란히 출력됨.

### 사람이 확인할 것
- 누락된 핵심 정보는 없는지
- 과도한 해석(원문에 없는 내용 추가)은 없는지
- 기술 스택 추출이 정확한지

### 완료 조건
검증한 공고 모두에서 심각한 오류가 없음을 사람이 확인함.

### 실패하면
- 반복적인 오류 패턴 발견 → 프롬프트 수정 후 재검증

### 완료 후 PROGRESS.md에 기록할 내용
STEP 13 → `DONE`

---

## STEP 14. Markdown 보고서 생성

### 목표
한 주간의 결과를 `reports/` 폴더에 Markdown 파일로 저장한다.

### 왜 하는가
Slack/Gmail로 보내기 전에, 사람이 먼저 읽고 검토할 수 있는 형태로 결과를 정리합니다.

### 시작 전 확인
- STEP 10(기본 분석), STEP 13(Gemini 검증) 완료

### 실행 명령
보고서에 포함할 항목: 신규 공고, 주요 키워드, 추천 공고, 수집 기준, 주의사항.

### 예상 결과
`reports/` 폴더에 날짜가 포함된 `.md` 파일 생성.

### 사람이 확인할 것
- 보고서 내용이 실제 분석 결과와 일치하는지
- 오타나 형식 오류가 없는지

### 완료 조건
보고서 파일이 생성되고 사람이 읽었을 때 내용이 이해 가능하고 정확함.

### 실패하면
- 통계 수치가 실제 DataFrame과 다름 → 보고서 생성 코드의 참조 변수 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 14 → `DONE`

---

## STEP 15. Slack 발송

### 목표
생성된 Markdown 보고서(또는 요약)를 Slack Webhook으로 전송한다.

### 왜 하는가
자동화의 첫 번째 실제 알림 채널입니다. Gmail보다 먼저 검증하여 문제를 빨리 발견합니다.

### 시작 전 확인
- STEP 14 완료 (보고서 생성)
- Slack Webhook URL 발급 완료

### 실행 명령
```python
import requests

response = requests.post(webhook_url, json={"text": message})
print(response.status_code)
```

### 예상 결과
HTTP 상태 코드 200, Slack 채널에 메시지 도착.

### 사람이 확인할 것
- Slack 채널에서 실제로 메시지를 확인
- 한글이 깨지지 않는지
- 링크가 클릭 가능한지

### 완료 조건
Slack 채널에서 메시지를 실제로 확인함 (사람 눈으로).

### 실패하면
- 상태 코드가 200이 아님 → Webhook URL 재확인
- 한글 깨짐 → 인코딩(UTF-8) 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 15 → `DONE`

---

## STEP 16. Gmail 발송

### 목표
동일한 보고서를 Gmail로도 발송한다.

### 왜 하는가
Slack과 별개로 이메일로도 기록을 남기기 위함입니다. Slack이 먼저 성공한 뒤에 진행하여, 두 채널의 문제를 동시에 디버깅하지 않습니다.

### 시작 전 확인
- STEP 15 완료 (Slack 발송 성공)
- Gmail 앱 비밀번호 발급 완료

### 실행 명령
`smtplib` 또는 유사 라이브러리를 이용해 `.env`의 `GMAIL_USER`/`GMAIL_APP_PASSWORD`로 인증 후 메일 발송.

### 예상 결과
발송 성공 메시지, 수신함에 메일 도착.

### 사람이 확인할 것
- 실제 수신함에서 메일 확인
- 제목/본문 형식이 올바른지

### 완료 조건
사람이 수신함에서 메일을 직접 확인함.

### 실패하면
- 인증 실패 → 앱 비밀번호(일반 비밀번호 아님) 재확인
- 스팸함으로 이동 → 발신자 정보 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 16 → `DONE`

---

## STEP 17. 함수화

### 목표
Notebook에서 검증한 코드를 재사용 가능한 함수 단위로 정리한다.

### 왜 하는가
셀 단위로 순서대로만 실행되던 코드를, 이후 `src/` 모듈과 `main.py`에서 호출할 수 있는 형태로 바꿉니다.

### 시작 전 확인
- STEP 05~16의 각 단계 코드가 Notebook에서 개별적으로 검증 완료

### 실행 명령
아래 함수들을 Notebook 내에 정의하고, 각각을 호출해 기존과 동일한 결과가 나오는지 재검증.

- `collect_jobs()`
- `clean_jobs()`
- `find_new_jobs()`
- `analyze_jobs()`
- `summarize_with_gemini()`
- `create_report()`
- `send_slack()`
- `send_email()`

### 예상 결과
각 함수를 호출했을 때 이전 셀 단위 코드와 동일한 결과 출력.

### 사람이 확인할 것
- 함수화 과정에서 로직이 바뀌지 않았는지 (결과 비교)

### 완료 조건
8개 함수 모두 정의되고, 개별 호출 결과가 기존 셀 단위 실행 결과와 일치.

### 실패하면
- 결과 불일치 → 함수 내부에서 변수 스코프/인자 누락 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 17 → `DONE`

---

## STEP 18. src 구조화

### 목표
Notebook에 정의된 함수들을 `src/` 하위의 각 모듈 파일로 이동한다.

### 왜 하는가
Notebook은 실험 환경이고, 실제 자동 실행(main.py, GitHub Actions)은 `.py` 모듈 구조가 필요합니다.

### 시작 전 확인
- STEP 17 완료 (함수화 완료)

### 실행 명령
함수를 아래 파일로 분배 이동:
- `crawler.py` ← `collect_jobs()`
- `preprocess.py` ← `clean_jobs()`, `find_new_jobs()`
- `analyzer.py` ← `analyze_jobs()`
- `gemini_client.py` ← `summarize_with_gemini()`
- `reporter.py` ← `create_report()`
- `notifier.py` ← `send_slack()`, `send_email()`

Notebook에서는 `from src.crawler import collect_jobs`처럼 import하여 동일하게 재검증.

### 예상 결과
Notebook에서 import한 함수들이 이전과 동일한 결과를 출력.

### 사람이 확인할 것
- import 경로 오류 없이 실행되는지
- 함수 이동 후 로직이 바뀌지 않았는지

### 완료 조건
Notebook에서 `src/` 모듈을 import하여 전체 흐름을 재현할 수 있음.

### 실패하면
- import 오류 → 패키지 구조(`__init__.py` 필요 여부) 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 18 → `DONE`

---

## STEP 19. main.py 통합

### 목표
`src/` 모듈의 함수들을 순서대로 호출하는 `main.py`를 작성한다.

### 왜 하는가
이 파일이 결국 GitHub Actions가 실행할 진입점입니다. 새로운 로직을 추가하지 않고, 기존에 검증된 함수 호출 순서만 연결합니다.

### 시작 전 확인
- STEP 18 완료 (src 구조화 완료)

### 실행 명령
`main.py`에서 STEP 05~16 순서대로 함수 호출 (수집 → 전처리 → 판별 → 분석 → 필터링 → 요약 → 보고서 → 발송).

### 예상 결과
파일 작성만으로는 실행 결과가 없음 (STEP 20에서 실행 검증).

### 사람이 확인할 것
- 함수 호출 순서가 실제 파이프라인 순서와 일치하는지

### 완료 조건
`main.py`가 문법 오류 없이 작성되고, 호출 순서가 리뷰됨.

### 실패하면
- 순서 누락 → PROJECT_SPEC.md 5번(운영 단계 구조)과 대조

### 완료 후 PROGRESS.md에 기록할 내용
STEP 19 → `DONE`

---

## STEP 20. 로컬 전체 실행 검증

### 목표
`python main.py`를 실행하여 전체 파이프라인이 끝까지 정상 동작하는지 확인한다.

### 왜 하는가
GitHub Actions에 올리기 전 반드시 로컬에서 전체 흐름이 성공해야 합니다. 이 단계를 건너뛰면 Actions에서 디버깅하기 훨씬 어렵습니다.

### 시작 전 확인
- STEP 19 완료 (`main.py` 작성 완료)
- `.env`에 모든 키가 설정되어 있어야 함

### 실행 명령
```powershell
python main.py
```

### 예상 결과
오류 없이 실행 완료, Slack/Gmail 실제 수신 확인, `reports/`에 새 보고서 파일 생성.

### 사람이 확인할 것
- 콘솔 출력에 에러가 없는지
- Slack/Gmail 실제 수신 여부
- 생성된 보고서 내용

### 완료 조건
`python main.py` 실행이 처음부터 끝까지 오류 없이 완료되고, 모든 출력물(보고서, Slack, Gmail)이 확인됨.

### 실패하면
- 특정 단계에서 예외 발생 → 어느 STEP에 해당하는 함수인지 확인 후 해당 STEP으로 돌아가 재검증

### 완료 후 PROGRESS.md에 기록할 내용
STEP 20 → `DONE`

---

## STEP 21. Git 저장 / Push

### 목표
지금까지의 변경 사항을 커밋하고 원격 저장소에 push한다.

### 왜 하는가
GitHub Actions는 저장소에 push된 코드 기준으로 동작하므로, 로컬 검증이 끝난 코드를 반드시 반영해야 합니다.

### 시작 전 확인
- STEP 20 완료 (로컬 전체 실행 검증 성공)

### 실행 명령
```powershell
git status
git diff
git add <검토한 파일들>
git commit -m "메시지"
git push
```

### 예상 결과
민감정보 없이 커밋 생성, push 성공.

### 사람이 확인할 것
- `git status`/`git diff`에서 `.env`, API 키, 비밀번호가 포함되지 않았는지 **반드시** 확인

### 완료 조건
push가 성공하고, GitHub 저장소에서 파일이 확인됨.

### 실패하면
- 민감정보 포함 발견 → 커밋 전에 반드시 제외, 이미 커밋했다면 즉시 사용자에게 알리고 조치

### 완료 후 PROGRESS.md에 기록할 내용
STEP 21 → `DONE`

---

## STEP 22. GitHub Actions 수동 실행

### 목표
`workflow_dispatch`를 이용해 GitHub Actions에서 수동으로 파이프라인을 실행해본다.

### 왜 하는가
스케줄 자동 실행 전에, 수동 트리거로 먼저 Actions 환경에서의 동작을 검증합니다.

### 시작 전 확인
- STEP 21 완료 (push 완료)
- workflow 파일(`.github/workflows/*.yml`) 작성 완료 (`workflow_dispatch` 트리거 포함)

### 실행 명령
GitHub 저장소 → Actions 탭 → 해당 workflow → "Run workflow" 클릭.

### 예상 결과
워크플로우 실행 로그가 성공(초록색 체크)으로 표시됨.

### 사람이 확인할 것
- Actions 로그에서 각 STEP 로그 확인
- Slack/Gmail 실제 수신 여부 (Actions 환경에서도 발송되는지)

### 완료 조건
수동 실행이 성공(success)으로 완료됨.

### 실패하면
- Secrets 누락 → STEP 23 확인
- 로컬과 다른 환경 오류 → Python 버전/의존성 버전 차이 확인 (`requirements.txt`)

### 완료 후 PROGRESS.md에 기록할 내용
STEP 22 → `DONE`

---

## STEP 23. GitHub Secrets

### 목표
`.env`에 있던 값들을 GitHub Secrets에 동일하게 등록한다.

### 왜 하는가
GitHub Actions는 로컬 `.env` 파일에 접근할 수 없으므로, Secrets를 통해 안전하게 값을 주입해야 합니다.

### 시작 전 확인
- STEP 22 진행 중 Secrets 누락 오류 확인 (또는 사전 준비)

### 실행 명령
GitHub 저장소 → Settings → Secrets and variables → Actions → New repository secret

등록할 값:
- `GEMINI_API_KEY`
- `SLACK_WEBHOOK_URL`
- `GMAIL_USER`
- `GMAIL_APP_PASSWORD`

### 예상 결과
Secrets 목록에 4개 항목이 등록됨 (값은 가려짐).

### 사람이 확인할 것
- 이름이 workflow 파일(`${{ secrets.XXX }}`)과 정확히 일치하는지

### 완료 조건
4개 Secrets 모두 등록되고, STEP 22 재실행 시 인증 관련 오류가 사라짐.

### 실패하면
- 이름 불일치 → workflow yml 파일의 참조 이름 재확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 23 → `DONE`

---

## STEP 24. GitHub Actions 주간 자동 실행

### 목표
매주 1회 자동으로 파이프라인이 실행되도록 스케줄을 등록한다.

### 왜 하는가
사람이 매번 수동으로 실행하지 않아도, 정기적으로 최신 채용 동향을 받아보기 위함입니다.

### 시작 전 확인
- STEP 22, 23 완료 (수동 실행 성공, Secrets 등록 완료)

### 실행 명령
workflow yml에 스케줄 추가:
```yaml
on:
  schedule:
    - cron: "0 0 * * 1"
  workflow_dispatch:
```
(UTC 월요일 00:00 = 한국시간 월요일 오전 9시)

### 예상 결과
지정된 시간에 Actions가 자동으로 실행됨 (실제 확인은 다음 스케줄 시점까지 대기 필요).

### 사람이 확인할 것
- Actions 탭에서 예정된 스케줄이 등록되어 있는지
- 실제 스케줄 도래 시 자동 실행 및 Slack/Gmail 수신 확인

### 완료 조건
최소 1회의 자동 스케줄 실행이 성공적으로 완료됨.

### 실패하면
- 스케줄이 실행되지 않음 → GitHub Actions는 저장소 활동이 적으면 스케줄이 지연/비활성화될 수 있음, 저장소 상태 확인

### 완료 후 PROGRESS.md에 기록할 내용
STEP 24 → `DONE` — 이 시점에서 전체 프로젝트 완료
