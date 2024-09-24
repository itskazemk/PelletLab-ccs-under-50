import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List
import uuid
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, NVARCHAR
import myDict

from persiantools.jdatetime import JalaliDate


class Base(DeclarativeBase):
    pass


class AreaAnalyzeRequest(Base):
    __tablename__ = 'AreaAnalyzeRequests'
    ID: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    SubAreaID: Mapped[uuid.UUID]
    SamplerUserID: Mapped[uuid.UUID] = mapped_column(default=uuid.UUID('E0F3DE0C-FE10-4C4A-BE6F-24A0083C9986'))
    AnalyserUserID: Mapped[uuid.UUID] = mapped_column(default=uuid.UUID('E0F3DE0C-FE10-4C4A-BE6F-24A0083C9986'))
    RegistererUserID: Mapped[uuid.UUID] = mapped_column(default=uuid.UUID('E0F3DE0C-FE10-4C4A-BE6F-24A0083C9986'))
    AnalysingCode: Mapped[str] = mapped_column(default='-', type_=NVARCHAR)
    CreatedDate: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    WorkingShiftId: Mapped[str] = mapped_column(default=uuid.UUID('D35B9192-EFD2-4C79-958B-F096A2E3E2A1'),
                                                type_=NVARCHAR)
    Description: Mapped[str] = mapped_column(nullable=True, type_=NVARCHAR(400))
    AnalyzeDate: Mapped[datetime.date]
    AnalyzeTime: Mapped[datetime.time]

    AreaAnalyzeRequestValues: Mapped[List['AreaAnalyzeRequestValue']] = relationship(
        back_populates='AreaAnalyzeRequest')

    def __repr__(self):
        return f"<Request: DateTime={JalaliDate(self.AnalyzeDate)}-{self.AnalyzeTime}, len(Values)={len(self.AreaAnalyzeRequestValues)}>"


class AreaAnalyzeRequestValue(Base):
    __tablename__ = 'AreaAnalyzeRequestValues'
    ID: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    AreaAnalyzeRequestId: Mapped[uuid.UUID] = mapped_column(ForeignKey('AreaAnalyzeRequests.ID'))
    AreaAnalyzeId: Mapped[uuid.UUID]
    Value: Mapped[float] = mapped_column(nullable=True)
    ValueType: Mapped[int]
    CreatedDate: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())
    PersonalCode: Mapped[int] = mapped_column(default=0)

    AreaAnalyzeRequest: Mapped['AreaAnalyzeRequest'] = relationship(back_populates='AreaAnalyzeRequestValues')

    def __repr__(self):
        aarParameter = myDict.areaAnalyzeIdToName.get(uuid.UUID(f'{self.AreaAnalyzeId}'))
        print(aarParameter)
        return f"<Value: Parameter={aarParameter}, Value={self.Value}>"
