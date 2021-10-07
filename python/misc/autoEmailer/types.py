from collections import namedtuple
from dataclasses import dataclass

@dataclass
class EmailText:
    text: str
    type: str = 'plain'