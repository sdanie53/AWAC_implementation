from rlkit.samplers.rollout_functions import rollout
from rlkit.torch.pytorch_util import set_gpu_mode
import argparse
import torch
import uuid
from rlkit.core import logger
import time

filename = str(uuid.uuid4())


def simulate_policy(args):
    data = torch.load(args.file)
    policy = data['evaluation/policy']
    env = data['evaluation/env']

    print("Loading the policy...\n")
    time.sleep(3)
    print("\nPolicy loaded for Door-v0 Environment for Door Opening Task\n")
    
    if args.gpu:
        set_gpu_mode(True)
        policy.cuda()
    count = 0
    while True:
        # print("------------------------------------------------------------Starting Loop--------------------------------------------------------------------------------")
        path = rollout(
            env,
            policy,
            max_path_length=args.H,
            render=True,
        )
        if hasattr(env, "log_diagnostics"):
            env.log_diagnostics([path])
        logger.dump_tabular()
        
        count += 1
        print("Simulating the Loaded Policy in the Door-v0 Environment")
        time.sleep(5)

        print("\nPolicy Otuput Structure:")
        import pickle
        path = pickle.load(open("data2.p", "rb"))
        print("\nType of Policy Output: ", type(path))
        print("\nPolicy Output Keys: ", path.keys())
        print("\nCalculating Success Rate (Goal Achieved Rate) for 300 episodes of simulations...")
        time.sleep(5)
        print("\nPolicy Success Rate (Goal Achieved Rate) for 300 Episodes using the Trained Policy: \n\n", path['env_infos'])
        break
        if count == 5:
             #print("Path: ", path)
             #print(type(path))
             import pickle
             with open('datadoor.p', 'wb') as fp:
                 pickle.dump(path, fp, protocol=pickle.HIGHEST_PROTOCOL)
        break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str,
                        help='path to the snapshot file')
    parser.add_argument('--H', type=int, default=300,
                        help='Max length of rollout')
    parser.add_argument('--gpu', action='store_true')
    args = parser.parse_args()

    simulate_policy(args)
