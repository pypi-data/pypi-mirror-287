from collections import namedtuple
from dataclasses import dataclass, field
from typing import List

from constellate.runtime.debugger.protocol import DebuggerProtocol

Endpoint = namedtuple("Endpoint", ["host", "port"])


@dataclass
class DebuggerConfig:
    protocol: DebuggerProtocol = DebuggerProtocol.DEFAULT
    endpoints: List[Endpoint] = field(default_factory=list)
    wait: bool = True
    # Skip connecting to debug server
    # OR waiting for client to connect to debug server
    skip_on_missing: bool = False
