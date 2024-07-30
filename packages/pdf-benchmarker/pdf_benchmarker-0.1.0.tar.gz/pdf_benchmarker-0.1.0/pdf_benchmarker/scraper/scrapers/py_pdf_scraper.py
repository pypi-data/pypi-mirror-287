from ..scraper_interface import ScraperInterface
from ...utils.decorators import monitor_performance

from pypdf import PdfReader


class PyPDFScraper(ScraperInterface):
    @property
    def name(self):
        return "pypdf"

    @monitor_performance
    def scrape(self, file_path: str) -> str:
        """
        Extracts text from a PDF file using PyPDF, preserving page structure.
        """
        try:
            reader = PdfReader(file_path)
            all_pages_text = []
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    all_pages_text.append(text)
                else:
                    all_pages_text.append("No text on this page.")
            # Join all pages text with a page break
            full_text = "\n\n--- Page Break ---\n\n".join(all_pages_text)
            return full_text
        except Exception as e:
            return f"An error occurred while attempting to scrape with py_pdf: {str(e)}"
