from diskcache import Cache
 
cache = Cache("./cache_dir")  # Disk-based cache

print(cache["key"])  # "Persistent Value"

# cache is stored in disk,not in memory,so even after shuting down the system we get output