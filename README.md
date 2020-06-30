Detectrons's config
===

1.train
---

        Python train_net.py --config-file "configs/centermask/centermask_lite_ V_19_eSE_ FPN_ms_4x.yaml"
---
2.eval
---

        python train_net.py --config-file "configs/centermask/centermask_V_39_eSE_FPN_ms_3x.yaml" --num-gpus 1 --eval-only MODEL.WEIGHTS centermask2-V-39-eSE-FPN-ms-3x.pth
---
3.demo
---
        python demo.py --config-file ../configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml \
          --input ../image_folder/\
          --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl
  
---
4.use config
---
        Some basic usage of the CfgNode object is shown below:

        from detectron2.config import get_cfg
        cfg = get_cfg()    # obtain detectron2's default config
        cfg.xxx = yyy      # add new configs for your own custom components
        cfg.merge_from_file("my_cfg.yaml")   # load values from a file

        cfg.merge_from_list(["MODEL.WEIGHTS", "weights.pth"])   # can also load values from a list of str
        print(cfg.dump())  # print formatted configs
---
5.use custom datasets
---

`Register a COCO Format Dataset`


        from detectron2.data.datasets import register_coco_instances
        register_coco_instances("my_dataset", {}, "json_annotation.json", "path/to/image/dir")
        
Once you've registered the dataset, you can use the name of the dataset (e.g., "my_dataset" in example above) in cfg.DATASETS.{TRAIN,TEST}

---
