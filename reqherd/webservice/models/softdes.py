from sqlalchemy import Column, Unicode, Integer, ForeignKey

from ..db.baseclass import Requirement


class Software_Design_Element(Requirement):

    doc_prefix = Column(Unicode(10), nullable=False, default="SWD")
    software_requirement_id = Column(
        Integer, ForeignKey("software_requirement.id"), nullable=False
    )

    def __repr__(self):
        return (
            "<Software_Design_Element(doc_prefix='%s', definition='%s', software_requirement_id='%s')>"
            % (self.doc_prefix, self.definition, self.software_requirement_id)
        )
