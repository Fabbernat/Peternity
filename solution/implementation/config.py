# C:\PycharmProjects\Peternity\solution\config.py
from dataclasses import dataclass
from pathlib import Path

from modules import BASE_PATH

# Define which dataset you want to work with
actual_working_dataset = 'train'

@dataclass
class Config:
    """Configuration for WiC classification."""
    base_path: Path = Path(BASE_PATH)
    data_file: Path = f"../../WiC_dataset/{actual_working_dataset}/{actual_working_dataset}.data.txt"
    gold_file: Path = f"../../WiC_dataset/{actual_working_dataset}/{actual_working_dataset}.gold.txt"
    model_name: str = 'sentence-transformers/all-MiniLM-L6-v2'
    similarity_threshold: float = 0.449
    gray_zone: tuple = (0.40, 0.50)


# data_loader.py
from pathlib import Path
from typing import List, Tuple


def load_wic_data(data_path: Path, gold_path: Path) -> Tuple[List[Tuple], List[str]]:
    """
    Loads the WiC dataset and its gold labels.

    Args:
        data_path: Path to the data file
        gold_path: Path to the gold labels file

    Returns:
        Tuple of (data, labels) where data is a list of tuples containing
        (word, pos, index1, index2, sentence_a, sentenceB)
    """
    data = []
    gold = []

    with open(data_path, 'r', encoding='utf-8') as f_data, \
            open(gold_path, 'r', encoding='utf-8') as f_gold:
        for line, label in zip(f_data, f_gold):
            parts = line.strip().split('\t')
            word, pos, index, sentence_a, sentence_b = parts

            try:
                index1, index2 = map(int, index.split('-'))
            except ValueError:
                continue

            gold.append(label.strip())
            data.append((word, pos, index1, index2, sentence_a, sentence_b))

    return data, gold