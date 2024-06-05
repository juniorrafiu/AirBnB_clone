"""
the module of Review.
it inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): the id of Place.
        user_id (str): the id of User.
        text (str): the review.
    """
    text = ''
    user_id = ''
    place_id = ''
