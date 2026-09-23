"""데이터 분석 관련 함수 (STEP 17에서 Notebook으로 검증한 로직을 그대로 옮김)."""


def filter_related_jobs(df, keywords):
    """
    df의 job_title에 keywords 중 하나 이상이 포함된 행만 반환합니다.
    (STEP 11에서 검증한 로직과 동일한 방식 — matched_keywords 컬럼 생성 방식 유지)
    """
    def find_matched_keywords(title):
        title_lower = str(title).lower()
        return [kw for kw in keywords if kw.lower() in title_lower]

    filtered = df.copy()
    filtered["matched_keywords"] = filtered["job_title"].apply(find_matched_keywords)
    related_mask = filtered["matched_keywords"].apply(len) > 0
    return filtered.loc[related_mask].copy()
