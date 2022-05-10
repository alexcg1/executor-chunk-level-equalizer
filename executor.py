from jina import Executor, DocumentArray, requests


class TextChunkLevelEqualizer(Executor):
    """
    - Remove original chunk if doc.text exists (bc we only want the sentencized versions)
    - Merges ALL chunks to doc.chunks (instead of lower levels)
    """

    @requests(on="/index")
    def merge_chunks(self, docs, **kwargs):
        for doc in docs:  # level 0 document
            # Remove original text chunks from doc.chunks (non-recursive)
            # Because original text was from huge lumps, not sentencized
            for chunk in doc.chunks:
                if doc.text:
                    docs.pop(chunk.id)
            doc.chunks = doc.chunks[...]
