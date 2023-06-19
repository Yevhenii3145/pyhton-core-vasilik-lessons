import shutil

# возвращает дотступные форматы архивов
# [('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"), ('tar', 'uncompressed tar file'), ('xztar', "xz'ed tar-file"), ('zip', 'ZIP file')]
print(shutil.get_archive_formats())
archive_file = shutil.make_archive("my_archive_file", "zip", "Test")
# C:\Users\Admin\Desktop\python-core-vasilik-lessons\my_archive_file.zip
print(archive_file)  # выведет путь к архиву
shutil.unpack_archive(archive_file, "Test/Temp/Inner")
