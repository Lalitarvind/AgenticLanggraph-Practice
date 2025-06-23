from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """_summary_
    Add two numbers
    """
    return a+b

@mcp.tool()
def multiply(a:int,b:int)->int:
    """Multiply two numbers"""
    return a*b

# transport='stdio' tells server to:
# Use standard input/output (stdin and stdout) to receive and respond to tool function calls
if __name__=="__main__":
    mcp.run(transport="stdio")