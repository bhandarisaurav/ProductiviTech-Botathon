import shutil
from os import path, mkdir, listdir

from app import processVideo

# the folder where the new videos will be placed.
desktop = path.normpath(path.expanduser("~/Desktop/Botathon"))
files = listdir(desktop)
# get the latest video file
latest_video_file = files[len(files) - 1]

if latest_video_file.split(".")[1] != "xlsx":
    # process the latest video and get the generated report file name
    saved_report_file = processVideo(latest_video_file)

    file_name_only = latest_video_file.split('.')[0]
    new_folder_name = f"{file_name_only} Report"
    if path.exists(desktop + "/" + new_folder_name):

        # delete folder if exists of the same name
        shutil.rmtree(desktop + "/" + new_folder_name, ignore_errors=True)
    mkdir(desktop + "/" + new_folder_name)
    folder_path = path.normpath(path.expanduser(f"~/Desktop/Botathon/{new_folder_name}"))
    file_to_save_name = file_name_only + "_report.xlsx"

    curr_dir = path.normpath(path.expanduser("~/PycharmProjects/FaceAndEyeDetection"))

    # save the report to the folder where the video was placed
    shutil.copy(f"{curr_dir}/{saved_report_file}", folder_path + f"/{file_to_save_name}")
