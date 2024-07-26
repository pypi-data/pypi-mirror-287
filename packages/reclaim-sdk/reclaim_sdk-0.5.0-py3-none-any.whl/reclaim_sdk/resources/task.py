# reclaim_sdk/resources/task.py

from pydantic import Field, field_validator
from datetime import datetime
from typing import ClassVar, Optional
from enum import Enum
from reclaim_sdk.resources.base import BaseResource
from reclaim_sdk.client import ReclaimClient


class PriorityEnum(str, Enum):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"


class TaskStatus(str, Enum):
    NEW = "NEW"
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    CANCELLED = "CANCELLED"
    ARCHIVED = "ARCHIVED"


class Task(BaseResource):
    ENDPOINT: ClassVar[str] = "/api/tasks"

    title: Optional[str] = Field(None, description="Task title")
    notes: Optional[str] = Field(None, description="Task notes")
    eventCategory: str = Field("WORK", description="Event category")
    eventSubType: Optional[str] = Field(None, description="Event subtype")
    timeChunksRequired: Optional[int] = Field(None, description="Time chunks required")
    minChunkSize: Optional[int] = Field(None, description="Minimum chunk size")
    maxChunkSize: Optional[int] = Field(None, description="Maximum chunk size")
    priority: PriorityEnum = Field(None, description="Task priority")
    onDeck: bool = Field(False, description="Task is on deck")
    alwaysPrivate: bool = Field(False, description="Task is always private")
    status: Optional[TaskStatus] = Field(None, description="Task status")
    due: Optional[datetime] = Field(None, description="Due date")
    snoozeUntil: Optional[datetime] = Field(None, description="Snooze until date")
    index: Optional[float] = Field(None, description="Task index")

    @field_validator(
        "timeChunksRequired", "minChunkSize", "maxChunkSize", mode="before"
    )
    @classmethod
    def validate_chunks(cls, v):
        if v is not None:
            return int(v)
        return v

    @property
    def duration(self) -> Optional[float]:
        return self.timeChunksRequired / 4 if self.timeChunksRequired else None

    @duration.setter
    def duration(self, hours: float) -> None:
        self.timeChunksRequired = int(hours * 4)

    @property
    def min_work_duration(self) -> Optional[float]:
        return self.minChunkSize / 4 if self.minChunkSize else None

    @min_work_duration.setter
    def min_work_duration(self, hours: float) -> None:
        self.minChunkSize = int(hours * 4)

    @property
    def max_work_duration(self) -> Optional[float]:
        return self.maxChunkSize / 4 if self.maxChunkSize else None

    @max_work_duration.setter
    def max_work_duration(self, hours: float) -> None:
        self.maxChunkSize = int(hours * 4)

    @property
    def up_next(self) -> bool:
        return self.onDeck

    @up_next.setter
    def up_next(self, value: bool) -> None:
        self.onDeck = value

    def mark_complete(self) -> None:
        client = ReclaimClient()
        response = client.post(f"/api/planner/done/task/{self.id}")
        self.__dict__.update(self.from_api_data(response["taskOrHabit"]).__dict__)

    def mark_incomplete(self) -> None:
        client = ReclaimClient()
        response = client.post(f"/api/planner/unarchive/task/{self.id}")
        self.__dict__.update(self.from_api_data(response["taskOrHabit"]).__dict__)

    @classmethod
    def prioritize_by_due(cls) -> None:
        client = ReclaimClient()
        client.patch("/api/tasks/reindex-by-due")

    def prioritize(self) -> None:
        client = ReclaimClient()
        client.post(f"/api/planner/prioritize/task/{self.id}")
        self.update()

    def update(self) -> None:
        updated_task = self.get(self.id)
        self.__dict__.update(updated_task.__dict__)

    def add_time(self, hours: float) -> None:
        minutes = int(hours * 60)
        rounded_minutes = round(minutes / 15) * 15
        client = ReclaimClient()
        response = client.post(
            f"/api/planner/add-time/task/{self.id}", params={"minutes": rounded_minutes}
        )
        self.__dict__.update(self.from_api_data(response["taskOrHabit"]).__dict__)

    def clear_exceptions(self) -> None:
        client = ReclaimClient()
        response = client.post(f"/api/planner/clear-exceptions/task/{self.id}")
        self.__dict__.update(self.from_api_data(response["taskOrHabit"]).__dict__)

    def log_work(self, minutes: int, end: Optional[datetime] = None) -> None:
        client = ReclaimClient()
        params = {"minutes": minutes}
        if end:
            params["end"] = end.isoformat()
        response = client.post(f"/api/planner/log-work/task/{self.id}", params=params)
        self.__dict__.update(self.from_api_data(response["taskOrHabit"]).__dict__)

    def start(self) -> None:
        client = ReclaimClient()
        response = client.post(f"/api/planner/start/task/{self.id}")
        self.__dict__.update(self.from_api_data(response["taskOrHabit"]).__dict__)

    def stop(self) -> None:
        client = ReclaimClient()
        response = client.post(f"/api/planner/stop/task/{self.id}")
        self.__dict__.update(self.from_api_data(response["taskOrHabit"]).__dict__)
