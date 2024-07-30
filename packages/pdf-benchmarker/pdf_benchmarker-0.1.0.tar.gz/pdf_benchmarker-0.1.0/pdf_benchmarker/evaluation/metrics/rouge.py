from rouge_score import rouge_scorer

from .text_utils import convert_rouge_scores_to_dict
from ..metric_interface import MetricInterface


class Rouge(MetricInterface):
    @property
    def name(self):
        return "rouge"

    def evaluate(self, scraped_file, ground_truth_file):
        with open(scraped_file, "r") as sf:
            scraped_data = sf.read()

        with open(ground_truth_file, "r") as gtf:
            ground_truth = gtf.read()

        scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL", "rougeLsum"])
        scores = scorer.score(ground_truth, scraped_data)
        scores_dict = convert_rouge_scores_to_dict(scores)
        return scores_dict
