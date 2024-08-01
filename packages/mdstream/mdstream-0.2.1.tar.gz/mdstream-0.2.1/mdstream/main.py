import contextlib
import io
import time
from typing import Literal

from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown
from rich.text import Text


class MarkdownStream:
    r"""Stream Markdown text to the terminal with live updates.
    
    Example:
        import time

        # Step 1: Instantiate the MarkdownStream class
        md_stream = MarkdownStream()

        # Step 2: Update the stream with initial text
        md_stream.update("# Welcome to MarkdownStream\nThis is a live stream of Markdown text.")

        # Simulate some delay
        time.sleep(2)

        # Step 3: Update the stream with more text
        md_stream.update("\n## More Content\nHere is some more content being streamed live.")

        # Simulate some more delay
        time.sleep(2)

        # Step 4: Final update to stop the stream
        md_stream.update("\n### End of Stream\nThank you for watching.", final=True)
    """
    live = None
    when = 0
    min_delay = 0.050

    def __init__(self, mdargs=None, style="default"):
        """Initialize the MarkdownStream class.

        Usage:
            >>> from mdstream import MarkdownStream
            >>> md = MarkdownStream(mdargs=None, style="default")
            >>> md.update("# This is a test", final=True)
            >>> md.update("This is a test", font="code", final=False)

        """
        self.printed = ""

        if mdargs:
            self.mdargs = mdargs
        else:
            self.mdargs = {
                "code_theme": "github-light", 
                "inline_code_theme": "github-light",
                "style": style or "reverse",
            }
        self.style = self.mdargs.get("style", "reverse")
        self.live = Live(Text(""), refresh_per_second=1.0 / self.min_delay)
        self.live.start()

    def __del__(self):  # noqa: D105
        if self.live:
            with contextlib.suppress(Exception):
                self.live.stop()

    def update(self, text, 
          final=False,
          font: Literal["text", "code", "li", "ul", "ol", "blockquote",
           "em", "strong", "a", "h1", "h2", "h3", "h4", "h5", "h6"] = "text", **kwargs) -> None:
        now = time.time()
        if not final and now - self.when < self.min_delay:
            return
        self.when = now

        self.mdargs.update(kwargs)
        if font == "code":
            text = f"```\n{text}\n```" if len(text.split("\n")) > 1 else f"`{text}`"
        elif font == "ul":
            text = "\n".join(f"- {line}" for line in text.split("\n"))
        elif font == "ol":
            text = "\n".join(f"{i+1}. {line}" for i, line in enumerate(text.split("\n")))
        elif font == "blockquote":
            text = "\n".join(f"> {line}" for line in text.split("\n"))
        elif font in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            text = f"{'#' * int(font[1:])} {text}"
        self.printed += text


        # Render the entire accumulated text as Markdown
        string_io = io.StringIO()
        console = Console(file=string_io, force_terminal=True, style=self.style)
        markdown = Markdown(self.printed, **self.mdargs)
        console.print(markdown)
        output = string_io.getvalue()

        # Apply the background color to the entire output
        full_text = Text.from_ansi(output)
        self.live.update(full_text)

        if final:
            self.live.stop()
            self.live = None

# Example usage of the MarkdownStream class
if __name__ == "__main__":
    # Step 1: Instantiate the MarkdownStream class
    md_stream = MarkdownStream(style="default")

    # Step 2: Update the stream with initial text
    md_stream.update("# Welcome to MarkdownStream\nThis is a live stream of Markdown text.")
    
    # Simulate some delay
    time.sleep(2)

    # Step 3: Update the stream with more text
    md_stream.update("\n## More Content\nHere is some more content being streamed live.")

    # Simulate some more delay
    time.sleep(2)

    # Step 4: Final update to stop the stream
    md_stream.update("\n### End of Stream\nThank you for watching.", final=True)