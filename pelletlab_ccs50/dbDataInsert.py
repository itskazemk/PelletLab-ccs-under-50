import pickle
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sqlalchemy

import dbModels

engine_newDb = create_engine("mssql+pymssql://sa:1@SANPAD-C2:1433/PelletDB_Converted", echo=False)

# areaAnalyzeRequestINSERTList = []
with open('insert_afterMix.data', 'rb') as filehandle:
    # Read the data as a binary data stream
    areaAnalyzeRequestINSERTList = pickle.load(filehandle)

    aa = areaAnalyzeRequestINSERTList[-2:]
    sfd1 = len(areaAnalyzeRequestINSERTList)
    sfd2 = len(set(areaAnalyzeRequestINSERTList))
    # sfd3 = 1

    # add data to db
    with Session(engine_newDb) as newSession:
        newSession.add_all(areaAnalyzeRequestINSERTList)
        newSession.commit()
