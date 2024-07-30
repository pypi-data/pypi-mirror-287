from ..scraper_interface import ScraperInterface
from ...utils.decorators import monitor_performance
from tika import parser
import os


class PdfTikaScraper(ScraperInterface):

    @property
    def name(self) -> str:
        return "pdftika"

    @monitor_performance
    def scrape(self, file_path: str) -> str:
        """
        Extracts text from a PDF file using PdfTika.

        Args:
        file_path (str): The path to the PDF file from which to extract text.

        Returns:
        str: The extracted text.
        """
        try:
            # Using tika's extract_text to scrape the PDF
            url = os.environ.get("TIKA_URL")
            if url:
                result = parser.from_file(filename=file_path, serverEndpoint=url)
            else:
                result = parser.from_file(file_path)
            return result["content"]
        except Exception as e:
            return f"An error occurred while attempting to scrape with pdftika: {e}"
