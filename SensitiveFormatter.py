import logging
import re


class SensitiveFormatter(logging.Formatter):
    """Formatter that removes sensitive information in logs."""

    @staticmethod
    def _filter(s):
        # default config is with => simbol
        # you can replace the validation for your purposes
        return re.sub(r"=> .*", "<MASKED>", s)

    def format(self, record):
        original = logging.Formatter.format(self, record)  # call parent method
        return self._filter(original)
