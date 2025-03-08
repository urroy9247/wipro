from diskcache import Cache
 
cache = Cache("./cache_dir")  # Disk-based cache
 
cache["key"] = "Persistent Value"
 
print(cache["key"])  # "Persistent Value"