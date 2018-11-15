from skimage import io
from skimage.measure import compare_ssim as ssim
from skimage.measure import compare_psnr as psnr
from PIL import Image

results_dir = './results/experiment_name/test_latest/images/'
imageNum = 100
avgPSNR = 0.0
avgSSIM = 0.0
counter = 0
for i in range(imageNum):
    real_A = io.imread("{}{:0>6d}_real_A.png".format(results_dir,i+1))
    fake_B = io.imread("{}{:0>6d}_fake_B.png".format(results_dir,i+1))  
    avgPSNR += psnr(real_A,fake_B)
    avgSSIM += ssim(real_A,fake_B,multichannel=True)

avgPSNR /= imageNum
avgSSIM /= imageNum
print('PSNR = %f, SSIM = %f' %
				  (avgPSNR, avgSSIM))
   