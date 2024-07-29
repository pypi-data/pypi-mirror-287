import subprocess

def bowtie2(reference_genome, input_1, input_2, output_sam, threads=1):
    """
    Run bowtie2 with default options.

    :param reference_genome: Path to the reference genome index prefix.
    :param input_1: Path to the first input fastq file.
    :param input_2: Path to the second input fastq file.
    :param output_sam: Path to the output SAM file.
    :param threads: Number of threads to use (default is 1).
    """
    cmd = [
        "bowtie2",
        "-x", reference_genome,
        "-1", input_1,
        "-2", input_2,
        "-S", output_sam,
        "--threads", str(threads)
    ]
    subprocess.run(cmd, check=True)


def parse_sam(sam_file, filter_1, filter_2):
    """
    Parses the SAM file and writes unmapped reads to output files.

    :param sam_file: Path to the SAM file.
    :param filter_1: Path to the output FASTQ file for first reads.
    :param filter_2: Path to the output FASTQ file for second reads.
    """

    with open(sam_file, 'r') as sam, \
            open(filter_1, 'w') as not_aligned1, \
            open(filter_2, 'w') as not_aligned2:

        read_buffer = []

        for line in sam:
            if line.startswith('@'):
                continue

            parts = line.strip().split('\t')
            flag = int(parts[1])
            seq = parts[9]
            qual = parts[10]
            read_id = parts[0]
            is_unmapped = (flag & 4) != 0

            read_buffer.append((read_id, seq, qual, is_unmapped))

            if len(read_buffer) == 2:
                (read_id1, seq1, qual1, is_unmapped1), (read_id2, seq2, qual2, is_unmapped2) = read_buffer

                # Add /1 to the first read and /2 to the second read
                fq_entry1 = f"@{read_id1}/1\n{seq1}\n+\n{qual1}\n"
                fq_entry2 = f"@{read_id2}/2\n{seq2}\n+\n{qual2}\n"

                if is_unmapped1 and is_unmapped2:
                    not_aligned1.write(fq_entry1)
                    not_aligned2.write(fq_entry2)
                else:
                    # Handle mixed cases if necessary
                    pass
                read_buffer = []



