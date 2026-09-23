# 현재 진행 상태

> 이 파일은 프로젝트를 다시 시작할 때 **가장 먼저** 열어보는 파일입니다.
> 아래 내용만 읽어도 "어디까지 했고, 다음에 무엇을 해야 하는지" 30초 안에 파악할 수 있어야 합니다.

## Repository migration completed (2026-09-23)

- 교육용 원본: `GilbertMoon/claude-code-agent-course` (로컬 `C:\dev\claude-code-agent-course`)
- 실습용(이 저장소): `GilbertMoon/claude-code-agent-course-practice`
- 새 로컬 경로: `C:\dev\claude-code-agent-course-practice`
- 원본 교육 저장소에는 이번 이관 작업으로 commit/push하지 않음 (원본은 읽기 전용으로만 확인함)
- 이후 STEP 작업(STEP 19 이후)은 오직 이 practice 저장소에서만 진행
- 이번 이관 작업 때문에 아래 STEP 번호나 상태를 변경하지 않았음 (STEP 18 DONE / STEP 19 IN_PROGRESS 그대로 유지)

## 요약 (한눈에 보기)

- **마지막 작업일**: 2026-09-23
- **마지막 완료 STEP**: STEP 18 src 모듈화
- **현재 STEP**: STEP 19 main.py 작성
- **현재 상태**: IN_PROGRESS
- **다음 작업**: `main.py`(프로젝트 루트)를 실행 관리자로 검증한다. Notebook에서 `import main`으로 존재 및 `main.main` callable 여부만 확인하고, 실제 `python main.py` 실행은 사용자가 터미널에서 직접 수행한다.
- **다음 작업 위치**: `main.py`, `notebooks/ax_job_pipeline.ipynb`
- **완료 기준**: 사용자가 Notebook에서 `import main` 성공을 확인하고, 터미널에서 `python main.py`를 직접 실행하여 보고서 저장 성공과 Slack/Gmail 자동 발송이 없음을 확인할 것 (STEP 19는 이 확인 전까지 `IN_PROGRESS` 유지)

---

## 현재 STEP

STEP 19 - main.py 작성

## 현재 상태

IN_PROGRESS

(상태 값: `NOT_STARTED` / `IN_PROGRESS` / `DONE` 중 하나)

## 마지막 완료 작업

STEP 18 완료 — src 모듈화 (사용자 직접 실행 및 확인 완료).

- `src/analyzer.py`, `src/reporter.py`, `src/notifier.py`, `src/__init__.py` 존재 확인
- Notebook에서 `sys.path` 추가 후 `from src.analyzer import ...` 등 import 성공 확인
- `filter_related_jobs()` 결과가 기존과 동일: 5건/5건, `job_url` 집합 비교 `True`
- `build_markdown_report()` 정상 동작 확인
- `send_slack_message()`/`send_gmail()` 실제 재발송 없음 확인

## 다음 작업

프로젝트 루트에 `main.py`를 새로 생성했습니다. `main.py`는 세부 기능을 직접 구현하지 않고, `src.analyzer.filter_related_jobs`, `src.reporter.build_markdown_report`, `src.notifier.send_slack_message`/`send_gmail`을 순서대로 호출하는 **실행 관리자(orchestrator)** 역할만 합니다. `SEND_SLACK = False`, `SEND_GMAIL = False`로 고정하여 이번 STEP에서는 외부 전송이 자동 실행되지 않으며, OpenAI는 import조차 하지 않습니다. `data/processed/` 폴더가 현재 존재하지 않아(실제 확인함) 입력 CSV가 없는 상태이므로, `main()`은 "실행 가능한 입력 CSV가 없습니다."를 출력하고 안전하게 종료하도록 작성했습니다 (가짜 데이터 생성 없음).

> Notebook에 STEP 19의 3-Cell(작업 계획 / 코드 / 결과 해석)을 작성했습니다. Code Cell은 `sys.path`에 프로젝트 루트를 추가한 뒤 `import main`만 수행하며, **`main.main()`은 호출하지 않습니다.** 실제 `python main.py` 실행은 사용자가 터미널에서 직접 수행해야 합니다.

### 실행 예정 위치

`main.py` (터미널에서 `python main.py`), `notebooks/ax_job_pipeline.ipynb`의 STEP 19 Code Cell (import 확인용)

