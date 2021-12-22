from sqlalchemy import Column, Unicode, Integer, ForeignKey

from ..db.baseclass import Requirement


class Hardware_Design_Element(Requirement):

    doc_prefix = Column(Unicode(10), nullable=False, default="HWD")
    hardware_requirement_id = Column(
        Integer, ForeignKey("hardware_requirement.id"), nullable=False
    )

    def __repr__(self):
        return (
            "<Hardware_Design_Element(doc_prefix='%s', definition='%s', hardware_requirement_id='%s')>"
            % (self.doc_prefix, self.definition, self.hardware_requirement_id)
        )
