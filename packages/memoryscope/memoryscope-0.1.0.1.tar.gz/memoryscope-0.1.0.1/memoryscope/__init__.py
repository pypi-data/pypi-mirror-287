import fire

from memoryscope.core.config.arguments import Arguments
from memoryscope.core.memoryscope import MemoryScope
from memoryscope.core.memoryscope import MemoryScope

""" Version of MemoryScope."""
__version__ = "0.1.0.1"


def cli_job(**kwargs):
    with MemoryScope(**kwargs) as ms:
        memory_chat = ms.default_memory_chat
        memory_chat.run()


if __name__ == "__main__":
    fire.Fire(cli_job)
