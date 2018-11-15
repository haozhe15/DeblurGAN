## cannot import name 'SSIM'
You need to change the code in test.py into "from util.metrics import SSIM".

## requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=8097):
This problem is related to visdom. You can start the visdom visualizatoin server by running 
```python -m visdom.server```. You can disable the visdom visualization by adding ```--display_id 0```

## run test
```bash
python test.py --dataroot ~/Desktop/GOPRO_Large/test/GOPR0384_11_00/blur --model test --dataset_mode single --learn_residual --gpu_ids -1
```