import cv2, numpy as np
from concurrent.futures import as_completed, ProcessPoolExecutor, ThreadPoolExecutor

MULTI_PROCESS = ProcessPoolExecutor
THREAD = ThreadPoolExecutor

def norm_single(img, dtype=np.float32):
    """
    단일 이미지를 정규화합니다.

    Parameters:
    img (numpy.ndarray): 입력 이미지

    Returns:
    numpy.ndarray: 정규화된 이미지
    """
    img = img.astype(dtype)
    img -= img.min()
    img /= img.max()
    return img

def norm(img_set:np.ndarray, dtype=np.float32, parallel_processing=None):
    """
    이미지 셋의 모든 이미지를 정규화합니다.

    Parameters:
    img_set (list of numpy.ndarray): 입력 이미지 셋
    parallel_processing (type or None): 병렬 처리에 사용할 Executor 클래스를 지정합니다. None이면 순차적으로 처리합니다.

    Returns:
    list of numpy.ndarray: 정규화된 이미지 셋
    """
    if parallel_processing is not None:
        with parallel_processing() as executor:
            normed_imgs = list(executor.map(norm_single, img_set))
    else:
        normed_imgs = [norm_single(img) for img in img_set]
    return np.array(normed_imgs, dtype=dtype)

def resize_single(img, size):
    """
    단일 이미지를 주어진 크기로 재조정합니다.

    Parameters:
    img (numpy.ndarray): 입력 이미지
    size (tuple): (width, height)의 형태로 주어진 새로운 크기

    Returns:
    numpy.ndarray: 재조정된 이미지
    """
    resized_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    return resized_img

def resize(img_set, size, dtype=None, parallel_processing=None):
    """
    이미지 셋의 모든 이미지를 주어진 크기로 재조정합니다.

    Parameters:
    img_set (list of numpy.ndarray): 입력 이미지 셋
    size (tuple): (width, height)의 형태로 주어진 새로운 크기
    parallel_processing (type or None): 병렬 처리에 사용할 Executor 클래스를 지정합니다. None이면 순차적으로 처리합니다.

    Returns:
    list of numpy.ndarray: 재조정된 이미지 셋
    """
    if parallel_processing is not None:
        with parallel_processing() as executor:
            resized_imgs = list(executor.map(resize_single, img_set, [size]*len(img_set)))
        return np.array(resized_imgs, dtype=dtype)
    else:
        resized_imgs = [resize_single(img, size) for img in img_set]
        return np.array(resized_imgs, dtype=dtype)