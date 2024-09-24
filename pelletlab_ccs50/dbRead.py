from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from pelletlab_ccs50 import dbModels

print("test")

engine = create_engine("mssql+pymssql://sa:1@SANPAD-C2:1433/PelletDB", echo=False)

# اضافه شدن جداول به دیتابیس بیس بر حسب مدل های تغریف شده
# modelsConvert.Base.metadata.create_all(bind=engine_newDb)

areaAnalyzeRequestINSERTList = []
with Session(bind=engine) as session:
    # models.Base.metadata.create_all(bind=engine)

    statement = (
        select(dbModels.AreaAnalyzeRequest)
        # .where(models.Aria.AreaCod == 5)
        # ).order_by(models.Aria.Date, models.Aria.Time, models.Vaset.Id)
    )

    result = session.scalars(statement).unique()

    adsfasdfasdf = result.all()
    counter = 1
    # for idx, requestItem in enumerate(result):
    #     # if counter == 500:
    #     #     break
    #     # counter += 1
    #     areaAnalyzeRequestValuesList = []

    #     ValueListClass = myDict.ValueListClass()
    #     for vasetItem in requestItem.Vasets:
    #         PartNameVaset_Custom = (
    #             "aftermix"
    #             if vasetItem.PartTable.Part.Part.strip().lower().replace(" ", "")
    #             == "aftermixer"
    #             else vasetItem.PartTable.Part.Part.strip().lower().replace(" ", "")
    #         )

    #         # باید در کوئری اصلاح شود که اصلا نیاد در ریزالت
    #         if any(
    #             item in PartNameVaset_Custom.lower()
    #             for item in ["disc", "sampler", "beforehpgr", "beforemixer"]
    #         ):
    #             continue

    #         # if vasetItem.FeOs:
    #         #     getattr(ValueListClass, f'area500_beforemix_feo_avg').append(round(statistics.mean([_.Result for _ in vasetItem.FeOs]), 4))
    #         #
    #         # if vasetItem.TFes:
    #         #     getattr(ValueListClass, f'area500_beforemix_feo_avg').append(round(statistics.mean([_.Result for _ in vasetItem.TFes]), 4))

    #         # داینامیک کردن مقدار دهی پارامتر ها که بدلیل نامعلوم فعلا کامنت شد

    #         for itemName, itemValue in vasetItem:
    #             # todo  باید حذف شود، خاصیتی ندارد
    #             if "disc" in itemName.lower():
    #                 continue

    #             elif itemName.lower() == "moisture500s":
    #                 continue
    #                 # for moistureGroup in itemValue:
    #                 #     for wfx, wfValue in moistureGroup:
    #                 #         getattr(ValueListClass,
    #                 #                 myDict.getAttrHtmName[f'{wfx}_moistures'.lower()]).append(
    #                 #             round(wfValue, 1))

    #             elif itemName.lower() == "xrays":
    #                 continue
    #                 # for xrayGroup in itemValue:
    #                 #     for xrayParameter, xrayValue in xrayGroup:
    #                 #         getattr(ValueListClass, f'area500_{PartNameVaset_Custom}_xray_{xrayParameter}').append(
    #                 #             round(xrayValue, 4))

    #             elif itemName.lower() == "belines":
    #                 continue
    #                 # for blaineGroup in itemValue:
    #                 #     if any(_ is None for _ in
    #                 #            [blaineGroup.Porosity, blaineGroup.DensityP, blaineGroup.Time1, blaineGroup.Time0]):
    #                 #         continue
    #                 #
    #                 #     blaineValue = (blaineGroup.Porosity / blaineGroup.DensityP) * (
    #                 #         math.sqrt((blaineGroup.Time1 / blaineGroup.Time0)))
    #                 #     getattr(ValueListClass, f'area500_{PartNameVaset_Custom}_blaine_result').append(
    #                 #         round(blaineValue))

    #             elif itemName.lower() == "moisture510bc1s":
    #                 for afterMixMoistureGroup in itemValue:
    #                     getattr(
    #                         ValueListClass,
    #                         myDict.getAttrHtmName[
    #                             f"{PartNameVaset_Custom}_{itemName}".lower()
    #                         ],
    #                     ).append(round(afterMixMoistureGroup.BC2, 1))

    #             # else:
    #             #     getattr(ValueListClass, myDict.getAttrHtmName[f'{PartNameVaset_Custom}_{itemName}'.lower()]).append(
    #             #         round(statistics.mean([_.Result for _ in itemValue]), 2))
    #     if True:
    #         for parameterName, parameterValues in ValueListClass:
    #             valueList = modelsConvert.AreaAnalyzeRequestValue(
    #                 AreaAnalyzeId=myDict.areaAnalyzeIds[
    #                     f"{parameterName}"
    #                 ].areaAnalyzeID,
    #                 Value=statistics.mean(parameterValues),
    #                 ValueType=myDict.areaAnalyzeIds[f"{parameterName}"].type,
    #             )
    #             areaAnalyzeRequestValuesList.append(valueList)

    #         if areaAnalyzeRequestValuesList:
    #             request = modelsConvert.AreaAnalyzeRequest(
    #                 SubAreaID=requestSubAreaId,
    #                 Description=requestItem.Usser.lower(),
    #                 AnalyzeDate=requestItem.Date,
    #                 AnalyzeTime=requestItem.Time,
    #                 AreaAnalyzeRequestValues=areaAnalyzeRequestValuesList,
    #             )
    #             print(request)
    #             areaAnalyzeRequestINSERTList.append(request)

# with open("insert_afterMix.data", "wb") as filehandle:
#     # Store the data as a binary data stream
#     pickle.dump(areaAnalyzeRequestINSERTList, filehandle)
