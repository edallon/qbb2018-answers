#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTATION=../genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
    mkdir $SAMPLE
    fastqc ${SAMPLE}.fastq
    hisat2 -p 8 -x $GENOME ${SAMPLE}.fastq -S ${SAMPLE}.sam
    samtools view -b -o ${SAMPLE}.bam ${SAMPLE}.sam 
    samtools sort -o ${SAMPLE}.sorted.bam ${SAMPLE}.bam
    samtools index ${SAMPLE}.sorted.bam ${SAMPLE}.bai
    stringtie ${SAMPLE}.sorted.bam -p 8 -e -G $ANNOTATION -o ${SAMPLE}.gtf -B
done

