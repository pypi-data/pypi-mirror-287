import unittest
import tempfile
import os

from composite import Composite
from masterpiece import MasterPiece


class TestComposite(unittest.TestCase):
    """Unit tests for `Composite` class."""

    def test_get_classid(self):
        classid = Composite.get_class_id()
        self.assertEqual("Composite", classid)

    def test_add(self):
        composite = Composite("parent")
        child = MasterPiece("child")
        composite.add(child)
        self.assertEqual(1, len(composite.children))

    def test_serialization(self):
        """Create hierarchical object and assert deserialization restores the
        structure.
        ::

            Composite("mycomposite")
            ├─ MasterPiece("child1")
            └─ Composite("child2")
                └─ MasterPiece("child3")

        """
        MasterPiece.register()
        composite = Composite("mycomposite")
        child1 = MasterPiece("child1")
        composite.add(child1)
        sub_composite = Composite("child2")
        composite.add(sub_composite)
        child_of_subcomposite = MasterPiece("child3")
        sub_composite.add(child_of_subcomposite)

        #  make sure the hierarchy is what we expect
        self.assertEqual(2, len(composite.children))
        self.assertEqual(1, len(sub_composite.children))

        # serialize
        with tempfile.TemporaryDirectory() as tmp:
            filename = os.path.join(tmp, "composite.json")

            with open(filename, "w") as f:
                composite.serialize_to_json(f)

            # deserialize
            composite2 = Composite("bar")
            with open(filename, "r") as f:
                composite2.deserialize_from_json(f)
            self.assertEqual("mycomposite", composite2.name)
            #  make sure the hierarchy is what we expect
            self.assertEqual(2, len(composite2.children))


if __name__ == "__main__":
    unittest.main()
