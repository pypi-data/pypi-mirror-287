from moapy.auto_convert import auto_schema, MBaseModel
from moapy.project.wgsd.wgsd_sectionproperty import SectionProperty
from pydantic import Field as dataclass_field
from typing import Union

class SectShape_H(MBaseModel):
    H: float = dataclass_field(default=300.0, description="H")
    B1: float = dataclass_field(default=300.0, description="B1")
    tw: float = dataclass_field(default=10.0, description="tw")
    tf1: float = dataclass_field(default=10.0, description="tf1")
    B2: float = dataclass_field(default=300.0, description="B2")
    tf2: float = dataclass_field(default=10.0, description="tf2")
    r1: float = dataclass_field(default=0.0, description="r1")
    r2: float = dataclass_field(default=0.0, description="r2")

class SectShape_SolidRectangle(MBaseModel):
    B: float = dataclass_field(default=300.0, description="B")
    H: float = dataclass_field(default=300.0, description="H")

@auto_schema
def calc_typicalsection_prop(shape: Union[SectShape_H, SectShape_SolidRectangle]) -> SectionProperty:
    if isinstance(shape, SectShape_H):
        return SectionProperty(Area=1000.0, Asy=100.0, Asz=100.0, Ixx=100.0, Iyy=100.0, Izz=100.0, Cy=100.0, Cz=100.0, Syp=100.0, Sym=100.0, Szp=100.0, Szm=100.0, Ipyy=100.0, Ipzz=100.0, Zy=100.0, Zz=100.0, ry=100.0, rz=100.0)
    elif isinstance(shape, SectShape_SolidRectangle):
        return SectionProperty(Area=2000.0, Asy=200.0, Asz=200.0, Ixx=200.0, Iyy=200.0, Izz=200.0, Cy=200.0, Cz=200.0, Syp=200.0, Sym=200.0, Szp=200.0, Szm=200.0, Ipyy=200.0, Ipzz=200.0, Zy=200.0, Zz=200.0, ry=200.0, rz=200.0)
    else:
        return SectionProperty(Area=1000.0, Asy=100.0, Asz=100.0, Ixx=100.0, Iyy=100.0, Izz=100.0, Cy=100.0, Cz=100.0, Syp=100.0, Sym=100.0, Szp=100.0, Szm=100.0, Ipyy=100.0, Ipzz=100.0, Zy=100.0, Zz=100.0, ry=100.0, rz=100.0)