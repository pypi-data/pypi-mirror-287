









from transformers import TrainingArguments

args = TrainingArguments(
    output_dir="./output",
    overwrite_output_dir=False,
    do_train=True,
    do_eval=True,
    do_predict=False,
    evaluation_strategy="no",
    prediction_loss_only=False,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    per_gpu_train_batch_size=None,
    per_gpu_eval_batch_size=None,
    gradient_accumulation_steps=1,
    eval_accumulation_steps=None,
    eval_delay=0,
    learning_rate=5e-5,
    weight_decay=0.0,
    adam_beta1=0.9,
    adam_beta2=0.999,
    adam_epsilon=1e-8,
    max_grad_norm=1.0,
    num_train_epochs=3.0,
    max_steps=-1,
    lr_scheduler_type="linear",
    warmup_ratio=0.0,
    warmup_steps=0,
    log_level="passive",
    log_level_replica="warning",
    log_on_each_node=True,
    logging_dir=None,
    logging_strategy="steps",
    logging_first_step=False,
    logging_steps=500,
    logging_nan_inf_filter=True,
    save_strategy="steps",
    save_steps=500,
    save_total_limit=None,
    save_safetensors=False,
    save_on_each_node=False,
    no_cuda=False,
    use_mps_device=False,
    seed=42,
    data_seed=None,
    jit_mode_eval=False,
    use_ipex=False,
    bf16=False,
    fp16=False,
    fp16_opt_level="O1",
    half_precision_backend="auto",
    bf16_full_eval=False,
    fp16_full_eval=False,
    tf32=None,
    local_rank=-1,
    xpu_backend=None,
    tpu_num_cores=None,
    tpu_metrics_debug=False,
    debug="",
    dataloader_drop_last=False,
    eval_steps=None,
    dataloader_num_workers=0,
    past_index=-1,
    run_name="./output",
    disable_tqdm=False,
    remove_unused_columns=True,
    label_names=None,
    load_best_model_at_end=False,
    metric_for_best_model=None,
    greater_is_better=None,
    ignore_data_skip=False,
    sharded_ddp="",
    fsdp="",
    fsdp_min_num_params=0,
    fsdp_config=None,
    fsdp_transformer_layer_cls_to_wrap=None,
    deepspeed=None,
    label_smoothing_factor=0.0,
    optim="adamw_hf",
    optim_args=None,
    adafactor=False,
    group_by_length=False,
    length_column_name="length",
    report_to=None,
    ddp_find_unused_parameters=None,
    ddp_bucket_cap_mb=None,
    dataloader_pin_memory=True,
    skip_memory_metrics=True,
    use_legacy_prediction_loop=False,
    push_to_hub=False,
    resume_from_checkpoint=None,
    hub_model_id=None,
    hub_strategy="every_save",
    hub_token=None,
    hub_private_repo=False,
    gradient_checkpointing=False,
    include_inputs_for_metrics=False,
    fp16_backend="auto",
    push_to_hub_model_id=None,
    push_to_hub_organization=None,
    push_to_hub_token=None,
    mp_parameters="",
    auto_find_batch_size=False,
    full_determinism=False,
    torchdynamo=None,
    ray_scope="last",
    ddp_timeout=1800,
    torch_compile=False,
    torch_compile_backend=None,
    torch_compile_mode=None,
)

