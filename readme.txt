####SYSTEM SETUP, DATA SET & TRAINING

System Setup:
Part 1: Setting up MuJoCo (Physics simulator) for RL by installing mjrl(https://github.com/aravindr93/mjrl/tree/master/setup)
	•sudo apt-get install libgl1-mesa-dev  libgl1-mesa-glx libglew-dev libosmesa6-dev build-essential libglfw3
	•conda env create -f setup/env.yml
	•source activate mjrl-env
	•pip install -e .
Part 2:  Setting up MuJoCo Environments which contains Dexterous Hand Manipulation Suite Tasks
	•git clone --récursive https://github.com/vikashplus/mj_envs.git
	•pip install -e .
Part 3: Setting up hand_dapg package(https://github.com/aravindr93/hand_dapg/tree/master/dapg/examples) that interfaces training algorithms on the hand manipulation tasks
Part 4: Setting up AWAC repository and installing UC Berkeley’s rlkit packages(https://github.com/rail-berkeley/rlkit)
	•git clone https://github.com/rail-berkeley/rlkit.git


Dataset and Training:
Dataset for all the three hand manipulation tasks can be found here(https://drive.google.com/file/d/1SsVaQKZnY5UkuR78WrInp9XxTdKHbF0x/view)
Modifications were made to the training script awac1.py (discussed further in the challenges section)
Once modifications were incorporated & dataset path, and hyperparameters were updated in the rlkit/launchers/experiments/awac/awac_rl.py file, the AWAC training can be commenced using the command:
python rlkit/examples/awac/hand/awac1.py