## 다음 작업 완료 기준

사용자가 Notebook에서 STEP 19 Code Cell을 실행해 `import main` 성공과 `main.main` callable 여부를 확인하고, 터미널에서 직접 `python main.py`를 실행하여 (data/processed/에 CSV를 준비했다면) 보고서 저장 성공, 또는 (CSV가 없다면) "실행 가능한 입력 CSV가 없습니다." 메시지가 안전하게 출력되는 것을 확인하며, Slack/Gmail이 자동으로 발송되지 않았음을 확인해야 합니다. 파일 생성 및 Claude Code의 사전 검증(문법 검사, import 검사)만으로 완료 처리하지 않으며 STEP 19는 `IN_PROGRESS`로 유지합니다.

## 작업 재개 시 먼저 실행할 명령

```powershell
cd C:\dev\claude-code-agent-course-practice
.\.venv\Scripts\Activate.ps1
git branch --show-current
git status
python --version
where.exe python
```

---

## STEP 체크리스트

| STEP | 작업 | 상태 | 완료 기준 |
|------|------|------|----------|
| STEP 00 | 저장소 준비 | DONE | GitHub 저장소 clone 완료, `main` 최신화, `ax-job-agent` 브랜치 생성, `chapter11/ax-job-agent` 폴더 생성 확인 |
| STEP 01 | Python 환경 준비 | DONE | `.venv` 생성 및 활성화, `python --version`이 3.12.10 출력, pip 26.2.1 업그레이드, pandas/requests/beautifulsoup4/jupyter/python-dotenv 설치 확인 |
| STEP 02 | Jupyter 환경 준비 | DONE | ipykernel 등록 완료(`ax-job-agent` / "Python (ax-job-agent)"), VS Code에서 커널 선택 확인, `notebooks/ax_job_pipeline.ipynb` 생성 확인 |
| STEP 03 | 데이터 명세 | DONE | DataFrame 컬럼 정의(PROJECT_SPEC.md 7번) 확정, Notebook 첫 Markdown Cell에 명세 기록, 사용자가 Code Cell 실행하여 `shape (0, 9)` 확인 완료 |
| STEP 04 | 웹 페이지 접근 테스트 | DONE | 검색어 1개, 페이지 1개로 요청 성공(상태 코드 200 확인됨), Content-Type/응답 길이/HTML 구조 사용자가 직접 확인 완료 |
| STEP 05 | 소량 데이터 수집 | DONE | 최대 5건 수집 성공(GS리테일/에스코어/㈜NAVER×2/㈜슈프리마), 사용자가 직접 실행하여 결과 확인 완료 |
| STEP 06 | DataFrame 생성 | DONE | 수집 결과를 DataFrame으로 변환, `shape (5, 9)`/`head()`/`columns` 사용자가 직접 실행하여 확인 완료 |
| STEP 07 | 데이터 전처리 | DONE | 결측값 확인(9개 컬럼 모두 0), 문자열 정리(공백), `collected_at` datetime 변환 — 사용자가 직접 실행하여 확인 완료 |
| STEP 08 | 중복 제거 | DONE | `job_url` 기준 중복 개수 0건 확인, 제거 전/후 shape `(5, 9)` 동일 — 사용자가 직접 실행하여 확인 완료 |
| STEP 09 | 신규 공고 판별 | DONE | 이력 파일 없음(첫 실행) → 기존 URL 0건, 현재 5건 전체가 신규로 판별됨 — 사용자가 직접 실행하여 확인 완료 |
| STEP 10 | 기본 분석 | DONE | 사용자 직접 실행으로 신규 5건, 회사별/지역별/경력별/검색어별 집계 및 날짜 값 확인 완료 |
| STEP 11 | 관련 공고 필터링 | DONE | 제목 키워드 기반 필터링 수행, 관련 공고 5건(100.0%) 정상 필터링 확인 완료 |
| STEP 12 | OpenAI API 연동 | DONE | `.env`/`.env.example` 생성, python-dotenv로 `OPENAI_API_KEY`/`OPENAI_MODEL` 로드, 키 Git 미포함, OpenAI Responses API 1건 테스트 호출 및 응답 확인 — 사용자가 직접 실행하여 확인 완료 |
| STEP 13 | OpenAI 응답 검증 | DONE | 공고 1건(GS리테일) 원문과 OpenAI 응답 비교, 근거 부족 표현 식별, "수정 후 사용 가능"으로 판단 완료 — 사용자가 직접 검증 완료 |
| STEP 14 | Markdown 보고서 생성 | DONE | `reports/`에 주간 보고서 생성, 신규 공고/통계/관련 공고 목록/AI 검증 예시/데이터 기준/주의사항 포함 — 사용자가 직접 실행하여 확인 완료 |
| STEP 15 | Slack 발송 | DONE | Slack Webhook으로 전송 성공, 실제 채널 메시지 도착/한글 표시 확인, 헤더 표시 개선 반영 — 사용자가 직접 실행하여 확인 완료 |
| STEP 16 | Gmail 발송 | DONE | Gmail SMTP 연결/인증/`send_message()` 성공, 실제 수신함 도착 확인(제목/한글/본문 정상) — 사용자가 직접 실행하여 확인 완료 |
| STEP 17 | 함수화 | DONE | `filter_related_jobs()`, `build_markdown_report()`, `send_slack_message()`, `send_gmail()` 함수 정의 및 앞 2개 함수 실행 검증(5/5/True) — 사용자가 직접 실행하여 확인 완료 |
| STEP 18 | src 구조화 | DONE | `src/analyzer.py`/`reporter.py`/`notifier.py` 분리, import 및 기본 동작(5/5/True) 확인 — 사용자가 직접 실행하여 확인 완료 |
| STEP 19 | main.py 통합 | IN_PROGRESS | `main.py`에서 각 모듈 함수를 순서대로 호출하는 흐름 작성 완료, `import main`만 확인 — 실제 `python main.py` 실행 및 확인 대기 중 |
| STEP 20 | 로컬 전체 실행 검증 | NOT_STARTED | `python main.py` 실행 시 전체 파이프라인이 오류 없이 끝까지 완료 |
| STEP 21 | Git 저장 / Push | NOT_STARTED | `git status`/`git diff`로 민감정보 미포함 확인 후 add/commit/push 완료 |
| STEP 22 | GitHub Actions 수동 실행 | NOT_STARTED | `workflow_dispatch`로 수동 실행 성공 |
| STEP 23 | GitHub Secrets | NOT_STARTED | `GEMINI_API_KEY`, `SLACK_WEBHOOK_URL`, `GMAIL_USER`, `GMAIL_APP_PASSWORD` GitHub Secrets 등록 완료 |
| STEP 24 | GitHub Actions 주간 자동 실행 | NOT_STARTED | `cron: "0 0 * * 1"` 스케줄 등록, 자동 실행 결과 확인 |

