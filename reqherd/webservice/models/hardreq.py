from sqlalchemy import Column, Unicode, Integer, ForeignKey

from ..db.baseclass import Requirement


class Hardware_Requirement(Requirement):

    doc_prefix = Column(Unicode(10), nullable=False, default="HWRS")
    system_requirement_id = Column(
        Integer, ForeignKey("system_requirement.id"), nullable=False
    )

    def __repr__(self):
        return "<Hardware_Requirement(doc_prefix='%s', definition='%s', system_requirement_id='%s')>" % (
            self.doc_prefix,
            self.definition,
            self.system_requirement_id,
        )
