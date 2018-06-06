"""
purpose : this script test the speed of writing fits file.
author : kouui
date : 2018-06-05
"""

import numpy as np
from astropy.io import fits
import datetime

if __name__=="__main__":


    hdu_list  = fits.HDUList([])
    nimg = 100
    for i in range(nimg):
        image = np.zeros((2048,2048), dtype=np.uint16)

        now = datetime.datetime.now()
        header = fits.Header()
        header['T_End'] = now.strftime("%Y-%m-%d %H:%M:%S")+'.'+str(now.microsecond)
        header['observer'] = 'kouui'

        hdu = fits.ImageHDU(image, header=header)
        hdu_list.append(hdu)

    start = datetime.datetime.now()
    hdu_list.writeto("./test_fits.fits")
    end = datetime.datetime.now()
    print("time collapsed: {} sec".format(end-start))
