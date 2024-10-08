#!/usr/bin/env python

from ffmpy import FFmpeg
import argparse

def ffmpeg_opt(input_file, output_file, fps, color):
    ff = FFmpeg(
        inputs={input_file: None},
        outputs={
            f'{output_file}': [
                "-filter_complex", 
                f"fps={fps},scale=1600:900:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors={color}[p];[s1][p]paletteuse=dither=bayer"]
        }
    )
    ff.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input', type=str)
    parser.add_argument('-o','--output', nargs='?', default=parser.parse_args().input.replace('mp4','gif'), type=str)
    parser.add_argument('-f', '--fps', nargs='?', default='5', type=int)
    parser.add_argument('-c','--color', nargs='?', default='32', type=int)

    args = parser.parse_args()

    ffmpeg_opt(args.input, args.fps, args.color, args.output)



