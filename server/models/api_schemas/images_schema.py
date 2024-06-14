from pydantic import BaseModel


class AnalyzePose(BaseModel):
    image: str
    
class EstimatePoseProb(BaseModel):
    image: str
    pose_to_check: str
