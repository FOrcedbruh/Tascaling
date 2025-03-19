import hashlib



class HashingUtility:

    @classmethod
    def hash_str(cls, data: str) -> bytes:
        res = hashlib.sha256()
        res.update(data)
        return res.hexdigest()