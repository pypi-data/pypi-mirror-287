from pydantic import BaseModel
from pathlib import Path


class Config(BaseModel):
    # 主路径
    main_path: str = "./LeafGames"
    # 默认显示字体
    fontname: str = "simsun"
    # 默认备用字体
    fallback_fonts: list[str] = [
        "Arial",
        "Tahoma",
        "Microsoft YaHei",
        "Segoe UI",
        "Segoe UI Emoji",
        "Segoe UI Symbol",
        "Helvetica Neue",
        "PingFang SC",
        "Hiragino Sans GB",
        "Source Han Sans SC",
        "Noto Sans SC",
        "Noto Sans CJK JP",
        "WenQuanYi Micro Hei",
        "Apple Color Emoji",
        "Noto Color Emoji",
    ]
