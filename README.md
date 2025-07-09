# Setup
Run the following commands to setup environment

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Load Model Weights

The following script run model on all samples in `<in_dir>`. Specifically, it will setup the environment variables, ensures that the weights are loaded, and run `nnUNet_predict` with appropriate configuration.

```bash
python predict.py -i <in_dir> -o <out_dir> -d <cpu/cuda>
```

Example:
```bash
python predict.py -i sample_data -o segmentations -d cuda
```

# SynthRAD2023 Segmetations
The segmentation pseudo-labels for SynthRAD2023 dataset can be accessed [here](https://drive.google.com/drive/folders/1v-5rAEcWVOheDzcPefsc7Yoptt4w2FcT?usp=sharing)# UAQ_Thesis_Model
