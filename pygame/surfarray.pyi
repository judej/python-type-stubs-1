from typing import Tuple

import numpy
from . import surface

def array2d(surface: surface.Surface) -> numpy.ndarray: ...
def pixels2d(surface: surface.Surface) -> numpy.ndarray: ...
def array3d(surface: surface.Surface) -> numpy.ndarray: ...
def pixels3d(surface: surface.Surface) -> numpy.ndarray: ...
def array_alpha(surface: surface.Surface) -> numpy.ndarray: ...
def pixels_alpha(surface: surface.Surface) -> numpy.ndarray: ...
def pixels_red(surface: surface.Surface) -> numpy.ndarray: ...
def pixels_green(surface: surface.Surface) -> numpy.ndarray: ...
def pixels_blue(surface: surface.Surface) -> numpy.ndarray: ...
def array_colorkey(surface: surface.Surface) -> numpy.ndarray: ...
def make_surface(array: numpy.ndarray) -> surface.Surface: ...
def blit_array(surface: surface.Surface, array: numpy.ndarray) -> None: ...
def map_array(surface: surface.Surface, array3d: numpy.ndarray) -> numpy.ndarray: ...
def use_arraytype(arraytype: str) -> None: ...
def get_arraytype() -> str: ...
def get_arraytypes() -> Tuple[str]: ...

