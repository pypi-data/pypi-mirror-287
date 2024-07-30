import os
from llama_parse import LlamaParse

from ..scraper_interface import ScraperInterface
from ...utils.decorators import monitor_performance


class LlamaParseScraper(ScraperInterface):
    name = "llama_parse"

    def __init__(self):
        self.api_key = os.environ.get("LLAMA_PARSE_API_KEY")
        self.client = LlamaParse(api_key=self.api_key, result_type="text")

    @monitor_performance
    def scrape(self, file_path: str) -> str:
        documents = self.client.load_data(file_path)
        if not documents:
            return ""
        return documents[0].get_content()
