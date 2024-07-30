from jiwer import cer

from ..metric_interface import MetricInterface


class Cer(MetricInterface):
    @property
    def name(self):
        return "cer"

    def evaluate(self, scraped_file, ground_truth_file):
        with open(scraped_file, "r") as sf:
            scraped_data = sf.read()

        with open(ground_truth_file, "r") as gtf:
            ground_truth = gtf.read()

        error_rate = cer(ground_truth, scraped_data)
        return {self.name: error_rate}
