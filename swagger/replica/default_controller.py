import connexion
import six
import replica

from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501


def get_original(file):  # noqa: E501
    """
    takes a filename input and returns metadata for the file
    """
    return replica.original(file)


def get_replica(file):
	    """
    takes a filename input and returns metadata for the file (replica)
    """
    return replica.replica(file)