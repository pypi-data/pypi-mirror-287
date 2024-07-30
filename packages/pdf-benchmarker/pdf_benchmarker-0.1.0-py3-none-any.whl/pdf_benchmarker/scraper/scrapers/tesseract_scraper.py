import pytesseract
from pdf2image import convert_from_path

from ..scraper_interface import ScraperInterface
from ...utils.decorators import monitor_performance


class TesseractScraper(ScraperInterface):
    @property
    def name(self):
        return "tesseract"

    @monitor_performance
    def scrape(self, file_path: str) -> str:
        images = convert_from_path(file_path)

        result = ""
        for index, image in enumerate(images):
            print(f"processing page: {index + 1} / {len(images)}")

            image_text = pytesseract.image_to_string(image)
            result += image_text

        return result
