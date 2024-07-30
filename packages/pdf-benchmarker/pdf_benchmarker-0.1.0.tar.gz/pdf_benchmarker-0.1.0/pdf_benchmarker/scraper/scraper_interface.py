from abc import ABC, abstractmethod


class ScraperInterface(ABC):
    @abstractmethod
    def scrape(self, file_path):
        """
        Scrape the PDF document located at file_path.
        Returns the extracted content.
        """
        raise NotImplementedError("Each scraper must implement the scrape method.")
