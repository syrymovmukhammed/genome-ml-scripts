# Genome ML Scripts

Automated scripts for genomic sequence analysis and ML — combining Bash pipelines for de novo assembly and variant calling with Python models (CNN, MLP, kNN). Designed for end-to-end processing of biological expression data. Includes tabular RNA-seq data manipulation via Pandas, feature engineering, and predictive phenotype clustering.

## Скрипты в репозитории:
- `mlp_classifier.py` — Классификация табличных данных экспрессии с помощью многослойного перцептрона (MLP).
- `cnn_sequence_model.py` — Поиск мотивов в последовательностях ДНК/РНК с использованием 1D CNN.
- `knn_clustering.py` — Кластеризация фенотипов методом k-ближайших соседей.
- `run_gatk_haplotype.sh` — Bash-пайплайн для поиска генетических вариантов (SNP/indels) через GATK.
- `run_denovo_assembly.sh` — Автоматизация de novo сборки геномов/транскриптомов с использованием SPAdes.

## Результаты
- Ключевые графики лежат в папке `plots/`
- Сводные показатели представлены в `data/summary_metrics.csv`
