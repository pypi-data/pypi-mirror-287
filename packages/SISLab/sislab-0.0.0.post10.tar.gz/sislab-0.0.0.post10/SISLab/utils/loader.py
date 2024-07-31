import os
from PIL import Image
import numpy as np
from concurrent.futures import as_completed, ProcessPoolExecutor, ThreadPoolExecutor

MULTI_PROCESS = ProcessPoolExecutor
THREAD = ThreadPoolExecutor

def load_image(file_path, index, as_ndarray):
    """
    단일 이미지를 로드하여 반환합니다.

    Parameters:
    file_path (str): 이미지 파일의 경로
    index (int): 파일의 인덱스
    as_ndarray (bool): True로 설정하면 이미지를 numpy ndarray로 로드합니다. False로 설정하면 PIL.Image 객체로 로드합니다.

    Returns:
    tuple: (index, img) 형태의 튜플
    """
    try:
        img = Image.open(file_path)
        if as_ndarray:
            img = np.array(img)
        return (index, img)
    except Exception as e:
        print(f"이미지 {file_path}을(를) 로드하는 중 에러 발생: {e}")
        return (index, None)

def load_images(folder_path: str,
        as_ndarray: bool = True,
        parallel_processing=None):
    """
    주어진 폴더 경로에서 jpg, jpeg, png 파일을 모두 로드하여 반환합니다.

    Parameters:
    folder_path (str): 이미지 파일이 저장된 폴더의 경로
    as_ndarray (bool): True로 설정하면 이미지를 numpy ndarray로 로드합니다. False로 설정하면 PIL.Image 객체로 로드합니다.
    parallel_processing (type or None): 병렬 처리에 사용할 Executor 클래스를 지정합니다. None이면 순차적으로 처리합니다.

    Returns:
    images (list): PIL.Image 객체 또는 numpy ndarray 객체의 리스트
    """
    valid_extensions = ('.jpg', '.jpeg', '.png')
    images = []

    # 폴더가 존재하는지 확인
    if not os.path.exists(folder_path):
        raise ValueError("해당 경로에 폴더가 존재하지 않습니다.")

    # 모든 파일 경로 수집
    file_paths = [os.path.join(folder_path, filename) 
                  for filename in os.listdir(folder_path)
                  if filename.lower().endswith(valid_extensions)]

    if parallel_processing:
        # 병렬 처리로 이미지 로드
        with parallel_processing() as executor:
            future_to_index = {executor.submit(load_image, file_path, index, as_ndarray): index for index, file_path in enumerate(file_paths)}
            for future in as_completed(future_to_index):
                index, img = future.result()
                if img is not None:
                    images.append((index, img))
        # 인덱스 순으로 정렬
        images.sort(key=lambda x: x[0])
        images = [img for index, img in images]
    else:
        # 순차 처리로 이미지 로드
        for index, file_path in enumerate(file_paths):
            img = load_image(file_path, index, as_ndarray)
            if img is not None:
                images.append(img)
        # 인덱스 순으로 정렬
        images.sort(key=lambda x: x[0])
        images = [img for index, img in images]

    return images