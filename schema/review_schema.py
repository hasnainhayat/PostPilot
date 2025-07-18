from pydantic import BaseModel

from .review_item import reviewItem

class Review(BaseModel):
    review_items:list[reviewItem]
    summary_comment:str
    specific_weaknesses_or_inconsistencies:str

review=Review