from datetime import datetime
from typing import Optional, Sequence

from pydantic import BaseModel


class Person(BaseModel):
    personid: int
    plastname: str
    pfirstname: str
    psurname: str
    ppsex: int
    isuser: bool
    pilogin: str
    pipassword: str
    caid: str
    caidname: str
    rspostid: str
    rspostidname: str
    personemail: str
    pstatus: int
    pextcode: str


class Persons:
    def __init__(self, persons: Sequence[Person], count: int):
        self._persons = persons
        self.count = count

    def __getitem__(self, key: int) -> Person:
        return self._persons[key]


class Measure(BaseModel):
    meid: int
    mename: str
    medescription: str
    metype: str
    mecode: str
    mestatus: str
    mestartdate: Optional[datetime] = None
    meenddate: Optional[datetime] = None
    meeduform: Optional[int] = None
    mecontenttype: Optional[int] = None
    testid: Optional[str] = None
    testidname: Optional[str] = None
    ugrid: Optional[int] = None
    ugridname: Optional[str] = None
    mepasses: Optional[int] = None

    def __str__(self):
        result = f"{self.mename}\n"
        if self.mestartdate:
            result += f"Начало: {self.mestartdate.strftime('%d.%m.%Y')}\n"
        if self.meenddate:
            result += f"Окончание: {self.meenddate.strftime('%d.%m.%Y')}\n"
        return result


class Measures:
    def __init__(self, measures: Sequence[Measure], count: int):
        self._measures = measures
        self.count = count

    def __getitem__(self, key: int) -> Measure:
        return self._measures[key]


class Member(BaseModel):
    isaccess: bool
    meid: int
    meidname: str
    mmfinishstatus: int
    mmid: int
    personid: int
    personidname: str

    def __str__(self):
        return self.personidname


class Members:
    def __init__(self, members: Sequence[Member], count: int):
        self._members = members
        self.count = count

    def __getitem__(self, key: int) -> Member:
        return self._members[key]

    def __str__(self):
        return "\n".join([member.personidname for member in self._members])


class Tutor(BaseModel):
    isaccess: bool
    meid: int
    meidname: str
    mtid: int
    personid: int
    personidname: str

    def __str__(self):
        return self.personidname


class Tutors:
    def __init__(self, tutors: Sequence[Tutor], count: int):
        self._tutors = tutors
        self.count = count

    def __getitem__(self, key: int) -> Tutor:
        return self._tutors[key]

    def __str__(self):
        return "\n".join([tutor.personidname for tutor in self._tutors])