---

## 갱신 이력 (최신이 위로)

- **2026-09-23**: 사용자가 STEP 18 Code Cell을 직접 실행하여 src 모듈 import 성공, `filter_related_jobs()`/`build_markdown_report()` 정상 동작(5/5/True), Slack/Gmail 재발송 없음을 확인 — STEP 18 `DONE` 처리. 프로젝트 루트에 `main.py` 신규 생성: `src.analyzer`/`src.reporter`/`src.notifier`를 import해 순서대로 호출하는 실행 관리자로 작성, `SEND_SLACK=False`/`SEND_GMAIL=False` 고정, OpenAI 미사용(import 없음), `data/processed/*.csv` 중 최신 파일을 입력으로 찾되 폴더 자체가 없음을 실제 확인하여(파일 구조 검증 완료) "실행 가능한 입력 CSV가 없습니다." 안내 후 안전 종료하도록 처리(가짜 데이터 생성 없음), 필수 컬럼 9개 검사 및 `RELATED_KEYWORDS`를 STEP 11과 동일하게 유지. `python -m py_compile main.py` 통과, `import main` 성공 및 `main.main` callable 확인(모두 Claude Code가 사전 검증, `main.main()`은 호출하지 않음). Notebook에 STEP 19(main.py 작성) 3-Cell 추가 — Code Cell은 `import main`만 수행하고 `main.main()` 호출 없음. 사용자의 Notebook 실행 및 터미널에서의 실제 `python main.py` 실행 확인이 필요하여 STEP 19 상태는 `IN_PROGRESS`.

