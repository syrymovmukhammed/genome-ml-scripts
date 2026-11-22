# genome-ml-scripts

![status](https://img.shields.io/badge/status-learning%20sketches-lightgrey)
![license](https://img.shields.io/badge/license-MIT-green.svg)

Early learning sketches (September 2026): minimal templates for common genomics
and ML tasks, written while learning the tools. They are **not** a tested
pipeline — there is no data, no test and no CI in this repository, and the
paths inside the scripts are placeholders.

For tested, reproducible work see the bacterial WGS set:
[wgs-variant-pipeline](https://github.com/syrymovmukhammed/wgs-variant-pipeline) ·
[variant-ml-filter](https://github.com/syrymovmukhammed/variant-ml-filter) ·
[popgen-vcf-analysis](https://github.com/syrymovmukhammed/popgen-vcf-analysis).

| File | What it sketches |
|---|---|
| `run_denovo_assembly.sh` | SPAdes paired-end assembly call |
| `run_gatk_haplotype.sh` | GATK HaplotypeCaller in GVCF mode |
| `mlp_classifier.py` | scikit-learn MLP on a table of expression values |
| `knn_clustering.py` | k-nearest-neighbours classifier on per-sample features |
| `cnn_sequence_model.py` | 1D CNN skeleton for one-hot encoded DNA (Keras) |

## License

MIT — see [LICENSE](LICENSE).
