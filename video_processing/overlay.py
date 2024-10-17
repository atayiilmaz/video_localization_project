import cv2
import os
from moviepy.editor import VideoFileClip, ImageClip, TextClip, CompositeVideoClip, AudioFileClip
from .green_area import detect_green_area

def wrap_text(text, max_chars=40):
    """Wraps text into multiple lines based on max character limit."""
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        # Check if adding this word exceeds the max length
        if len(current_line) + len(word) + 1 <= max_chars:
            current_line += (word + " ")
        else:
            # Start a new line
            lines.append(current_line.strip())
            current_line = word + " "
    
    # Append the last line
    if current_line:
        lines.append(current_line.strip())
        
    return "\n".join(lines)


def overlay_image_on_video(video_clip, image_path):
    """Overlays an image onto the detected green area of the video."""
    image = ImageClip(image_path).set_duration(video_clip.duration)
    
    def process_frame(get_frame, t):
        frame = get_frame(t)
        frame_cv = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        green_area = detect_green_area(frame_cv)
        
        if green_area:
            x, y, w, h = green_area
            resized_image = cv2.resize(cv2.imread(image_path), (w, h))
            frame_cv[y:y+h, x:x+w] = resized_image
        
        return cv2.cvtColor(frame_cv, cv2.COLOR_BGR2RGB)
    
    return video_clip.fl(process_frame)

def create_localized_videos(base_video_path, images, titles, musics, font_size, output_dir):
    """Creates multiple localized videos by overlaying images and titles on a base video."""
    base_video = VideoFileClip(base_video_path)
    
    if len(images) != len(titles) != len(musics):
        raise ValueError("Number of images, titles and musics do not match!")
    
    for i, (image_path, title_text, music_path) in enumerate(zip(images, titles, musics)):
        video_with_overlay = overlay_image_on_video(base_video, image_path)

        wrapped_title = wrap_text(title_text, max_chars=40)
        
        title_clip = TextClip(wrapped_title, fontsize=font_size, color='white', stroke_color='black', stroke_width=2)
        title_clip = title_clip.set_duration(base_video.duration).set_position(("center", 100))
        
        final_video = CompositeVideoClip([video_with_overlay, title_clip])

        # Load the corresponding music file
        audio_clip = AudioFileClip(music_path)
        audio_clip = audio_clip.subclip(0, min(final_video.duration, audio_clip.duration))  # Trim audio to video length
        final_video = final_video.set_audio(audio_clip)

        output_path = os.path.join(output_dir, f"localized_video_{i + 1}.mp4")
        
        final_video.write_videofile(output_path, codec="libx264")
    
    base_video.close()
