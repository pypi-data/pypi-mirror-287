from datetime import datetime
from typing import Optional, Literal

from .base_api import BaseAPI
from .models import (
    Measure,
    Person,
    Measures,
    Persons,
    Members,
    Member,
    Tutors,
    Tutor
)


class VirtualRoom(BaseAPI):
    def __init__(
            self,
            base_link: str,
            secret_key: str,
            app_id: str
    ):
        super().__init__(
            base_link,
            secret_key,
            app_id
        )

    async def get_persons(
            self,
            limit: int = 200,
            offset: int = 0
    ) -> Optional[Persons]:
        """
        Получение информации о физических лицах
        :rtype: list[Person]
        :param limit: Количество записей (200 максимально)
        :param offset: Сдвиг страницы
        :return: List of Persons
        """
        persons = await self._get(
            route="/service/v2/persons",
            params={
                "limit": limit,
                "offset": offset,
            }
        )
        if persons:
            return Persons(
                [Person(**person) for person in persons['data']],
                persons['count']
            )
        else:
            return None

    async def get_person(self, person_id: int) -> Optional[Person]:
        """
        Получение информации о физическом лице
        :rtype: Person
        :param person_id: идентификатор физического лица
        :return: Person
        """
        person = await self._get(
            route=f"/service/v2/persons/{person_id}"
        )
        if person:
            return Person(**person)
        else:
            return None

    async def get_measures(
            self,
            limit: int = 200,
            offset: int = 0
    ) -> Optional[Measures]:
        """
        Получение информации о мероприятиях
        :rtype: list[Measure]
        :param limit: Количество записей (200 максимально)
        :param offset: Сдвиг страницы
        :return: List of Measures
        """
        measures = await self._get(
            route="/service/v2/measures",
            params={
                "limit": limit,
                "offset": offset,
            }
        )
        if measures:
            return Measures(
                [Measure(**measure) for measure in measures['data']],
                measures['count']
            )
        else:
            return None

    async def get_measure(self, measure_id: int) -> Optional[Measure]:
        """
        Получение информации о мероприятии
        :rtype: Measure
        :param measure_id: идентификатор мероприятия
        :return: Measure
        """
        measure = await self._get(
            route=f"/service/v2/measures/{measure_id}"
        )
        if measure:
            return Measure(**measure)
        else:
            return None

    async def get_members(
            self,
            measure_id: int,
            limit: int = 200,
            offset: int = 0
    ) -> Optional[Members]:
        """
        Получение информации об участниках мероприятия
        :rtype: Members
        :param measure_id: идентификатор мероприятия
        :param limit: Количество записей (200 максимально)
        :param offset: Сдвиг страницы
        :return: List of Members
        """
        members = await self._get(
            route=f"/service/v2/measures/{measure_id}/members",
            params={
                "limit": limit,
                "offset": offset,
            }
        )
        if members:
            return Members(
                [Member(**member) for member in members['data']],
                members['count']
            )
        else:
            return None

    async def get_tutors(
            self,
            measure_id: int,
            limit: int = 200,
            offset: int = 0
    ) -> Optional[Tutors]:
        """
        Получение информации о преподавателях мероприятия
        :rtype: Tutors
        :param measure_id: идентификатор мероприятия
        :param limit: Количество записей (200 максимально)
        :param offset: Сдвиг страницы
        :return: List of tutors
        """
        tutors = await self._get(
            route=f"/service/v2/measures/{measure_id}/tutors",
            params={
                "limit": limit,
                "offset": offset,
            }
        )
        if tutors:
            return Tutors(
                [Tutor(**tutor) for tutor in tutors['data']],
                tutors['count']
            )
        else:
            return None

    async def get_measures_info(self):
        measures_info = await self._get(
            route="/service/v2/measures/info"
        )
        return measures_info

    async def create_measure(
            self,
            measure: Measure,
    ) -> Optional[Measure]:
        """
        Добавление мероприятия
        :param measure: объект мероприятия
        :return: созданное мероприятие
        """
        created_measure = await self._post(
            "/service/v2/measures",
            data=measure.model_dump_json(indent=4, exclude_none=True),
        )
        if created_measure:
            return Measure(**created_measure)

    async def delete_measure(self, measure_id: int) -> Optional[bool]:
        """
        Удаление мероприятия
        :param measure_id: идентификатор мероприятия
        """
        measure = await self._delete(
            route=f"/service/v2/measures/{measure_id}"
        )
        if measure:
            return True
        else:
            return False
