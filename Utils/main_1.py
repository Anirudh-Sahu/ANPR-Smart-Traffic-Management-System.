from Utils.video_utils import read_video, save_video, detect_vehicles
from Object_Trac.tracker_2 import Tracker

def main():

    frames = read_video("traffic.mp4")

    #object tracking
    obj_tracker = Tracker()
    # result = obj_tracker.detect_objects(frames)

    # output_frames = obj_tracker.draw_annotations(frames, result)
    output_frames = obj_tracker.process_video(frames)


    save_video(output_frames, "D:\Project\Output_Video/avi")

if __name__ == '__main__':
    main()
