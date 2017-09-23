#!/usr/bin/env python

import os


new_list = ["A01_09.fastq", "A01_11.fastq", "A01_23.fastq", "A01_24.fastq","A01_27.fastq", 
"A01_31.fastq","A01_35.fastq","A01_39.fastq","A01_62.fastq","A01_63.fastq"]


for i in range(len(new_list)):
    os.system("bwa mem " + "-R " + "'@RG\\tID:" + str(new_list[i]) + "\\tSM:'" + str(new_list[i])  + " -o " + str(new_list[i][:6]) + ".sam" + " fa_sacCer3.fa " + str(new_list[i]))
    os.system( "samtools sort " + str(new_list[i][:6]) + ".sam" + ">" +  str(new_list[i][:6]) + ".bam")
    os.system( "samtools index " + str(new_list[i][:6]) + ".bam")