- **2026-09-23**: 사용자가 STEP 17 Code Cell을 직접 실행하여 4개 함수 정의, `filter_related_jobs()` 결과가 기존 `related_jobs`와 동일(5건/5건, `job_url` 집합 `True`), `build_markdown_report()` 정상 동작, Slack/Gmail 함수 실제 재발송 없음을 확인 — STEP 17 `DONE` 처리. `src/` 폴더 신규 생성: `src/__init__.py`(빈 파일), `src/analyzer.py`(`filter_related_jobs`), `src/reporter.py`(`build_markdown_report`, 파일 저장 책임 없음), `src/notifier.py`(`send_slack_message`, `send_gmail`, 환경변수 직접 읽지 않음). 각 모듈 문법 검사 및 역할 분리(analyzer/reporter에 smtplib·requests·pandas·os.getenv·class 없음, notifier에 pandas 없음) 확인. `sys.path`에 프로젝트 루트를 추가해 `from src.analyzer import ...` 형태로 import하는 방식으로 실제 실행 검증 완료(5/5/True, Markdown 문자열 정상 생성 및 7개 핵심 문구 포함 확인). Notebook에 STEP 18(src 모듈화) 3-Cell 추가. Slack/Gmail 함수는 import와 `callable()` 확인만 하고 실제 호출하지 않음. main.py/crawler.py/openai_client.py는 생성하지 않음(STEP 19 예정). 사용자의 Notebook 실행 확인이 필요하여 STEP 18 상태는 `IN_PROGRESS`.

