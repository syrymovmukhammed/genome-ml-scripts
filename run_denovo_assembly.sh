#!/bin/bash
# Скрипт для de novo сборки с использованием SPAdes

# Входные файлы (парноконцевые чтения)
READS_1="data/sample_R1.fastq.gz"
READS_2="data/sample_R2.fastq.gz"
OUT_DIR="spades_assembly_output"

# Количество потоков и доступная оперативная память (в ГБ)
THREADS=16
MEMORY=64

echo "Начинаем de novo сборку в директорию $OUT_DIR..."

spades.py \
    -1 "$READS_1" \
    -2 "$READS_2" \
    -o "$OUT_DIR" \
    -t $THREADS \
    -m $MEMORY \
    --careful

echo "Сборка завершена. Граф сборки и контиги находятся в папке $OUT_DIR."
