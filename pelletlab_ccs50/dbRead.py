import pickle
import uuid

from sqlalchemy import and_, create_engine, or_, select
from sqlalchemy.orm import Session

from pelletlab_ccs50 import areaAnalyzeIds, dbModels, myDict

print("test")

engine = create_engine("mssql+pymssql://sa:1@SANPAD-C2:1433/PelletDB", echo=False)

# اضافه شدن جداول به دیتابیس بیس بر حسب مدل های تغریف شده
# modelsConvert.Base.metadata.create_all(bind=engine_newDb)

areaAnalyzeRequestINSERTList = []
with Session(bind=engine) as session:
    # models.Base.metadata.create_all(bind=engine)

    statement = (
        select(dbModels.AreaAnalyzeRequest)
        .join(dbModels.AreaAnalyzeRequest.AreaAnalyzeRequestValues)
        .join(dbModels.AreaAnalyzeRequestValue.AreaAnalyze)
        .join(dbModels.AreaAnalyze.SubAnalyze)
        .join(dbModels.SubAnalyze.Analyze)
        .where(
            and_(
                or_(
                    dbModels.AreaAnalyzeRequest.SubAreaID
                    == "26183f75-cbe7-4e60-88f9-aeb4d05ace6e",  # 820
                    dbModels.AreaAnalyzeRequest.SubAreaID
                    == "25191d4b-1549-48bf-836a-d2dc2796c7f2",  # 810
                ),
                # dbModels.AreaAnalyzeRequestValue.AreaAnalyzeId.in_(
                #     areaAnalyzeIds.ccsIds
                # ),
                dbModels.Analyze.HtmControlName == "CCS",
            )
        )
        # ).order_by(models.Aria.Date, models.Aria.Time, models.Vaset.Id)
    )

    print(statement.compile())

    result = session.scalars(statement)
    # adsfasdfasdf = result.all()
    # print(11, len(adsfasdfasdf))
    # counter = 1

    for request in result:
        ccs_inputs = []
        ccs_50 = []

        for _requestValue in request.AreaAnalyzeRequestValues:
            if (
                "input" in _requestValue.AreaAnalyze.SubAnalyze.HtmControlName.lower()
                and _requestValue.AreaAnalyze.SubAnalyze.Analyze.HtmControlName.lower()
                == "ccs"
            ):
                ccs_inputs.append(_requestValue)
                if _requestValue.Value < 50:
                    ccs_50.append(_requestValue)

        ccs_sum = sum(item.Value for item in ccs_inputs)
        ccs_50_percent = (len(ccs_50) / len(ccs_inputs)) * 100

        if ccs_sum == 0:
            continue

        _areaAnalyzeId = ""
        if request.SubAreaID == uuid.UUID(
            "25191d4b-1549-48bf-836a-d2dc2796c7f2"
        ):  # 810
            _areaAnalyzeId = "9352F98C-ECBA-458A-BC2E-BB0A63AAF064"

        elif request.SubAreaID == uuid.UUID(
            "26183f75-cbe7-4e60-88f9-aeb4d05ace6e"
        ):  # 820
            _areaAnalyzeId = "DAC42144-3252-4098-9000-2882913FB4F5"

        requestValue_ccs50 = dbModels.AreaAnalyzeRequestValue(
            AreaAnalyzeRequestId=request.ID,
            AreaAnalyzeId=uuid.UUID(_areaAnalyzeId),
            Value=round(ccs_50_percent, 1),
            ValueType=2,
        )
        areaAnalyzeRequestINSERTList.append(requestValue_ccs50)


with open("ccs_50.data", "wb") as filehandle:
    # Store the data as a binary data stream
    pickle.dump(areaAnalyzeRequestINSERTList, filehandle)
