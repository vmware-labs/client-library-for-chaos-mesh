from dataclasses import dataclass

from typing import List


@dataclass
class Selector:
    namespaces: List[str] = None
    labelSelectors: dict = None
    pods: List[str] = None
