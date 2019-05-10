import torch
from utils.BERT_MUL_CNN import BERT_MUL_CNN
import numpy as np
from pytorch_pretrained_bert import BertTokenizer
from utils.config import opt
import json
id2r = json.loads(open(opt.id2r_dir, 'r').readline())
tokenizer = BertTokenizer.from_pretrained(opt.bert_vocab_unk, do_lower_case=True)
print("init model...")
model = BERT_MUL_CNN(opt)
model.load(opt.ckpt_path)
model.eval()
print("init model finish")

def processSen(text):
# 一共修改3处， util中一处 此文件两处去掉首位空格，然后将空格替换为@
    text = text.strip().replace(' ', '$')
    word_list = tokenizer.tokenize(text)
    sen = tokenizer.convert_tokens_to_ids(word_list)
    PAD = tokenizer.convert_tokens_to_ids(['[PAD]'])
    if len(word_list) < opt.seq_length:
        sen = sen + PAD * (opt.seq_length - len(sen))
    else:
        sen = sen[:opt.seq_length]
    return torch.LongTensor(np.array(sen)).unsqueeze(0)

def getTriple(text):
    sen = processSen(text)
    _, triples = model(sen, None, None)
    text = text.strip().replace(' ', '$')
    word_list = tokenizer.tokenize(text)
    word_list = [word.replace('#', '')for word in word_list]
    spo_list = []
    for sample in triples[0]:
        o_s, o_e, s_s, s_e, r = sample
        if r == 49:
            continue
        obj, sbj = '',''
        if max(o_s, o_e, s_s, s_e) >= len(word_list):
            continue
        for i in range(o_s, o_e+1):
            obj = obj + word_list[i]
        for i in range(s_s, s_e+1):
            sbj = sbj + word_list[i]
        obj = obj.replace('$', ' ')
        sbj = sbj.replace('$', ' ')
        spo_unit = {}
        spo_unit['object'] = obj
        spo_unit['subject'] = sbj
        spo_unit['predicate'] = id2r[str(r)]
        spo_list.append(spo_unit)

    ieData = {"nodes": [], "links": []}
    existNodes = set()
    for spo in spo_list:
        obj = spo['object']
        sbj = spo['subject']
        if sbj not in existNodes:
            each_node = {}
            each_node['name'] = sbj
            ieData['nodes'].append(each_node)
            existNodes.add(sbj)
        if obj not in existNodes:
            each_node = {}
            each_node['name'] = obj
            ieData['nodes'].append(each_node)
            existNodes.add(obj)
        relation = spo['predicate']
        each_link = {}
        each_link['source'] = obj
        each_link['target'] = sbj
        each_link['value'] = relation
        ieData['links'].append(each_link)
    return ieData
