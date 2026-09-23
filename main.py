"""AX Job Agent - 실행 관리자 (main.py)

이 파일은 세부 기능을 직접 구현하지 않습니다.
src/ 아래에 이미 검증된 함수들을 불러와서, 정해진 순서대로 호출하는
"실행 관리자(orchestrator)" 역할만 합니다.

이번 단계에서는 Slack/Gmail 자동 발송과 OpenAI 호출을 하지 않습니다.
"""

import os
from datetime import date
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

from src.analyzer import filter_related_jobs
from src.reporter import build_markdown_report
from src.notifier import send_slack_message, send_gmail

PROJECT_ROOT = Path(__file__).resolve().parent
ENV_PATH = PROJECT_ROOT / ".env"

# 환경변수로 켜고 끌 수 있습니다. 기본값은 항상 false(외부 전송 없음)입니다.
SEND_SLACK = os.getenv("SEND_SLACK", "false").lower() == "true"
SEND_GMAIL = os.getenv("SEND_GMAIL", "false").lower() == "true"

# Notebook STEP 11에서 사용한 키워드 목록과 동일합니다.
RELATED_KEYWORDS = [
    "ax", "ai", "인공지능", "데이터 분석", "생성형 ai", "생성형ai",
    "llm", "machine learning", "머신러닝", "data scientist",
    "데이터 사이언티스트", "ai engineer", "ai 엔지니어",
]

REQUIRED_COLUMNS = {
    "company_name",
    "job_title",
    "career",
    "location",
    "posted_date",
    "closing_date",
    "job_url",
    "search_keyword",
    "collected_at",
}


def main():
    print("=== AX Job Agent ===\n")

    # 1. .env 로드
    load_dotenv(ENV_PATH)

    # 2. 입력 CSV 확인 (data/processed/new_jobs.csv 고정 경로)
    input_path = PROJECT_ROOT / "data" / "processed" / "new_jobs.csv"

    if not input_path.exists():
        print("data/processed/new_jobs.csv 파일이 없습니다.")
        return

    print("입력 파일:", input_path.name)

    # 3. pandas로 데이터 읽기
    input_df = pd.read_csv(input_path)

    # 4. 필수 컬럼 검사
    missing_columns = REQUIRED_COLUMNS - set(input_df.columns)
    if missing_columns:
        print("필수 컬럼이 부족합니다.")
        print("누락 컬럼:", missing_columns)
        return

    print("전체 공고 수:", len(input_df))

    # 5. 관련 공고 필터링 (analyzer)
    related_jobs = filter_related_jobs(input_df, RELATED_KEYWORDS)
    print("관련 공고 수:", len(related_jobs))

    # 6. Markdown 보고서 생성 (reporter)
    #    이번 STEP에서는 검증된 OpenAI 예시를 새로 만들지 않습니다.
    report_text = build_markdown_report(input_df, related_jobs)

    # 7. 보고서 저장
    reports_dir = PROJECT_ROOT / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    report_date = date.today().isoformat()
    report_path = reports_dir / f"weekly_ax_jobs_{report_date}.md"
    report_path.write_text(report_text, encoding="utf-8")

    print("\n보고서 생성 완료:")
    print(report_path.relative_to(PROJECT_ROOT))

    # 8. Slack 전송 여부 (기본 OFF)
    if SEND_SLACK:
        slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
        if not slack_webhook_url:
            print("\nSlack 전송: SLACK_WEBHOOK_URL이 없어 건너뜁니다.")
        else:
            response = send_slack_message(slack_webhook_url, report_text)
            print("\nSlack 전송 요청 완료. 상태 코드:", response.status_code)
    else:
        print("\nSlack 전송: 생략")

    # 9. Gmail 전송 여부 (기본 OFF)
    if SEND_GMAIL:
        gmail_address = os.getenv("GMAIL_ADDRESS")
        gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")
        gmail_to = os.getenv("GMAIL_TO")

        if not gmail_address or not gmail_app_password or not gmail_to:
            print("Gmail 전송: GMAIL_ADDRESS/GMAIL_APP_PASSWORD/GMAIL_TO 중 일부가 없어 건너뜁니다.")
        else:
            subject = f"[AX 채용 동향] {report_path.stem}"
            send_gmail(gmail_address, gmail_app_password, gmail_to, subject, report_text)
            print("Gmail 전송 완료.")
    else:
        print("Gmail 전송: 생략")

    print("\n파이프라인 실행 완료")


if __name__ == "__main__":
    main()
