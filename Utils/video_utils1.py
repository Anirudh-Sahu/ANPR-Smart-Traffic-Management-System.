import cv2

def read_video(filename="traffic.mp4"):

    cap = cv2.VideoCapture("traffic.mp4")
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames


def save_video(output_video_frames, output_video_path):

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    out = cv2.VideoWriter('D:\Project\Output_Video\output_video.avi', fourcc, 24.0, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))

    for frame in output_video_frames:
        out.write(frame)
    out.release()

def detect_vehicles(frames):
    pass