import datetime
import re

from typing import Self

TIME_FORMAT = "%Y/%m/%d %I:%M:%S %p"


class CheckIn:
    RE = re.compile(r"^i ([^ ]+ [^ ]+ (?:AM|PM)) (.+?) {2}(.+?)$", re.MULTILINE)

    def __init__(
        self, *, timestamp: datetime.datetime, account: str, task: str
    ) -> None:
        self.timestamp = timestamp
        self.account = account
        self.task = task
        self.metadata: dict[str, str] = {}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CheckIn):
            return False
        return self.__dict__ == other.__dict__

    @classmethod
    def parse(cls, directive: str) -> Self | None:
        checkin_match = cls.RE.match(directive)
        if checkin_match:
            return cls(
                timestamp=datetime.datetime.strptime(
                    checkin_match.group(1), TIME_FORMAT
                ),
                account=checkin_match.group(2),
                task=checkin_match.group(3),
            )

        return None


class CheckOut:
    RE = re.compile(r"^o ([^ ]+ [^ ]+ (?:AM|PM))$", re.MULTILINE)

    def __init__(self, *, timestamp: datetime.datetime) -> None:
        self.timestamp = timestamp
        self.metadata: dict[str, str] = {}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CheckOut):
            return False
        return self.__dict__ == other.__dict__

    @classmethod
    def parse(cls, directive: str) -> Self | None:
        checkout_match = cls.RE.match(directive)
        if checkout_match:
            return cls(
                timestamp=datetime.datetime.strptime(
                    checkout_match.group(1), TIME_FORMAT
                )
            )

        return None
