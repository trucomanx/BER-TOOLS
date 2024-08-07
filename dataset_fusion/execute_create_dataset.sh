

InTrD="../../BER2024-SOURCE"
DName="ber2024-source"
OutDir="../../BER2024/BER2024-FUSION"

#strings=("train.csv" "test.csv")
strings=("test.csv")

ipynb-py-convert create_dataset.ipynb create_dataset.py

for CsvFile in "${strings[@]}"; do
    python3 create_dataset.py   --model-type-body 'efficientnet_b3' \
                                --model-type-face 'efficientnet_b3' \
                                --model-type-skel 20 \
                                --dataset-dir $InTrD \
                                --dataset-file $CsvFile \
                                --dataset-name $DName \
                                --output-dir $OutDir
done




rm -f create_dataset.py
