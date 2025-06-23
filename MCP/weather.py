from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str):
    """GET the weather location"""
    return "rainy"

if __name__=='__main__':
    mcp.run(transport="streamable-http")