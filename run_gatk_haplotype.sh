#!/bin/bash
# Скрипт для поиска вариантов с помощью GATK HaplotypeCaller

REF_GENOME="reference/genome.fasta"
INPUT_BAM="alignments/sample_sorted_marked.bam"
OUTPUT_VCF="results/sample_variants.vcf"

echo "Запуск GATK HaplotypeCaller..."

gatk HaplotypeCaller \
    -R "$REF_GENOME" \
    -I "$INPUT_BAM" \
    -O "$OUTPUT_VCF" \
    -ERC GVCF

echo "Поиск вариантов завершен. Результат сохранен в $OUTPUT_VCF"
