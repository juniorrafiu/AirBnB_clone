from models.base_model import BaseModel
class Review(BaseModel):
    text = ''
    user_id = ''
    place_id = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)