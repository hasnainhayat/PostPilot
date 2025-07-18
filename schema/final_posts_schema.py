from pydantic import BaseModel, Field


class FinalPostsSchema(BaseModel):
    facebook_post:str=Field(description="Please provide Improved facebook post")
    twitter_post:str=Field(description="Please provide Improved twitter post")
    linkedin_post:str=Field(description="Please provide Improved linkedin post")
    blog_post:str=Field(description="Please provide Improved blog post")

finalPosts=FinalPostsSchema