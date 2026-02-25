from dataclasses import dataclass

@dataclass
class RatingComponents:
    design: float
    usability: float
    performance: float

@dataclass
class DeveloperRating:
    rating: float
    components: RatingComponents
