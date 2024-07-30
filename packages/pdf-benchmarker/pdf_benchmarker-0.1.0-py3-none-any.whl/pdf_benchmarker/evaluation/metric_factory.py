from .metric_interface import MetricInterface
from .metrics import CosineSimilarity, Cer, Wer, EntityAndPredicate, Rouge


class MetricFactory:

    @staticmethod
    def get_metric(metric_name: str) -> MetricInterface:
        if metric_name == "cosine_similarity":
            return CosineSimilarity()
        elif metric_name == "cer":
            return Cer()
        elif metric_name == "wer":
            return Wer()
        elif metric_name == "entity_and_predicate":
            return EntityAndPredicate()
        elif metric_name == "rouge":
            return Rouge()
        else:
            raise ValueError("Unknown scraper name provided")
