from typing import List, Optional

class Track:
    def __init__(self, title: str, artist: str, duration: int) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value

    @property
    def artist(self) -> str:
        return self._artist

    @artist.setter
    def artist(self, value: str) -> None:
        if not value:
            raise ValueError("Artist cannot be empty")
        self._artist = value

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Duration must be positive")
        self._duration = value

    def is_short(self) -> bool:
        return self.duration <= 180

    def __str__(self) -> str:
        return f"{self.title} - {self.artist} ({self.duration} seconds)"


class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tracks = []

    def add_track(self, track: Track) -> None:
        self.tracks.append(track)

    def total_duration(self) -> int:
        return sum(item.duration for item in self.tracks)

    def __str__(self) -> str:
        return f"Playlist: {self.name} ({len(self.tracks)} tracks)"


class CD:
    def __init__(self, title: str, artist: str, tracks: Optional[List[Track]] = None) -> None:
        self.title = title
        self.artist = artist
        self.tracks = tracks if tracks is not None else []

    def add_track(self, track: Track) -> None:
        self.tracks.append(track)

    @property
    def total_duration(self) -> int:
        total_sec = 0
        for item in self.tracks:
            total_sec += item.duration
        return total_sec

    def filter_by_artist(self, artist: str) -> List[Track]:
        filtered = []
        for item in self.tracks:
            if artist == item.artist:
                filtered.append(item)
        return filtered

    def copy_tracks(self) -> List[str]:
        return [str(item) for item in self.tracks]