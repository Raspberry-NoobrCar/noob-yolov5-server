# emoji-transfer-yolov5

Detect your and your friends expressions!

Maybe gestures also can be recognized well!🤩

## Train

You can set the a series of config in running command

```sh
python train.py \
  --weight="weight/yolov5l.pt" \
  --cfg="models/yolov5l.yaml" \
  --data="..emoji-dataset/emoji.yaml" \
  --workers=8 \
  --epochs=300 \
  --batch-size=16
```

## Detect

You can place the detect images in specific directory declared in `--source`.

```sh
python3 detect.py \
  --weight="runs/train/exp/weights/best.pt" \
  --source="../emoji-dataset/tests" \
  --data="../emoji-dataset/emoji.yaml"
```
