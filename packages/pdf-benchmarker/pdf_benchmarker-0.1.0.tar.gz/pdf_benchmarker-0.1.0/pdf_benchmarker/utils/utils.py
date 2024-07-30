import os
import time
from typing import Optional
from ..scraper import ScraperFactory, ScraperInterface
from ..models import ScrapeDocumentResult


def scrape_document(
    file_path: str,
    scraper_name: str = "pdfminer",
    custom_scraper: Optional[ScraperInterface] = None,
) -> ScrapeDocumentResult:
    """
    Scrape a PDF document using the specified scraper.

    Args:
        file_path (str): The file path of the PDF document to be scraped.
        scraper_name (str, optional): The name of the scraper to use. Defaults to "pdfminer".
        custom_scraper (ScraperInterface, optional): A custom scraper instance. If provided, overrides scraper_name.

    Returns:
        ScrapeDocumentResult: The result of the scraping operation.

    Raises:
        ValueError: If file_path is empty or None.
        FileNotFoundError: If the file does not exist.
        TypeError: If custom_scraper is provided but doesn't implement ScraperInterface.
    """
    if not file_path:
        raise ValueError("file_path cannot be empty or None")
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File does not exist: {file_path}")

    if custom_scraper:
        if not isinstance(custom_scraper, ScraperInterface):
            raise TypeError("custom_scraper must implement ScraperInterface")
        scraper = custom_scraper
    else:
        scraper = ScraperFactory.get_scraper(scraper_name)

    start_time = time.time()
    result = scraper.scrape(file_path)
    end_time = time.time()
    time_taken = end_time - start_time

    return ScrapeDocumentResult(text=result, time_taken=time_taken)
