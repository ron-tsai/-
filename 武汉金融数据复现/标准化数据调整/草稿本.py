import numpy as np

def shuffle_data(fif_data,daily_data,target,train_num,test_num,fif_back,daily_back):

    a = list(range(train_num-daily_back))
    # shuffle_list = np.random.choice(a, train_num-test_num, replace=False)
    shuffle_list=
    rows = list(range(train_num-daily_back)) #总共1489个数据，由于扣除前面20个数据，所以为1469
    val_list = list(set(rows)-set(shuffle_list))
    daily_train_samples = np.zeros((len(shuffle_list),
                         daily_back,
                         5))
    fif_train_samples = np.zeros((len(shuffle_list),
                        fif_back,
                        5))
    daily_val_samples = np.zeros((train_num-daily_back-len(shuffle_list),
                                    daily_back,
                                    5))
    fif_val_samples = np.zeros((train_num-daily_back-len(shuffle_list),
                                  fif_back,
                                  5))
    train_targets = np.zeros((train_num-test_num,))
    val_targets = np.zeros((test_num-daily_back,))

    for i,v in enumerate(shuffle_list):

        fif_train_samples[i] = fif_data[v]
        daily_train_samples[i] = daily_data[v]
        train_targets[i] = target[v]
    for i,v in enumerate(val_list):
        daily_val_samples[i] = daily_data[v]
        fif_val_samples[i] = fif_data[v]
        val_targets[i] = target[v]
    print('打乱十五分钟频训练:' ,fif_train_samples.shape)
    print('打乱日频训练；', daily_train_samples.shape)
    print('打乱十五分钟频验证：',fif_val_samples.shape)
    print('打乱日频验证：',daily_val_samples.shape)
    print('打乱训练标签：',train_targets.shape)
    print('打乱验证标签：',val_targets.shape)

    return {'fif_train_samples':fif_train_samples,
            'daily_train_samples':daily_train_samples,
            'train_targets':train_targets,
            'fif_val_samples':fif_val_samples,
            'daily_val_samples':daily_val_samples,
            'val_targets':val_targets}



