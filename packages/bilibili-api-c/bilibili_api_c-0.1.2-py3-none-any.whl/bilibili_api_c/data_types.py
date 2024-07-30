from dataclasses import dataclass


@dataclass
class BilibiliVideoDetailCreativeCenter:
    bvid: str
    aid: int
    title: str
    description: str
    tags: list[str]
    duration: int
    copyright: int
    source: str
    zone_id: int  # tid
    zone_name: str  # typename
    subtitle_count: int
    # date related
    ptime: int
    ctime: int
