import os
import gdown

if __name__ == "__main__":
    nnUNet_results = "./nnUNet_results"
    Dataset001_custom = os.path.join(nnUNet_results, "Dataset001_custom")
    nnUNetTrainer__nnUNetPlans__3d_fullres = os.path.join(Dataset001_custom, "nnUNetTrainer__nnUNetPlans__3d_fullres")
    dataset_fingerprint_json = os.path.join(nnUNetTrainer__nnUNetPlans__3d_fullres, "dataset_fingerprint.json")
    datdaset_json = os.path.join(nnUNetTrainer__nnUNetPlans__3d_fullres, "dataset.json")
    plans_json = os.path.join(nnUNetTrainer__nnUNetPlans__3d_fullres, "plans.json")
    
    fold_all = os.path.join(nnUNetTrainer__nnUNetPlans__3d_fullres, "fold_all")
    checkpoint_best = os.path.join(fold_all, "checkpoint_best.pth")
    checkpoint_final = os.path.join(fold_all, "checkpoint_final.pth")
    checkpoint_latest = os.path.join(fold_all, "checkpoint_latest.pth")
    
    os.makedirs(nnUNet_results, exist_ok=True)
    os.makedirs(Dataset001_custom, exist_ok=True)
    os.makedirs(nnUNetTrainer__nnUNetPlans__3d_fullres, exist_ok=True)
    os.makedirs(fold_all, exist_ok=True)
    
    if not os.path.exists(dataset_fingerprint_json):
        dataset_fingerprint_json_url = "https://drive.google.com/file/d/1kweIb1R8AqBuif5jXWLBFd75UTMRy8U9/view?usp=sharing"
        gdown.download(dataset_fingerprint_json_url, dataset_fingerprint_json, quiet=False, fuzzy=True)
    
    if not os.path.exists(datdaset_json):
        datdaset_json_url = "https://drive.google.com/file/d/1-bQ7oyiGXqoPA_HyoabTk9dxDRf0yIC_/view?usp=sharing"
        gdown.download(datdaset_json_url, datdaset_json, quiet=False, fuzzy=True)
    
    if not os.path.exists(plans_json):
        plans_json_url = "https://drive.google.com/file/d/1wiPiCxcOeJCh_n_uuKqLh20rz8aGhlDZ/view?usp=sharing"
        gdown.download(plans_json_url, plans_json, quiet=False, fuzzy=True)
    
    if not os.path.exists(checkpoint_best):
        checkpoint_best_url = "https://drive.google.com/file/d/1YlW_7uwX9l3xY2pg8aQs6L6_XHoxyTw7/view?usp=sharing"
        gdown.download(checkpoint_best_url, checkpoint_best, quiet=False, fuzzy=True)
    
    if not os.path.exists(checkpoint_final):
        checkpoint_final_url = "https://drive.google.com/file/d/1iFS4soAlQ8XLBVcBoy6pljpAGjMBDhBi/view?usp=sharing"
        gdown.download(checkpoint_final_url, checkpoint_final, quiet=False, fuzzy=True)
    
    if not os.path.exists(checkpoint_latest):
        checkpoint_latest_url = "https://drive.google.com/file/d/14BUR90f6U5y-bo7qURAYT7olsJ704iJS/view?usp=sharing"
        gdown.download(checkpoint_latest_url, checkpoint_latest, quiet=False, fuzzy=True)           
    
    print("All files downloaded successfully.")