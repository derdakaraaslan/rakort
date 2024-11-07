from sqlalchemy import Column, Integer, String
from database import Base

class ProcessInfo(Base):
    __tablename__ = 'process_info'

    id = Column(Integer, primary_key=True, index=True)
    pid = Column(Integer)
    status = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    cpu_usage = Column(Integer)
    memory_usage = Column(Integer)