def get_block_trainer_config():
    return {
        "lr": 1e-4,
        "batch_size": 512,
        "max_epochs": 1000,
        "weight_decay": 0.001,
        "add_batchnorm": True,
        "input_dropout_p": 0.05,
        "enc_h_dropout_p": 0.05,
        "dec_h_dropout_p": 0.05,
        "val_proportion": 0.1,
        "use_standardized_genotype": False,
        "model/activation": "GELU",
        "model/rep_size": 256,
        "model/enc_layers": [500, 200],
        "model/dec_layers": [200, 1000],
    }
