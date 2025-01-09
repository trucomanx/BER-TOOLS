

InTrD="../../BER2024-SOURCE"
DName="ber2024-source"
OutDir="../../BER2024/BER2024-FUSION"

SubDir="ncod53_efficientnet_b3_efficientnet_b3_minus_v2"

strings=("train_refface.csv" "test_refface.csv")
outstr=("train.csv" "test.csv")


ipynb-py-convert create_dataset.ipynb create_dataset.py

for ((i=0; i<${#strings[@]}; i++)); do
    CsvFile="${strings[i]}"
    CsvOutFile="${outstr[i]}"
    python3 create_dataset.py   --model-type-body 'efficientnet_b3' \
                                --model-type-face 'efficientnet_b3' \
                                --model-type-skel 53 \
                                --dataset-dir $InTrD \
                                --dataset-file $CsvFile \
                                --dataset-out-file $CsvOutFile \
                                --dataset-name $DName \
                                --sub-dir $SubDir \
                                --output-dir $OutDir \
                                --minus true
done




rm -f create_dataset.py
