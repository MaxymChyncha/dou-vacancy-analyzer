from dataclasses import dataclass, fields


@dataclass
class Vacancy:
    title: str
    location: str
    experience: str
    technologies: str


VACANCY_FIELDS = [field.name for field in fields(Vacancy)]
