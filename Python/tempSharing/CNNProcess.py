from utils.Preprocessing.revise import REVISE
from utils.Preprocessing.resize import RESIZE

revise = REVISE(originalImagesPath = './OriginalImages')

revise.Rename()

revise.Encode()

RESIZE(
    chartsPath = './utils/charts',
    presetting = revise.block
)