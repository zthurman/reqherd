from sqlalchemy import Column, Unicode
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, Unicode, Integer, ForeignKey

from ..db.baseclass import Requirement


class Software_Requirement(Requirement):

    doc_prefix = Column(Unicode(10), nullable=False, default="SWRS")
    system_requirement_id = Column(
        Integer, ForeignKey("system_requirement.id"), nullable=False
    )

    def __repr__(self):
        return (
            "<Software_Requirement(doc_prefix='%s', definition='%s', system_requirement_id='%s')>"
            % (self.doc_prefix, self.definition, self.system_requirement_id)
        )
