import os


def copy_image(origin_path, target_path):
    """_summary_
        copy image
    Args:
        origin_path (_type_): _description_
        target_path (_type_): _description_
    """
    origin = open(origin_path, "rb")
    target = open(target_path, "wb")
    size = 1024
    read = origin.read(size)

    while read:
        target.write(read)
        read = origin.read(size)

    origin.close()
    target.close()


copy_image("/Users/ethan/Desktop/1.png", os.path.join(os.getcwd(), "6_file/1.png"))
# copy_image("/Users/ethan/Desktop/1.png", os.getcwd() + "/6_file/1.png")
