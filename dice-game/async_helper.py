import sys
import asyncio

# Check if running inside Pyodide / WebAssembly environment
IS_PYODIDE = "pyodide" in sys.modules

if IS_PYODIDE:
    import js  # Pyodide's built-in JavaScript bridge

    async def input_async(prompt_str=""):
        if prompt_str:
            print(prompt_str, end="", flush=True)
        # Call the Xterm.js promise reader on the browser side
        return await js.readTerminalInput()

else:
    async def input_async(prompt_str=""):
        # Local terminal: run standard synchronous input() inside an async thread executor
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, input, prompt_str)