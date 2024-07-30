import pymupdf


class PyMuPDFScraper:
    @property
    def name(self) -> str:
        return "pymupdf"

    def scrape(self, file_path: str) -> str:
        with pymupdf.open(file_path) as document:
            contents = [page.get_text() for page in document]

        return "\n".join(contents)
