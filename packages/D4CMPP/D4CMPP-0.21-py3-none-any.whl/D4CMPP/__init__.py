import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import train as train
from grid_search import grid_search as grid_search
from src import Analyzer as Analyzer
from src.utils.sculptor import Segmentator as Segmentator
