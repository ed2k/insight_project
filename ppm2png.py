from glob import glob
import cv2

def read_masks_folder():
    """
    List all valid masks in images folder
        output:
            :dict_masks: (list) - list of dict where each dict has {k: val} with k=img_filename and 
                        val: mask_filename is the status of the mask 1=valid, 0=not valid
    """
    path_mats = '*release'
    #path_mats = path_mats +"/"+ self.masks_folder +"/*.mat"
    path_mats = path_mats +"/"+ 'data/images_mask' +"/*.ppm"
    print(path_mats)
    dict_mats = dict()
    for i, mat_p in enumerate(glob(path_mats)):
        print(mat_p)
        mat = cv2.imread(mat_p)
        img_fname = mat_p.replace(".ppm", ".png")
        print(img_fname)
        cv2.imwrite(img_fname, mat)
        #mask_arr = mat["mask"] #uint8 format 0 to 1
        #if self.validate_img(mask_arr * 255.):
        dict_mats[img_fname] = mat_p

    return

read_masks_folder()