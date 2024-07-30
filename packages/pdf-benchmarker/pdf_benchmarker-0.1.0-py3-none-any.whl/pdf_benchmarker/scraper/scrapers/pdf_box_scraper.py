import subprocess
from pathlib import Path

from ..scraper_interface import ScraperInterface
from ...utils.decorators import monitor_performance


class PDFBoxScraper(ScraperInterface):
    @property
    def name(self):
        return "pdfbox"

    @property
    def JAR_PATH(self):
        return Path.cwd().joinpath("pdf-benchmarker", "javalib", "pdfbox-app-3.0.2.jar")

    @monitor_performance
    def scrape(self, file_path: str) -> str:
        """
        Extracts text from a PDF file using PDFBox
        """
        result = subprocess.run(
            ["java", "-jar", self.JAR_PATH, "export:text", "-console", "-i", file_path],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

        return result.stdout
