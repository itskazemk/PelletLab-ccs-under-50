import datetime
import uuid
from typing import List

from persiantools.jdatetime import JalaliDate
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mssql import NVARCHAR, UNIQUEIDENTIFIER
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from pelletlab_ccs50 import myDict


class Base(DeclarativeBase):
    pass


class AreaAnalyzeRequest(Base):
    __tablename__ = "AreaAnalyzeRequests"

    ID: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    SubAreaID: Mapped[uuid.UUID]
    SamplerUserID: Mapped[uuid.UUID] = mapped_column(
        default=uuid.UUID("E0F3DE0C-FE10-4C4A-BE6F-24A0083C9986")
    )
    AnalyserUserID: Mapped[uuid.UUID] = mapped_column(
        default=uuid.UUID("E0F3DE0C-FE10-4C4A-BE6F-24A0083C9986")
    )
    RegistererUserID: Mapped[uuid.UUID] = mapped_column(
        default=uuid.UUID("E0F3DE0C-FE10-4C4A-BE6F-24A0083C9986")
    )
    AnalysingCode: Mapped[str] = mapped_column(default="-", type_=NVARCHAR)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now()
    )
    WorkingShiftId: Mapped[str] = mapped_column(
        default=uuid.UUID("D35B9192-EFD2-4C79-958B-F096A2E3E2A1"), type_=NVARCHAR
    )
    Description: Mapped[str] = mapped_column(nullable=True, type_=NVARCHAR(400))
    AnalyzeDate: Mapped[datetime.date]
    AnalyzeTime: Mapped[datetime.time]

    AreaAnalyzeRequestValues: Mapped[List["AreaAnalyzeRequestValue"]] = relationship(
        back_populates="AreaAnalyzeRequest"
    )

    def __repr__(self):
        return f"<Request: DateTime={JalaliDate(self.AnalyzeDate)}-{self.AnalyzeTime}, len(Values)={len(self.AreaAnalyzeRequestValues)}>"


class AreaAnalyzeRequestValue(Base):
    __tablename__ = "AreaAnalyzeRequestValues"

    ID: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    AreaAnalyzeRequestId: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("AreaAnalyzeRequests.ID"), nullable=False
    )
    AreaAnalyzeId: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("AreaAnalyzes.ID"), nullable=False
    )
    Value: Mapped[float] = mapped_column(nullable=True)
    ValueType: Mapped[int] = mapped_column(nullable=False)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now, nullable=False
    )
    PersonalCode: Mapped[int] = mapped_column(default=0)

    # Relationships
    AreaAnalyzeRequest: Mapped["AreaAnalyzeRequest"] = relationship(
        back_populates="AreaAnalyzeRequestValues"
    )
    AreaAnalyze: Mapped["AreaAnalyze"] = relationship(
        back_populates="AreaAnalyzeRequestValues"
    )

    # def __repr__(self):
    #     return f"<Value: Value={self.Value}, ValueType={self.ValueType}>"

    def __repr__(self):
        aarParameter = myDict.areaAnalyzeIdToName.get(
            uuid.UUID(f"{self.AreaAnalyzeId}")
        )
        return f"<Value: Parameter={aarParameter}, Value={self.Value}>"


class AreaAnalyze(Base):
    __tablename__ = "AreaAnalyzes"

    ID: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    SubAnalyzeID: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("SubAnalyzes.ID"), nullable=False
    )
    SubAreaID: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("SubAreas.ID"), nullable=False
    )
    MinValue: Mapped[float] = mapped_column(nullable=True)
    MaxValue: Mapped[float] = mapped_column(nullable=True)
    Precision: Mapped[int] = mapped_column(nullable=True)
    DefaultValue: Mapped[float] = mapped_column(nullable=True)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now, nullable=False
    )

    # Relationships
    SubAnalyze: Mapped["SubAnalyze"] = relationship(back_populates="AreaAnalyzes")
    AreaAnalyzeRequestValues: Mapped[List["AreaAnalyzeRequestValue"]] = relationship(
        back_populates="AreaAnalyze"
    )

    def __repr__(self):
        return f"<AreaAnalyze: MinValue={self.MinValue}, MaxValue={self.MaxValue}>"


class SubAnalyze(Base):
    __tablename__ = "SubAnalyzes"

    ID: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    AnalyzeID: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("Analyzes.ID"), nullable=False
    )
    Title: Mapped[str] = mapped_column(nullable=False, type_=NVARCHAR(200))
    Formula: Mapped[str] = mapped_column(nullable=True, type_=NVARCHAR(400))
    Type: Mapped[int] = mapped_column(nullable=False)
    ExperimentCount: Mapped[int] = mapped_column(nullable=True)
    HtmControlName: Mapped[str] = mapped_column(nullable=True, type_=NVARCHAR(100))
    DefaultValue: Mapped[float] = mapped_column(nullable=True)
    MinValue: Mapped[float] = mapped_column(nullable=True)
    MaxValue: Mapped[float] = mapped_column(nullable=True)
    PersonalCode: Mapped[int] = mapped_column(nullable=True)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now, nullable=False
    )

    # Relationships
    Analyze: Mapped["Analyze"] = relationship(back_populates="SubAnalyzes")
    AreaAnalyzes: Mapped[List["AreaAnalyze"]] = relationship(
        back_populates="SubAnalyze"
    )

    def __repr__(self):
        return f"<SubAnalyze: Title={self.Title}, Formula={self.Formula}>"


class Analyze(Base):
    __tablename__ = "Analyzes"

    ID: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    Title: Mapped[str] = mapped_column(nullable=False, type_=NVARCHAR(200))
    CreatedDate: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now, nullable=False
    )
    HtmControlName: Mapped[str] = mapped_column(nullable=False, type_=NVARCHAR(100))

    # Relationships
    SubAnalyzes: Mapped[List["SubAnalyze"]] = relationship(back_populates="Analyze")

    def __repr__(self):
        return f"<Analyze: Title={self.Title}>"
