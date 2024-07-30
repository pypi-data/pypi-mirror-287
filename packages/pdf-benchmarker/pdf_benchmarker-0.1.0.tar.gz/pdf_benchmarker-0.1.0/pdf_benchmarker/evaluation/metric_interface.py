from abc import ABC, abstractmethod


class MetricInterface(ABC):
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError("Each metric should implement the name")

    @abstractmethod
    def evaluate(self, scraped_file, ground_truth_file) -> dict:
        """
        Compare the scraped file and ground_truth file and calculate metrics
        """
        raise NotImplementedError("Each metric should implement the evaluate method")
