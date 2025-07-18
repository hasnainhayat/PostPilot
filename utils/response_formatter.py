from schema.review_schema import review


def format_review_for_prompt(review: review) -> str:
    platform_blocks = "\n\n".join([
        f"--- {item.platform.capitalize()} Post ---\n"
        f"Original Content:\n{item.original_post_content}\n\n"
        f"Tone: {item.tone}\n"
        f"Clarity Score: {item.clarity_score}/5\n"
        f"Suggested Improvements: {item.suggested_improvements}"
        for item in review.review_items
    ])

    return f"""{platform_blocks}

--- CMO Review Summary ---
{review.summary_comment}

--- Identified Weaknesses ---
{review.specific_weaknesses_or_inconsistencies}
"""
