python3 -u test_multipose.py  \
        --names rs_model \
        --dataset example \
        --list_start 0 \
        --list_end  10 \
        --dataset_mode allface \
        --gpu_ids 0 \
        --netG rotatespade \
        --norm_G spectralsyncbatch \
        --model rotatespade \
        --label_nc 5 \
        --nThreads 8 \
        --heatmap_size 1\
        --chunk_size 1 \
        --no_gaussian_landmark \
        --multi_gpu \
        --device_count 2 \
        --render_thread 1 \
        --label_mask \
        --align \
        --erode_kernel 21 \
        --yaw_poses 0 5 10 15 20 25 30 35 40.5 45 50 55 60 \
        --pitch_poses 0 5 10 15 20 25 30 35 40.5 45 \
        