from IPython.display import HTML
import os
import base64

def showanyVideo(fname):
    # Function to display any video in Ipython or Jupyter Notebook given a directory in which the video exists and the video file name.
    # Args:
    #     fname: Filename of the video.
    
    baseDir = "/Users/diegohiguerasruiz/NO_git_files/Bioinspired_projects/Human_hand/mov_src/"
    location = os.path.join(baseDir, fname)
    
    if os.path.isfile(location):
        ext = 'mov'
    else:
        print("Error: Please check the path.")
        return None

    with open(location, "rb") as video_file:
        video_encoded = base64.b64encode(video_file.read()).decode('utf-8')

    video_tag = f'<video width="640" height="480" controls><source src="data:video/{ext};base64,{video_encoded}" type="video/{ext}"></video>'
    
    return HTML(data=video_tag)

# Example usage
showanyVideo("Screen Recording 2023-11-13 at 10.52.52 AM.mov")
