"""
Module to create a video that reports the depth in meters from an array input.
"""

import os.path
from typing import Tuple
from moviepy import TextClip, VideoClip, concatenate_videoclips
from depthviz.logger import DepthVizProgessBarLogger
from depthviz.optimizer.linear_interpolation import (
    LinearInterpolationDepth,
    LinearInterpolationDepthError,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class DepthReportVideoCreatorError(Exception):
    """Base class for exceptions in this module."""


class VideoNotRenderError(DepthReportVideoCreatorError):
    """Exception raised for video not rendered errors."""


class VideoFormatError(DepthReportVideoCreatorError):
    """Exception raised for invalid video format errors."""


class DepthReportVideoCreator:
    """
    Class to create a video that reports the depth in meters from an array input.
    """

    def __init__(
        self,
        font: str = os.path.abspath(
            os.path.join(BASE_DIR, "assets/fonts/Open_Sans/static/OpenSans-Bold.ttf")
        ),
        fontsize: int = 100,
        interline: int = -20,
        color: str = "white",
        bg_color: str = "black",
        stroke_color: str = "black",
        stroke_width: int = 2,
        align: str = "center",
        size: Tuple[int, int] = (640, 360),
        fps: int = 25,
    ):
        self.font = font
        self.fontsize = fontsize
        self.interline = interline
        self.color = color
        self.bg_color = bg_color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        self.align = align
        self.size = size
        self.fps = fps
        self.final_video = None
        self.progress_bar_logger = DepthVizProgessBarLogger(
            description="Rendering", unit="f", color="#3982d8"
        )

    def __clip_duration_in_seconds(
        self, current_pos: int, time_data: list[float]
    ) -> float:
        """
        Returns the total duration of the video in seconds.

        Args:
            current_pos: The current position in the array.
            time_data: An array of time values in seconds.

        Returns:
            The total duration of the video in seconds.
        """
        if current_pos == len(time_data) - 1:
            # If it's the last element, return the difference between the last two elements
            return abs(time_data[current_pos] - time_data[current_pos - 1])
        # Otherwise, return the difference between the current and next element
        return abs(time_data[current_pos + 1] - time_data[current_pos])

    def render_depth_report_video(
        self, time_data: list[float], depth_data: list[float]
    ) -> None:
        """
        Creates a video that reports the depth in meters from an array input.

        Args:
            time_data: An array of time values in seconds.
            depth_data: An array of depth values in meters.

        Returns:
            The processed video.
        """
        # TODO: Add a progress bar to show the preprocessing progress
        # Interpolate the depth data
        try:
            interpolated_depth = LinearInterpolationDepth(
                times=time_data, depths=depth_data, fps=self.fps
            )
            interpolated_depths = interpolated_depth.get_interpolated_depths()
            interpolated_times = interpolated_depth.get_interpolated_times()

            # Create a text clip for each depth value
            clips = []
            clip_count = len(interpolated_times)
            for i in range(clip_count):
                duration = self.__clip_duration_in_seconds(i, interpolated_times)
                rounded_depth = round(interpolated_depths[i])
                if rounded_depth == 0:
                    text = "0m"
                else:
                    text = f"-{rounded_depth}m"
                clip = TextClip(
                    text=text,
                    font=self.font,
                    font_size=self.fontsize,
                    interline=self.interline,
                    color=self.color,
                    bg_color=self.bg_color,
                    stroke_color=self.stroke_color,
                    stroke_width=self.stroke_width,
                    text_align=self.align,
                    size=self.size,
                    duration=duration,
                )
                clips.append(clip)

            # Concatenate all the clips into a single video
            self.final_video = concatenate_videoclips(clips)
        except LinearInterpolationDepthError as e:
            raise DepthReportVideoCreatorError(f"Interpolation Error; ({e})") from e

    def save(self, path: str) -> None:
        """
        Saves the video to a file.

        Args:
            path: The path to save the video (expected file format: .mp4).
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
                if not path.endswith(".mp4"):
                    raise VideoFormatError(
                        "Invalid file format: The file format must be .mp4"
                    )
                self.final_video.write_videofile(
                    path, fps=self.fps, logger=self.progress_bar_logger
                )
            else:
                raise VideoNotRenderError(
                    "Cannot save video because it has not been rendered yet."
                )
        else:
            raise FileNotFoundError(f"Parent directory does not exist: {parent_dir}")

    def get_video(self) -> VideoClip:
        """
        Returns the processed video.

        Returns:
            The processed video.
        """
        return self.final_video
