from fastmcp import FastMCP
import json

mcp = FastMCP(name="custome-mcp")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

@mcp.tool
def greet(name: str) -> str:
    """Greet a person."""
    return f"Hello, {name}!"

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    return a / b

def mcp_main():
    # HTTP server or stdio, your choice
    mcp.run(transport="http", host="0.0.0.0", port=8000)
    # or just: mcp.run()


if __name__ == "__main__":
    mcp_main()