- **2026-09-23**: 사용자가 STEP 16 Code Cell(실제 발송 버전)을 직접 실행하여 Gmail SMTP 연결 성공, 앱 비밀번호 인증 성공, `send_message()` 성공, 실제 Gmail 수신함에서 메일 도착(제목 `[AX 채용 동향] weekly_ax_jobs_2026-09-23`, 한글/본문 정상)을 확인 — STEP 16 `DONE` 처리. Notebook에 STEP 17(함수화) 3-Cell 추가: `filter_related_jobs(df, keywords)`(STEP 11 로직), `build_markdown_report(new_jobs, related_jobs, ai_example=None)`(STEP 14 로직, 파일 저장은 제외), `send_slack_message(webhook_url, message_text)`(STEP 15 로직), `send_gmail(gmail_address, gmail_app_password, gmail_to, subject, body)`(STEP 16 로직) 총 4개 함수를 전역 변수 참조 없이 인자 기반으로 정의. `filter_related_jobs`/`build_markdown_report`는 Claude Code가 동일 데이터로 사전 실행하여 기존 결과와 일치함을 확인(관련 공고 5건/5건, URL 집합 동일, 보고서 8개 섹션 모두 포함, 길이 1818자). `send_slack_message`/`send_gmail`은 정의만 하고 실제 호출하지 않음(중복 발송 방지). src 폴더 분리는 하지 않음(STEP 18 예정). 사용자의 Notebook 실행 확인이 필요하여 STEP 17 상태는 `IN_PROGRESS`.
- **2026-09-23**: 사용자가 STEP 16 준비 Code Cell을 직접 실행하여 `.env` 존재, `GMAIL_ADDRESS`/`GMAIL_APP_PASSWORD`/`GMAIL_TO` 존재 여부 모두 `True`, 보고서 파일/메일 제목/본문 길이(2230자) 확인, `EmailMessage` 생성 완료를 확인. 이에 따라 STEP 16의 기존 3-Cell(새 STEP 추가 없이 최소 수정)에 실제 Gmail SMTP 발송 로직 추가: `smtplib.SMTP_SSL("smtp.gmail.com", 465)` 연결 → 앱 비밀번호 로그인 → `send_message()`로 1건만 발송(반복문 없음), `SMTPAuthenticationError`/`SMTPException`/일반 `Exception`을 구분해 오류 안내, `GMAIL_APP_PASSWORD` 값은 어디에도 출력하지 않음을 재검증. Markdown 제목을 "STEP 16. Gmail 발송 준비" → "STEP 16. Gmail 발송"으로 변경하고 "실행할 때마다 실제 메일 1건 발송" 경고 추가. Slack(STEP 15)은 재수정하지 않았고 OpenAI도 재호출하지 않음. **Claude Code는 이 Code Cell을 직접 실행하지 않았음** — 실제 발송 및 수신함 확인은 사용자 몫으로 남김. 사용자의 실제 실행 및 수신함 확인 전까지 STEP 16 상태는 `IN_PROGRESS` 유지.
- **2026-09-23**: 사용자가 STEP 15 Code Cell을 직접 실행하여 실제 Slack 채널에서 메시지 도착(한글 정상, 보고서 내용/통계/공고 목록 정상 표시)을 확인 — STEP 15 `DONE` 처리. 확인 과정에서 발견된 개선 사항 2건 처리: (1) Markdown 헤더(`#`/`##`/`###`)가 Slack에서 기호 그대로 보이던 문제를 STEP 15 코드에서 Slack 전송용 문자열만 별도로 `*텍스트*` 형식으로 변환하도록 최소 수정(원본 보고서 파일은 그대로 유지), (2) STEP 14/15의 실제 생성 보고서와 Notebook Cell 전체를 검사했으나 Gemini 관련 잘못된 provider 명칭은 발견되지 않아 별도 수정 없음(남아있는 Gemini 언급은 STEP 05~11의 "이번 STEP에서 하지 않는 것" 목록뿐이며 전체 삭제 대상이 아님). Notebook에 STEP 16(Gmail 발송 준비) 3-Cell 추가 — `.env`의 `GMAIL_ADDRESS`/`GMAIL_APP_PASSWORD`/`GMAIL_TO` 존재 확인과 `EmailMessage` 객체 생성까지만 진행, 실제 SMTP 연결/발송 코드는 작성하지 않음. `.env.example`에 Gmail 3개 항목 추가. 현재 `.env`에 Gmail 값이 없어(`False`) 실제 EmailMessage 생성 전 사용자의 값 입력이 필요. 사용자의 Notebook 실행 확인이 필요하여 STEP 16 상태는 `IN_PROGRESS`.
- **2026-09-23**: STEP 14(Markdown 보고서 생성) `DONE` 처리. Notebook에 STEP 15(Slack 발송) 3-Cell 추가, `reports/` 폴더의 최신 `weekly_ax_jobs_*.md` 파일을 읽어 `.env`의 `SLACK_WEBHOOK_URL`로 `requests.post()` 전송하는 코드 작성 (Webhook URL 미출력, 보고서 재생성/OpenAI 재호출 없음). 현재 환경 확인 결과 `.env`의 `SLACK_WEBHOOK_URL`은 설정되어 있음(`True`)이 확인되었으나 `reports/` 폴더는 아직 생성되지 않은 상태 — 코드는 두 경우 모두(Webhook 없음/보고서 없음) 안내 메시지만 출력하고 안전하게 종료하도록 방어적으로 작성됨. 사용자의 STEP 14 실행(보고서 생성), STEP 15 Notebook 실행 및 Slack 채널 확인이 필요하여 상태는 `IN_PROGRESS`.
- **2026-09-23**: 사용자가 STEP 13 Code Cell을 직접 실행하여 GS리테일 공고 원문과 STEP 12 OpenAI 응답을 비교 — 원본과 일치(GS리테일/MD/물류/AX 담당), 근거 부족("AI·데이터 기반 혁신" 등 확장 해석), 과도한 해석 일부 있음, 최종 판단 "수정 후 사용 가능"으로 확정 — STEP 13 `DONE` 처리. Notebook에 STEP 14(Markdown 보고서 생성) 3-Cell 추가, pandas로 다시 계산한 통계와 검증된 OpenAI 예시 1건을 조합해 `reports/weekly_ax_jobs_{날짜}.md`를 생성하는 코드 작성 (OpenAI 추가 호출 없음, 응답 변수 없으면 AI 섹션 생략 처리). 사용자의 Notebook 실행 확인이 필요하여 상태는 `IN_PROGRESS`.
- **2026-09-23**: 사용자가 STEP 12 Code Cell을 직접 실행하여 `.env`/`OPENAI_API_KEY`/`OPENAI_MODEL` 로드 확인, `related_jobs.iloc[0]`(GS리테일) 1건에 대해 OpenAI Responses API 호출 성공(응답 길이 174) 및 실제 응답 텍스트 출력을 확인 — STEP 12 `DONE` 처리. Notebook에 STEP 13(OpenAI 응답 검증) 3-Cell 추가, STEP 12의 `sample_job`/`response` 변수를 재사용하여 새 API 호출 없이 원본 데이터와 응답을 나란히 출력하는 코드 작성, 자동 점수화 없이 사람이 직접 검증하도록 Markdown 구조화. 사용자의 실제 검증 판단이 필요하여 상태는 `IN_PROGRESS`.
- **2026-09-23**: STEP 12를 Gemini API 기준에서 **OpenAI API 기준으로 변경**. Notebook STEP 12의 기존 3-Cell을 그대로 교체(새 STEP 추가 없음)하여 `google.genai`/`GEMINI_API_KEY` 사용 코드를 제거하고, 공식 OpenAI Python SDK(`openai`, v3.19.0 설치 확인)의 **Responses API**(`client.responses.create`)로 재작성. `.env`의 `OPENAI_API_KEY`/`OPENAI_MODEL`만 사용하며 모델명은 코드에 하드코딩하지 않음. `.env.example`에 OpenAI 항목 추가. STEP 12 상태는 사용자의 실제 API 호출 확인 전까지 `IN_PROGRESS` 유지. (PROJECT_SPEC.md 등 다른 문서의 Gemini 문구는 별도 정리 작업으로 남겨둠)
- **2026-09-23**: 사용자 실행 확인으로 STEP 11 `DONE` 처리(신규 5건 중 5건 모두 관련 공고로 필터링됨). STEP 12 Gemini API 연동 3-Cell 작성 완료. 사용자 실행 및 API 호출 응답 확인 대기 상태로 STEP 12는 `IN_PROGRESS`. STEP 13 이후 작업은 진행하지 않음.
- **2026-09-23**: 사용자 실행 확인을 근거로 STEP 10 `DONE` 처리(신규 5건, 분포 및 날짜 정상). STEP 11 제목 기반 필터링 3-Cell 추가. 사용자 실행 및 결과 해석 대기 상태이므로 STEP 11은 `IN_PROGRESS`. STEP 12 이후 작업은 진행하지 않음.

