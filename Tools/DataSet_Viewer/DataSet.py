import h5py as h5
import numpy as np

data_dir = '../Data_zoo/'
train_data = data_dir+'vidf1_33_000.y_data.h5'
n_frame = 198
IMAGE_SIZE = (50, 50)

def sample_count():
    with h5.File(train_data, 'r') as f:
        return f['data'].shape[0]

def sample_size():
    with h5.File(train_data, 'r') as f:
        return (f['data'].shape[1], f['data'].shape[2])

def feed_dict(_nBatch, _shuffle=True):
    n = 0

    def make_rand_indx(upper_lim, lower_lim=0):
        return np.random.randint(lower_lim, upper_lim, _nBatch)

    def make_batchdata(_data):
        if _shuffle is True:
            indx = make_rand_indx(_data.shape[0])
        else:
            indx = np.arange(n*_nBatch, (n+1)*_nBatch)
        sub_data = np.empty((_nBatch, _data.shape[1], _data.shape[2], _data.shape[3]))
        for i in xrange(indx.shape[0]):
            sub_data[i] = _data[indx[i]]
        return sub_data

    with h5.File(train_data, 'r') as f:
        data=f['data']
        while 1:
            batch_data=make_batchdata(data)
            batch_data = np.transpose(batch_data, (0,2,3,1))
            yield batch_data[:, :, :, 0:5], np.reshape(batch_data[:, :, :, 5], (batch_data.shape[0],
                                                                                batch_data.shape[1],
                                                                                batch_data.shape[2],
                                                                                1))
            n += 1