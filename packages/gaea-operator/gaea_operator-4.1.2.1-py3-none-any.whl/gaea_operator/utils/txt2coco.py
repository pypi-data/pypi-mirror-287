r"""
txtcoco from lvfeng02@baidu.com
"""

import json
import os
import cv2

def txt2coco(img_path, ann_path, res):
    """txt2coco
    """
    with open(ann_path, 'r') as f:
        lines = f.readlines()
        img_count = 1
        ann_count = 1

        for line in lines:
            line = line.strip()
            img_name = line.split(' ')[0]
            label = line.split(' ')[1:]
            # 跳过没有标注的图片
            if len(label) == 0:
                continue

            img = cv2.imread(os.path.join(img_path, img_name))
            h, w = img.shape[:2]
            imginfo = {}
            imginfo['file_name'] = img_name
            imginfo['height'] = h
            imginfo['width'] = w
            imginfo['id'] = img_count
            res['images'].append(imginfo)
            

            num = len(label) // 5
            for i in range(num):
                x1, y1, x2, y2, cls_id = map(float, label[5 * i: 5 * (i + 1)])
                w, h = x2 - x1, y2 - y1
                anninfo = {}
                anninfo['bbox'] = [x1, y1, w, h]
                anninfo['image_id'] = img_count
                anninfo['id'] = ann_count
                anninfo['area'] = w * h
                anninfo['iscrowd'] = 0
                anninfo['category_id'] = int(cls_id)  # 1-n,也可以-1, 0-n-1
                ann_count += 1
                res['annotations'].append(anninfo)

            img_count += 1
    return res

    

if __name__ == '__main__':
    # 自定义categories
    categories = [{"id":1, "name":"car"}, {"id":2, "name":"truck"}]
    res = {"annotations": [], "images": [], "categories": categories}
    # 图片存放路径
    img_path = 'datasets/pszt'
    # 标注文件路径
    ann_path = 'test.txt' 

    res = txt2coco(img_path, ann_path, res)
    with open('train.json', 'w') as f:
        json.dump(res, f, indent=2)