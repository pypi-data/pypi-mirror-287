from .scrapers import (
    PdfMinerScraper,
    PyPDFScraper,
    PDFBoxScraper,
    TesseractScraper,
    UnstructuredScraper,
    LlamaParseScraper,
    PdfTikaScraper,
    PyMuPDFScraper,
)
from .scraper_interface import ScraperInterface
import click


class UnknownScraperError(Exception):
    """
    Custom exception class that is raised when an unknown scraper name is provided.
    """

    def __init__(self, message="Unknown scraper name provided", scraper_name=None):
        super().__init__(message)
        self.scraper_name = scraper_name

    def log_error(self):
        """
        Logs the error message using the logging module.
        """
        click.echo(str(self))


class ScraperFactory:
    scraper_mapping = {
        "pdfminer": lambda: PdfMinerScraper(),
        "pypdf": lambda: PyPDFScraper(),
        "pdfbox": lambda: PDFBoxScraper(),
        "tesseract": lambda: TesseractScraper(),
        "unstructured": lambda: UnstructuredScraper(),
        "llama_parse": lambda: LlamaParseScraper(),
        "pdftika": lambda: PdfTikaScraper(),
        "pymupdf": lambda: PyMuPDFScraper(),
    }

    @classmethod
    def get_scraper(cls, scraper_name: str) -> ScraperInterface:
        if not isinstance(scraper_name, str):
            click.echo("scraper_name must be a string")
            raise TypeError("scraper_name must be a string")
        if not scraper_name:
            click.echo("Scraper name cannot be empty or None")
            raise ValueError("Scraper name cannot be empty or None")
        if scraper_name in cls.scraper_mapping:
            click.echo(f"Returning the {scraper_name} scraper")
            scraper = cls.scraper_mapping[scraper_name]()
            click.echo(f"Scraper object: {scraper.name}")
            return scraper
        else:
            click.echo("Unknown scraper name provided")
            raise UnknownScraperError("Unknown scraper name provided", scraper_name)
