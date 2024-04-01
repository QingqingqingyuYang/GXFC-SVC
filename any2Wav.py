import sys 
sys.path.append('/root/autodl-tmp/external-libraries')

import librosa
import os,tqdm
import multiprocessing as mp
import soundfile as sf
from glob import glob
import argparse

def trans_wav_format(input_paths, output_path):
    # 统一输入音频格式
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    input_paths=""
    input_path=""
    input_paths = glob("/home/aistudio/CoMoSVC/dataset_raw/PopBuTFy/*/*.mp3")
    print("input_paths",len(input_paths))
    for input_path in input_paths:
        wavPath="" 
        songname=input_path.split("/")[-2]
        wavPath=output_path + "/" + songname
        if not os.path.exists(wavPath):
            os.makedirs(wavPath) 
        wavPath=wavPath + "/" + input_path.split("/")[-1].split(".")[-2] + ".wav"
        cmd = f"ffmpeg -i {input_path} -ac 1 -ar 24000 -acodec pcm_s16le {wavPath}"
        os.system(cmd)
        if not os.path.exists(output_path):
            print(f"文件转换失败，请检查报错: {input_path}")
            return None
        else:
            continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-in","--input_paths", type=str, default="CoMoSVC/dataset", help="the input_paths of the files need to trans")
    parser.add_argument("-out","--output_path", type=str, default="CoMoSVC/dataset", help="the output_paths to store wav files")
    args = parser.parse_args()
    input_paths = args.input_paths
    output_path = args.output_path
    trans_wav_format(input_paths, output_path)