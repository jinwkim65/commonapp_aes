#!/bin/bash

#SBATCH --job-name=assign_scores
#SBATCH --output=gpu_job.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --gpus=2
#SBATCH --partition=gpu
#SBATCH --time=10:00:00
#SBATCH --mem-per-cpu=10G

module load miniconda
conda activate elevator_env
python assign_scores.py