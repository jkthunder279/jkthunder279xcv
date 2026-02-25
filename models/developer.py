from dataclasses import dataclass

@dataclass
class FinancialData:
    symbol: str
    price: float
    volume: int
    market_cap: float

@dataclass
class NewsData:
    title: str
    description: str
    publication_date: str
    source: str

@dataclass
class Developer:
    name: str
    experience_years: int
    skills: list
    email: str
