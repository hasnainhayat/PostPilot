from langchain_core.prompts import PromptTemplate

review_prompt = PromptTemplate(
    template="""
You are a Chief Marketing Officer and editorial lead at a content agency.

Your team has written platform-specific posts for the same topic.  
Review all of them and provide structured feedback.

--- Twitter Post ---
{twitter}

--- LinkedIn Post ---
{linkedin}

--- Facebook Post ---
{facebook}

--- Blog Post ---
{blog}

Instructions:
- Evaluate each post individually on:
  - Tone (fit for platform)
  - Clarity
  - Engagement or emotional appeal
- Highlight specific weaknesses or inconsistencies
- Suggest improvements for each platform
- Note if the messaging feels unified or disjointed

Output format (you may follow this structure):

**Twitter Review**
Tone: ....
Clarity Score: X (X is an integer between 0 and 5)  
Suggestions: ...

**LinkedIn Review**
...

**Facebook Review**
...

**Blog Review**
...

Also include an overall summary comment about cross-platform consistency and improvements.
""",
    input_variables=["twitter", "linkedin", "facebook", "blog"]
)
