# The Colab Notebook:
[WiC POS Tagging Word Comparison Notebook](https://colab.research.google.com/drive/1_UdMjugchWWHVrgETc9T1wsYs0R-67wh#scrollTo=9OlQSKyWfH9Y)

# The paper:
[Comparing the Performance of Language Models on a Word-in-Context Benchmark and Developing a Custom Evaluation System in Python](https://www.overleaf.com/read/hdsmwqzsjyhy#e73a16)

# My home page:
[Bernát Fábián](https://fabbernat.github.io/)

# Word in Context (WiC) Task
By design, word embeddings are unable to model the dynamic nature of words' semantics, i.e., the property of words to correspond to potentially different meanings. To address this limitation, dozens of specialized meaning representation techniques such as sense or contextualized embeddings have been proposed. However, despite the popularity of research on this topic, very few evaluation benchmarks exist that specifically focus on the dynamic semantics of words. In this paper we show that existing models have surpassed the performance ceiling of the standard evaluation dataset for the purpose, i.e., Stanford Contextual Word Similarity, and highlight its shortcomings. To address the lack of a suitable benchmark, Pilehvar and his team put forward a large-scale Word in Context dataset, called WiC, based on annotations curated by experts, for generic evaluation of context-sensitive representations. WiC is released in https://pilehvar.github.io/wic/.

This repository contains an algorithm to achieve as much accuracy as possible on the WiC
binary classification task. Each instance in WiC
has a target word w for which two contexts are
provided, each invoking a specific meaning of w.
The task is to determine whether the occurrences
of w in the two contexts share the same meaning
or not, clearly requiring an ability to identify the
word’s semantic category. The WiC task is defined
over supersenses (Pilehvar and Camacho-Collados,
2019) – the negative examples include a word used
in two different supersenses and the positive ones
include a word used in the same supersense.

# Illustration of results:
![Large Language Models Table](https://github.com/user-attachments/assets/b5c7e5db-df58-4cbb-815b-d23d88f1f1da)
![image](https://github.com/user-attachments/assets/40cec6ac-9306-49ab-9749-156a22308541)

# Usage of the scripts:
![image](https://github.com/user-attachments/assets/ae79159c-16c2-4018-a51c-c483ade90183)
![image](https://github.com/user-attachments/assets/768bc99d-7a77-4ab5-877d-1e5578afb8f1)
![image](https://github.com/user-attachments/assets/d3221ae1-f9a1-4295-bfb5-8f6db278d777)
![image](https://github.com/user-attachments/assets/f99d52f4-4af6-4f3b-9571-0b4d8ba01170)


- The Google Colab notebook running the models can be found [at this link](https://colab.research.google.com/drive/1yA8IAd5z2oreKUXha-16Du2YrNhemNiU?usp=sharing).
- The evaluation system and function library can be downloaded from the [Fabbernat/Peternity](https://github.com/Fabbernat/Peternity) GitHub repository.
- Testing and evaluation of language models can be viewed in the [Generative Language Models](https://docs.google.com/spreadsheets/d/1y49lg52LHVFmTom-0ibCqYqWA1pKKhiUny-Pf3KVTIg/edit?usp=sharing) spreadsheet.