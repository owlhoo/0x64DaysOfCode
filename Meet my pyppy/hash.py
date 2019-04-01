import hashlib

sha1_obj = hashlib.sha1()                # sha1, sha224, sha256, sha512, md5 and so on have the same looking constructor
some_string = 'Don\'t sha1 me :('
sha1_obj.update(some_string.encode('utf-8'))
print(sha1_obj.digest())

md5_obj = hashlib.md5(some_string.encode('utf-8'))
print(md5_obj.digest())
print(md5_obj.digest_size)
print(md5_obj.block_size)


