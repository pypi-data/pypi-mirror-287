#!/bin/bash

#SBATCH --job-name="find_problem_light_curve_files"
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=5
#SBATCH --mem-per-cpu=4G
#SBATCH --time=5-00:00:00

echo "Start shell script."
srun --unbuffered python -m scripts.find_problem_light_curves
