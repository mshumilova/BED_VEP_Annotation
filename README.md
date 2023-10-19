_____________________________________________________________________________________________
#### Copy code from git
_____________________________________________________________________________________________

      git clone git@github.com:mshumilova/BED_VEP_Annotation.git

_____________________________________________________________________________________________
#### Quick Start
_____________________________________________________________________________________________
      1. Fill out the "config" file
      2. Run Docker Desktop (the first "sudo docker run" command may ask to type your password)
      3. Run "python3 main.py"
_____________________________________________________________________________________________
#### Steps Explanation
_____________________________________________________________________________________________
#### Step 1. Docker Pull
Pull the required containers (bwa-samtools, gatk, ensemble-vep)
_____________________________________________________________________________________________
#### Step 2. Folders  Creating 
All folders required for the project will be created during this step.
If a folder does not exist, it will be created.
If a folder exists, the creating will not be performed
_____________________________________________________________________________________________
#### Step 3. Reference Genome Downloading 
The human reference genome will be downloaded in "ref" folder, unzipped and indexed.
If "ref" folder is not empty, the downloading will not be performed.
_____________________________________________________________________________________________
#### Step 4. VEP Plugins Downloading (GnomAD, CADD, ClinVar + homo_sapience)
The VEP Plugins will be downloaded in "vep" folder, unzipped if needed.
If "vep" folder is not empty, the downloading will not be performed.
_____________________________________________________________________________________________
#### Step 5. Copy initial data to the working directory
To stay safe your initial data, .bed or .vcf files from input_directory will be copied to the working ("inp_dir") directory.
If your file format is .bed, it will be converted to .vcf format using PLINK and save in "inp_dir".
If your file format is .vcf, it will be copied to "inp_dir" right away.
_____________________________________________________________________________________________
#### Step 6. VEP Annotation 
VEP annotation will be performed based on the genome assembly (37 or 38) indicated in "config" file and the following plugins:
GnomAD Exomes, GnomAD Genomes, CADD Whole Genome and ClinVar.
