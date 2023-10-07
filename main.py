from code import docker_pull
from code import folders_creating
from code import reference_genome_downloading
from code import vep_plugins_downloading
from code import bed_to_vcf
from code import vep_annotation


docker_pull()
folders_creating()
#reference_genome_downloading()
#vep_plugins_downloading()
bed_to_vcf()
vep_annotation()
