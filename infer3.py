import traceback
import logging
import sys
logger = logging.getLogger(__name__)
import shutil
import numpy as np
import soundfile as sf
import torch
import soundfile as sf
from infer.modules.vc.utils import *
from scipy.io import wavfile
import warnings
from infer.modules.vc.modules import VC
from configs.config import Config
now_dir = os.getcwd()
sys.path.append(now_dir)
logging.getLogger("numba").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

tmp = os.path.join(now_dir, "TEMP")
shutil.rmtree(tmp, ignore_errors=True)
shutil.rmtree("%s/runtime/Lib/site-packages/infer_pack" % (now_dir), ignore_errors=True)
shutil.rmtree("%s/runtime/Lib/site-packages/uvr5_pack" % (now_dir), ignore_errors=True)
os.makedirs(tmp, exist_ok=True)
os.makedirs(os.path.join(now_dir, "logs"), exist_ok=True)
os.makedirs(os.path.join(now_dir, "assets/weights"), exist_ok=True)
os.environ["TEMP"] = tmp
warnings.filterwarnings("ignore")
torch.manual_seed(114514)

config = Config()
vc = VC(config)
sid0="VenomSM2.pth"  # Write your model name (model should be inside weights folder)
protect0=0.33
protect1=0.33

spk_item, protect0, protect1, file_index2, file_index4=vc.get_vc(sid0, protect0,protect1)
print(spk_item,protect1, file_index2, file_index4)
input_audio0 = "Sound 01.wav"
f0_up_key = 0    # increase or decrease pitch [-12 to 12]
vc_transform0=0  
f0_file = None  # You can provide the path to an F0 curve file if needed
f0method0 = "pm"  # Adjust the pitch extraction algorithm as needed ['pm','harvest', 'crepe', 'rmvpe']
file_index1 = "added_IVF53_Flat_nprobe_1_VenomSM2_v2.index"  # write name of your index file (it should be present inside logs folder)
# file_index2 = None  # You can use this for automatic detection
index_rate1 = 0.75
filter_radius0 = 3
resample_sr0 = 0  # adjust your output sample rate [maximum=48000]
rms_mix_rate0 = 0.25 # increasing it can help but keep under 0.5
protect0 = 0.33

file_index=f"logs/{file_index1}"


output_txt, (tgt_sr, audio_opt)=vc.vc_single(0,input_audio0,vc_transform0,f0_file,f0method0,file_index1,file_index2,index_rate1,filter_radius0,resample_sr0,rms_mix_rate0,protect0)

wavfile.write('test123.wav', tgt_sr, audio_opt)
print(output_txt)