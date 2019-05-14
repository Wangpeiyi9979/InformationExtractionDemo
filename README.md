# 效果图片
![效果截图](./example.png)

# 所需环境
- Ubuntu 16.04
- Python 3.6
- Pytorch 1.x
- Flask

# 项目目录
```
├── static      # 存放网页相关前端配置
│ ├── css       # css相关配置
│ ├── js        # js文件
├── templates   # 存放html文件
├── utils       # 存放模型相关文件
│ ├── bert-base-chinese 
│ ├── |—— bert-base-chinese.tar.gz # bert预训练参数
│ ├── |—— vocab_unk.txt # bert词典库
│ ├──  checkpoints # 存放已训练好的模型
│ ├──  json_data # 存放各种标签到数字的装换数据  
│ ├──  BERT_MUL_CNN.py # 模型
│ ├──  config.py     # 存放配置文件 
│ ├── encoder.py  # 封装了cnn层
│ ├── findTriple.py # 提供句子加工以及三元组处理函数
│ ├──  metrics.py # 提供实体切割函数
├── app.py # Flask程序主入口
├── README.md
```
# 使用说明
- 克隆项目
```
git clone https://github.com/Wangpeiyi9979/InformationExtractionDemo.git
```
- 安装相关库
```
pip3 install https://download.pytorch.org/whl/cu100/torch-1.1.0-cp36-cp36m-linux_x86_64.whl
pip3 intall flask
```
- 下载训练好的模型
    - 下载[bert预训练参数](https://pan.baidu.com/s/1rWjReg82akD3w6Cfyqo2XA), 提取码:lizu 
        - 将下载的文件放入`uitls/bert-base-chinese/`目录下
    - 下载[预训练模型](https://pan.baidu.com/s/1HEG6yVHsvL103QzNZRhzEg), 提取码:40jh
        - 创建目录
        ```
        cd utils
        mkdir checkpoints
        *mv ../ckpt checkpoints/(将下载的ckpt放入checkpoins下)
        ```
- 切换到主目录，运行flask
```
python app.py
```
- 打开浏览器，输入

```
localhost:5000
```



