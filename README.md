Detectrons's config
===

train
---

        Python train_net.py --config-file "configs/centermask/centermask_lite_ V_19_eSE_ FPN_ms_4x.yaml"
---
eval
---

        python train_net.py --config-file "configs/centermask/centermask_V_39_eSE_FPN_ms_3x.yaml" --num-gpus 1 --eval-only MODEL.WEIGHTS centermask2-V-39-eSE-FPN-ms-3x.pth
---
demo
---
        python demo.py --config-file ../configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml \
          --input ../image_folder/\
          --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl
  
---

Use Configs
---
        Some basic usage of the CfgNode object is shown below:

        from detectron2.config import get_cfg
        cfg = get_cfg()    # obtain detectron2's default config
        cfg.xxx = yyy      # add new configs for your own custom components
        cfg.merge_from_file("my_cfg.yaml")   # load values from a file

        cfg.merge_from_list(["MODEL.WEIGHTS", "weights.pth"])   # can also load values from a list of str
        print(cfg.dump())  # print formatted configs
