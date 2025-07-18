from prompts.prompt_registery import post_improvement_prompt
from schema.final_posts_schema import finalPosts

from llm.llm_init import get_model


model=get_model().with_structured_output(finalPosts)

post_improvement_chain= post_improvement_prompt | model

