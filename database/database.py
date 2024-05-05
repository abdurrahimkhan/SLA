from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://user:password@server/database"

connection_string = "DRIVER={SQL Server};SERVER=localhost;DATABASE=Transport;UID=portal_user;PWD=huawei123#"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})


engine = create_engine(connection_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
