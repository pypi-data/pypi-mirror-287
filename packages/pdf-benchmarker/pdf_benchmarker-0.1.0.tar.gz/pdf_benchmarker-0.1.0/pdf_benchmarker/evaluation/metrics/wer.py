from jiwer import wer

from ..metric_interface import MetricInterface


class Wer(MetricInterface):
    @property
    def name(self):
        return "wer"

    def evaluate(self, scraped_file, ground_truth_file):
        with open(scraped_file, "r") as sf:
            scraped_data = sf.read()

        with open(ground_truth_file, "r") as gtf:
            ground_truth = gtf.read()

        error_rate = wer(ground_truth, scraped_data)
        return {self.name: error_rate}
