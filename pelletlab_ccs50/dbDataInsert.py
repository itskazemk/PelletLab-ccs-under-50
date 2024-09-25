import pickle

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("mssql+pymssql://sa:1@SANPAD-C2:1433/PelletDB", echo=False)

# areaAnalyzeRequestINSERTList = []
with open("ccs_50.data", "rb") as filehandle:
    # Read the data as a binary data stream
    areaAnalyzeRequestINSERTList = pickle.load(filehandle)

    # add data to db
    with Session(engine) as newSession:
        newSession.add_all(areaAnalyzeRequestINSERTList)
        newSession.commit()
