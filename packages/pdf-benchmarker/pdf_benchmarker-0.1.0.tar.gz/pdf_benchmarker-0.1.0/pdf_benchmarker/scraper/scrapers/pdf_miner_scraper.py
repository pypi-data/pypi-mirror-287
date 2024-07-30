from ..scraper_interface import ScraperInterface
from ...utils.decorators import monitor_performance

from pdfminer.high_level import extract_text


class PdfMinerScraper(ScraperInterface):
    @property
    def name(self) -> str:
        return "pdfminer"

    @monitor_performance
    def scrape(self, file_path: str) -> str:
        """
        Extracts text from a PDF file using PdfMiner.

        Args:
        file_path (str): The path to the PDF file from which to extract text.

        Returns:
        str: The extracted text.
        """
        try:
            # Using pdfminer's extract_text to scrape the PDF
            text = extract_text(file_path)
            return text
        except Exception as e:
            return (
                f"An error occurred while attempting to scrape with pdfminer: {str(e)}"
            )