- **2026-09-23**: 사용자가 STEP 09 Code Cell을 직접 실행하여 이력 파일 없음(첫 실행) → 기존 URL 0건, 현재 5건 전체가 신규 공고로 판별됨을 확인 — STEP 09 `DONE` 처리. Notebook에 STEP 10(신규 공고 기본 분석) 3-Cell 추가, `new_jobs` 대상 회사별/지역별/경력별/검색어별 `value_counts()` 및 날짜 컬럼 확인 코드 작성. 사용자의 Notebook 실행 확인이 필요하여 상태는 `IN_PROGRESS`.
- **2026-09-23**: 사용자가 STEP 08 Code Cell을 직접 실행하여 `job_url` 기준 중복 개수 0건, 제거 전/후 shape `(5, 9)` 동일함을 확인 — STEP 08 `DONE` 처리. Notebook에 STEP 09(신규 공고 판별) 3-Cell 추가, `data/processed/jobs_history.csv` 이력 파일과 현재 `job_url`을 비교하는 코드 작성 (첫 실행이라 이력 파일 없음 → 전체 신규로 판단). 사용자의 Notebook 실행 확인이 필요하여 상태는 `IN_PROGRESS`.
- **2026-09-23**: 사용자가 Notebook에서 STEP 05 → STEP 06 → STEP 07 Code Cell을 순서대로 직접 실행하여 `posted_date`/`closing_date`가 정상 수집되고 `isna().sum()` 결과 9개 컬럼 모두 결측 0건임을 확인 — STEP 07 `DONE` 처리. Notebook에 STEP 08(중복 공고 확인 및 제거) 3-Cell 추가, `job_url` 기준 `duplicated()`/`drop_duplicates()` 코드 작성. 사용자의 Notebook 실행 확인이 필요하여 상태는 `IN_PROGRESS`.
- **2026-09-23**: 사용자가 STEP 06 Code Cell을 직접 실행하여 `DataFrame shape: (5, 9)`, 9개 컬럼, 5건의 실제 데이터를 확인 — STEP 06 `DONE` 처리. Notebook에 STEP 07(결측값/문자열/날짜 상태 확인) 3-Cell 추가, `df` 변수를 사용해 `isna().sum()`, 문자열 `strip()`, `collected_at`의 `pd.to_datetime()` 변환을 수행하는 코드 작성. `posted_date`/`closing_date`는 억지로 채우지 않고 결측 상태만 확인. 사용자의 Notebook 실행 확인이 필요하여 상태는 `IN_PROGRESS`.
- **2026-09-23**: 사용자가 STEP 05 Code Cell을 직접 실행하여 `찾은 채용공고 후보 수: 20`, `수집 건수: 5`와 5건의 실제 데이터(GS리테일/에스코어/㈜NAVER×2/㈜슈프리마)를 확인 — STEP 05 `DONE` 처리. Notebook에 STEP 06(DataFrame 생성) 3-Cell 추가, `jobs` 리스트를 `pd.DataFrame(jobs)`로 변환하는 코드 작성. 사용자의 Notebook 실행 확인이 필요하여 상태는 `IN_PROGRESS`.
- **2026-09-23**: 사용자가 STEP 04 Code Cell을 `TEST_URL = "https://www.jobkorea.co.kr/Search/?stext=ax&tabType=recruit"`로 직접 실행하여 `Status Code: 200`, HTML 정상 반환 확인 — STEP 04 `DONE` 처리. Notebook에 STEP 05(소량 채용공고 데이터 수집) 3-Cell 추가, 실제 HTML 구조(`data-sentry-component="CardJob"` 등)를 확인해 만든 선택자로 코드를 사전 실행하여 GS리테일/에스코어/㈜NAVER 등 5건을 확보. 사용자의 Notebook 재실행 및 브라우저 대조가 필요하여 상태는 `IN_PROGRESS`.
- **2026-09-23**: 사용자가 STEP 03 Code Cell을 직접 실행하여 `컬럼 수: 9`, `DataFrame shape: (0, 9)` 확인 — STEP 03 `DONE` 처리. Notebook에 STEP 04(채용공고 페이지 접근 테스트) 3-Cell 추가, `TEST_URL`이 비어 있어 상태는 `IN_PROGRESS`(사용자의 URL 입력 및 실행 대기 중).
- **2026-09-23**: 사용자 확인 기준으로 STEP 02(Jupyter 환경 준비) `DONE` 처리 — ipykernel 등록(`ax-job-agent` / "Python (ax-job-agent)") 완료, VS Code 커널 선택 확인, `notebooks/ax_job_pipeline.ipynb` 생성 확인. 현재 STEP을 STEP 03(수집 데이터 명세)으로 갱신, 상태 `NOT_STARTED`.
- **2026-09-23**: 실제 환경 재확인. `.venv` 및 기본 패키지 설치는 확인됨(STEP 00~01 DONE). Jupyter 커널(`ax-job-agent`)은 아직 등록되지 않아 STEP 02는 `NOT_STARTED`로 기록. `docs/` 폴더와 3개 문서, 루트 `README.md` 생성.

## 특이사항

- 프로젝트 루트 경로: `C:\dev\claude-code-agent-course-practice` (2026-09-23 저장소 이관 이후 현재 경로. 이관 전에는 `C:\dev\claude-code-agent-course\chapter11\ax-job-agent`였음 — 아래 "Repository migration" 항목 참고)
- Git 브랜치: `main` (practice 저장소의 기본 브랜치. 이관 전 원본 저장소에서는 `ax-job-agent` 브랜치를 사용했음)
- STEP 05에서 확인된 사실: jobkorea 검색 결과 목록(list) 화면에는 `posted_date`(등록일)와 `closing_date`(마감일) 정보가 존재하지 않음. 이 두 컬럼은 상세 페이지(`job_url`)에 들어가야 확인 가능하며, 상세 페이지 순회는 STEP 05 범위 밖이라 이번 STEP에서는 `None`으로 남겨둠.
- `src/`, `data/`, `reports/`, `.env.example`, `.gitignore`, `requirements.txt`, `main.py`는 아직 생성되지 않은 "예정" 항목 (자세한 내용은 `PROJECT_SPEC.md` 6번 참고).
