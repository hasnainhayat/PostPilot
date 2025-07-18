from pydantic import BaseModel,Field

class ReviewItem(BaseModel):
    platform:str=Field(description="Please provide the platform for which this post is written e.g blog,twitter,linkedin,facebook")
    tone:str=Field(description="Please provide what is tone of the post and whether it is suitable for this post and platform")
    clarity_score:int=Field(description="Please provide the clarity score for this post", le=5,ge=0)
    suggested_improvements:str=Field(description="Please list down the suggested imporovements for this post for current platform")
    original_post_content:str=Field(description="Please provide the original post content exactly as provided")

reviewItem=ReviewItem