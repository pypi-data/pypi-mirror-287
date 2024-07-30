from typing import Tuple
import re

import spacy
from transformers import AutoTokenizer, AutoModel
import torch
from collections import namedtuple

tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/bert-base-nli-mean-tokens"
)
model = AutoModel.from_pretrained("sentence-transformers/bert-base-nli-mean-tokens")
nlp = spacy.load("en_core_web_sm")

rouge_score_pattern = r"(\w+)=(\d+\.\d+)"
# Define named tuple for entity and predicate counts
EntityPredicateCount = namedtuple(
    "EntityPredicateCount",
    ["entity_count", "predicate_count", "entities", "predicates"],
)


def embed_text(text: str) -> torch.Tensor:
    """Generate text embedding for given text."""
    encoded_text = tokenizer(
        text, return_tensors="pt", padding=True, truncation=True, max_length=512
    )

    with torch.no_grad():
        model_output = model(**encoded_text)

    embeddings = model_output.last_hidden_state
    attention_mask = encoded_text["attention_mask"]
    mask_expanded = attention_mask.unsqueeze(-1).expand(embeddings.size()).float()
    sum_embeddings = torch.sum(embeddings * mask_expanded, dim=1)
    sum_mask = torch.clamp(mask_expanded.sum(1), min=1e-9)

    return sum_embeddings / sum_mask


def count_entities_and_predicates(text: str) -> EntityPredicateCount:
    """Count entities and predicates in the given text."""
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]
    predicates = [token.lemma_ for token in doc if token.pos_ == "VERB"]

    return EntityPredicateCount(len(entities), len(predicates), entities, predicates)


def convert_rouge_scores_to_dict(scores):
    results = {}
    for rouge_type in scores:
        score_list = re.findall(rouge_score_pattern, str(scores[rouge_type]))
        score_dict = {f"{rouge_type} {k}": float(v) for k, v in score_list}
        results |= score_dict

    return results
