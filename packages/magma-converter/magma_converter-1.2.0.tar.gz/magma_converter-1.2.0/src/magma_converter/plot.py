import seaborn as sns
import os

from matplotlib import pyplot as plt
from PIL import Image
from .sds import SDS
from obspy import Trace
from typing import List
sns.set_style("whitegrid")


class Plot:
    types: List[str] = ['normal', 'dayplot', 'relative', 'section']

    def __init__(self, sds: SDS, plot_type: str = 'normal'):
        """Plot daily seismogram

        Args:
            sds: SDS object
            plot_type: Plot type must be between 'normal', 'dayplot', 'relative', 'section'.
        """
        assert type not in self.types, f"Plot type must be between 'normal', 'dayplot', 'relative', 'section'."

        self.sds: SDS = sds
        self.trace: Trace = sds.trace
        self.sampling_rate = sds.results['sampling_rate']
        self.date = sds.results['date']
        self.filename: str = f"{sds.filename}.jpg"
        self.plot_type = plot_type

        output_dir: str = os.path.dirname(sds.path).replace('SDS', 'Seismogram')
        os.makedirs(output_dir, exist_ok=True)
        self.output_dir: str = output_dir

        thumbnail_dir: str = os.path.join(output_dir, 'thumbnail')
        os.makedirs(thumbnail_dir, exist_ok=True)
        self.thumbnail_dir: str = thumbnail_dir

    @property
    def title(self):
        """Plot title

        Returns:
            title (str)
        """
        return (f"{self.date} | {self.trace.id} | {self.sampling_rate} Hz | "
                f"{self.trace.stats.npts} samples")

    def thumbnail(self, seismogram: str) -> str:
        """Generate thumbnail of seismogram.

        Args:
            seismogram (str): Seismogram image path
        """
        outfile = os.path.join(self.thumbnail_dir, self.filename)

        image = Image.open(seismogram)

        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        image.thumbnail((320, 180))
        image.save(outfile)

        return outfile

    def save(self) -> tuple[str, str]:
        """Save plot to file.

        Returns:
            seismogram_image_path (str), thumbnail_image_path (str)
        """
        seismogram = os.path.join(self.output_dir, self.filename)

        self.trace.plot(
            type=self.plot_type,
            title=self.title,
            outfile=seismogram,
            dpi=150,
            show=False
        )
        plt.close('all')

        thumbnail = self.thumbnail(seismogram)

        return seismogram, thumbnail
