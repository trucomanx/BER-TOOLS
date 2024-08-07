

InTrD="../../BER2024-SOURCE"
DName="ber2024"
OutDir="output"

ipynb-py-convert create_dataset.ipynb create_dataset.py

python3 create_dataset.py   --model-type-body 'efficientnet_b3' \
                            --model-type-face 'efficientnet_b3' \
                            --model-type-skel 20 \
                            --dataset-dir $InTrD \
                            --dataset-file "train.csv" \
                            --dataset-name $DName \
                            --output-dir $OutDir


rm -f create_dataset.py
