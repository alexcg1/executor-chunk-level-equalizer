# ChunkLevelEqualizer

Put all text chunks on doc.chunks level, not lower traversal levels. Used in [PDF search example](https://medium.com/jina-ai/building-an-ai-powered-pdf-search-engine-with-python-part-1-9102654e6ea1?source=collection_home---------0----------------------------)

Note: This REMOVES all top-level text chunks from doc.chunks and then moves all lower-level text chunks to doc.chunks

## Usage

#### via Docker image (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://ChunkLevelEqualizer')
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://ChunkLevelEqualizer')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`
