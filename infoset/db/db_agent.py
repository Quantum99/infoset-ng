"""Module of infoset database functions. Agent table."""

# Python standard libraries
from collections import defaultdict

# Infoset libraries
from infoset.utils import general
from infoset.db import db
from infoset.db.db_orm import Agent


class GetIDXAgent(object):
    """Class to return agent data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_agent):
        """Function for intializing the class.

        Args:
            idx_agent: Agent idx_agent

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = ['idx_agent', 'id_agent', 'name', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_agent, int) is False:
            idx_agent = None

        # Only work if the value is an integer
        if isinstance(idx_agent, int) is True and idx_agent is not None:
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(Agent).filter(
                Agent.idx_agent == idx_agent)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_agent'] = idx_agent
                    self.data_dict[
                        'id_agent'] = general.decode(instance.id_agent)
                    self.data_dict['name'] = general.decode(instance.name)
                    self.data_dict['enabled'] = bool(instance.enabled)
                    self.data_dict['exists'] = True
                    break

            # Return the session to the database pool after processing
            database.close()

    def exists(self):
        """Tell if row is exists.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['exists']
        return value

    def idx_agent(self):
        """Get idx_agent value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_agent']
        return value

    def id_agent(self):
        """Get id_agent value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['id_agent']
        return value

    def name(self):
        """Get agent name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['name']
        return value

    def enabled(self):
        """Get agent enabled.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['enabled']

        # Return
        return value

    def everything(self):
        """Get all agent data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


class GetIDAgent(object):
    """Class to return agent data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, id_agent):
        """Function for intializing the class.

        Args:
            id_agent: Identifier of agent

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = ['idx_agent', 'name', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Encode the id_agent
        value = id_agent.encode()

        # Establish a database session
        database = db.Database()
        session = database.session()
        result = session.query(Agent).filter(Agent.id_agent == value)

        # Massage data
        if result.count() == 1:
            for instance in result:
                self.data_dict['id_agent'] = id_agent
                self.data_dict['idx_agent'] = instance.idx_agent
                self.data_dict['name'] = general.decode(instance.name)
                self.data_dict['enabled'] = bool(instance.enabled)
                self.data_dict['exists'] = True
                break

        # Return the session to the database pool after processing
        database.close()

    def exists(self):
        """Tell if row is exists.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['exists']
        return value

    def idx_agent(self):
        """Get idx_agent value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_agent']
        return value

    def id_agent(self):
        """Get id_agent value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['id_agent']
        return value

    def name(self):
        """Get agent name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['name']
        return value

    def enabled(self):
        """Get agent enabled.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['enabled']

        # Return
        return value

    def everything(self):
        """Get all agent data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def id_agent_exists(id_agent):
    """Determine whether the Identifier exists.

    Args:
        id_agent: Identifier value for agent

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Get information on agent from database
    data = GetIDAgent(id_agent)
    if data.exists() is True:
        exists = True

    # Return
    return exists


def idx_agent_exists(idx_agent):
    """Determine whether the idx_agent exists.

    Args:
        idx_agent: idx_agent value for datapoint

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_agent, int) is False:
        idx_agent = None

    # Get information on agent from database
    data = GetIDXAgent(idx_agent)
    if data.exists() is True:
        exists = True

    # Return
    return exists


def get_all_agents():
    """Get data on all agents in the database.

    Args:
        None

    Returns:
        data: List of dicts of agent data.

    """
    # Initialize important variables
    data = []

    # Establish a database session
    database = db.Database()
    session = database.session()
    result = session.query(Agent)

    # Massage data
    for instance in result:
        # Get next record
        data_dict = defaultdict(dict)
        data_dict['id_agent'] = general.decode(instance.id_agent)
        data_dict['idx_agent'] = instance.idx_agent
        data_dict['name'] = general.decode(instance.name)
        data_dict['enabled'] = bool(instance.enabled)
        data_dict['exists'] = True

        # Append to list
        data.append(data_dict)

    # Return the session to the database pool after processing
    database.close()

    # Return
    return data
