#!/bin/bash

#SBATCH --job-name=finetune_llama
#SBATCH --output=gpu_job.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --gpus=2
#SBATCH --partition=gpu
#SBATCH --time=2:00:00
#SBATCH --mem-per-cpu=10G

module load CUDA
module load cuDNN
source activate elevator_env
python finetune_llama.py