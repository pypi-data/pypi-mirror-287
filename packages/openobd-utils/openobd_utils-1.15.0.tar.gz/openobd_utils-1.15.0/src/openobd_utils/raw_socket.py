from openobd import *
from .stream_handler import StreamHandler


class RawSocket:

    def __init__(self, openobd_session: OpenOBDSession, raw_channel: RawChannel, timeout: float | None = 10):
        self.stream_handler = StreamHandler(openobd_session.open_raw_stream, outgoing_stream=True)
        self._channel = raw_channel
        self.timeout = timeout

    def send(self, payload: str, flush_incoming_messages: bool = False) -> None:
        message = RawFrame(channel=self._channel, payload=payload)
        self.stream_handler.send(message, flush_incoming_messages)

    def receive(self, block: bool = True, timeout: float | None = None) -> str:
        timeout = timeout if timeout is not None else self.timeout
        response = self.stream_handler.receive(block, timeout)
        return response.payload.upper()

    def stop_stream(self) -> None:
        """
        Closes the gRPC stream if it is not already closed. A new RawSocket object will have to be created to start
        another stream.
        """
        self.stream_handler.stop_stream()
