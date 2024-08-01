# zyx ==============================================================================

_all__ = [
    "Toolkit",
    "Tool",
    "Calculator",
    "ApifyTools",
    "DuckDuckGo",
    "CsvTools",
    "ArxivToolkit",
    "WikipediaTools",
    "WebsiteTools",
    "JinaReaderTools",
    "YouTubeTools",
    "SQLTools",
]

from ..core import _UtilLazyLoader


class Toolkit(_UtilLazyLoader):
    pass


Toolkit.init("phi.tools.toolkit", "Toolkit")


class Tool(_UtilLazyLoader):
    pass


Tool.init("phi.tools.tool", "Tool")


class Calculator(_UtilLazyLoader):
    pass


Calculator.init("phi.tools.calculator", "Calculator")


class ApifyTools(_UtilLazyLoader):
    pass


ApifyTools.init("phi.tools.apify", "ApifyTools")


class DuckDuckGo(_UtilLazyLoader):
    pass


DuckDuckGo.init("phi.tools.duckduckgo", "DuckDuckGo")


class CsvTools(_UtilLazyLoader):
    pass


CsvTools.init("phi.tools.csv_tools", "CsvTools")


class ArxivToolkit(_UtilLazyLoader):
    pass


ArxivToolkit.init("phi.tools.arxiv_toolkit", "ArxivToolkit")


class WikipediaTools(_UtilLazyLoader):
    pass


WikipediaTools.init("phi.tools.wikipedia", "WikipediaTools")


class WebsiteTools(_UtilLazyLoader):
    pass


WebsiteTools.init("phi.tools.website", "WebsiteTools")


class JinaReaderTools(_UtilLazyLoader):
    pass


JinaReaderTools.init("phi.tools.jina_tools", "JinaReaderTools")


class YouTubeTools(_UtilLazyLoader):
    pass


YouTubeTools.init("phi.tools.youtube_tools", "YouTubeTools")


class SQLTools(_UtilLazyLoader):
    pass


SQLTools.init("phi.tools.sql", "SQLTools")
