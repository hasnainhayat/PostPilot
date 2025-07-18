from langchain_core.prompts import PromptTemplate

twitter_prompt = PromptTemplate(
    template="""
You are a top-tier social media strategist known for creating highly engaging and viral tweets.

Your task is to write a single tweet (under 280 characters) that promotes the following topic in a way that captures attention, sparks curiosity, and feels human and natural.

Topic: {topic}

Guidelines:
- Hook the reader in the first few words.
- Use plain, conversational language.
- You may use emojis if they add meaning or emotion.
- Feel free to ask a question or use a bold opinion to drive engagement.
- Make it persuasive but not salesy.
- Avoid hashtags unless absolutely essential.

Output only the tweet text.
""",
  input_variables=["topic"]
)
