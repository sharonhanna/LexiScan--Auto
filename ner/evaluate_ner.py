import spacy
from spacy.scorer import Scorer
from spacy.training import Example
import os

# Load trained model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "legal_ner_model")

nlp = spacy.load(MODEL_PATH)

# Sample evaluation data (small but valid)
EVAL_DATA = [
    (
        "This Agreement is made on 12 January 2022 between ABC Corp and XYZ Ltd for $50000.",
        {
            "entities": [
                (27, 42, "DATE"),
                (51, 59, "ORG"),
                (64, 71, "ORG"),
                (76, 82, "MONEY")
            ]
        }
    )
]

scorer = Scorer()
examples = []

for text, annotations in EVAL_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    example.predicted = nlp(text)
    examples.append(example)

scores = scorer.score(examples)

print("\n📊 NER Evaluation Metrics")
print("------------------------")
print(f"Precision: {scores['ents_p']:.2f}")
print(f"Recall:    {scores['ents_r']:.2f}")
print(f"F1-score:  {scores['ents_f']:.2f}")
