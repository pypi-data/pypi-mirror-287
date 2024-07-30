import os
import asyncio
from typing import List, Dict, Any
from ..scraper.scraper_factory import ScraperFactory
from docqa_bench import (
    Benchmark,
    PreprocessedDocument,
    SimpleChunker,
    OpenAIEmbedder,
    ChromaStore,
    OpenAIQuestionGenerator,
    OpenAIAnswerGenerator,
    F1Evaluator,
)


async def process_pdf(pdf_path: str, scraper_name: str) -> Dict[str, Any]:
    # Get the scraper
    scraper = ScraperFactory.get_scraper(scraper_name)

    # Scrape the PDF
    scraped_content = scraper.scrape(pdf_path)

    # Set up docqa_bench components
    document = PreprocessedDocument(scraped_content)
    chunker = SimpleChunker(chunk_size=1000, chunk_overlap=200)
    embedder = OpenAIEmbedder("text-embedding-ada-002")
    vector_store = ChromaStore(f"benchmark_{os.path.basename(pdf_path)}")
    question_generator = OpenAIQuestionGenerator("gpt-4o")
    answer_generator = OpenAIAnswerGenerator("gpt-4o")
    evaluator = F1Evaluator()

    # Create and run benchmark
    benchmark = Benchmark(
        document,
        chunker,
        embedder,
        vector_store,
        question_generator,
        answer_generator,
        evaluator,
    )
    results = await benchmark.run()

    return {"pdf": pdf_path, "scraper": scraper_name, "results": results}


async def process_directory(
    directory: str, scraper_names: List[str]
) -> List[Dict[str, Any]]:
    tasks = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            for scraper_name in scraper_names:
                tasks.append(process_pdf(pdf_path, scraper_name))

    return await asyncio.gather(*tasks)
