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
    def title(self, new_title: str) -> None:
        if len(new_title.strip()) == 0:
            raise ValueError("Invalid title: string is empty")
        self._title = new_title

    @property
    def artist(self) -> str:
        return self._artist

    @artist.setter
    def artist(self, new_artist: str) -> None:
        if len(new_artist.strip()) == 0:
            raise ValueError("Invalid artist: string is empty")
        self._artist = new_artist

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, new_duration: int) -> None:
        if new_duration <= 0:
            raise ValueError("Invalid duration: must be greater than zero")
        self._duration = new_duration

    def is_short(self) -> bool:
        if self.duration <= 180:
            return True
        return False

    def __str__(self) -> str:
        return f"{self.title} by {self.artist} - {self.duration}s"


class Playlist:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tracks: List[Track] = []

    def add_track(self, new_track: Track) -> None:
        self.tracks.append(new_track)

    def total_duration(self) -> int:
        total = 0
        for track in self.tracks:
            total += track.duration
        return total

    def __str__(self) -> str:
        return f"{self.name} [Total tracks: {len(self.tracks)}]"


class CD:
    def __init__(self, title: str, artist: str, tracks: Optional[List[Track]] = None) -> None:
        self.title = title
        self.artist = artist
        if tracks is None:
            self.tracks: List[Track] = []
        else:
            self.tracks = tracks

    def add_track(self, new_track: Track) -> None:
        self.tracks.append(new_track)

    @property
    def total_duration(self) -> int:
        seconds = 0
        for track in self.tracks:
            seconds += track.duration
        return seconds

    def get_short_tracks(self) -> List[Track]:
        short_list: List[Track] = []
        for track in self.tracks:
            if track.is_short():
                short_list.append(track)
        return short_list

    def remove_track(self, title: str) -> bool:
        for track in self.tracks:
            if track.title == title:
                self.tracks.remove(track)
                return True
        return False