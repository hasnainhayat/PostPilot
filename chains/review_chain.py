from langchain_core.runnables import RunnableParallel

from .post_generation_chain import post_generation_chain
from llm.llm_init import get_model
from utils.pasrsers import stringOutputParser
from prompts.prompt_registery import review_prompt
from schema.review_schema import review
model=get_model().with_structured_output(review)

review_chain= post_generation_chain | review_prompt | model
