from grpclib.client import Channel
from proto.grpc.api.v1 import IpServiceStub


class ScarxApiChannel:
    def __init__(self, client_name: str, api_token: str):
        self.__channel = Channel(host="api.scarx.net", port=443, ssl=True)
        self.IpServiceV1 = IpServiceStub(self.__channel, metadata={
            "client-name": client_name,
            "api-token": api_token
        })

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__channel.close()
