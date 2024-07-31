# Copyright (c) OpenMMLab. All rights reserved.
import base64
import os

import cv2
import mmcv
import torch
from mmengine.model.utils import revert_sync_batchnorm
from ts.torch_handler.base_handler import BaseHandler

from mmseg.apis import inference_model, init_model


class MMsegHandler(BaseHandler):

    def initialize(self, context):
        properties = context.system_properties
        self.map_location = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.device = torch.device(self.map_location + ':' +
                                   str(properties.get('gpu_id')) if torch.cuda.
                                   is_available() else self.map_location)
        self.manifest = context.manifest

        model_dir = properties.get('model_dir')
        serialized_file = self.manifest['model']['serializedFile']
        checkpoint = os.path.join(model_dir, serialized_file)
        self.config_file = os.path.join(model_dir, 'config.py')

        self.model = init_model(self.config_file, checkpoint, self.device)
        self.model = revert_sync_batchnorm(self.model)
        self.initialized = True

    def preprocess(self, data):
        images = []

        for row in data:
            image = row.get('data') or row.get('body')
            if isinstance(image, str):
                image = base64.b64decode(image)
            image = mmcv.imfrombytes(image)
            images.append(image)

        return images

    def inference(self, data, *args, **kwargs):
        results = [inference_model(self.model, img) for img in data]
        return results

    # def postprocess(self, data):
    #     output = []

    #     for image_result in data:
    #         _, buffer = cv2.imencode('.png', image_result[0].astype('uint8'))
    #         content = buffer.tobytes()
    #         output.append(content)
    #     return output

    def postprocess(self, data):
        output = []

        for image_result in data:
            # Access the segmentation mask data
            seg_mask = image_result.pred_sem_seg.data

            # Convert to numpy array, move to CPU if necessary
            seg_mask = seg_mask.cpu().numpy()

            # The seg_mask is already in the range [0, 1], so we need to scale it to [0, 255]
            seg_mask = (seg_mask * 255).astype('uint8')

            # If the mask is 3D (has a channel dimension), take the first channel
            if seg_mask.ndim == 3:
                seg_mask = seg_mask[0]

            # Encode the mask as a PNG image
            _, buffer = cv2.imencode('.png', seg_mask)
            content = buffer.tobytes()
            output.append(content)

        return output