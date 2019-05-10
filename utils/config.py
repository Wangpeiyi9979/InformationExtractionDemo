# -*- coding: utf-8 -*-

class Config(object):
    # -----------数据集选择--------------------#
    tag_nums = 19*2+1       # tag类型数量
    rel_nums = 50           # 关系数量

    # -------------dir ----------------#
    bert_model_dir = './utils/bert-base-chinese/bert-base-chinese.tar.gz'
    bert_vocab_unk = './utils/bert-base-chinese/vocab_unk.txt'
    json_data_root = './utils/json_data/'
    id2type_dir = json_data_root + 'id2type.json'
    type2id_dir = json_data_root + 'type2id.json'
    tag2id_dir = json_data_root + 'tag2id.json'
    r2id_dir = json_data_root + 'r2id.json'
    id2r_dir = json_data_root + 'id2r.json'
    id2tag_dir = json_data_root + 'id2tag.json'
    type2types_dir = json_data_root + 'type2types.json'

    #  -------------- 模型超参数 -----------#
    filters = [5, 9, 13]               # CNN卷积核宽度
    filter_num = 230 # CNN卷积核个数
    seq_length = 180
    tuple_max_len = 13
    bert_hidden_size = 768   # bert隐层维度，固定

    # --------------main.py ----------------#
    ckpt_path = './utils/checkpoints/ckpt'
    # ------------optimizer ------------------#
    model = 'BERT_MUL_CNN'  # 'BERT_CNN_CRF'
    use_gpu = 0

    def parse(self, kwargs):
        '''
        user can update the default hyperparamter
        '''
        for k, v in kwargs.items():
            if not hasattr(self, k):
                raise Exception('opt has No key: {}'.format(k))
            setattr(self, k, v)

        print('*************************************************')
        print('user config:')
        for k, v in self.__class__.__dict__.items():
            if not k.startswith('__'):
                print("{} => {}".format(k, getattr(self, k)))

        print('*************************************************')
opt = Config()
