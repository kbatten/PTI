import utils.align_data
import scripts.run_pti

if __name__ == "__main__":
    utils.align_data.pre_process_images('/home/keith/src/PTI/input')
    scripts.run_pti.run_PTI(run_name='', use_wandb=False, use_multi_id_training=False)
