from langchain_core.runnables import RunnableParallel

from llm.llm_init import get_model
from utils.pasrsers import stringOutputParser
from prompts.prompt_registery import facebook_prompt,twitter_prompt,blog_prompt,linkedin_prompt
model=get_model()
post_generation_chain= RunnableParallel(
    {
        "twitter": twitter_prompt | model | stringOutputParser,
        "linkedin":linkedin_prompt | model | stringOutputParser,
        "blog": blog_prompt | model | stringOutputParser,
        "facebook":facebook_prompt | model | stringOutputParser

    }
)

