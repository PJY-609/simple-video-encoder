PARA_DICT = {
    'crf': 1,    # CRF
    'qp': 1,     # QP
    'b': 100,  # bit rate
    'br_method': 'crf',  # bit rate contorll method: crf, qp, b
    'r': 25,  # frame rate
    'preset': 'default',
    'tune': 'default',
    'deblock': 0,
    'deblockalpha': 0,
    'deblockbeta': 0,
    'keyint_min': 25,  # IDR min
    'g': 250,  # IDR max
    'refs': 3,
    'sc_threshold': 40,  # scenecut
    'bf': 3,  # B frame
    'b_adapt': 1
}

BR_TABLE = [
    'crf',
    'qp',
    'b'
]

PRESET_TABLE = [
    "default",
    "ultrafast",
    "superfast",
    "veryfast",
    "fast",
    "medium",
    "slow",
    "slower",
    "veryslow",
    "placebo"
]

TUNE_TABLE = [
    "default",
    "film",
    "animation",
    "grain",
    "stillimage",
    "psnr",
    "ssim",
    "fastdecode",
    "zerolatency"
]

def getPARA_DICT():
    global PARA_DICT
    return PARA_DICT

def getIndexFromBR_TABLE(elemt):
    global BR_TABLE
    return BR_TABLE.index(elemt)

def getElementFromBR_TABLE(index):
    global BR_TABLE
    return BR_TABLE[index]

def getIndexFromPRESET_TABLE(elemt):
    global PRESET_TABLE
    return PRESET_TABLE.index(elemt)

def getElementFromePRESET_TABLE(index):
    global PRESET_TABLE
    return PRESET_TABLE[index]

def getIndexFromTUNE_TABLE(elemt):
    global TUNE_TABLE
    return TUNE_TABLE.index(elemt)

def getElementFromeTUNE_TABLE(index):
    global TUNE_TABLE
    return TUNE_TABLE[index]