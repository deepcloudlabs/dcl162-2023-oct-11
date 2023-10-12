"""
Persistence -> File (abstraction)
 i) character array -> Text I/O -> HRF
ii) byte array      -> Binary I/O

resources -> memory, files, socket, connection, ...
"""
data: int = 42  # Text I/O -> 2 chars 4|2
data = 3615  # 3|6|1|5
data = 1_000_000  # 1|0|0|0|0|0|0

numbers: list[int] = [4, 8, 15, 16, 23, 42]
# 4|,|8|,|1|5|,|1|6|,|2|3|,|4|2
