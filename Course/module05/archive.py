import shutil

BACKUP_PATH = "backup_data"

#  make archive
shutil.make_archive(base_name="backup_data", format="zip", root_dir="data")

# unpack
shutil.unpack_archive(filename=f"{BACKUP_PATH}.zip",
                      extract_dir="data2",
                      format="zip")