from sqlalchemy import Column, Unicode

from ..db.baseclass import Requirement


class System_Requirement(Requirement):

    doc_prefix = Column(Unicode(10), nullable=False, default="SRS")

    def __repr__(self):
        return "<System_Requirement(doc_prefix='%s', definition='%s')>" % (
            self.doc_prefix,
            self.definition,
        )
