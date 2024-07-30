import os
from pathlib import Path

from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError

from ..scraper_interface import ScraperInterface
from ...utils.decorators import monitor_performance


class UnstructuredScraper(ScraperInterface):
    @property
    def name(self):
        return "unstructured"

    @property
    def api_key(self):
        return os.environ.get("UNSTRUCTURED_API_KEY")

    @property
    def client(self):
        return UnstructuredClient(self.api_key)

    @monitor_performance
    def scrape(self, file_path: str | Path) -> str:
        with open(file_path, "rb") as f:
            files = shared.Files(content=f.read(), file_name=str(file_path))

        request = shared.PartitionParameters(
            files=files, strategy="hi_res", hi_res_model_name="yolox"
        )

        try:
            response = self.client.general.partition(request)
            return "\n".join([element["text"] for element in response.elements])
        except SDKError as e:
            print(e)

        return ""
