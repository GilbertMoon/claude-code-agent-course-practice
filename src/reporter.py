"""Markdown 보고서 생성 관련 함수 (STEP 17에서 Notebook으로 검증한 로직을 그대로 옮김)."""

from datetime import date


def build_markdown_report(new_jobs, related_jobs, ai_example=None):
    """
    신규 공고(new_jobs)와 관련 공고(related_jobs)를 바탕으로
    주간 AX 채용 동향 Markdown 문자열을 만들어 반환합니다. (STEP 14 로직과 동일, 파일 저장은 하지 않음)

    ai_example: {"company_name": ..., "job_title": ..., "response_text": ...} 형태의 dict.
                검증된 OpenAI 응답이 없으면 None으로 둡니다.
    """
    new_count = len(new_jobs)
    related_count = len(related_jobs)
    related_ratio = (related_count / new_count * 100) if new_count > 0 else 0

    company_counts = new_jobs["company_name"].value_counts()
    location_counts = new_jobs["location"].value_counts()
    career_counts = new_jobs["career"].value_counts()

    report_date = date.today().isoformat()
    lines = []

    lines.append("# 주간 AX 채용 동향")
    lines.append("")
    lines.append(f"실행일: {report_date}")
    lines.append("")

    lines.append("## 1. 이번 주 요약")
    lines.append("")
    lines.append(f"- 신규 공고: {new_count}건")
    lines.append(f"- 관련 공고: {related_count}건")
    lines.append(f"- 관련 공고 비율: {related_ratio:.1f}%")
    lines.append("- 검색어: ax")
    lines.append("")

    lines.append("## 2. 회사별 공고 수")
    lines.append("")
    for name, count in company_counts.items():
        lines.append(f"- {name}: {count}건")
    lines.append("")

    lines.append("## 3. 지역별 공고 수")
    lines.append("")
    for name, count in location_counts.items():
        lines.append(f"- {name}: {count}건")
    lines.append("")

    lines.append("## 4. 경력 조건별 공고 수")
    lines.append("")
    for name, count in career_counts.items():
        lines.append(f"- {name}: {count}건")
    lines.append("")

    lines.append("## 5. 관련 공고 목록")
    lines.append("")
    for _, job in related_jobs.head(5).iterrows():
        lines.append(f"### {job['company_name']} — {job['job_title']}")
        lines.append("")
        lines.append(f"- 경력: {job['career']}")
        lines.append(f"- 지역: {job['location']}")
        lines.append(f"- 등록일: {job['posted_date']}")
        lines.append(f"- 마감일: {job['closing_date']}")
        lines.append(f"- 공고 링크: {job['job_url']}")
        lines.append("")

    lines.append("## 6. OpenAI 검증 예시")
    lines.append("")
    if ai_example is not None:
        lines.append(f"- 회사명: {ai_example['company_name']}")
        lines.append(f"- 공고 제목: {ai_example['job_title']}")
        lines.append("")
        lines.append("**OpenAI 응답:**")
        lines.append("")
        lines.append(ai_example["response_text"])
        lines.append("")
        lines.append("**검증 결과:** 수정 후 사용 가능")
        lines.append("")
        lines.append(
            "> OpenAI 응답에는 원본 필드에서 직접 확인할 수 없는 "
            "확장 해석이 일부 포함될 수 있으므로, 최종 보고서 사용 전 원문 확인이 필요하다."
        )
    else:
        lines.append("현재 커널에 검증된 AI 응답이 없습니다. (OpenAI API를 추가로 호출하지 않았습니다.)")
    lines.append("")

    lines.append("## 7. 데이터 기준")
    lines.append("")
    lines.append("- 검색어: ax")
    lines.append("- 수집 페이지: 1페이지")
    lines.append("- 분석 대상: 현재 신규 공고")
    lines.append("- 신규 판별 기준: job_url")
    lines.append("- 관련 공고 필터 기준: 제목의 키워드 포함 여부")
    ai_count = 1 if ai_example is not None else 0
    lines.append(f"- AI 검증 공고 수: {ai_count}건")
    lines.append("")

    lines.append("## 8. 주의사항")
    lines.append("")
    lines.append("- 현재 실습 데이터는 5건뿐이므로 시장 전체를 대표하지 않는다.")
    lines.append("- 검색어도 현재 ax 하나만 사용했다.")
    lines.append("- 실제 지원 전 원문 채용공고를 다시 확인해야 한다.")
    lines.append("- OpenAI 결과는 원본에 없는 내용을 확장 해석할 수 있다.")
    lines.append("")

    return "\n".join(lines)
