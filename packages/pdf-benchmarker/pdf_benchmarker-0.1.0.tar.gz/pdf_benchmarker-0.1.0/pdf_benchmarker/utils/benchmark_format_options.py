from enum import Enum


class BenchmarkResults(Enum):
    """
    Enum class representing the formats to save benchmark results.
    """

    CSV = "csv"

    @classmethod
    def validate_input_format(cls, format: str) -> bool:
        """Validate the input format."""
        return format in [result.value for result in cls]

    @classmethod
    def validate_output_format(cls, format: str) -> bool:
        """Validate the output format."""
        return format in [result.value for result in cls]
