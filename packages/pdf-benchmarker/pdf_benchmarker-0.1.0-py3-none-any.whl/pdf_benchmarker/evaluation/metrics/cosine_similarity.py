import torch

from .text_utils import embed_text
from ..metric_interface import MetricInterface


class CosineSimilarity(MetricInterface):
    @property
    def name(self):
        return "cosine_similarity"

    def evaluate(self, scraped_file, ground_truth_file):
        print("scraped_file: ", scraped_file)
        with open(scraped_file, "r") as sf:
            scraped_data = sf.read()

        with open(ground_truth_file, "r") as gtf:
            ground_truth = gtf.read()

        scraped_embedding = embed_text(scraped_data)
        ground_truth_embedding = embed_text(ground_truth)

        cosine_similarity = torch.nn.functional.cosine_similarity(
            scraped_embedding, ground_truth_embedding
        )
        return {self.name: cosine_similarity.item()}

    def evaluate_data(self, scraped_data, ground_truth_data):

        scraped_embedding = embed_text(scraped_data)
        ground_truth_embedding = embed_text(ground_truth_data)

        cosine_similarity = torch.nn.functional.cosine_similarity(
            scraped_embedding, ground_truth_embedding
        )
        return {self.name: cosine_similarity.item()}
