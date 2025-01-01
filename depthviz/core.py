"""
Module to create a video that reports the depth in meters from an array input.
"""

import os.path
import moviepy.editor as mpy

# from depthviz.csv_parser import CsvParser


class DepthReportVideoCreatorError(Exception):
    """Base class for exceptions in this module."""


class VideoNotRenderError(DepthReportVideoCreatorError):
    """Exception raised for video not rendered errors."""


class DepthReportVideoCreator:
    """
    Class to create a video that reports the depth in meters from an array input.
    """

    def __init__(
        self,
        sample_rate=0.250,
        font="Arial-Rounded-MT-Bold",
        fontsize=100,
        interline=-20,
        color="white",
        bg_color="black",
        stroke_color="black",
        stroke_width=2,
        align="center",
        size=(640, 360),
    ):
        self.sample_rate = sample_rate
        self.font = font
        self.fontsize = fontsize
        self.interline = interline
        self.color = color
        self.bg_color = bg_color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.align = align
        self.size = size
        self.final_video = None

    def render_depth_report_video(self, depth_data):
        """
        Creates a video that reports the depth in meters from an array input.

        Args:
            depth_data: An array of depth values in meters.

        Returns:
            The processed video.
        """

        # Create a text clip for each depth value
        clips = []
        for i, depth in enumerate(depth_data):
            rounded_depth = round(depth)
            if rounded_depth == 0:
                text = "0m"
            else:
                text = f"-{rounded_depth}m"
            clip = mpy.TextClip(
                text,
                font=self.font,
                fontsize=self.fontsize,
                color=self.color,
                bg_color=self.bg_color,
                stroke_color=self.stroke_color,
                stroke_width=self.stroke_width,
                align=self.align,
                size=self.size,
            )
            clip = clip.set_duration(self.sample_rate).set_start(i * self.sample_rate)
            clips.append(clip)

        # Concatenate all the clips into a single video
        self.final_video = mpy.concatenate_videoclips(clips)

    def save(self, path, fps=25):
        """
        Saves the video to a file.

        Args:
            path: The path to save the video (expected file format: .mp4).
            fps: The frames per second of the video.
        """
        parent_dir = os.path.dirname(path)
        if parent_dir == "":
            parent_dir = "./"
        if os.path.exists(parent_dir):
            if os.path.isdir(path):
                raise NameError(
                    f"{path} is a directory, please add a file name to the path. \
                        (e.g., path/to/mydepth_video.mp4)"
                )
            if self.final_video is not None:
                self.final_video.write_videofile(path, fps=fps)
            else:
                raise VideoNotRenderError(
                    "Cannot save video because it has not been rendered yet."
                )
        else:
            raise FileNotFoundError(f"Parent directory does not exist: {parent_dir}")

    def get_video(self):
        """
        Returns the processed video.

        Returns:
            The processed video.
        """
        return self.final_video


# if __name__ == "__main__":
#     # Main function to create a depth report video
#     csv_parser = CsvParser()
#     csv_parser.parse("tests/data/valid_depth_data_trimmed.csv")
#     depth_data_from_csv = csv_parser.get_depth_data()
#     depth_report_video_creator = DepthReportVideoCreator(
#         sample_rate=1  # Sample rate of the dive computer in seconds (e.g., 1, 0.50, 0.25)
#     )
#     depth_report_video_creator.render_depth_report_video(depth_data_from_csv)
#     depth_report_video_creator.save(path=".depth_overlay.mp4", fps=25)
