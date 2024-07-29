"""
Factory unit tests
"""
#pylint: disable-all

import unittest
from co_simulations.factory.simulation import Factory, Node

# testing rules for simple layouts
rules = {
    "Production": {
        "wire": ["copper"]
    },
    "Resource":{
        "copper": [],
    },
    "Output": {
        "wire": ["wire"]
    }
}


class TestFactorySimulation(unittest.TestCase):
    def setUp(self):
        # create fresh new factory for testing each time
        self.factory = Factory(rules)

    def tearDown(self):
        # make sure factory is totally tore down and disposed of after each run
        del self.factory

    def test_create_node(self):
        # create 2 nodes
        node_1_id = self.factory.create_node("Production", "wire", [])
        node_2_id = self.factory.create_node("Resource", "copper", [])
        self.assertIsNotNone(self.factory.get_node(node_1_id))
        self.assertIsNotNone(self.factory.get_node(node_2_id))

        # create invalid node
        node_1_id = self.factory.create_node("Production", "copper", [])
        self.assertEqual(node_1_id, "")

        # assert factory only has 2 nodes
        self.assertEqual(len(self.factory.get_all_nodes()), 2)
    
    def test_remove_node(self):
        # add nodes to factory
        node_1_id = self.factory.create_node("Production", "wire", [])
        node_2_id = self.factory.create_node("Resource", "copper", [])
        self.assertEqual(len(self.factory.get_all_nodes()), 2)
        
        # delete the first node
        status = self.factory.delete_node(node_1_id)
        self.assertIsNone(self.factory.get_node(node_1_id))

        # delete the second node
        status = self.factory.delete_node(node_2_id)
        self.assertIsNone(self.factory.get_node(node_2_id))

        # try to re-delete the first node (should return false, node does not exist)
        status = self.factory.delete_node(node_1_id)
        self.assertFalse(status)

        # assert factory has no nodes (2 created, 2 deleted)
        self.assertEqual(len(self.factory.get_all_nodes()), 0)
    
    def test_create_link(self):
        # create all 3 types of nodes
        node_1_id = self.factory.create_node("Resource", "copper", [])
        node_2_id = self.factory.create_node("Production", "wire", [])
        node_3_id = self.factory.create_node("Output", "wire", [])
        self.assertEqual(len(self.factory.get_all_nodes()), 3)

        # create link between Resource -> Production
        self.factory.create_link(node_1_id, node_2_id)
        node_1 = self.factory.get_node(node_1_id)
        # assert node has the other listed in its links
        self.assertIn(node_2_id, node_1.links)

        # create link between Production -> Output
        self.factory.create_link(node_2_id, node_3_id)
        node_2 = self.factory.get_node(node_2_id)
        # assert node has the other listed in its links
        self.assertIn(node_3_id, node_2.links)

        # create invalid link between Resource -> Output
        status = self.factory.create_link(node_1_id, node_3_id)
        self.assertFalse(status)

    def test_delete_link(self):
        # create all 3 types of nodes
        node_1_id = self.factory.create_node("Resource", "copper", [])
        node_2_id = self.factory.create_node("Production", "wire", [])
        node_3_id = self.factory.create_node("Output", "wire", [])
        self.assertEqual(len(self.factory.get_all_nodes()), 3)

        # create link between Resource -> Production
        status = self.factory.create_link(node_1_id, node_2_id)
        self.assertTrue(status)

        # create link between Production -> Output
        status = self.factory.create_link(node_2_id, node_3_id)
        self.assertTrue(status)

        # delete link between Resource -> Production
        status = self.factory.delete_link(node_1_id, node_2_id)
        self.assertTrue(status)
        node_1 = self.factory.get_node(node_1_id)
        self.assertNotIn(node_2_id, node_1.links)

        # delete link that does not exist (should return status false)
        status = self.factory.delete_link(node_1_id, node_2_id)
        self.assertFalse(status)

    def test_valid_factory(self):
        # create all 3 types of nodes
        node_1_id = self.factory.create_node("Resource", "copper", [])
        node_2_id = self.factory.create_node("Production", "wire", [])
        node_3_id = self.factory.create_node("Output", "wire", [])
        self.assertEqual(len(self.factory.get_all_nodes()), 3)

        # create link between Resource -> Production
        status = self.factory.create_link(node_1_id, node_2_id)
        self.assertTrue(status)

        # create link between Production -> Output
        status = self.factory.create_link(node_2_id, node_3_id)
        self.assertTrue(status)

        # test current factory: 1 Resource -> 1 Production -> 1 Output
        valid = self.factory.validate_factory()
        self.assertTrue(valid)

    def test_invalid_factory(self):
        # bypassing creation protections to make invalid layout
        Node_1 = Node("Resource", "copper", ['aaaa'])
        Node_2 = Node("Output", "copper", [])
        Node_1.id = 'aaaa'
        Node_2.id = 'bbbb'

        self.factory.nodes = {
            'aaaa': Node_1,
            'bbbb': Node_2
        }

        # test current invalid factory: 1 Resource -> 1 Output
        valid = self.factory.validate_factory()
        self.assertFalse(valid)

if __name__ == '__main__':
    unittest.main()