from collections import namedtuple
from . import CosineSimilarity
from .text_utils import count_entities_and_predicates
from ..metric_interface import MetricInterface


class EntityAndPredicate(MetricInterface):
    @property
    def name(self):
        return "entity_and_predicate"

    def evaluate(self, scraped_file: str, ground_truth_file: str) -> dict:
        scraped_data = self._read_file(scraped_file)
        ground_truth = self._read_file(ground_truth_file)

        scraped_metrics = self._calculate_metrics(scraped_data)
        ground_truth_metrics = self._calculate_metrics(ground_truth)

        entity_similarity = self._calculate_similarity(
            scraped_metrics.entities, ground_truth_metrics.entities
        )
        predicate_similarity = self._calculate_similarity(
            scraped_metrics.predicates, ground_truth_metrics.predicates
        )

        return {
            "entities_percent": scraped_metrics.entity_count
            / ground_truth_metrics.entity_count,
            "predicate_percent": scraped_metrics.predicate_count
            / ground_truth_metrics.predicate_count,
            "entity_similarity": entity_similarity,
            "predicate_similarity": predicate_similarity,
        }

    def _read_file(self, file_path: str) -> str:
        with open(file_path, "r") as file:
            return file.read()

    def _calculate_metrics(self, text: str):
        entity_count, predicate_count, entities, predicates = (
            count_entities_and_predicates(text)
        )
        Metrics = namedtuple(
            "Metrics", ["entity_count", "predicate_count", "entities", "predicates"]
        )
        return Metrics(entity_count, predicate_count, entities, predicates)

    def _calculate_similarity(self, scraped_items, ground_truth_items):
        cosine_similarity_evaluator = CosineSimilarity()
        similarity_result = cosine_similarity_evaluator.evaluate_data(
            " ".join(scraped_items), " ".join(ground_truth_items)
        )
        return similarity_result[cosine_similarity_evaluator.name]
