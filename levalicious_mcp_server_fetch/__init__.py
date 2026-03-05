from .server import serve
from tap import Tap

class FetchRequestParser(Tap):
    user_agent: str # pyright: ignore[reportUninitializedInstanceVariable]
    ignore_robots_txt: bool = False
    proxy_url: str  # pyright: ignore[reportUninitializedInstanceVariable]

def main():
    """MCP Fetch Server - HTTP fetching functionality for MCP"""
    import asyncio
    
    args = FetchRequestParser(underscores_to_dashes=True).parse_args()
    asyncio.run(serve(args.user_agent, args.ignore_robots_txt, args.proxy_url))


if __name__ == "__main__":
    main()