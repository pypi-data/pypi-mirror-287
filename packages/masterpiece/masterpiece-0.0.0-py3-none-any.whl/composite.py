import json
from typing import List
from masterpiece import MasterPiece


class Composite(MasterPiece):
    """Group base class that can consist of `MasterPiece` and `Group` objects as
    children.

    This class can be used for grouping masterpieces into larger logical entities.

    Example:
    ::

        motion_sensors = Group("motionsensors")
        motion_sensors.add(ShellyMotionSensor("downstairs"))
        motion_sensors.add(ShellyMotionSensor("upstairs"))
    """

    _class_id = ""

    def __init__(self, name: str = "group") -> None:
        super().__init__(name)
        self.children: List = []
        self.role: str = "union"

    def add(self, h: MasterPiece) -> None:
        """Add new automation object as children. The object to be inserted
        must be derived from Object base class.

        Args:
            h (Object): object to be inserted.
        """
        self.children.append(h)

    def to_dict(self):
        data = super().to_dict()
        data["_group"] = {
            "role": self.role,
            "children": [child.to_dict() for child in self.children],
        }
        return data

    def from_dict(self, data):
        """Recursively deserialize the group from a dictionary, including it
        children.

        Args:
            data (dict): data to deserialize from.

        """
        super().from_dict(data)
        for key, value in data.get("_group", {}).items():
            if key == "children":
                for child_dict in value:
                    child = MasterPiece.instantiate(child_dict["_class"])
                    self.add(child)
                    child.from_dict(child_dict)
            else:
                setattr(self, key, value)

    @classmethod
    def register(cls):
        if cls._class_id == "":
            MasterPiece.register()
            cls.initialize_class()
