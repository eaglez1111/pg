import cv2
assert cv2.__version__[0] == '3', 'The fisheye module requires opencv version >= 3.0.0'
import numpy as np
import os
import glob
import sys

DIM=(640, 720)
#cam0
K=np.array([[189.35144213743058, 0.0, 318.7193226367838], [0.0, 189.12842218615634, 319.25318522358043], [0.0, 0.0, 1.0]])
D=np.array([[-0.021861138221506215], [0.019505299718219172], [-0.006667800976048625], [-0.00031347154943495284]])
#cam1
K=np.array([[189.04837356763042, 0.0, 320.33502818808], [0.0, 188.8631149519064, 319.6692104955649], [0.0, 0.0, 1.0]])
D=np.array([[-0.021572964417454973], [0.022703454815758625], [-0.008609733857852585], [-3.083770851860034e-05]])


def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR)#, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted", undistorted_img)
    #cv2.imwrite("/home/liquid/proj/pg/und.png", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    #for p in sys.argv[1:]:
    #    undistort(p)
    images = glob.glob(sys.argv[1]+'*.png')

    for fname in images:
        undistort(fname)
