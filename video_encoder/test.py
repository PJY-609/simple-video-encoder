import ffmpeg
stream = ffmpeg.input('D:/ffmpeg1/football_cif.264')

# stream = ffmpeg.output(stream, 'D:/ffmpeg1/output.mp4',  refs=5), preset='ultrafast', profile='high',
#                        qscale=255, crf=51, qp=100, level=10, qmin, qmax, me_method, b_adapt, deblock, g, keyint_min, sc_threshold, deblock='0:0', b='1k')
stream = ffmpeg.output(stream, 'D:/ffmpeg1/output.mp4', vcodec='libx264', b_adapt=2)
ffmpeg.run(stream)

# import ffmpeg
# (
#     ffmpeg
#     .input('D:/ffmpeg/b200k.mp4')
#     .hflip()
#     .output('D:/ffmpeg/output.mp4')
#     .run()
# )


