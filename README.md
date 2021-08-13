# Task Adaptive Pretraining on Pinyin-to-Characters for XLSR-Wav2Vec2

## Introduction

This project aims to show a proof-of-concept for improving the XLSR-Wav2Vec2
model's transcription of Mandarin Chinese speech by re-training the model on a
new semi-supervised task: converting pinyin (a phonological transcription of
Chinese characters) to Chinese Characters.

## Creating Pinyin from Chinese Text

To create the dataset for the new pretraining task, we input Chinese text into
another neural network trained to generate pinyin from Chinese characters,
G2pM.

## Previous Work

Original paper for task adaptive pretraining:

```bibtex
@misc{gururangan2020dont,
      title={Don't Stop Pretraining: Adapt Language Models to Domains and Tasks}, 
      author={Suchin Gururangan and Ana Marasović and Swabha Swayamdipta and Kyle Lo and Iz Beltagy and Doug Downey and Noah A. Smith},
      year={2020},
      eprint={2004.10964},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

Original paper for XLSR-Wav2Vec2:

```bibtex
@misc{conneau2020unsupervised,
      title={Unsupervised Cross-lingual Representation Learning for Speech Recognition}, 
      author={Alexis Conneau and Alexei Baevski and Ronan Collobert and Abdelrahman Mohamed and Michael Auli},
      year={2020},
      eprint={2006.13979},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

Paper for G2pM:

```bibtex
@misc{park2020g2pm,
      title={g2pM: A Neural Grapheme-to-Phoneme Conversion Package for Mandarin Chinese Based on a New Open Benchmark Dataset}, 
      author={Kyubyong Park and Seanie Lee},
      year={2020},
      eprint={2004.03136},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
