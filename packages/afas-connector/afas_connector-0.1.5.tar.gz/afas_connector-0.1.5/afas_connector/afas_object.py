

from .afas_connector import AfasConnector


class AfasObject:
    """AfasObject is a class that represents an object in AFAS Profit.

    Attributes:
        type (str): The unique identifier of the object.
        fields (dict): The fields of the object.
    """

    def __init__(self, type, fields: dict | None = None, metadata: dict | None = None, objects: list | None = None):
        """Initializes AfasObject with the given parameters.

        Args:
            type (str): The unique identifier of the object.
            fields (dict, optional): The fields of the object. Defaults to {}.
        """
        self.type = type
        self.set(fields, metadata, objects)

        self.afas_connector = AfasConnector()

    def set(self, fields: dict | None = None, metadata: dict | None = None, objects: list | None = None):
        """Sets the fields of the object.

        Args:
            fields (dict): The fields of the object.
        """
        self.fields = fields
        self.objects = objects
        self.metadata = metadata

    def payload(self):
        """Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary representation of the object.
        """
        p = {
            self.type: {
                "Element": {}
            }
        }

        # Append fields to payload
        if self.metadata is not None:
            p[self.type]["Element"] = self.metadata
        
        if self.fields is not None:
            p[self.type]["Element"]["Fields"] = self.fields
        
        if self.objects is not None:
            p[self.type]["Element"]["Objects"] = self.objects

        return p
        
    def update(self):
        """Updates the object in AFAS Profit.

        Returns:
            tuple: A tuple containing the status code and the JSON response from the AFAS Connector.
        """
        return self.afas_connector.put(self.type, self.payload())

    def __str__(self):
        """Returns a string representation of the object.

        Returns:
            str: A string representation of the object.
        """
        return f"AfasObject(id={self.id}, name={self.name}, type={self.type}, description={self.description}, fields={self.fields})"