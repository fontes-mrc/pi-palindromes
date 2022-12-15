def file_chunks(filename: str, size: int, offset: int = 0, rewind: int = 0) -> str:
    """
    Yield successive chunks of a file considering a given offset and rewind values.
    
    Offset: number of characters to skip at the beginning of the file.
    Rewind: number of characters to rewind at the end of each chunk.
    """
    n = 0
    idx = offset
    with open(filename, "r") as inF:
        inF.seek(0, 2)
        file_length = inF.tell()

        inF.seek(idx)
        chunk = inF.read(size) 
        while chunk: 
            yield idx, file_length, chunk
            n += 1
            idx = offset + (n * size) - (n*rewind)
            inF.seek(idx)
            chunk = inF.read(size)