from langchain_core.prompts import PromptTemplate

linkedin_prompt = PromptTemplate(
    template="""
You are a professional content strategist specializing in high-performing LinkedIn content.

Write a compelling and human-sounding LinkedIn post about the following topic:
Topic: {topic}

Guidelines:
- Begin with a personal hook or short story to grab attention.
- Clearly communicate the core value or insight in a relatable way.
- Keep tone authentic, professional, and a bit conversational — not robotic.
- Aim to inspire, educate, or challenge thinking.
- Use short paragraphs and line breaks for readability.
- End with a thoughtful CTA or question to spark comments or discussion.

Do NOT include hashtags or links. Output only the post body.
""",
input_variables=["topic"]
)
