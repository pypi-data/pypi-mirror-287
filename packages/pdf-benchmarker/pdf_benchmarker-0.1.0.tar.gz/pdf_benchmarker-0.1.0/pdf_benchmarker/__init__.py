from .scraper import ScraperFactory, ScraperInterface
from .evaluation import MetricFactory, MetricInterface
from .utils.utils import scrape_document
from .models import ScrapeDocumentResult

__all__ = [
    "ScraperFactory",
    "ScraperInterface",
    "MetricFactory",
    "MetricInterface",
    "scrape_document",
    "ScrapeDocumentResult",
]

__version__ = "0.1.0"
