from asyncua import Client, ua
from opcua.ua.uaerrors import UaStatusCodeError, UaError

class OPCUAClient:
    def __init__(self, opc_url, opc_policy, opc_mode, opc_certificate_path, opc_private_key, opc_username, opc_password, application_uri):
        self.opc_url = opc_url
        self.opc_policy = opc_policy
        self.opc_mode = opc_mode
        self.opc_certificate_path = opc_certificate_path
        self.opc_private_key = opc_private_key
        self.opc_username = opc_username
        self.opc_password = opc_password
        self.application_uri = application_uri
        self.client = None  # Attribute to store the client instance

    async def connect_to_opc(self):
        """
        This function connects to OPC UA using the provided configuration information.
        """
        try:
            self.client = Client(self.opc_url)  # Create the client
            security_string = (
                f"{self.opc_policy},"
                f"{self.opc_mode},"
                f"{self.opc_certificate_path},"
                f"{self.opc_private_key}"
            )  # Configure security

            await self.client.set_security_string(security_string)  # Set security
            self.client.set_user(self.opc_username)  # Set username
            self.client.set_password(self.opc_password)  # Set password
            self.client.application_uri = self.application_uri  # Set URI
            await self.client.connect()  # Connect

            print("Connection complete to OPC UA.")
        except UaStatusCodeError as e:
            print(f"OPC UA Status Code Error: {str(e)}")
        except UaError as e:
            print(f"OPC UA Error: {str(e)}")
        except Exception as e:
            print(f"Unexpected error for connection to OPC UA: {str(e)}")

    async def get_node_value(self, node_name):
        """
        Function to retrieve the value of a node.
        """
        if self.client is None:
            raise RuntimeError("Client not connected")
        
        try:
            node = self.client.get_node(node_name)
            node_value = await node.get_value()  # Read the node value
            return node_value
        except UaStatusCodeError as e:
            connection_errors = [
                ua.StatusCodes.BadConnectionClosed,
                ua.StatusCodes.BadCommunicationError,
                ua.StatusCodes.BadTimeout
            ]
            if e.code in connection_errors:
                print(f"OPC connection error: {e}")
                raise
            else:
                print(f"OPC error: {e.code.name}")
                raise
        except UaError as e:
            print(f"General OPC UA error: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise
