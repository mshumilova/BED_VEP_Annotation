hg = {}

#reference genome
ref_genome_url = 'https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Homo_sapiens/all_assembly_versions/GCF_000001405.40_GRCh38.p14/GCF_000001405.40_GRCh38.p14_genomic.fna.gz'
ref_name_gz = 'hg38_p14.fna.gz'

hg['ref_genome_url'] = ref_genome_url #928 M
hg['ref_name_gz'] = ref_name_gz

#vep plugins

#gnomAD
url_gnomad_exomes_gz = 'http://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh38/variation_genotype/gnomad.exomes.r2.0.1.sites.GRCh38.noVEP.vcf.gz'
url_gnomad_exomes_tbi = 'http://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh38/variation_genotype/gnomad.exomes.r2.0.1.sites.GRCh38.noVEP.vcf.gz.tbi'
url_gnomad_genomes_gz = 'http://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh38/variation_genotype/gnomad.genomes.r2.0.1.sites.GRCh38.noVEP.vcf.gz'
url_gnomad_genomes_tbi = 'http://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh38/variation_genotype/gnomad.genomes.r2.0.1.sites.GRCh38.noVEP.vcf.gz.tbi'

hg['url_gnomad_exomes_gz'] = url_gnomad_exomes_gz #5.9 Gb
hg['url_gnomad_exomes_tbi'] = url_gnomad_exomes_tbi #883 K
hg['url_gnomad_genomes_gz'] = url_gnomad_genomes_gz #26 Gb
hg['url_gnomad_genomes_tbi'] = url_gnomad_genomes_tbi #2.6 M

#cadd
url_cadd_whole_genome_gz = 'https://krishna.gs.washington.edu/download/CADD/v1.6/GRCh38/whole_genome_SNVs.tsv.gz'
url_cadd_whole_genome_tbi = 'https://krishna.gs.washington.edu/download/CADD/v1.6/GRCh38/whole_genome_SNVs.tsv.gz.tbi'

hg['url_cadd_whole_genome_gz'] = url_cadd_whole_genome_gz #81 Gb
hg['url_cadd_whole_genome_tbi'] = url_cadd_whole_genome_tbi #2.6 M

#clinvar
url_clinvar_gz = 'https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz'
url_clinvar_tbi = 'https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz.tbi'

hg['url_clinvar_gz'] = url_clinvar_gz #78 M
hg['url_clinvar_tbi'] = url_clinvar_tbi #494 K

#ref
url_homo_sapiens_gz = 'https://ftp.ensembl.org/pub/release-110/variation/vep/homo_sapiens_refseq_vep_110_GRCh38.tar.gz'

hg['url_homo_sapiens_gz'] = url_homo_sapiens_gz #18 Gb
