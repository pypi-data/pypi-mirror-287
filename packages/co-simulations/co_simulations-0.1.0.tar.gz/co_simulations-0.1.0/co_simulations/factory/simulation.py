"""
simulation.py
"""

from typing import List, Dict
import time
import uuid
import logging
LOGGER = logging.getLogger(__name__)

# this will become a config file passed to the deployment
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


class Node():
    """
    A class representing a node in the factory

    Attributes
    ----------
        type : str
            the type of the node (resource, production, store) 
        special_type : str
            the specific sub type of the node (i.e. node_type = resource, special_type = copper)
        id : uuid
            unique id of the node
    """
    def __init__(self, node_type:str, special_type:str, links:List[str]):
        """
        Initalize new node

        Parameters
        ----------
            node_type : str
                the type of the node, (resource, production, store) 
            special_type : str
                the specific sub type of the node (i.e. node_type = resource, special_type = copper)
            links : List[str]
                a list of node_ids this node is linked to.
            id : uuid
                unique id of the node
        """

        #TODO integrate numeric values

        self.node_type:str = node_type
        self.special_type:str = special_type
        self.links:List[str] = links
        self.id:str = uuid.uuid4().hex[:8]

    def calculate_output(self):
        """
        Calculates a nodes output based on its inputs
        """
        # evaluate inputs to calculate outputs
        return

    def serialize(self):
        """
        Serialize the node
        """
        serialized = {
            "node_type": self.node_type,
            "specia_type": self.special_type,
            "links": self.links,
            "id": self.id,
        }
        return serialized


class Factory():
    """
    A class to represent a Factory.

    ...

    Attributes
    ----------
    nodes : Dict[str, Node]
        a dictionary contaning all of the nodes in the factory with their id's as keys.
    configuration : Dict[str, Rule]
        a configuration file passed to the simulation to establish node behaviours.
    duration : int 
        how long the current simulation has run
    running : bool 
        whether or not the simulation is currently active

    Methods
    -------
    create_node(self, node_type:str, special_type:str, links:List[str]) -> str:
        create node in factory

    delete_node(self, node_id) -> bool:
        delete a node in the factory
    
    
    """
    def __init__(self, config:Dict):
        """
        A class representing a factory simulation

        Attributes:
            nodes (Dict[str, Node]): a dictionary containing all of the nodes in the factory.
            configuration (Dict[str, Rule]): a configuration file passed to the simulation.
            duration (int): how long the current simulation has run
            running (bool): whether or not the simulation is currently active
        """
        self.nodes:Dict[str,Node] = {}
        self.configuration:Dict = config
        self.duration:int = 0
        self.running:bool = True

    def __del__(self):
        print("Factory Simulation being deleted....")
        print("Final State:")
        print(self.serialize())

    def create_node(self, node_type:str, special_type:str, links:List[str]) -> str:
        """
        Creates a new node in the factory

        Parameters:
            node_type (str): the type of node to be created (Production, Resource, or Store)
            special_type (str): the special sub type of a node.
            links List(str): the list of linked nodes to associate with this node.
        """

        # check if node is valid according to rules
        if node_type in rules and special_type in rules[node_type]:
            # begin node creation
            new_node = Node(node_type, special_type, links)
            self.nodes[new_node.id] = new_node
            LOGGER.info('Node (%s) created Succesfully!', new_node.id)
            return new_node.id

        LOGGER.info('rule violation')
        return ""

    def delete_node(self, node_id) -> bool:
        """
        Deletes a node in the factory

        Parameters:
            node_id (str): the id of the node to be deleted

        Returns:
            (bool): status of the operation
        """
        # TODO make sure when nodes are removed their links are deleted

        # TODO add try catch for error handling
        if self.nodes.get(node_id) is not None:
            del self.nodes[node_id]
            LOGGER.info('{node_id} Node Succesfuly Removed!')
            return True

        LOGGER.info('Node does not exsist')
        return False

    def create_link(self, source_node_id, target_node_id) -> bool:
        """
        Creates a link between two nodes in a factory

        Parameters:
            source_node_id (str): the id of the source node to be linked
            target_node_id (str): the id of the target node to be linked
        
        Returns:
            (bool): status of the operation
        """
        source_node = self.get_node(source_node_id)
        target_node = self.get_node(target_node_id)
        if source_node is not None and target_node is not None:
            if source_node.special_type in self.configuration.get(
                target_node.node_type, {}).get(
                target_node.special_type):
                source_node.links.append(target_node_id)
                LOGGER.info('Link {source_node_id} -> {target_node_id} created')
                return True

            LOGGER.info('Invalid Link')
        LOGGER.info('Target or Source Node not found')

        return False

    def delete_link(self, source_node_id, target_node_id) -> bool:
        """
        Deletes a link between two nodes in a factory

        Parameters:
            source_node_id (str): the id of the source node to be linked
            target_node_id (str): the id of the target node to be linked
        
        Returns:
            (bool): status of the operation
        """
        source_node = self.get_node(source_node_id)
        if source_node is not None:
            if target_node_id in source_node.links:
                source_node.links.remove(target_node_id)
                LOGGER.info('Link {source_node_id} -> {target_node_id} removed')
                return True

            LOGGER.info('Link {source_node_id} -> {target_node_id} does not exist')
        LOGGER.info('Source node not found')

        return False

    def get_node(self, node_id:str) -> Node:
        """
        Gets a specified node in a factory

        Parameters:
            node_id (str): the id of the node to be fetched

        Returns:
            (Node): the desired node
        """
        return self.nodes.get(node_id, None)

    def get_all_nodes(self):
        """
        Return all the nodes in factory

        Returns:
            nodes (Dict[str, Node]): all nodes in the factory
        """
        return self.nodes

    def validate_links(self, source_node_id:str) -> bool:
        """
        Validates the links that a given node has are valid 

        Parameters:
            source_node_id (str): the id of the node to be validated)
        
        Returns:
            (bool): whether or not the links are valid
        """
        source_node = self.get_node(source_node_id)
        if source_node is None:
            print("Source node not found!")
            return False

        if len(source_node.links) < 1:
            print("No links associated with node")
            # if there are no links the node does not break any rules
            return True

        for link in source_node.links:
            target_node = self.get_node(link)
            if target_node is None:
                print("Target node not found!")
                return False

            if source_node.special_type in self.configuration.get(
                target_node.node_type, {}).get(
                target_node.special_type):
                return True

        return False

    def validate_factory(self) -> bool:
        """
        Validates the entire factory

        Parameters:
            None
        
        Returns:
            (bool): whether or not the given layout is valid
        """
        for node_id in self.nodes:
            if not self.validate_links(node_id):
                return False
        return True

    def serialize(self) -> Dict:
        """
        Serializes the factory for use in the API

        Parameters:
            None
        
        Returns:
            (object): serialized state of the layout
        """
        serialized = {
            "nodes": [node.serialize() for _, node in self.nodes.items()],
            "size": len(self.nodes),
            "duration": self.duration,
            "running": self.running
        }

        return serialized

    def main_loop(self):
        """
        Start factory simulation.
        """
        print("Main Loop Initiated")
        while self.running:
            print("Main Loop Running")
            time.sleep(1)
