from langchain_core.prompts import PromptTemplate

post_improvement_prompt = PromptTemplate(
    input_variables=["formatted_review"],
    template="""
You are a professional content strategist and copywriter.

Below is a complete editorial review of draft posts for multiple platforms, including feedback from the CMO.

{formatted_review}

Your task is to revise **each post individually** based on the review.

Guidelines:
- Apply review suggestions carefully.
- Improve tone, clarity, and engagement.
- Keep platform-specific tone and limits in mind (e.g., tweet length).
- Keep core message unchanged.

Output Format:

**Improved Twitter Post**  
...

**Improved LinkedIn Post**  
...

**Improved Facebook Post**  
...

**Improved Blog Post**  
...
"""
)
