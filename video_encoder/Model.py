import ffmpeg
import os.path
from Para import *
import type_exceptions as type_exc

class Model:
    def __init__(self):
        self._para = getPARA_DICT()
        self._filename = None
        self._output = None

    def updatePara(self, key, value):
        self._para[key] = value

    def updateFilename(self, filename):
        if filename is None:
            raise type_exc.PathIsEmpty("You have not chosen any file yet")
        else:
            self._filename = filename

    def updateOutput(self, output):
        path = os.path.split(output)

        if os.path.isfile(output):
            raise type_exc.FileAlreadyExists("{} already exists, please change another path".format(output))
        elif not os.path.exists(path[0]):
            raise type_exc.PathNotExists("invalid path".format(path[0]))
        else:
            self._output = output

    def getPara(self, key):
        return self._para[key]

    def getFilename(self):
        return self._filename

    def getOutput(self):
        return self._output

    def encodeVideo(self):
        kwargs = {}
        br_method = self._para['br_method']
        if br_method == 'b':
            kwargs.update({br_method: self._para[br_method] * 1000})
        else:
            kwargs.update({br_method: self._para[br_method]})

        kwargs.update({'r': self._para['r']})

        preset_tmp = self._para['preset']
        if preset_tmp != 'default':
            kwargs.update({'preset': preset_tmp})

        tune_tmp = self._para['tune']
        if tune_tmp != 'default':
            kwargs.update({'tune': tune_tmp})

        if self._para['deblock']:
            kwargs.update({'deblock': "%d:%d" % (self._para['deblockalpha'], self._para['deblockbeta'])})

        kwargs.update({'keyint_min': self._para['keyint_min'], 'g': self._para['g'], 'refs': self._para['refs'],
                       'sc_threshold': self._para['sc_threshold'], 'b_adapt': self._para['b_adapt'],
                       'bf': self._para['bf']})
        print(kwargs)
        stream = ffmpeg.input(self._filename)
        stream = ffmpeg.output(stream, self._output, **kwargs)
        ffmpeg.run(stream)


if __name__ == '__main__':
    m = Model()
    m.updateFilename('D:/ffmpeg1/football_cif.264')
    m.updateOutput('D:/ffmpeg1/output.mp4')
    kwargs = {'crf': 50}
    m.encodeVideo()
