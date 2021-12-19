from sqlalchemy import Column, BigInteger, Unicode, DateTime
from sqlalchemy.ext.declarative import declared_attr, as_declarative


@as_declarative()
class Base(object):
    id = Column(BigInteger, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value


class Requirement(Base):
    """

    `Abstract concrete Base <https://docs.sqlalchemy.org/en/13/orm/inheritance.html#abstract-concrete-classes>`_
    augmentation used to inherit definition and prefix columns to children.

    Attributes
    ----------
    __abstract__ : bool
        Abstract concrete base class flag.
    doc_prefix : sqlalchemy.Column
        Documentation prefix column for inheritance in child objects (Not nullable).
    definition : sqlalchemy.Column
        Definition column for inheritance in child objects (Not nullable).
    modified_date : sqlalchemy.Column
        Modified date column for inheritance in child objects (Not nullable).

    """

    __abstract__ = True
    doc_prefix = Column(Unicode(10), nullable=False)
    definition = Column(Unicode(1000), nullable=False)
    modified_date = Column(DateTime, nullable=False)
