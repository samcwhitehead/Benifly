
import time, os, sys
from Benifly import MainWindow
from filemanager import FileManager

# USER: set these variables
# ---------------------------------------------------------------------------------------
root = '/media/sam/SamData/Mosquitoes/'  # folder with video files
targetdir = os.path.join(root, 'tracked')  # where to save output data & video
vidname = 'frames'  # name of video variable in MATLAB .mat file (does not apply to videos of other formats)
# ---------------------------------------------------------------------------------------

FileSelect = FileManager() # create FileManager instance
FileSelect.Select(root) # open file selection GUI in root folder

Benifly = MainWindow() # create Benifly instance

# Loop files to set auto-zero ===> press "w" when done with file
# Benifly.loopMat(FileSelect.files[0], vidname)
Benifly.loopVid(FileSelect.files[0])

print('Files to track:')
print('-------------------------------------')
for f in FileSelect.basename:
    print(f)
print('-------------------------------------\n')

# Loop through and track all files
for f in FileSelect.files:
    print 'Tracking: ' , f

    # USER: uncomment method to use    #---------------------------------------------------
    # Benifly.loopMat(f, vidname)
    # Benifly.loopVid(f)
    # Benifly.runMat(f, vidname, targetdir)
    Benifly.runVid(f, targetdir)
    # Benifly.loopLive()
    #----------------------------------------------------

    time.sleep(1)

print('----------DONE----------')
sys.exit()
